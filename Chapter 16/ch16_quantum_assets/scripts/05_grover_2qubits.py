# Grover's algorithm for 2-qubit search (target = |11>)
from qiskit import QuantumCircuit, transpile
from utils.sim import get_simulator

qc = QuantumCircuit(2, 2)

# 1) Create uniform superposition
qc.h([0,1])

# 2) Oracle: flip phase on |11>
qc.cz(0,1)

# 3) Diffusion operator
qc.h([0,1])
qc.x([0,1])
qc.h(1)
qc.cx(0,1)
qc.h(1)
qc.x([0,1])
qc.h([0,1])

# Measurement
qc.measure([0,1], [0,1])

sim = get_simulator()
compiled = transpile(qc, sim)
res = sim.run(compiled, shots=1000).result()
print("Grover 2-qubit counts:", res.get_counts())