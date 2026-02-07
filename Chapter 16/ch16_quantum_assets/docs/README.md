# Chapter 16 – Quantum Computing Assets (Qiskit, Gates, DJ & Grover, QNN)

This bundle contains runnable Python scripts that mirror the examples from Chapter 16:
quantum gates, Bloch sphere, superposition/parallelism, Deutsch–Jozsa, Grover,
and small Quantum Neural Network demos (classification + regression).

## Contents
- `scripts/01_basic_circuits.py` — Hadamard superposition + entanglement (H + CNOT) with histograms.
- `scripts/02_bloch_sphere.py` — Bloch sphere for a |0> -> H superposition (saved as PNG).
- `scripts/03_rotations_bloch.py` — Bloch sphere after an Rx(pi/4) rotation.
- `scripts/04_deutsch_jozsa.py` — Deutsch–Jozsa for n=2 with a balanced oracle (XOR).
- `scripts/05_grover_2qubits.py` — Grover search for the |11> marked state (N=4).
- `scripts/06_superposition_parallelism.py` — 2‑qubit superposition (uniform counts over 4 states).
- `scripts/07_qnn_classifier.py` — Toy QNN classifier via `EstimatorQNN` (ZZFeatureMap + RealAmplitudes).
- `scripts/08_qnn_regression_sin.py` — 1‑qubit QNN regresses `y = sin(x)` on [0, π] via finite‑diff training.
- `utils/sim.py` — Helper that prefers `AerSimulator` and falls back to `BasicAer` if needed.
- `requirements.txt` — Python dependencies (Qiskit, Aer, ML, plotting).
- `environment.yml` — Optional Conda environment file.

All scripts save figures under `outputs/` alongside the scripts.

## Setup

**Option A – pip (recommended)**
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -U pip
pip install -r requirements.txt
```

**Option B – Conda**
```bash
conda env create -f environment.yml
conda activate qc-ch16
```

### Notes on Qiskit packages
- `qiskit` provides circuits/transpilation.
- `qiskit-aer` provides fast simulators (`AerSimulator`).
- `qiskit-machine-learning` provides `EstimatorQNN` used in QNN demos.
- If `AerSimulator` is unavailable, we try to fall back to `BasicAer` (older Qiskit) via `utils/sim.py`.

### Common hiccups
- **Plot windows don’t appear:** scripts save plots to PNG files in `outputs/`.
- **qiskit-aer install issues (Apple Silicon/Windows):** ensure a current Python (>=3.9) and latest pip.
- **Warnings like “No gradient function provided”:** harmless; the demo builds a finite‑difference gradient.

## Run examples

From the project root:
```bash
python scripts/01_basic_circuits.py
python scripts/02_bloch_sphere.py
python scripts/03_rotations_bloch.py
python scripts/04_deutsch_jozsa.py
python scripts/05_grover_2qubits.py
python scripts/06_superposition_parallelism.py
python scripts/07_qnn_classifier.py
python scripts/08_qnn_regression_sin.py
```

## IBM Quantum real hardware (optional)
These scripts use simulators. To run on real hardware, create an IBM Quantum account and
swap the simulator backend with an IBMQ provider backend; keep shot counts low and be
mindful of queue times and noise.

---
© Chapter 16 support pack.