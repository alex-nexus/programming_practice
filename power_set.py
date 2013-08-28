def power_set(input_set):
	if len(input_set)==0:
		return [[]]
	else:
		results = []
		n = input_set.pop()	
	  	for ps in power_set(input_set):
	  		results.extend([[n]+ps]+[ps])	  			  		
  		return results

if __name__ == '__main__':
	input_array = set(['A', 'B', 'C'])
	print 'input_array', input_array
	
	output_array = power_set(input_array)
	print 'output_array', output_array