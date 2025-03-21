#DO NOT CHANGE THE NAMES OF THE FILE, CLASS or METHOD

class BitOperator(object):

	def bitOperator(self,bit1,bit2):
		#Start writing your code from here
		string1 = ""
		string2 = ""
		for i in range(5):
			if(bit1[i] == '1' or bit2[i] == '1'):
				string1 += '1'
			else:
				string1 += '0'
			if(bit1[i] == bit2[i] == '1'):
				string2 += '1'
			else:
				string2 +='0'
		return (string1, string2)