#!/usr/bin/env python
"""
Update Course Prices

This script updates all course prices to be in Indian Rupees (under 500 rupees).
It assigns different price points based on course level.
"""

import os
import django
import random

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tutee_admin.settings')
django.setup()

from main.models import Course

# Define price ranges for different course levels (in Indian Rupees)
PRICE_RANGES = {
    'Beginner': (199, 299),
    'Intermediate': (299, 399),
    'Advanced': (399, 499),
}

# Default price range for unknown levels
DEFAULT_PRICE_RANGE = (249, 399)

def update_course_prices():
    """Update all course prices to be in Indian Rupees and under 500"""
    courses = Course.objects.all()
    updated_count = 0
    
    if not courses:
        print("No courses found in the database.")
        return
    
    print(f"Updating prices for {courses.count()} courses...")
    
    for course in courses:
        # Get price range based on course level
        level_lower = course.level.lower()
        price_range = None
        
        for level_key, range_value in PRICE_RANGES.items():
            if level_key.lower() in level_lower:
                price_range = range_value
                break
        
        if not price_range:
            price_range = DEFAULT_PRICE_RANGE
            
        # Generate a random price within the range
        new_price = random.randint(price_range[0], price_range[1])
        
        # Make sure the price ends in 9 for psychological pricing
        if new_price % 10 != 9:
            new_price = (new_price // 10) * 10 + 9
            
        # Ensure we're under 500 rupees
        if new_price >= 500:
            new_price = 499
        
        # Update the course price
        course.price = new_price
        course.save()
        
        print(f"Updated price for '{course.title}' ({course.level}): ₹{new_price}")
        updated_count += 1
    
    print(f"\nSuccessfully updated prices for {updated_count} courses.")

if __name__ == "__main__":
    update_course_prices() 