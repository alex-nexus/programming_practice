import numpy as NP

class Sudoku:
	def __init__(self, sudoku_string):
		self.board = NP.fromstring(sudoku_string, dtype=int, sep=' ').reshape(9,9)
	
	def fill(self, i, j, v):
		self.board[i,j] = v
		
	def unfill(self, i, j):
		self.board[i,j] = 0

	def get_one_unfilled_cell(self):
		for index, v in NP.ndenumerate(self.board): 
			if v==0:
				return index
		
	def get_candidates_by_cell(self, i, j):
		candidates=set(range(1,10)) #initial candidates: 1,2,...,9
		candidates-=set(self.board[:,j]) #filter out numbers in its column
		candidates-=set(self.board[i, :]) #filter out number in its row

		i/=3; j/=3 #floor to the multiple of 3
		candidates-= set(self.board[3*i:3*(i+1), 3*j:3*(j+1)].ravel()) #filter out number in its square
		return candidates

	###########
	# TESTING #
	###########
	def is_solved(self):
		return self.get_num_unfilled_cells()==0 and self.is_valid()

	def get_num_unfilled_cells(self):
		return len([index for index, v in NP.ndenumerate(self.board) if v==0])
		
	#verify there is no repeats for each row, column, and square, ignoreing zeros
	def is_valid(self):
		for i in range(9): #verify all rows, columns
			if self.has_any_repeat(self.board[i,:])or self.has_any_repeat(self.board[:, i]):
				return False			
		for i in range(3): #verify all squares
			for j in range(3):
				if self.has_any_repeat(self.board[3*i:3*(i+1), 3*j:3*(j+1)].ravel()):
					return False							
		return True

	def has_any_repeat(self, nums):
		nonzero_nums = [n for n in list(nums) if n!=0]
		return len(nonzero_nums)!=len(set(nonzero_nums))			
			
#this solver uses brute force DFS to traverse down the solution space
def solve(s):
	#find an unfilled cell and its index
    index = s.get_one_unfilled_cell()
    if not index:
        return s
    i, j = index

    #iterate all the candidates given an unfilled index
    for v in s.get_candidates_by_cell(i, j):
        s.fill(i, j, v)
        soln = solve(s)
        if soln:
            return soln
    #if not solution found, rollback the cell change
    s.unfill(i, j)

easy = """
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

#I found this in the hardest level in a sudoku book
hard = """
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

#this takes outs all the 1, 2, and 3, which is tricky because some initiali guess is needed, 
#which means that the solver needs to rollback too
tricky = """
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

if __name__ == '__main__':
	for sudoku_string in [easy, hard, tricky]:
		print '----------------------'
		s=Sudoku(sudoku_string)
		print 'Sudoku Initialization:'
		print s.board

		s = solve(s)
		if s.is_solved():
			print 'Solution Verified:'
			print s.board
		else:
			print 'Wrong solution'