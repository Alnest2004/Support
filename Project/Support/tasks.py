# Сюда можно писать различные фоновые задачи для celery с использованием брокера redis
from Project.celery import app


@app.task()
def add(x, y):
    a = x + y
    return a
