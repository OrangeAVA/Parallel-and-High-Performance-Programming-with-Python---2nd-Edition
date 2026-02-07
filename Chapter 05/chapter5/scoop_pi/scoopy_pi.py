from scoop import futures
import random

def simulate_points(n_points):
    inside = 0
    for _ in range(n_points):
        x, y = random.random(), random.random()
        if x*x + y*y <= 1:
            inside += 1
    return inside

def main():
    n_points_total = 10_000_00  # 1e6 (adjust up for more accuracy)
    n_workers = 4
    n_points_per_worker = n_points_total // n_workers
    results = futures.map(simulate_points, [n_points_per_worker] * n_workers)
    total_inside = sum(results)
    pi_estimate = 4 * total_inside / n_points_total
    print(f"Estimate value of pi: {pi_estimate}")

if __name__ == "__main__":
    main()
