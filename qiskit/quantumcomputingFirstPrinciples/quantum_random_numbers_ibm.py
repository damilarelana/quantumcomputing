from projectq import MainEngine  # import the main compiler engine
from projectq.ops import H, Measure  # import the operations we want to perform (Hadamard and measurement)
from projectq.backends import IBMBackend
import projectq.setups.ibm

eng = MainEngine(IBMBackend(),
                 engine_list=projectq.setups.ibm.get_engine_list())
qubit = eng.allocate_qubit()  # allocate a quantum register with 1 qubit


# allocate one qubit
q1 = eng.allocate_qubit()

H | qubit  # apply a Hadamard gate
Measure | qubit  # measure the qubit

eng.flush()  # flush all gates (and execute measurements)
print("Measured {}".format(int(qubit)))  # converting a qubit to int or bool gives access to the measurement result