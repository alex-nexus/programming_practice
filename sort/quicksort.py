from random import shuffle

def quicksort(inputs):
	if len(inputs)<=1 :
		return inputs
	p = inputs.pop()
	left_inputs = filter(lambda n: n < p, inputs)	
	right_inputs = filter(lambda n: n >= p, inputs)
	return quicksort(left_inputs) + [p] + quicksort(right_inputs)

#test 1
inputs1 = range(50)+range(50)
shuffle(inputs1)
print 'inputs: ', inputs1
outputs = quicksort(inputs1)
print 'outputs', outputs

#test 2
inputs2 = range(100)
shuffle(inputs2)
print 'inputs: ', inputs2
outputs = quicksort(inputs2)
print 'outputs', outputs