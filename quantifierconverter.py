#DO NOT CHANGE THE NAMES OF THE FILE, CLASS or METHOD

class QuantifierConverter(object):

	def quantifierConverter(self,s):
		s = s.replace("for every", "\u2200")
		s = s.replace("there exists", "\u2203")
		return s
