def money_change(total, changes):
	if len(changes)==0 or total < 0:
		return None
	elif total == 0:
		return [[]]
	else:
		results = []
		copied_changes = list(changes)
		c = copied_changes.pop()
		
		soln = money_change(total-c, copied_changes)
		if soln:
			for mc in soln: 
				results.append([c] + mc)
		
		soln = money_change(total-c, changes)
		if soln:
			for mc in soln:
				results.append([c] + mc)
		
		soln = money_change(total, copied_changes)
		if soln: 
			for mc in soln:
				results.append(mc)
		return results

total = 100
changes=[50, 20, 10, 5]
print 'input:', changes, 'total:', total

mc_set = money_change(total, changes)
mc_set = set([("-").join(sorted(map(str, mc))) for mc in mc_set])
output_array = [mc_str.split('-') for mc_str in mc_set]
print 'output_array', output_array