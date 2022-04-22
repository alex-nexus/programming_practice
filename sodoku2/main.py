def has_any_repeat(numbers):
    numbers = [n for n in numbers if n != 0]
    return len(set(numbers)) != len(numbers)


class Sudoku:
    N = 9

    def __init__(self, input_string):
        self.board = [list(map(lambda x: int(x), row.split(' ')))
                      for row in input_string.split("\n")]

    def transpose(self):
        return [[self.board[j][i] for j in range(self.N)]
                for i in range(self.N)]

    def solve(self):
        while(self.valid() and not self.solved()):
            self.print_board()

            for i in range(self.N):
                for j in range(self.N):
                    if self.board[i][j] == 0:
                        candidates = self.find_candidates(i, j)

                        if len(candidates) == 1:
                            print(f'fill ({i},{j}) with {candidates[0]}')
                            self.board[i][j] = candidates[0]
            break

    def find_candidates(self, i, j):
        candidates = list(range(1, 10))

        # horizontal
        for v in self.board[i]:
            if v in candidates:
                candidates.remove(v)

        # vertical
        for v in self.transpose()[j]:
            if v in candidates:
                candidates.remove(v)

        # cubic
        cube = self.cubes()[(i // 3) * 3 + j // 3]
        for v in cube:
            if v in candidates:
                candidates.remove(v)

        print(f'({i},{j}) candidates: {candidates}')
        return candidates

    def get_nines(self):
        nines = self.board
        nines += self.transpose()
        nines += self.cubes()
        return nines

    def valid(self) -> bool:
        # horizontal
        for nine in get_nines:
            if has_any_repeat(row):
                return False

        # vertical
        for col in self.transpose():
            if has_any_repeat(col):
                return False

        # cubic
        for cube in self.cubes():
            if has_any_repeat(cube):
                return False

        return True

    def solved(self) -> bool:
        for nine in get_nines:
            if sum(nine) != 45:
                return False

        return True

    def cubes(self):
        cubes = []
        for i in range(3):
            for j in range(3):
                cube = []
                for row in self.board[i * 3:(i + 1) * 3]:
                    cube += row[j * 3:(j + 1) * 3]
                cubes.append(cube)
        return cubes

    def print_board(self):
        for row in self.board:
            print(row)
        print(f'valid:{self.valid()}')
        print(f'solved:{self.solved()}')


if __name__ == '__main__':
    input_string = """4 1 2 3 6 8 7 9 5
0 3 0 0 0 0 0 0 0
0 0 0 7 0 0 0 0 0
0 2 0 0 0 0 0 6 0
0 0 0 0 8 0 4 0 0
0 0 0 0 1 0 0 0 0
0 0 0 6 0 3 0 7 0
5 0 0 2 0 0 0 0 0
1 0 4 0 0 0 0 0 0"""

    s = Sudoku(input_string)
    s.print_board()
    # print(s.get_nines())
    s.solve()
