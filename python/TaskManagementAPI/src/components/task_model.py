import sqlite3
from datetime import date

class TaskModel():
    def __init__(self, task_id, title, description, due_date: date, status):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

class Task(TaskModel):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.conn = sqlite3.connect('tasks.db')
        self.initial()

    def initial(self):
        with self.conn as connection:
            cursor = connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tasks(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title VARCHAR(20),
                    description VARCHAR(500),
                    due_date DATETIME,
                    status varchar(50)
                )
            ''')

    def create(self):
        try:
            print('creating new row')
            cursor = self.conn.cursor()
            cursor.execute(f"""
                INSERT INTO tasks (title, description, due_date, status) VALUES
                ('{self.title}', '{self.description}', {self.due_date}, '{self.status}')
            """)
            self.conn.commit()

        except Exception as e:
            print(f"Error creating new row: {e}")
            cursor.close()

    def update(self):
        # Implement the update logic using self.property
        ...

    def retrieve_by_id(self):
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute(
                f'''SELECT * FROM tasks WHERE id={self.task_id}'''
            )
            result = cursor.fetchall()
            print(result)

    def retrieve_all(self):
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute(
                '''SELECT * FROM tasks'''
            )
            result = cursor.fetchall()
            print(result)

    def delete(self):
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute(
                f'''DELETE FROM tasks WHERE id={self.task_id}'''
            )

if __name__ == '__main__':
    today = date.today()
    task = Task(task_id=None, 
                title='FIRST', 
                description='RANDOM TASK', due_date=today, status='DONE')

    task.retrieve_all()
