#DO NOT CHANGE THE NAMES OF THE FILE, CLASS or METHOD

class LogicGates(object):

	def get_circuit_output(self, A, B, C):
		if((((not A and B)and (not C and not A))!= (B and C))):
			return True
		else:
			return False