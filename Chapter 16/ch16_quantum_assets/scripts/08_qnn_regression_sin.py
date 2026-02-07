# QNN regression demo: approximate y = sin(x) on [0, pi] with 1 qubit using EstimatorQNN.
import numpy as np
import matplotlib.pyplot as plt
from qiskit.circuit import QuantumCircuit, Parameter
from qiskit.circuit.library import RealAmplitudes
from qiskit_machine_learning.neural_networks import EstimatorQNN
from qiskit.primitives import StatevectorEstimator
import os, logging

logging.getLogger("qiskit_machine_learning").setLevel(logging.ERROR)
logging.getLogger("qiskit.primitives").setLevel(logging.ERROR)

OUTDIR = os.path.join(os.path.dirname(__file__), "..", "outputs")
os.makedirs(OUTDIR, exist_ok=True)

# Model
num_qubits = 1
estimator = StatevectorEstimator()
x_param = Parameter("x")
feature_map = QuantumCircuit(1)
feature_map.ry(x_param, 0)
ansatz = RealAmplitudes(num_qubits, reps=2)
circuit = feature_map.compose(ansatz)

qnn = EstimatorQNN(
    circuit=circuit,
    input_params=[x_param],
    weight_params=ansatz.parameters,
    estimator=estimator
)

# Data
rng = np.random.RandomState(42)
x_train = np.linspace(0.0, np.pi, 12)
y_train = np.sin(x_train)              # [0,1] on [0, pi]
y_train_scaled = 2*y_train - 1         # scale to [-1,1]

def preds_scaled(qnn, x_vals, w):
    return np.array([qnn.forward(input_data=[float(xv)], weights=w).item() for xv in x_vals])

def mse_loss(qnn, x_vals, y_scaled, w):
    p = preds_scaled(qnn, x_vals, w)
    return np.mean((p - y_scaled)**2)

def fd_grad_on_loss(qnn, x_vals, y_scaled, w, eps=1e-2):
    g = np.zeros_like(w, dtype=float)
    for i in range(len(w)):
        w_plus  = w.copy(); w_plus[i]  += eps
        w_minus = w.copy(); w_minus[i] -= eps
        l_plus  = mse_loss(qnn, x_vals, y_scaled, w_plus)
        l_minus = mse_loss(qnn, x_vals, y_scaled, w_minus)
        g[i] = (l_plus - l_minus) / (2*eps)
    return g

# Train (simple finite-difference GD)
weights = rng.rand(len(ansatz.parameters))
lr = 0.2
for epoch in range(40):
    grad = fd_grad_on_loss(qnn, x_train, y_train_scaled, weights)
    weights -= lr * grad
    if (epoch+1) % 10 == 0:
        print(f"Epoch {epoch+1:02d}  Loss: {mse_loss(qnn, x_train, y_train_scaled, weights):.4f}")

# Evaluate
x_test = np.linspace(0.0, np.pi, 60)
y_true = np.sin(x_test)
y_pred_scaled = preds_scaled(qnn, x_test, weights)
y_pred = (y_pred_scaled + 1)/2

# Plot
plt.figure(figsize=(6,4))
plt.plot(x_test, y_true, label="sin(x)")
plt.scatter(x_test, y_pred, s=10, label="QNN predictions")
plt.xlabel("x"); plt.ylabel("y")
plt.title("QNN Regression: sin(x)")
plt.legend()
plt.tight_layout()
outpath = os.path.join(OUTDIR, "qnn_regression_sin.png")
plt.savefig(outpath, dpi=150)
plt.close()
print("Saved regression plot to", outpath)