from tasks import add
# Basic fire-and-forget enqueue
r1 = add.delay(4, 4)
# Or via apply_async
r2 = add.apply_async(args=[10, 5])

print("Queued tasks. If you have a result backend configured, you can .get():")
try:
    print("add(4,4) =", r1.get(timeout=10))
    print("add(10,5) =", r2.get(timeout=10))
except Exception as e:
    print("Could not fetch results (did you configure a backend?):", e)
