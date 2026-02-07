from celery import Celery, group, chord
import random

app = Celery('pi_calculator', broker='redis://localhost//', backend='redis://localhost')
app.conf.broker_connection_retry_on_startup = True

@app.task
def simulate_points(n_points: int):
    inside = 0
    for _ in range(n_points):
        x, y = random.random(), random.random()
        if x*x + y*y <= 1.0:
            inside += 1
    return {'inside': inside, 'total': n_points}

@app.task
def calculate_pi(partials):
    total_points = sum(d['total'] for d in partials)
    inside = sum(d['inside'] for d in partials)
    return 4.0 * inside / total_points

@app.task
def run_simulation(n_points_per_task: int, n_tasks: int):
    sims = group(simulate_points.s(n_points_per_task) for _ in range(n_tasks))
    return chord(sims, calculate_pi.s())()
