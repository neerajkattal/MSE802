from qiskit import QuantumCircuit, Aer, execute

# Define QASM string
qasm_code = """
OPENQASM 2.0;
include "qelib1.inc";

qreg q[2];
creg c[2];

h q[0];
cx q[0], q[1];
measure q -> c;
"""

# Load circuit from QASM
qc = QuantumCircuit.from_qasm_str(qasm_code)

# Simulate
simulator = Aer.get_backend('qasm_simulator')
result = execute(qc, simulator).result()

# Output
counts = result.get_counts()
print(counts)

# Draw circuit
qc.draw('mpl')