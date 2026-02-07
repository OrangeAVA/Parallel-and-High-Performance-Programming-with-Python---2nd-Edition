# Basic quantum circuits: single-qubit Hadamard, entanglement with CNOT, and measurement histogram.
import os
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, transpile
from utils.sim import get_simulator

OUTDIR = os.path.join(os.path.dirname(__file__), "..", "outputs")
os.makedirs(OUTDIR, exist_ok=True)

# 1) Single qubit with Hadamard (superposition)
qc_h = QuantumCircuit(1, 1)
qc_h.h(0)
qc_h.measure(0, 0)

# 2) Entanglement with H + CNOT and measure both qubits
qc_ent = QuantumCircuit(2, 2)
qc_ent.h(0)
qc_ent.cx(0, 1)
qc_ent.measure([0,1], [0,1])

# Run both and plot histograms
sim = get_simulator()

# Superposition run
compiled_h = transpile(qc_h, sim)
res_h = sim.run(compiled_h, shots=1000).result()
counts_h = res_h.get_counts()
plt.figure()
plt.bar(counts_h.keys(), counts_h.values())
plt.title("Hadamard superposition measurements")
plt.xlabel("State"); plt.ylabel("Occurrences")
plt.tight_layout()
plt.savefig(os.path.join(OUTDIR, "hadamard_hist.png"), dpi=150)
plt.close()

# Entanglement run
compiled_ent = transpile(qc_ent, sim)
res_ent = sim.run(compiled_ent, shots=1000).result()
counts_ent = res_ent.get_counts()
plt.figure()
plt.bar(counts_ent.keys(), counts_ent.values())
plt.title("Entanglement (H + CNOT) measurements")
plt.xlabel("State"); plt.ylabel("Occurrences")
plt.tight_layout()
plt.savefig(os.path.join(OUTDIR, "entanglement_hist.png"), dpi=150)
plt.close()

# Save ASCII drawings of circuits
with open(os.path.join(OUTDIR, "circuit_h.txt"), "w") as fh:
    fh.write(QuantumCircuit(1).h(0).draw(output="text") if False else qc_h.draw(output="text"))
with open(os.path.join(OUTDIR, "circuit_entanglement.txt"), "w") as fh:
    fh.write(qc_ent.draw(output="text"))
print("Done. Outputs saved in:", os.path.abspath(OUTDIR))