import numpy as NP
import sys
from collections import defaultdict

class Sudoku:
	def __init__(self, sudoku_string):
		self.board = NP.fromstring(sudoku_string, dtype=int, sep=' ').reshape(9,9)
		#self.get_cells_to_candidates()
		
	def get_unfilled_cells(self):
		return [index for index, v in NP.ndenumerate(self.board) if v == 0]

	def get_square(self, i, j):
		i/=3
		j/=3
		return self.board[3*i:3*(i+1), 3*j:3*(j+1)]
	
	def get_row(self, i, j):
		return self.board[i,:]

	def get_col(self, i, j):
		return self.board[:, j]

	def is_solved(self):
		return self.is_valid() and len(self.get_unfilled_cells())==0
		
	#basically find out if there are any repeats for each row, column, and square, discount zeros/unfilled 	
	def is_valid(self):
		#validate all rows, columns that none has repeats
		for i in range(9):
			if self.has_any_repeat(list(self.board[i,:])) or self.has_any_repeat(list(self.board[:, i])):
				return False			
		#check all squares
		for i in range(3):
			for j in range(3):
				if self.has_any_repeat(list(self.board[3*i:3*(i+1), 3*j:3*(j+1)].ravel())):
					return False							
		return True
	# def find_one_candidate(self):
	# 	x, candidates = self.cell_to_candidates[0] 
	# 	i, j = x.split('-')
	# 	if len(candidates) == 1:
	# 		v = candidates[0]
	# 	else: 
	# 		v = candidates[0]
	# 	return i, j, v

	def get_cells_to_candidates(self):		
		cell_to_candidates = dict([(str(i)+'-'+str(j), sorted(self.compute_candidates(i, j))) for i, j in self.get_unfilled_cells()])
		cell_to_candidates = sorted(cell_to_candidates.items(), key=lambda x: len(x[1]))
		print cell_to_candidates
		return cell_to_candidates
	
	def compute_candidates(self, i, j):
		if self.board[i, j] != 0:
			raise 'filled already'
		candidates=set(range(1,10))
		candidates-=set(self.get_row(i ,j)) #row
		candidates-=set(self.get_col(i, j)) #row		
		candidates-= set(self.get_square(i, j).ravel())
		return candidates

	def has_any_repeat(self, nums):
		nonzero_nums = [n for n in nums if n!=0]
		return len(nonzero_nums)!=len(set(nonzero_nums))		

	def fill(self, i, j, v):
		print 'fill', i, j, 'with', v
		self.board[i,j] = v
		#self.compute_cells_to_candidates() #always re-compute cell to candidates		
		return self

	def unfill(self, i, j):
		print 'unfill', i, j
		self.board[i,j] = 0
		#self.compute_cells_to_candidates() #always re-compute cell to candidates		

def solve(s):
	print '---------------'			
	if s.is_solved():
		print 'solution found'
		return s
	elif not s.is_valid() or len(s.get_cells_to_candidates()[0][1])==0:	
		raise Exception('invalid, deadend, rollback')
	else:
		for x, candidates in s.get_cells_to_candidates():
			i, j = x.split('-')
			print i, j, candidates
			for v in candidates:
				s_new = s.fill(i, j, v)
				print s_new.board
				try:
					return solve(s_new)
				except Exception as e:
					print 'except', e
					continue
				
sudoku_string = """
0 0 0 8 5 4 0 0 1
0 0 0 0 0 0 9 3 8
0 0 0 0 0 0 0 0 7
3 0 0 0 0 2 8 0 0
0 1 0 0 7 0 0 6 0 
0 0 6 5 0 0 0 0 9
1 0 0 0 0 0 0 0 0 
6 4 2 0 0 0 0 0 0
8 0 0 1 4 7 0 0 0
"""
sudoku_string = """
4 1 2 3 6 8 7 9 5
0 3 0 0 0 0 0 0 0
0 0 0 7 0 0 0 0 0
0 2 0 0 0 0 0 6 0
0 0 0 0 8 0 4 0 0 
0 0 0 0 1 0 0 0 0 
0 0 0 6 0 3 0 7 0
5 0 0 2 0 0 0 0 0
1 0 4 0 0 0 0 0 0
"""
sudoku_string2 = """
4 0 0 0 6 8 7 9 5
7 0 8 0 9 5 0 4 6
9 5 6 7 0 4 8 0 0
8 0 5 4 0 7 9 6 0
0 9 0 5 8 6 4 0 7
6 4 7 9 0 0 5 0 8
0 8 9 6 5 0 0 7 4
5 7 0 0 4 0 6 8 9
0 6 4 8 7 9 0 5 0
"""
s=Sudoku(sudoku_string)
s = solve(s)

print 'solution'
print s.board