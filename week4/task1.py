from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_state_qsphere
import matplotlib.pyplot as plt

# Create circuit
qc = QuantumCircuit(2)

# Put qubit in superposition
qc.h(0)

# Apply 90° phase shift (S gate)
qc.s(0)

# Entangle
qc.cx(0, 1)

# Get statevector
state = Statevector.from_instruction(qc)

# Plot Q-sphere
plot_state_qsphere(state)
plt.show()

