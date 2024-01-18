from app import app,db
from models import Task

def seed_data():
    # Create some sample tasks
    task1 = Task(title="Task 1", due_date="2024-01-20")
    task2 = Task(title="Task 2", due_date="2024-01-21")
    task3 = Task(title="Task 3", due_date="2024-01-22")

    # Add tasks to the database
    db.session.add_all([task1, task2, task3])
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables before seeding data
        seed_data()
