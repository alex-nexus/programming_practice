def reverse_string(str):
	if len(str)==0:
		return str
	return reverse_string(str[1:])+str[0]

str="Computer Science"
print reverse_string(str)
