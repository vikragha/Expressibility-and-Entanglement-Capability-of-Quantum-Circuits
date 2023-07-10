def local_cost_simple_1(params, num_qubits, layers):
    for l in range(layers):
        for i in range(num_qubits):
            qml.RX(params[l][i], wires=i)
            qml.RZ(params[l][i], wires=i)
    return qml.expval(qml.PauliZ(0))

def local_cost_simple_2(params, num_qubits, layers):
    for l in range(layers):
        for i in range(num_qubits):
            qml.RX(params[l][i], wires=i)
            qml.RZ(params[l][i], wires=i)
        for i in reversed(range(num_qubits-1)):
            qml.CNOT(wires=[i + 1, i])
    return qml.expval(qml.PauliZ(0))

def local_cost_simple_3(params, num_qubits, layers):
    for l in range(layers):
        for i in range(num_qubits):
            qml.RX(params[l][i], wires=i)
            qml.RZ(params[l][i], wires=i)
        for i in reversed(range(wires-1)):
            qml.CRZ(params[l][i], wires=[i + 1, i])
    return qml.expval(qml.PauliZ(0))

def local_cost_simple_4(params, num_qubits, layers):
    for l in range(layers):
        for i in range(wires):
            qml.RX(params[l][i], wires=i)
            qml.RZ(params[l][i], wires=i)
        for i in reversed(range(wires-1)):
            qml.CRX(params[l][i], wires=[i + 1, i])
    return qml.expval(qml.PauliZ(0))

def local_cost_simple_5(params, num_qubits, layers):
    for l in range(layers):
        for i in range(num_qubits):
            qml.RX(params[l][i], wires=i)
            qml.RZ(params[l][i], wires=i)

        for i in range(1, num_qubits - 1, 4):
            qml.CRZ(params[l][i], wires=[i+2, i+1])

        for i in range(1, num_qubits - 1, 4):
            qml.CRZ(params[l][i], wires=[i+2, i])

        for i in range(1, num_qubits - 1, 4):
            qml.CRZ(params[l][i], wires=[i+2, i-1])

        for i in range(1, num_qubits - 1, 4):
            qml.CRZ(params[l][i], wires=[i+1, i+2])

        for i in range(1, num_qubits - 1, 4):
            qml.CRZ(params[l][i], wires=[i+1, i])

        for i in range(1, num_qubits - 1, 4):
            qml.CRZ(params[l][i], wires=[i+1, i-1])

        for i in range(1, num_qubits - 1, 4):
            qml.CRZ(params[l][i], wires=[i, i+2])

        for i in range(1, num_qubits - 1, 4):
            qml.CRZ(params[l][i], wires=[i, i+1])

        for i in range(1, num_qubits - 1, 4):
            qml.CRZ(params[l][i], wires=[i, i-1])

        for i in range(1, num_qubits - 1, 4):
            qml.CRZ(params[l][i], wires=[i-1, i+2])

        for i in range(1, num_qubits - 1, 4):
            qml.CRZ(params[l][i], wires=[i-1, i+1])

        for i in range(1, num_qubits - 1, 4):
            qml.CRZ(params[l][i], wires=[i-1, i])

        for i in range(num_qubits):
            qml.RX(params[l][i], wires=i)
            qml.RZ(params[l][i], wires=i)

    return qml.expval(qml.PauliZ(0))

def local_cost_simple_6(params, num_qubits, layers):
    for l in range(layers):
        for i in range(num_qubits):
            qml.RX(params[l][i], wires=i)
            qml.RZ(params[l][i], wires=i)

        for i in range(1, num_qubits - 1, 4):
            qml.CRX(params[l][i], wires=[i+2, i+1])

        for i in range(1, num_qubits - 1, 4):
            qml.CRX(params[l][i], wires=[i+2, i])

        for i in range(1, num_qubits - 1, 4):
            qml.CRX(params[l][i], wires=[i+2, i-1])

        for i in range(1, num_qubits - 1, 4):
            qml.CRX(params[l][i], wires=[i+1, i+2])

        for i in range(1, num_qubits - 1, 4):
            qml.CRX(params[l][i], wires=[i+1, i])

        for i in range(1, num_qubits - 1, 4):
            qml.CRX(params[l][i], wires=[i+1, i-1])

        for i in range(1, num_qubits - 1, 4):
            qml.CRX(params[l][i], wires=[i, i+2])

        for i in range(1, num_qubits - 1, 4):
            qml.CRX(params[l][i], wires=[i, i+1])

        for i in range(1, num_qubits - 1, 4):
            qml.CRX(params[l][i], wires=[i, i-1])

        for i in range(1, num_qubits - 1, 4):
            qml.CRX(params[l][i], wires=[i-1, i+2])

        for i in range(1, num_qubits - 1, 4):
            qml.CRX(params[l][i], wires=[i-1, i+1])

        for i in range(1, num_qubits - 1, 4):
            qml.CRX(params[l][i], wires=[i-1, i])

        for i in range(num_qubits):
            qml.RX(params[l][i], wires=i)
            qml.RZ(params[l][i], wires=i)

    return qml.expval(qml.PauliZ(0))

