def power_set(input_set):
	if len(input_set)==0:
		return [[]]	
	n = input_set.pop()	
	return reduce(lambda x,y:x+y, [[[n]+ps]+[ps] for ps in power_set(input_set)])
	
if __name__ == '__main__':
	input_array = set(['A', 'B', 'C'])
	print 'input_array', input_array	
	output_array = power_set(input_array)
	print 'output_array', output_array, len(output_array)