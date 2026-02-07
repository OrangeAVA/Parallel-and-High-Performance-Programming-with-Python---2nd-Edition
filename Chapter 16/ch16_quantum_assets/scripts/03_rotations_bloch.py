# Demonstrate Rx rotation by pi/4 on the Bloch sphere
import os, numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector

OUTDIR = os.path.join(os.path.dirname(__file__), "..", "outputs")
os.makedirs(OUTDIR, exist_ok=True)

qc = QuantumCircuit(1)
qc.rx(np.pi/4, 0)
state = Statevector.from_instruction(qc)

fig = plot_bloch_multivector(state)
fig.savefig(os.path.join(OUTDIR, "bloch_rx_pi_over_4.png"), dpi=150, bbox_inches="tight")
plt.close(fig)
print("Saved Bloch sphere with Rx(pi/4) rotation.")