def local_cost_simple_7(params, num_qubits, layers):
    for l in range(layers):
        for i in range(num_qubits):
            qml.RX(params[l][i], wires=i)
            qml.RZ(params[l][i], wires=i)

        for i in range(1, num_qubits - 1, 4):  # Update the range
            qml.CRZ(params[l][i], wires=[i, i-1])
        for i in range(1, num_qubits - 1, 4):  # Update the range
            qml.CRZ(params[l][i], wires=[i+2, i+1])


        for i in range(num_qubits):
            qml.RX(params[l][i], wires=i)
            qml.RZ(params[l][i], wires=i)

        for i in range(1, num_qubits - 1, 4):  # Update the range
            qml.CRZ(params[l][i], wires=[i+1, i])
    return qml.expval(qml.PauliZ(0))


def local_cost_simple_8(params, num_qubits, layers):
    for l in range(layers):
        for i in range(num_qubits):
            qml.RX(params[l][i], wires=i)
            qml.RZ(params[l][i], wires=i)

        for i in range(1, num_qubits - 1, 4):  # Update the range
            qml.CRX(params[l][i], wires=[i, i-1])
        for i in range(1, num_qubits - 1, 4):  # Update the range
            qml.CRX(params[l][i], wires=[i+2, i+1])


        for i in range(num_qubits):
            qml.RX(params[l][i], wires=i)
            qml.RZ(params[l][i], wires=i)

        for i in range(1, num_qubits - 1, 4):  # Update the range
            qml.CRX(params[l][i], wires=[i+1, i])
    return qml.expval(qml.PauliZ(0))


def local_cost_simple_9(params, num_qubits, layers):
    for l in range(layers):
        for i in range(num_qubits):
            qml.Hadamard(wires=i)
        for i in reversed(range(num_qubits-1)):
            qml.CZ(wires=[i + 1, i])
    return qml.expval(qml.PauliZ(0))


def local_cost_simple_10(params, num_qubits, layers):
    for i in range(num_qubits):
            qml.RY(params[i], wires=i)
    for l in range(layers):
        for i in reversed(range(num_qubits-1)):
            qml.CZ(wires=[i + 1, i])
        for i in range(0, num_qubits - (num_qubits-1), 1):
            qml.CZ(wires=[i + (wires-1), i])
        for i in range(num_qubits):
            qml.RY(params[l][i], wires=i)
    return qml.expval(qml.PauliZ(0))


def local_cost_simple_11(params, num_qubits, layers):
    for l in range(layers):
        for i in range(num_qubits):
            qml.RY(params[l][i], wires=i)
            qml.RZ(params[l][i], wires=i)

        for i in range(0, (num_qubits - 1), 2):
            qml.CNOT(wires=[i + 1, i])

        for i in range(1, num_qubits - 1, 4):
            qml.RY(params[l][i], wires=i)
            qml.RZ(params[l][i], wires=i)
        for i in range(1, num_qubits - 1, 4):
            qml.RY(params[l][i+1], wires=i+1)
            qml.RZ(params[l][i+1], wires=i+1)

        for i in range(1, num_qubits - 1, 4):
            qml.CNOT(wires=[i + 1, i])

    return qml.expval(qml.PauliZ(0))



def local_cost_simple_12(params, num_qubits, layers):
    for l in range(layers):
        for i in range(num_qubits):
            qml.RY(params[l][i], wires=i)
            qml.RZ(params[l][i], wires=i)

        for i in range(0, (num_qubits - 1), 2):
            qml.CZ(wires=[i + 1, i])

        for i in range(1, num_qubits - 1, 4):  # Update the range
            qml.RY(params[l][i], wires=i)
            qml.RZ(params[l][i], wires=i)
        for i in range(1, num_qubits - 1, 4):  # Update the range
            qml.RY(params[l][i+1], wires=i+1)
            qml.RZ(params[l][i+1], wires=i+1)

        for i in range(1, num_qubits - 1, 4):
            qml.CZ(wires=[i + 1, i])

    return qml.expval(qml.PauliZ(0))


