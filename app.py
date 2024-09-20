from flask import Flask, render_template, request, redirect, url_for

import uuid

app = Flask(__name__)

class Task:
    def __init__(self, title, description):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_title, description):
        new_task = Task(task_title, description)
        self.tasks.append(new_task)

    def get_tasks(self):
        return self.tasks

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.id !=task_id]
    

task_manager = TaskManager()

@app.route('/')
def index():
    tasks = task_manager.get_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_title = request.form['task_title']
    task_description = request.form['task_description']
    if task_title:
        task_manager.add_task(task_title=task_title, description=task_description)
    return redirect(url_for('index'))

@app.route('/delete/<task_id>', methods=['POST'])
def delete_task(task_id):
    task_manager.delete_task(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)