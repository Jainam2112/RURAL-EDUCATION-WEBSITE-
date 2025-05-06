import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tutee_admin.settings')
django.setup()

from main.models import Course
from decimal import Decimal

# List of computer engineering courses to add
engineering_courses = [
    {
        'title': 'Data Structures and Algorithms',
        'description': 'Master fundamental data structures (arrays, linked lists, trees, graphs) and algorithms (sorting, searching, dynamic programming). Learn to analyze algorithm efficiency and solve complex computational problems with optimized solutions.',
        'duration': '12 weeks',
        'level': 'Intermediate',
        'price': Decimal('89.99')
    },
    {
        'title': 'Database Management Systems',
        'description': 'Learn database design, normalization, SQL, query optimization, and transaction processing. Explore both relational and NoSQL databases, indexing techniques, and how to build efficient database-backed applications.',
        'duration': '10 weeks',
        'level': 'Intermediate',
        'price': Decimal('79.99')
    },
    {
        'title': 'Computer Networks',
        'description': 'Understand network architecture, protocols (TCP/IP, HTTP), routing algorithms, and security mechanisms. Learn how data travels across networks, from local area networks to the global internet infrastructure.',
        'duration': '8 weeks',
        'level': 'Intermediate',
        'price': Decimal('84.99')
    },
    {
        'title': 'Operating Systems Design',
        'description': 'Explore OS concepts including process management, memory management, file systems, and concurrency. Learn about scheduling algorithms, deadlock prevention, virtual memory, and kernel-level implementation of system calls.',
        'duration': '14 weeks',
        'level': 'Advanced',
        'price': Decimal('99.99')
    },
    {
        'title': 'Artificial Intelligence Fundamentals',
        'description': 'Learn core AI concepts including search algorithms, knowledge representation, machine learning, natural language processing, and computer vision. Implement intelligent agents and understand the ethical implications of AI systems.',
        'duration': '16 weeks',
        'level': 'Intermediate',
        'price': Decimal('109.99')
    },
    {
        'title': 'Computer Architecture',
        'description': 'Study processor design, instruction set architecture, memory hierarchy, and system interconnects. Analyze performance bottlenecks and explore advanced topics like pipelining, superscalar execution, and parallel architectures.',
        'duration': '12 weeks',
        'level': 'Advanced',
        'price': Decimal('94.99')
    },
    {
        'title': 'Cybersecurity Essentials',
        'description': 'Learn threat modeling, cryptography, network security, and secure software development. Practice identifying vulnerabilities, implementing countermeasures, and responding to security incidents in real-world scenarios.',
        'duration': '12 weeks',
        'level': 'Intermediate',
        'price': Decimal('89.99')
    },
    {
        'title': 'Software Engineering Principles',
        'description': 'Master software development life cycles, requirement analysis, system design, testing methodologies, and project management. Apply industry best practices for building maintainable, scalable, and reliable software systems.',
        'duration': '10 weeks',
        'level': 'Beginner',
        'price': Decimal('69.99')
    }
]

# Add courses to the database
added_count = 0
for course_data in engineering_courses:
    # Check if the course already exists
    if not Course.objects.filter(title=course_data['title']).exists():
        Course.objects.create(**course_data)
        added_count += 1
        print(f"Added course: {course_data['title']}")
    else:
        print(f"Course already exists: {course_data['title']}")

print(f"\nAdded {added_count} new computer engineering courses to the database.") 