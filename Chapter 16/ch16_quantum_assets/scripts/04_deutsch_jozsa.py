# Deutsch-Jozsa algorithm for n=2 with a balanced oracle (XOR)
# Prints counts (should be '11' for balanced oracle with 2 inputs).
from qiskit import QuantumCircuit, transpile
from utils.sim import get_simulator

n = 2  # number of input qubits
qc = QuantumCircuit(n + 1, n)

# Initialize aux qubit in |1> then H
qc.x(n)
qc.h(n)

# H on input qubits
for i in range(n):
    qc.h(i)

# Balanced oracle: XOR of input qubits into aux (two CNOTs)
qc.cx(0, n)
qc.cx(1, n)

# H again on input qubits
for i in range(n):
    qc.h(i)

# Measure only the input qubits
qc.measure(range(n), range(n))

sim = get_simulator()
compiled = transpile(qc, sim)
res = sim.run(compiled, shots=1000).result()
print("Deutsch-Jozsa counts:", res.get_counts())