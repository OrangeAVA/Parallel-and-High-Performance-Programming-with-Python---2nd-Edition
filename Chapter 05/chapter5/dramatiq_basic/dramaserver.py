import dramatiq
import time

# Tip: For Redis broker, you can configure via environment variables or explicit setup.
# This minimal example relies on defaults when launched with `dramatiq dramaserver`.

@dramatiq.actor
def wait(t, n):
    time.sleep(t)
    print(f"I am the actor {n} and I will wait for {t} secs")
