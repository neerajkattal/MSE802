from qiskit import QuantumCircuit
import random

qc = QuantumCircuit(3)

gates = ['h', 'x', 'y', 'z']

# Apply random gates
for i in range(5):
    qubit = random.randint(0, 2)
    gate = random.choice(gates)

    if gate == 'h':
        qc.h(qubit)
    elif gate == 'x':
        qc.x(qubit)
    elif gate == 'y':
        qc.y(qubit)
    elif gate == 'z':
        qc.z(qubit)

# Add some entanglement
qc.cx(0, 1)
qc.cx(1, 2)

# Draw circuit
qc.draw('mpl')