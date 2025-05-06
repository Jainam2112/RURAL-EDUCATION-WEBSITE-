import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tutee_admin.settings')
django.setup()

from main.models import Course
from decimal import Decimal

# List of beginner computer engineering courses to add
beginner_courses = [
    {
        'title': 'Introduction to Computer Engineering',
        'description': 'Build a solid foundation in computer engineering principles. Learn about computer organization, binary representation, Boolean logic, and the fundamentals of hardware and software interaction. No prior experience required.',
        'duration': '8 weeks',
        'level': 'Beginner',
        'price': Decimal('59.99')
    },
    {
        'title': 'Programming for Engineers',
        'description': 'Learn programming fundamentals with a focus on engineering applications. Cover variables, control structures, functions, object-oriented concepts, and problem-solving strategies using Python and C++.',
        'duration': '10 weeks',
        'level': 'Beginner',
        'price': Decimal('69.99')
    },
    {
        'title': 'Digital Logic Design',
        'description': 'Master the building blocks of digital circuits including logic gates, flip-flops, registers, and counters. Design and simulate combinational and sequential circuits using industry-standard tools.',
        'duration': '8 weeks',
        'level': 'Beginner',
        'price': Decimal('64.99')
    },
    {
        'title': 'Web Technologies for Engineers',
        'description': 'Learn front-end and back-end web development technologies with an engineering perspective. Build responsive websites and web applications using HTML, CSS, JavaScript, and popular frameworks.',
        'duration': '10 weeks',
        'level': 'Beginner',
        'price': Decimal('74.99')
    },
    {
        'title': 'Computer Hardware Basics',
        'description': 'Understand the fundamental components of computer hardware including processors, memory, storage, motherboards, and peripheral devices. Learn assembly techniques and basic troubleshooting skills.',
        'duration': '6 weeks',
        'level': 'Beginner',
        'price': Decimal('49.99')
    }
]

# Add courses to the database
added_count = 0
for course_data in beginner_courses:
    # Check if the course already exists
    if not Course.objects.filter(title=course_data['title']).exists():
        Course.objects.create(**course_data)
        added_count += 1
        print(f"Added course: {course_data['title']}")
    else:
        print(f"Course already exists: {course_data['title']}")

print(f"\nAdded {added_count} new beginner computer engineering courses to the database.") 