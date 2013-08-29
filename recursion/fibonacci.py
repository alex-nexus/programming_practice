def fibonacci(n):
	if n<=1:
		return n
	return fibonacci(n-1)+fibonacci(n-2)
print [fibonacci(i) for i in range(11)]
