from celery import group, chain, chord
from tasks import add, mul, xsum

# GROUP: run many independent tasks and collect all results
g = group(add.s(i, i) for i in range(10))()
print("GROUP results:", g.get())

# CHAIN: pipe result from one task into the next
c = chain(add.s(4, 4) | mul.s(8))()
print("CHAIN result:", c.get())

# CHORD: fan-out (group) + fan-in (callback)
# Requires a backend that supports chords (Redis, Database, Memcached, ...).
ch = chord((add.s(i, i) for i in range(10)), xsum.s())()
print("CHORD result:", ch.get())
