# This code is part of Qiskit.
#
# (C) Copyright IBM 2022.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""Parametric Circuit Module"""

from typing import Any
import numpy as np
import pennylane as qml


class Ansatz:

    """
    This class creates methods to create the parameteric circuits
    mentioned in https://doi.org/10.1007/s42484-021-00038-w with random
    parameters as initialization routine for testing the experessibility
    and entangling capacity of a given parametric circuit.

    """

    def __init__(self, repitition, feature_dim, circuit_id) -> None:

        """
        Args:
            repitition: The no of repitition of the layers of parametric circuit
            feature_dim: The no. of qubits required for a the parametric circuit
            circuit_id: The id of the circuit in the order mentioned in
                        https://doi.org/10.1007/s42484-021-00038-w to get the
                        particular circuit.
        """
        self.repitition = repitition
        self.feature_dim = feature_dim
        self.circuit_id = circuit_id

      def get_ansatz(self):
          if self.circuit_id == 1:
              return self.circuit_1_pennylane()
          elif self.circuit_id == 2:
              return self.circuit_2_pennylane()
          elif self.circuit_id == 3:
              return self.circuit_3_pennylane()
          elif self.circuit_id == 4:
              return self.circuit_4_pennylane()
          elif self.circuit_id == 5:
              return self.circuit_5_pennylane()
          elif self.circuit_id == 6:
              return self.circuit_6_pennylane()
          elif self.circuit_id == 7:
              return self.circuit_7_pennylane()
          elif self.circuit_id == 8:
              return self.circuit_8_pennylane()
          elif self.circuit_id == 9:
              return self.circuit_9_pennylane()
          elif self.circuit_id == 10:
              return self.circuit_10_pennylane()
          elif self.circuit_id == 11:
              return self.circuit_11_pennylane()
          elif self.circuit_id == 12:
              return self.circuit_12_pennylane()
          elif self.circuit_id == 13:
              return self.circuit_13_pennylane()
          elif self.circuit_id == 14:
              return self.circuit_14_pennylane()
          elif self.circuit_id == 15:
              return self.circuit_15_pennylane()
          elif self.circuit_id == 16:
              return self.circuit_16_pennylane()
          elif self.circuit_id == 17:
              return self.circuit_17_pennylane()
          elif self.circuit_id == 18:
              return self.circuit_18_pennylane()
          elif self.circuit_id == 19:
              return self.circuit_19_pennylane()
          else:
              raise ValueError("Invalid circuit ID")


    def circuit_1_pennylane(self):
        dev = qml.device("default.qubit", wires=self.feature_dim)
        
        @qml.qnode(dev)
        def circuit_1(*params):
            for _ in range(self.repitition):
                for i in range(self.feature_dim):
                    qml.RX(params[2 * i], wires=i)
                    qml.RZ(params[2 * i + 1], wires=i)
            return [qml.expval(qml.PauliZ(i)) for i in range(self.feature_dim)]
        return circuit_1
      

    def circuit_2_pennylane(self):
        dev = qml.device("default.qubit", wires=self.feature_dim)
        
        @qml.qnode(dev)
        def circuit_2(*params):
            for _ in range(self.repitition):
                for i in range(self.feature_dim):
                    qml.RX(params[i], wires=i)
                    qml.RZ(params[i + 1], wires=i)
                for i in reversed(range(self.feature_dim - 1)):
                    qml.CNOT(wires=[i + 1, i])
            return [qml.expval(qml.PauliZ(i)) for i in range(self.feature_dim)]
        return circuit_2

    def circuit_3_pennylane(self):
        dev = qml.device("default.qubit", wires=self.feature_dim)
        
        @qml.qnode(dev)
        def circuit_3(*params):
            for _ in range(self.repitition):
                for i in range(self.feature_dim):
                    qml.RX(params[i], wires=i)
                    qml.RZ(params[i + 1], wires=i)
                for i in reversed(range(self.feature_dim - 1)):
                    qml.CRZ(params[i + self.feature_dim], wires=[i + 1, i])
            return [qml.expval(qml.PauliZ(i)) for i in range(self.feature_dim)]

        return circuit_3

    def circuit_4_pennylane(self):
        dev = qml.device("default.qubit", wires=self.feature_dim)
        
        @qml.qnode(dev)
        def circuit_4(*params):
            for _ in range(self.repitition):
                for i in range(self.feature_dim):
                    qml.RX(params[2 * i], wires=i)
                    qml.RZ(params[2 * i + 1], wires=i)
                for i in reversed(range(self.feature_dim - 1)):
                    qml.CRX(params[self.feature_dim + i], wires=[i + 1, i])
            return [qml.expval(qml.PauliZ(i)) for i in range(self.feature_dim)]
        return circuit_4

    def circuit_5_pennylane(self):
        dev = qml.device("default.qubit", wires=self.feature_dim)
        
        @qml.qnode(dev)
        def circuit_5(*params):
            paravec = params[:2]
            paravec_2 = params[2:]
            
            blocks = []
            for block in reversed(range(self.feature_dim)):
                block_circ = qml.QubitCircuit(self.feature_dim)
                p_pointer = 0
                for i in reversed(range(self.feature_dim)):
                    if i != block:
                        block_circ.CRZ(paravec_2[p_pointer], wires=[block, i])
                        p_pointer += 1
                blocks.append(block_circ)

            rot_layer = qml.QubitCircuit(1)
            rot_layer.RX(paravec[0], wires=0)
            rot_layer.RZ(paravec[1], wires=0)

            ansatz = qml.templates.NLocal(
                wires=self.feature_dim,
                rotation_blocks=rot_layer,
                entanglement_blocks=blocks,
                reps=self.repitition,
            )

            return [qml.expval(qml.PauliZ(i)) for i in range(self.feature_dim)]

        return circuit_5

    def circuit_6_pennylane(self):
        dev = qml.device("default.qubit", wires=self.feature_dim)
        
        @qml.qnode(dev)
        def circuit_6(*params):
            paravec = params[:2]
            paravec_2 = params[2:]
            
            blocks = []
            for block in reversed(range(self.feature_dim)):
                block_circ = qml.QubitCircuit(self.feature_dim)
                p_pointer = 0
                for i in reversed(range(self.feature_dim)):
                    if i != block:
                        block_circ.CRX(paravec_2[p_pointer], wires=[block, i])
                        p_pointer += 1
                blocks.append(block_circ)

            rot_layer = qml.QubitCircuit(1)
            rot_layer.RX(paravec[0], wires=0)
            rot_layer.RZ(paravec[1], wires=0)

            ansatz = qml.templates.NLocal(
                wires=self.feature_dim,
                rotation_blocks=rot_layer,
                entanglement_blocks=blocks,
                reps=self.repitition,
            )

            return [qml.expval(qml.PauliZ(i)) for i in range(self.feature_dim)]

        return circuit_6

    def circuit_7_pennylane(self):
        dev = qml.device("default.qubit", wires=self.feature_dim)
        
        @qml.qnode(dev)
        def circuit_7(*params):
            paravec = params[:2 * self.feature_dim * self.repitition]
            arg_count = 0
            
            for _ in range(self.repitition):
                for i in range(dev.num_wires):
                    qml.RX(paravec[arg_count], wires=i)
                    qml.RZ(paravec[arg_count + 1], wires=i)
                    arg_count += 2

                for i in range(0, dev.num_wires - 1, 2):
                    qml.CRZ(paravec[arg_count], wires=[i, i + 1])
                    arg_count += 1
                qml.barrier()

                for i in range(dev.num_wires):
                    qml.RX(paravec[arg_count], wires=i)
                    qml.RZ(paravec[arg_count + 1], wires=i)
                    arg_count += 2

                for i in range(1, dev.num_wires - 1, 2):
                    qml.CRZ(paravec[arg_count], wires=[i, i + 1])
                    arg_count += 1

            return [qml.expval(qml.PauliZ(i)) for i in range(self.feature_dim)]

        return circuit_7


    def circuit_8_pennylane(self):
        dev = qml.device("default.qubit", wires=self.feature_dim)
        
        @qml.qnode(dev)
        def circuit_8(*params):
            paravec = params[:2 * self.feature_dim * self.repitition]
            arg_count = 0
            
            for _ in range(self.repitition):
                for i in range(dev.num_wires):
                    qml.RX(paravec[arg_count], wires=i)
                    qml.RZ(paravec[arg_count + 1], wires=i)
                    arg_count += 2

                for i in range(0, dev.num_wires - 1, 2):
                    qml.CRX(paravec[arg_count], wires=[i, i + 1])
                    arg_count += 1
                qml.barrier()

                for i in range(dev.num_wires):
                    qml.RX(paravec[arg_count], wires=i)
                    qml.RZ(paravec[arg_count + 1], wires=i)
                    arg_count += 2

                for i in range(1, dev.num_wires - 1, 2):
                    qml.CRX(paravec[arg_count], wires=[i, i + 1])
                    arg_count += 1

            return [qml.expval(qml.PauliZ(i)) for i in range(self.feature_dim)]

        return circuit_8

    def circuit_9_pennylane(self):
        dev = qml.device("default.qubit", wires=self.feature_dim)
        
        @qml.qnode(dev)
        def circuit_9(*params):
            paravec = params[:self.feature_dim * self.repitition]
            arg_count = 0
            
            for _ in range(self.repitition):
                for i in range(self.feature_dim):
                    qml.Hadamard(wires=i)
                for i in reversed(range(self.feature_dim - 1)):
                    qml.CZ(wires=[i + 1, i])
                for i in range(self.feature_dim):
                    qml.RX(paravec[arg_count], wires=i)
                    arg_count += 1

            return [qml.expval(qml.PauliZ(i)) for i in range(self.feature_dim)]
        return circuit_9

    def circuit_10_pennylane(self):
        dev = qml.device("default.qubit", wires=self.feature_dim)

        @qml.qnode(dev)
        def circuit_10(*params):
            for i in range(self.feature_dim):
                qml.RY(params[i], wires=i)
            for i in range(self.feature_dim - 1):
                qml.CZ(wires=[i, i + 1])
            for i in range(self.feature_dim):
                qml.RX(params[i + self.feature_dim], wires=i)
            return [qml.expval(qml.PauliZ(i)) for i in range(self.feature_dim)]

        return circuit_10


    def circuit_11_pennylane(self):
        dev = qml.device("default.qubit", wires=self.feature_dim)

        @qml.qnode(dev)
        def circuit_11(*params):
            for _ in range(self.repetition):
                for i in range(self.feature_dim):
                    qml.RX(params[2 * i], wires=i)
                    qml.RZ(params[2 * i + 1], wires=i)

                for i in range(0, self.feature_dim - 1, 2):
                    qml.CNOT(wires=[i, i + 1])

                for i in range(1, self.feature_dim - 1, 2):
                    qml.RY(params[4 * self.feature_dim + (i - 1) * 4], wires=i)
                    qml.RZ(params[4 * self.feature_dim + (i - 1) * 4 + 1], wires=i)
                    qml.RY(params[4 * self.feature_dim + (i - 1) * 4 + 2], wires=i + 1)
                    qml.RZ(params[4 * self.feature_dim + (i - 1) * 4 + 3], wires=i + 1)

                for i in range(1, self.feature_dim - 1, 2):
                    qml.CNOT(wires=[i, i + 1])

            return [qml.expval(qml.PauliZ(i)) for i in range(self.feature_dim)]

        return circuit_11

    def circuit_12_pennylane(self):
        dev = qml.device("default.qubit", wires=self.feature_dim)

        @qml.qnode(dev)
        def circuit_12(*params):
            for _ in range(self.repetition):
                for i in range(self.feature_dim):
                    qml.RX(params[2 * i], wires=i)
                    qml.RZ(params[2 * i + 1], wires=i)

                for i in range(0, self.feature_dim - 1, 2):
                    qml.CNOT(wires=[i, i + 1])

                for i in range(1, self.feature_dim - 1, 2):
                    qml.RY(params[4 * self.feature_dim + (i - 1) * 4], wires=i)
                    qml.RZ(params[4 * self.feature_dim + (i - 1) * 4 + 1], wires=i)
                    qml.RY(params[4 * self.feature_dim + (i - 1) * 4 + 2], wires=i + 1)
                    qml.RZ(params[4 * self.feature_dim + (i - 1) * 4 + 3], wires=i + 1)

                for i in range(1, self.feature_dim - 1, 2):
                    qml.CNOT(wires=[i + 1, i])

            return [qml.expval(qml.PauliZ(i)) for i in range(self.feature_dim)]

        return circuit_12

    def circuit_13_pennylane(self):
        dev = qml.device("default.qubit", wires=self.feature_dim)

        @qml.qnode(dev)
        def circuit_13(*params):
            for _ in range(self.repetition):
                for i in range(self.feature_dim):
                    qml.RY(params[i], wires=i)

                qml.CRZ(params[self.feature_dim], wires=[self.feature_dim - 1, 0])

                for i in range(self.feature_dim - 1):
                    qml.CRZ(params[self.feature_dim + 1 + i], wires=[i, i + 1])

                for i in range(self.feature_dim):
                    qml.RY(params[2 * self.feature_dim + 1 + i], wires=i)

                qml.CRZ(params[3 * self.feature_dim + 1], wires=[self.feature_dim - 1, self.feature_dim - 2])
                qml.CRZ(params[3 * self.feature_dim + 2], wires=[0, self.feature_dim - 1])

                for i in range(self.feature_dim - 2):
                    qml.CRZ(params[3 * self.feature_dim + 3 + i], wires=[i + 1, i])

            return [qml.expval(qml.PauliZ(i)) for i in range(self.feature_dim)]

        return circuit_13

    def circuit_14_pennylane(self):
        dev = qml.device("default.qubit", wires=self.feature_dim)

        @qml.qnode(dev)
        def circuit_14(*params):
            for _ in range(self.repetition):
                for i in range(self.feature_dim):
                    qml.RY(params[i], wires=i)

                qml.CRX(params[self.feature_dim], wires=[self.feature_dim - 1, 0])

                for i in range(self.feature_dim - 1):
                    qml.CRX(params[self.feature_dim + 1 + i], wires=[i, i + 1])

                for i in range(self.feature_dim):
                    qml.RY(params[2 * self.feature_dim + 1 + i], wires=i)

                qml.CRX(params[3 * self.feature_dim + 1], wires=[self.feature_dim - 1, self.feature_dim - 2])
                qml.CRX(params[3 * self.feature_dim + 2], wires=[0, self.feature_dim - 1])

                for i in range(self.feature_dim - 2):
                    qml.CRX(params[3 * self.feature_dim + 3 + i], wires=[i + 1, i])

            return [qml.expval(qml.PauliZ(i)) for i in range(self.feature_dim)]

        return circuit_14

    def circuit_15_pennylane(self):
        dev = qml.device("default.qubit", wires=self.feature_dim)

        @qml.qnode(dev)
        def circuit_15(*params):
            for _ in range(self.repetition):
                for i in range(self.feature_dim):
                    qml.RY(params[i], wires=i)

                qml.CX(wires=[self.feature_dim - 1, 0])

                for i in range(self.feature_dim - 1):
                    qml.CX(wires=[i, i + 1])

                for i in range(self.feature_dim):
                    qml.RY(params[self.feature_dim + i], wires=i)

                qml.CX(wires=[self.feature_dim - 1, self.feature_dim - 2])
                qml.CX(wires=[0, self.feature_dim - 1])

                for i in range(self.feature_dim - 2):
                    qml.CX(wires=[i + 1, i])

            return [qml.expval(qml.PauliZ(i)) for i in range(self.feature_dim)]

        return circuit_15

    def circuit_16_pennylane(self):
        dev = qml.device("default.qubit", wires=self.feature_dim)

        @qml.qnode(dev)
        def circuit_16(*params):
            for _ in range(self.repetition):
                for i in range(self.feature_dim):
                    qml.RX(params[2 * i], wires=i)
                    qml.RZ(params[2 * i + 1], wires=i)

                for i in range(0, self.feature_dim - 1, 2):
                    qml.CRZ(params[3 * self.feature_dim - 1 + i // 2], wires=[i + 1, i])

                for i in range(1, self.feature_dim - 1, 2):
                    qml.CRZ(params[3 * self.feature_dim - 1 + (i - 1) // 2], wires=[i + 1, i])

            return [qml.expval(qml.PauliZ(i)) for i in range(self.feature_dim)]

        return circuit_16

    def circuit_17_pennylane(self):
        dev = qml.device("default.qubit", wires=self.feature_dim)

        @qml.qnode(dev)
        def circuit_17(*params):
            for _ in range(self.repetition):
                for i in range(self.feature_dim):
                    qml.RX(params[2 * i], wires=i)
                    qml.RZ(params[2 * i + 1], wires=i)

                for i in range(0, self.feature_dim - 1, 2):
                    qml.CRX(params[3 * self.feature_dim - 1 + i // 2], wires=[i + 1, i])

                for i in range(1, self.feature_dim - 1, 2):
                    qml.CRX(params[3 * self.feature_dim - 1 + (i - 1) // 2], wires=[i + 1, i])

            return [qml.expval(qml.PauliZ(i)) for i in range(self.feature_dim)]

        return circuit_17

    def circuit_18_pennylane(self):
        dev = qml.device("default.qubit", wires=self.feature_dim)

        @qml.qnode(dev)
        def circuit_18(*params):
            for _ in range(self.repetition):
                for i in range(self.feature_dim):
                    qml.RX(params[i], wires=i)
                    qml.RZ(params[i], wires=i)

                qml.CRZ(params[3 * self.feature_dim - 1], wires=[self.feature_dim - 1, 0])

                for i in range(self.feature_dim - 1):
                    qml.CRZ(params[3 * self.feature_dim - 1 + i + 1], wires=[i, i + 1])

            return [qml.expval(qml.PauliZ(i)) for i in range(self.feature_dim)]

        return circuit_18

    def circuit_19_pennylane(self):
        dev = qml.device("default.qubit", wires=self.feature_dim)

        @qml.qnode(dev)
        def circuit_19(*params):
            for _ in range(self.repetition):
                for i in range(self.feature_dim):
                    qml.RX(params[i], wires=i)
                    qml.RZ(params[i], wires=i)

                qml.CRX(params[3 * self.feature_dim - 1], wires=[self.feature_dim - 1, 0])

                for i in range(self.feature_dim - 1):
                    qml.CRX(params[3 * self.feature_dim - 1 + i + 1], wires=[i, i + 1])

            return [qml.expval(qml.PauliZ(i)) for i in range(self.feature_dim)]

        return circuit_19

    def get_ansatz(self) -> Any:
    """
    Returns:
        ansatzes: Circuits mentioned in https://doi.org/10.1007/s42484-021-00038-w by
        declaring the particular circuit identity in the class variables e.g. circuit_id = 1 will return
        the 1st circuit mentioned in https://doi.org/10.1007/s42484-021-00038-w
    """

    ansatzes = {
        1: self.circuit_1_pennylane(),
        2: self.circuit_2_pennylane(),
        3: self.circuit_3_pennylane(),
        4: self.circuit_4_pennylane(),
        5: self.circuit_5_pennylane(),
        6: self.circuit_6_pennylane(),
        7: self.circuit_7_pennylane(),
        8: self.circuit_8_pennylane(),
        9: self.circuit_9_pennylane(),
        10: self.circuit_10_pennylane(),
        11: self.circuit_11_pennylane(),
        12: self.circuit_12_pennylane(),
        13: self.circuit_13_pennylane(),
        14: self.circuit_14_pennylane(),
        15: self.circuit_15_pennylane(),
        16: self.circuit_16_pennylane(),
        17: self.circuit_17_pennylane(),
        18: self.circuit_18_pennylane(),
        19: self.circuit_19_pennylane(),
    }

    return ansatzes[self.circuit_id]