def local_cost_simple_13(params, num_qubits, layers):
    for l in range(layers):
        for i in range(num_qubits):
            qml.RY(params[l][i], wires=i)

        for i in range(0, num_qubits - (num_qubits-1), 1):
            qml.CRZ(params[l][i], wires=[i + (wires-1), i])

        for i in reversed(range(num_qubits-1)):
            qml.CRZ(params[l][i], wires=[i + 1, i])

        for i in range(num_qubits):
            qml.RY(params[l][i], wires=i)

        for i in range(0, num_qubits - (num_qubits-1), 2):
            qml.CRZ(params[l][i], wires=[i+(wires-1), i+(wires-2)])

        for i in range(0, num_qubits - (num_qubits-1), 2):
            qml.CRZ(params[l][i], wires=[i, i+(wires-1)])

        for i in (range(num_qubits-2)):
            qml.CRZ(params[l][i], wires=[i + 1, i])

    return qml.expval(qml.PauliZ(0))


def local_cost_simple_14(params, num_qubits, layers):
    for l in range(layers):
        for i in range(num_qubits):
            qml.RY(params[l][i], wires=i)

        for i in range(0, num_qubits - (num_qubits-1), 1):
            qml.CRX(params[l][i], wires=[i + (wires-1), i])

        for i in reversed(range(num_qubits-1)):
            qml.CRX(params[l][i], wires=[i + 1, i])

        for i in range(num_qubits):
            qml.RY(params[l][i], wires=i)

        for i in range(0, num_qubits - (num_qubits-1), 2):
            qml.CRX(params[l][i], wires=[i+(wires-1), i+(wires-2)])

        for i in range(0, num_qubits - (num_qubits-1), 2):
            qml.CRX(params[l][i], wires=[i, i+(wires-1)])

        for i in (range(num_qubits-2)):
            qml.CRX(params[l][i], wires=[i + 1, i])

    return qml.expval(qml.PauliZ(0))


def local_cost_simple_15(params, num_qubits, layers):
    for l in range(layers):
        for i in range(num_qubits):
            qml.RY(params[l][i], wires=i)

        for i in range(0, num_qubits - (num_qubits-1), 1):
            qml.CNOT(wires=[i + (wires-1), i])

        for i in reversed(range(num_qubits-1)):
            qml.CNOT(wires=[i + 1, i])

        for i in range(num_qubits):
            qml.RY(params[l][i], wires=i)

        for i in range(0, num_qubits - (num_qubits-1), 2):
            qml.CNOT(wires=[i+(wires-1), i+(wires-2)])

        for i in range(0, num_qubits - (num_qubits-1), 2):
            qml.CNOT(wires=[i, i+(wires-1)])

        for i in (range(num_qubits-2)):
            qml.CNOT(wires=[i+1, i])

    return qml.expval(qml.PauliZ(0))


def local_cost_simple_16(params, num_qubits, layers):
    for l in range(layers):
        for i in range(num_qubits):
            qml.RX(params[l][i], wires=i)
            qml.RZ(params[l][i], wires=i)

        for i in range(1, num_qubits - 1, 4):
            qml.CRZ(params[l][i], wires=[i , i-1])


        for i in range(1, num_qubits - 1, 4):  # Update the range
            qml.CRZ(params[l][i], wires=[i+2, i+1])

        for i in range(1, num_qubits - 1, 4):  # Update the range
            qml.CRZ(params[l][i], wires=[i+1, i])
    return qml.expval(qml.PauliZ(0))


def local_cost_simple_17(params, num_qubits, layers):
    for l in range(layers):
        for i in range(num_qubits):
            qml.RX(params[l][i], wires=i)
            qml.RZ(params[l][i], wires=i)

        for i in range(1, num_qubits - 1, 4):
            qml.CRX(params[l][i], wires=[i , i-1])


        for i in range(1, num_qubits - 1, 4):  # Update the range
            qml.CRX(params[l][i], wires=[i+2, i+1])

        for i in range(1, num_qubits - 1, 4):  # Update the range
            qml.CRX(params[l][i], wires=[i+1, i])
    return qml.expval(qml.PauliZ(0))


def local_cost_simple_18(params, num_qubits, layers):
    for l in range(layers):
        for i in range(num_qubits):
            qml.RX(params[l][i], wires=i)
            qml.RZ(params[l][i], wires=i)

        for i in range(0, num_qubits - (num_qubits-1), 1):
            qml.CRZ(params[l][i], wires=[i + (wires-1), i])

        for i in reversed(range(num_qubits-1)):
            qml.CRZ(params[l][i], wires=[i + 1, i])

    return qml.expval(qml.PauliZ(0))


def local_cost_simple_19(params, num_qubits, layers):
    for l in range(layers):
        for i in range(num_qubits):
            qml.RX(params[l][i], wires=i)
            qml.RZ(params[l][i], wires=i)

        for i in range(0, num_qubits - (num_qubits-1), 1):
            qml.CRX(params[l][i], wires=[i + (wires-1), i])

        for i in reversed(range(num_qubits-1)):
            qml.CRX(params[l][i], wires=[i + 1, i])

    return qml.expval(qml.PauliZ(0))
