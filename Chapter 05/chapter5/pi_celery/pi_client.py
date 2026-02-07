from pi_calculator import run_simulation, simulate_points, calculate_pi
from celery import group

# Two ways to run: 1) group + get + calculate locally; 2) single chord via run_simulation

# 1) Group then reduce manually
n_points_per_task = 200_000
n_tasks = 10
grp_res = group(simulate_points.s(n_points_per_task) for _ in range(n_tasks))()
partials = grp_res.get()
pi1 = calculate_pi(partials)
print("Pi (manual reduce):", pi1)

# 2) Single chord
chord_res = run_simulation.delay(n_points_per_task, n_tasks)
print("Pi (chord):", chord_res.get())
