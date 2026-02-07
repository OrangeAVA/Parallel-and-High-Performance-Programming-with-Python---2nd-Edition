# QNN classifier demo with EstimatorQNN (ZZFeatureMap + RealAmplitudes), 2 qubits.
import os
import numpy as np
import matplotlib.pyplot as plt
import logging

from qiskit.circuit.library import ZZFeatureMap, RealAmplitudes
from qiskit_machine_learning.neural_networks import EstimatorQNN
from qiskit.primitives import StatevectorEstimator

logging.getLogger("qiskit_machine_learning").setLevel(logging.ERROR)
logging.getLogger("qiskit.primitives").setLevel(logging.ERROR)

OUTDIR = os.path.join(os.path.dirname(__file__), "..", "outputs")
os.makedirs(OUTDIR, exist_ok=True)

num_qubits = 2
estimator = StatevectorEstimator()
feature_map = ZZFeatureMap(feature_dimension=num_qubits, reps=2)
ansatz = RealAmplitudes(num_qubits, reps=2)
circuit = feature_map.compose(ansatz)

qnn = EstimatorQNN(
    circuit=circuit,
    input_params=feature_map.parameters,
    weight_params=ansatz.parameters,
    estimator=estimator
)

rng = np.random.RandomState(7)
weights = rng.rand(len(ansatz.parameters))

def normalize_output(x):
    return (x + 1)/2.0

# Sample inputs
inputs = np.array([
    [0.1, 0.2],
    [0.5, 1.5],
    [0.8, 0.9],
    [0.3, 0.7],
    [0.9, 1.0],
])

outputs = [normalize_output(qnn.forward(input_data=x, weights=weights).item()) for x in inputs]
classes = [1 if y > 0.5 else 0 for y in outputs]

# Scatter
plt.figure(figsize=(6,4))
for x, c in zip(inputs, classes):
    plt.scatter(x[0], x[1], c="red" if c==1 else "blue", label=f"Class {c}")
# Avoid duplicate labels in legend
handles, labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys())
plt.xlabel("Feature 1"); plt.ylabel("Feature 2")
plt.title("QNN Classification (toy)")
plt.tight_layout()
plt.savefig(os.path.join(OUTDIR, "qnn_classification.png"), dpi=150)
plt.close()

print("Saved QNN classification plot to outputs/qnn_classification.png")