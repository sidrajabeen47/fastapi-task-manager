from fastapi import FastAPI
from database import engine,SessionLocal
from models import Task,Base

app=FastAPI()
#To create our database structure
Base.metadata.create_all(bind=engine)

@app.get('/')
def home():
    return "API is running"

@app.get('/get.tasks')
def home():
    try:
        db=SessionLocal()
        tasks=db.query(Task).all()
        return tasks
    except Exception as e:
        return {"Error":str(e)} 
    finally:
        db.close()

#{"title":"Value"}
@app.post('/add task')
def add_task(data:dict):
    task_title=data['title']
    try:
        db=SessionLocal()
        task=Task(title=task_title)
        db.add(task)
        db.commit()
        db.refresh(task)
        return task
    except Exception as e:
        return {"Error":str(e)}
    finally:
        db.close()


@app.delete('/delete/{task_id}')
def delete_task(task_id:int):
    db=SessionLocal()
    record=db.query(Task).filter(Task.task_id -- task_id).first()
    if not record:
        return f"No task found with the ID {task_id}"
    db.delete(record)
    db.commit()
    db.close()
    return "Task deleted successfully"

@app.put('/update.task/{task_id}')
def update_task(task_id:int,data:dict):
    db=None
    try:
        new_task_title=data['title']
        new_task_status=data['status']
        db=SessionLocal()
        record=db.query(Task).filter(Task.task_id -- task_id).first()
        if not record:
            return f"Task not found with ID {task_id}"
        record.title=new_task_title
        record.status=new_task_status
        db.commit()
        db.refresh(record)
        return record
    except Exception as e:
        return str(e)
    finally:
        if db is not None:
            db.close()