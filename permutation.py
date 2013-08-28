def permutation(characters):
	if len(characters)==1:
		return [characters]
	else:
		results = []
		for i in range(len(characters)):
			copied_characters = list(characters)
			n = copied_characters.pop(i)
			for pm in permutation(copied_characters):
				results.append([n]+pm)
		return results

if __name__ == '__main__':
	input_array = ['A', 'B', 'C', 'T']
	output_array = permutation(input_array)
	print 'input_array', input_array
	print 'output_array', output_array