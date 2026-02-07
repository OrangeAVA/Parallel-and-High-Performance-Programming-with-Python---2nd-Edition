from celery import Celery
from kombu import Queue, Exchange

app = Celery('myapp', broker='redis://localhost//', backend='redis://localhost/')
app.conf.broker_connection_retry_on_startup = True

# Define queues and exchanges
app.conf.task_queues = (
    Queue('default', Exchange('default'), routing_key='default'),
    Queue('high_priority', Exchange('priority'), routing_key='high.#'),
    Queue('low_priority',  Exchange('priority'), routing_key='low.#'),
)

# Routing rules
app.conf.task_routes = {
    'tasks.send_email':      {'queue': 'high_priority'},
    'tasks.process_data':    {'queue': 'low_priority'},
    'tasks.backup_database': {'queue': 'default'},
}

# Misc
app.conf.imports = ('tasks',)
app.conf.task_default_queue = 'default'
app.conf.task_default_exchange = 'default'
app.conf.task_default_routing_key = 'default'
app.conf.result_expires = 3600
