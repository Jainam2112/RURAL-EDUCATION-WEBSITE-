#!/usr/bin/env python
"""
Check Course Images

This script verifies that all course image paths in the database 
actually exist in the filesystem.
"""

import os
import django
from pathlib import Path

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tutee_admin.settings')
django.setup()

from main.models import Course
from django.conf import settings

def check_course_images():
    """Check that all course image paths in the database exist in the filesystem"""
    print("\n=== CHECKING COURSE IMAGES ===")
    
    all_good = True
    courses = Course.objects.all()
    
    if not courses.exists():
        print("No courses found in the database.")
        return
    
    print(f"Checking {courses.count()} courses...")
    
    for course in courses:
        if not course.image:
            print(f"⚠️ Course '{course.title}' has no image set.")
            all_good = False
            continue
        
        # Get the full path to the image file
        # Note: Django ImageField.path property gives absolute path to the file
        try:
            image_path = course.image.path
            if os.path.exists(image_path):
                print(f"✓ Course '{course.title}' → {course.image} (exists)")
            else:
                print(f"❌ Course '{course.title}' → {course.image} (FILE NOT FOUND at {image_path})")
                all_good = False
        except ValueError as e:
            print(f"❌ Course '{course.title}' → {course.image} (ERROR: {e})")
            all_good = False
    
    if all_good:
        print("\n✅ All course images are valid and exist in the filesystem.")
    else:
        print("\n⚠️ Some course images are missing or invalid. Run update_course_media.py to fix.")
    
    print("\nSettings information:")
    print(f"MEDIA_ROOT: {settings.MEDIA_ROOT}")
    print(f"MEDIA_URL: {settings.MEDIA_URL}")
    print(f"STATIC_ROOT: {settings.STATIC_ROOT}")
    print(f"STATIC_URL: {settings.STATIC_URL}")

if __name__ == "__main__":
    check_course_images() 