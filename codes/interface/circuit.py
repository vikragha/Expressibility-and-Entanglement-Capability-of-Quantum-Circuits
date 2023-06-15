import typing
import numpy as np
import sympy

import qiskit
import qiskit.quantum_info


def convert_to_qiskit(circuit: qiskit.QuantumCircuit) -> qiskit.QuantumCircuit:
    """Converts the circuit to Qiskit format.
    :param circuit: Input circuit in Qiskit format
    :return: Circuit in Qiskit format
    """
    return circuit


class CircuitDescriptor:
    """The interface for users to provide a circuit in Qiskit and visualize it in qLEET.

    It consists of 3 parts:
    * Circuit: which has the full ansatz preparation from the start where
    * Params: list of parameters which are used to parameterize the circuit
    * Cost Function: presently a Pauli String, which we measure to get the
        output we are optimizing over

    Combined they form the full the parameterized quantum circuit from the initial qubits to the end
    measurement.
    """

    def __init__(
        self,
        circuit: qiskit.QuantumCircuit,
        params: typing.List[typing.Union[sympy.Symbol, qiskit.circuit.Parameter]],
        cost_function: typing.Union[qiskit.quantum_info.PauliList, None] = None,
    ):
        """Constructor for the CircuitDescriptor.

        :param circuit: The full circuit which generates the required quantum state
        :param params: List of parameters to optimize over
        :param cost_function: Measurement operation as a PauliString
        """
        self._circuit = circuit
        self._params = params
        self._cost = cost_function

    @property
    def default_backend(self) -> str:
        """Returns the backend in which the user had provided the circuit.
        :returns: The name of the default backend
        :rtype: str
        """
        return "qiskit"

    @classmethod
    def from_qasm(
        cls,
        qasm_str: str,
        params: typing.List[typing.Union[sympy.Symbol, qiskit.circuit.Parameter]],
        cost_function: typing.Union[qiskit.quantum_info.PauliList, None] = None,
        backend: str = "qiskit",
    ):
        """Generate the descriptor from OpenQASM string.

        :param qasm_str: OpenQASM string for each part of the circuit
        :param params: List of sympy symbols which act as parameters for the PQC
        :param cost_function: Pauli-string operator to implement the cost function
        :param backend: Backend for the circuit descriptor objects
        :return: The CircuitDescriptor object
        """
        circuit = qiskit.QuantumCircuit.from_qasm_str(qasm_str)
        return CircuitDescriptor(
            circuit=circuit, params=params, cost_function=cost_function
        )

    @property
    def parameters(
        self,
    ) -> typing.List[typing.Union[sympy.Symbol, qiskit.circuit.Parameter]]:
        """The list of sympy symbols to resolve as parameters, will be swept from 0 to 2*pi.
        :return: List of parameters
        """
        return self._params

    def __len__(self) -> int:
        """Number of parameters in the variational circuit.
        :return: Number of parameters in the circuit
        """
        return len(self.parameters)

    @property
    def qiskit_circuit(self) -> qiskit.QuantumCircuit:
        """Get the circuit in Qiskit.
        :return: The Qiskit representation of the circuit
        :rtype: qiskit.QuantumCircuit
        """
        return self._circuit

    @property
    def num_qubits(self) -> int:
        """Get the number of qubits for a circuit.
        :return: The number of qubits in the circuit
        :rtype: int
        """
        return self._circuit.num_qubits

    @property
    def qiskit_cost(self) -> qiskit.quantum_info.PauliList:
        """Returns the cost function, which is a function that takes in the state vector or the
        density matrix and returns the loss value of the solution envisioned by the Quantum Circuit.
        :return: Cost function
        :rtype: qiskit.quantum_info.PauliList
        """
        return self._cost

    def __eq__(self, other: typing.Any) -> bool:
        """Checks equality between a CircuitDescriptor and another object"""
        if isinstance(other, CircuitDescriptor):
            return (
                np.array_equal(self.parameters, other.parameters)
                and self.qiskit_circuit == other.qiskit_circuit
            )
        return False

    def __repr__(self) -> str:
        """Prints the representation of the CircuitDescriptor.
        You can eval this to get the object back.

        :returns: The repr string
        :rtype: str
        """
        return f"qleet.CircuitDescriptor({repr(self._circuit)}, {repr(self._params)})"

    def __str__(self) -> str:
        """Prints the string form of the CircuitDescriptor.

        :returns: The string form
        :rtype: str
        """
        return f"qleet.CircuitDescriptor({repr(self._circuit)})"
