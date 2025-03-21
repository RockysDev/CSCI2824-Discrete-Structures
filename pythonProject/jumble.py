class Jumble():
	
	def get_total_distinct_combinations(self, input_string):
		
		## Your code here
		length = len(input_string)
		numSameLetters = 0
		for i in input_string:
			numOccurences = input_string.count(i)
			if numOccurences == length:
				return 1
			if numOccurences > 1:
				if numSameLetters == 0:
					numSameLetters+=1
				numSameLetters = numSameLetters
		ans = 1
		for i in range(1, length+1): #compute factorial of length of string
			ans = ans*i
		if numSameLetters != 0:
			ans = ans/numSameLetters
		return ans




		