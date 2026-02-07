# Demonstrate 2-qubit superposition (quantum parallelism demo)
import matplotlib.pyplot as plt
import os
from qiskit import QuantumCircuit, transpile
from utils.sim import get_simulator

OUTDIR = os.path.join(os.path.dirname(__file__), "..", "outputs")
os.makedirs(OUTDIR, exist_ok=True)

qc = QuantumCircuit(2, 2)
qc.h([0,1])
qc.measure([0,1], [0,1])

sim = get_simulator()
compiled = transpile(qc, sim)
res = sim.run(compiled, shots=1000).result()
counts = res.get_counts()

plt.figure()
plt.bar(counts.keys(), counts.values())
plt.title("Quantum Parallelism: |00>,|01>,|10>,|11> ~ uniform")
plt.xlabel("State"); plt.ylabel("Occurrences")
plt.tight_layout()
plt.savefig(os.path.join(OUTDIR, "parallelism_hist.png"), dpi=150)
plt.close()
print("Saved histogram to outputs/parallelism_hist.png")