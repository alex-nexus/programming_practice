class Board
  """
  this class holds the grid of all the slots (player 1, 2 or empty)
  also provide a printing utility function
  """

  EMPTY_SLOT = '_'
  ROWS_COUNT = 6
  COLUMNS_COUNT = 7

  # [0, 0], [0, 6], [5, 0], [5, 6]

  DIAGONALS = [
    [[0, 0], [1, 1], [2, 2], [3, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 4]],
    [[0, 2], [1, 3], [2, 4], [3, 5]],
    [[0, 3], [1, 4], [2, 5], [3, 6]],

    [[1, 0], [2, 1], [3, 2], [4, 3]],
    [[1, 1], [2, 2], [3, 3], [4, 4]],
    [[1, 2], [2, 3], [3, 4], [4, 5]],
    [[1, 3], [2, 4], [3, 5], [4, 6]],

    [[2, 0], [3, 1], [4, 2], [5, 3]],
    [[2, 1], [3, 2], [4, 3], [5, 4]],
    [[2, 2], [3, 3], [4, 4], [5, 5]],
    [[2, 3], [3, 4], [4, 5], [5, 6]],

    [[0, 6], [1, 5], [2, 4], [3, 3]],
    [[0, 5], [1, 4], [2, 3], [3, 2]],
    [[0, 4], [1, 3], [2, 2], [3, 1]],
    [[0, 3], [1, 2], [2, 1], [3, 0]],

    [[1, 6], [2, 5], [3, 4], [4, 3]],
    [[1, 5], [2, 4], [3, 3], [4, 2]],
    [[1, 4], [2, 3], [3, 2], [4, 1]],
    [[1, 3], [2, 2], [3, 1], [4, 0]],

    [[2, 6], [3, 5], [4, 4], [5, 3]],
    [[2, 5], [3, 4], [4, 3], [5, 2]],
    [[2, 4], [3, 3], [4, 2], [5, 1]],
    [[2, 3], [3, 2], [4, 1], [5, 0]]
  ].freeze


  def add_piece(column, player)
    if row_number = highest_empty_row(column)
      grid[ROWS_COUNT-row_number-1][column] = player.mark
    else
      raise "Column:#{column}is already full."
    end
  end

  def rows
    grid
  end

  def columns
    # Turn row info columns with transpose
    grid.transpose
  end

  def diagonals
    DIAGONALS.map do |coordinates|
      coordinates.map { |x, y| grid[x][y] }
    end
  end

  def print_board
    grid.each do |row|
      print row
      print "\n"
    end
  end

  private

  def highest_empty_row(column)
    # return the highest empty row number to which column the player can add a new piece
    grid.reverse.each.with_index do |row, row_index|
      return row_index if row[column] == EMPTY_SLOT
    end
    nil
  end

  def grid
    @grid ||= Array.new(ROWS_COUNT) { Array.new(COLUMNS_COUNT) { EMPTY_SLOT } }
  end
end
