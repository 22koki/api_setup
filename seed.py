from app import db,app
from models import Task

def seed_data():
    # Create some sample tasks with completed set to True for the first 3 tasks
    tasks = [
        Task(title="Task 1", due_date="2024-01-20", completed=True),
        Task(title="Task 2", due_date="2024-01-21", completed=True),
        Task(title="Task 3", due_date="2024-01-22", completed=True),
        Task(title="Task 4", due_date="2024-01-23", completed=False),
        Task(title="Task 5", due_date="2024-01-24", completed=False),
        Task(title="Task 6", due_date="2024-01-25", completed=False),
        # Add more tasks as needed
    ]

    # Add tasks to the database
    db.session.add_all(tasks)
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables before seeding data
        seed_data()
