from projectq import MainEngine  # import the main compiler engine
from projectq.ops import H, Measure  # import the operations we want to perform (Hadamard and measurement)
from projectq.backends import IBMBackend
from os import getenv
import projectq.setups.ibm

# extract IBM Quantum Experience login details from environ 
ibmqe_user = getenv('IBMQE_USER')
ibmqe_password = getenv('IBMQE_PASSWORD')

# login to IBM and instantiate the quantumEngine object
eng = MainEngine(IBMBackend(user=ibmqe_user, password=ibmqe_password),
                 engine_list=projectq.setups.ibm.get_engine_list())
qubit = eng.allocate_qubit()  # allocate a quantum register with 1 qubit


# allocate one qubit
q1 = eng.allocate_qubit()

H | qubit  # apply a Hadamard gate
Measure | qubit  # measure the qubit

eng.flush()  # flush all gates (and execute measurements)
print("Measured {}".format(int(qubit)))  # converting a qubit to int or bool gives access to the measurement result