from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.today())


Base.metadata.create_all(engine)


def add_task(new):  # Shadows name 'new_task' from outer scope, so change parameter name
    new_row = Task(task = new)  # Class name write i.e Task
    session.add(new_row)
    session.commit()


def display_today_task():
    rows = session.query(Task).all()
    print("Today:")
    if session.query(Task).count() == 0:  # To check if there are no rows
        print("Nothing to do!")
    else:
        for row in rows:
            print(row.id, row.task)


value = True


while value:
    print("""
1) Today's tasks
2) Add task
0) Exit
     """)

    choice = int(input())

    if choice == 1:
        display_today_task()

    elif choice == 2:
         print("Enter task")
         new_task = input()
         add_task(new_task)

    elif choice == 0:
        print("Bye!")
        value = False




