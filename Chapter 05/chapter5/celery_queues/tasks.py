from celery_app import app
import time

@app.task(queue='high_priority', priority=0)  # max priority
def send_email(recipient, subject, body):
    print(f"Sent email to {recipient} with subject '{subject}'")
    time.sleep(2)
    return f"Email sent to {recipient}"

@app.task(queue='low_priority', priority=9)   # min priority
def process_data(data):
    print(f"Start processing data: {data}")
    time.sleep(10)
    return f"Processed Data: {data}"

@app.task(queue='default')
def backup_database():
    print("Backup of database is running...")
    time.sleep(5)
    return "Backup completed"
