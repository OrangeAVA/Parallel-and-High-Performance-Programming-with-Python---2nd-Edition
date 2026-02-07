def get_simulator():
    """Return an AerSimulator if available, else fall back to BasicAer qasm_simulator."""
    try:
        from qiskit_aer import AerSimulator
        return AerSimulator()
    except Exception:
        try:
            # BasicAer is deprecated in newer Qiskit, but this provides a fallback.
            from qiskit import BasicAer
            return BasicAer.get_backend('qasm_simulator')
        except Exception as e:
            raise RuntimeError("No Qiskit simulator backend available. Install qiskit-aer or a compatible backend.") from e