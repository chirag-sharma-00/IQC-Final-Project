''' 
Implementation of the Quantum Fourier Transform for a 3 qubit input.
This case is discussed as an example on https://en.wikipedia.org/wiki/Quantum_Fourier_transform 
'''

import cirq
import numpy as np

#Returns the matrix for the controlled phase gate R_k.
def R(k):
	p = np.e ** ((2 * np.pi * 1j)/(2 ** k))
	return cirq.TwoQubitMatrixGate(np.array([[1, 0, 0, 0],
											 [0, 1, 0, 0],
											 [0, 0, 1, 0],
											 [0, 0, 0, p]]))


#Prints the result of measuring the 3 qubits after applying QFT to them.
def main():
	qubits = [cirq.NamedQubit('q{}'.format(i)) for i in range(3)]
	circuit = cirq.Circuit(
		cirq.H(qubits[2]),
		R(2)(qubits[1], qubits[2]),
		cirq.H(qubits[1]),
		R(3)(qubits[0], qubits[2]),
		R(2)(qubits[0], qubits[1]),
		cirq.H(qubits[0]),
		cirq.measure(qubits[0], key='c0'),
    	cirq.measure(qubits[1], key='c1'),
    	cirq.measure(qubits[2], key='c2'),
		)
	print('Circuit:')
	print(circuit)
	simulator = cirq.Simulator()
	result = simulator.run(circuit)
	print()
	print('Measured bits:')
	print(result)