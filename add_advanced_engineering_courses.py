import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tutee_admin.settings')
django.setup()

from main.models import Course
from decimal import Decimal

# List of advanced computer engineering courses to add
advanced_courses = [
    {
        'title': 'Cloud Computing Architecture',
        'description': 'Explore cloud service models (IaaS, PaaS, SaaS), deployment strategies, virtualization technologies, and distributed computing concepts. Learn to design scalable, fault-tolerant applications for major cloud platforms like AWS, Azure, and Google Cloud.',
        'duration': '10 weeks',
        'level': 'Advanced',
        'price': Decimal('119.99')
    },
    {
        'title': 'Machine Learning for Engineers',
        'description': 'Apply machine learning techniques to solve engineering problems. Cover supervised and unsupervised learning algorithms, feature engineering, model evaluation, and deployment strategies for production environments.',
        'duration': '14 weeks',
        'level': 'Advanced',
        'price': Decimal('129.99')
    },
    {
        'title': 'Embedded Systems Programming',
        'description': 'Learn to design and program resource-constrained embedded systems. Cover microcontroller architecture, real-time operating systems, interfacing with sensors/actuators, and optimization techniques for performance and power efficiency.',
        'duration': '12 weeks',
        'level': 'Advanced',
        'price': Decimal('99.99')
    },
    {
        'title': 'Parallel and Distributed Computing',
        'description': 'Master techniques for designing parallel algorithms and distributed systems. Learn about concurrency models, synchronization, load balancing, fault tolerance, and performance analysis for multi-core and distributed architectures.',
        'duration': '16 weeks',
        'level': 'Advanced',
        'price': Decimal('109.99')
    },
    {
        'title': 'Computer Graphics and Visualization',
        'description': 'Study 2D/3D rendering pipelines, geometric transformations, shading algorithms, and real-time visualization techniques. Implement interactive graphics applications using industry-standard APIs like OpenGL and WebGL.',
        'duration': '14 weeks',
        'level': 'Intermediate',
        'price': Decimal('94.99')
    },
    {
        'title': 'Compiler Design',
        'description': 'Learn the principles of programming language translation, including lexical analysis, parsing, semantic analysis, code generation, and optimization. Build a working compiler for a subset of a modern programming language.',
        'duration': '16 weeks',
        'level': 'Advanced',
        'price': Decimal('104.99')
    },
    {
        'title': 'Quantum Computing Fundamentals',
        'description': 'Explore quantum mechanics principles relevant to computation, quantum gates and circuits, quantum algorithms, and quantum error correction. Implement quantum programs using frameworks like Qiskit or Q#.',
        'duration': '12 weeks',
        'level': 'Advanced',
        'price': Decimal('139.99')
    }
]

# Add courses to the database
added_count = 0
for course_data in advanced_courses:
    # Check if the course already exists
    if not Course.objects.filter(title=course_data['title']).exists():
        Course.objects.create(**course_data)
        added_count += 1
        print(f"Added course: {course_data['title']}")
    else:
        print(f"Course already exists: {course_data['title']}")

print(f"\nAdded {added_count} new advanced computer engineering courses to the database.") 