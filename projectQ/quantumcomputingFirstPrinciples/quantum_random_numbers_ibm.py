from projectq import MainEngine  # import the main compiler engine
from projectq.ops import H, Measure  # import the operations we want to perform (Hadamard and measurement)
from projectq.backends import IBMBackend
import os
import projectq.setups.ibm as ibm_setup

# extract IBM Quantum Experience login details from environ 
ibmqe_user = os.environ.get('IBMQE_USER')
ibmqe_password = os.environ.get('IBMQE_PASSWORD')

# login to IBM and instantiate the quantumEngine object
eng = MainEngine(
  IBMBackend(use_hardware=True, num_runs=1024, verbose=False, user=ibmqe_user, password=ibmqe_password, device='ibmqx4', num_retries=3000, interval=1, retrieve_execution=None),
  engine_list=ibm_setup.get_engine_list())

# allocate a quantum register with 1 qubit
qubit = eng.allocate_qubit()

# apply a Hadamard gate to put in super position
H | qubit

# measure the qubit
Measure | qubit

eng.flush()  # flush all gates (and execute measurements)
print("Measured {}".format(int(qubit)))  # converting a qubit to int or bool gives access to the measurement result