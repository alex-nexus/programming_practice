def combination(characters, m):
	if m==1:
		return [[c] for c in characters]
	if m==len(characters):
		return [characters]
	else:
		results = []
		for i in range(len(characters)):
			copied_characters = list(characters)
			n = copied_characters.pop(i)
			results.extend([[n]+cb for cb in combination(copied_characters, m-1)])
			results.extend([cb for cb in combination(copied_characters, m)])						
		return results

if __name__ == '__main__':
	input_array = ['A', 'B', 'C', 'D', 'E']
	output_array = combination(input_array, 3)
	print 'input_array', input_array

	cb_set = set([("-").join(sorted(cb)) for cb in output_array])
	output_array = [cb_str.split('-') for cb_str in cb_set]
	print 'output_array', output_array