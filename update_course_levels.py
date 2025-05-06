#!/usr/bin/env python
"""
Update Course Levels

This script ensures we have courses in each level category (Beginner, Intermediate, Advanced)
"""

import os
import django
import random

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tutee_admin.settings')
django.setup()

from main.models import Course

# Course level mapping based on course titles and content
COURSE_LEVEL_MAPPING = {
    'introduction': 'Beginner',
    'basic': 'Beginner',
    'fundamentals': 'Beginner',
    'beginner': 'Beginner',
    
    'intermediate': 'Intermediate',
    'advanced': 'Advanced',
    'expert': 'Advanced',
    'master': 'Advanced',
}

# Course levels with their distribution percentages
LEVEL_DISTRIBUTION = {
    'Beginner': 0.4,       # 40% of courses
    'Intermediate': 0.4,   # 40% of courses
    'Advanced': 0.2,       # 20% of courses
}

def update_course_levels():
    """Update course levels to ensure we have a mix of beginner, intermediate, and advanced courses"""
    courses = Course.objects.all()
    updated_count = 0
    
    if not courses:
        print("No courses found in the database.")
        return
    
    # Calculate target counts
    total_courses = courses.count()
    beginner_target = int(total_courses * LEVEL_DISTRIBUTION['Beginner'])
    intermediate_target = int(total_courses * LEVEL_DISTRIBUTION['Intermediate'])
    advanced_target = total_courses - beginner_target - intermediate_target
    
    print(f"Updating levels for {total_courses} courses...")
    print(f"Target distribution: {beginner_target} Beginner, {intermediate_target} Intermediate, {advanced_target} Advanced")
    
    # First pass: assign levels based on course title keywords
    beginner_count = 0
    intermediate_count = 0
    advanced_count = 0
    
    for course in courses:
        # Check course title for keywords
        title_lower = course.title.lower()
        assigned = False
        
        for keyword, level in COURSE_LEVEL_MAPPING.items():
            if keyword in title_lower:
                course.level = level
                course.save()
                updated_count += 1
                
                if level == 'Beginner':
                    beginner_count += 1
                elif level == 'Intermediate':
                    intermediate_count += 1
                else:  # Advanced
                    advanced_count += 1
                
                assigned = True
                print(f"Updated course '{course.title}' to {level} level (keyword match)")
                break
        
        # If not assigned by keyword, we'll handle in the second pass
        if not assigned:
            continue
    
    # Second pass: randomly assign levels to meet target distribution
    unassigned_courses = []
    for course in courses:
        title_lower = course.title.lower()
        # Skip if already assigned based on keywords
        assigned = False
        for keyword in COURSE_LEVEL_MAPPING:
            if keyword in title_lower:
                assigned = True
                break
        
        if not assigned:
            unassigned_courses.append(course)
    
    # Shuffle the unassigned courses for random assignment
    random.shuffle(unassigned_courses)
    
    # Calculate how many more of each level we need
    beginner_needed = max(0, beginner_target - beginner_count)
    intermediate_needed = max(0, intermediate_target - intermediate_count)
    advanced_needed = max(0, advanced_target - advanced_count)
    
    # Assign remaining courses to meet target distributions
    for course in unassigned_courses:
        if beginner_needed > 0:
            course.level = 'Beginner'
            beginner_needed -= 1
        elif intermediate_needed > 0:
            course.level = 'Intermediate'
            intermediate_needed -= 1
        else:
            course.level = 'Advanced'
            advanced_needed -= 1
        
        course.save()
        updated_count += 1
        print(f"Updated course '{course.title}' to {course.level} level (distribution balancing)")
    
    print(f"\nSuccessfully updated levels for {updated_count} courses.")
    
    # Final counts
    beginner_final = Course.objects.filter(level__icontains='Beginner').count()
    intermediate_final = Course.objects.filter(level__icontains='Intermediate').count()
    advanced_final = Course.objects.filter(level__icontains='Advanced').count()
    
    print(f"Final distribution: {beginner_final} Beginner, {intermediate_final} Intermediate, {advanced_final} Advanced")

if __name__ == "__main__":
    update_course_levels() 