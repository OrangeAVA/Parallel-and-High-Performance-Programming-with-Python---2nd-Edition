from celery import Celery

# Choose your broker/backend; here we default to Redis on localhost.
# For RabbitMQ, set broker='pyamqp://guest@localhost//' and a suitable backend (e.g. 'rpc://', or Redis).
app = Celery('tasks', broker='redis://localhost//', backend='redis://localhost')
# Helpful for startup races with broker containers
app.conf.broker_connection_retry_on_startup = True

@app.task
def add(x, y):
    return x + y

@app.task
def mul(x, y):
    return x * y

@app.task
def xsum(numbers):
    return sum(numbers)
