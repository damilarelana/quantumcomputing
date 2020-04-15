from projectq import MainEngine  # import the main compiler engine
from projectq.ops import H, Measure  # import the operations we want to perform (Hadamard and measurement)

# extract IBM Quantum Experience login details from environ 
# ibmqe_user = os.environ.get('IBMQE_USER')
# ibmqe_password = os.environ.get('IBMQE_PASSWORD')

# instantiate the quantumEngine object simulator
eng = MainEngine()

# allocate a quantum register with 1 qubit
qubit = eng.allocate_qubit()

# apply a Hadamard gate to put in super position
H | qubit

# measure the qubit
Measure | qubit

# flush all gates (and execute measurements)
eng.flush()

print("Measured {}".format(int(qubit)))  # converting a qubit to int or bool gives access to the measurement result