class Policy < Struct.new(:board)  
  """
  this policy object determines if the board is in a finished condition
  return true if there is a winner and false otherwise
  (any one player has connected 4 pieces)
  """

  def finished?
    # if any rows, columns or diagnoals have more than 4 connected pieces, then the game is finished
    (board.rows + board.columns + board.diagonals).any? do |pieces|
      has_4_connected_pieces?(pieces)
    end
  end

  private

  def has_4_connected_pieces?(pieces)
    # return true if the row has more than 4 connected pieces and false otherwise
    pieces.each_cons(4).each do |con_pieces|
      # all pieces are of the same value
      return true if con_pieces.uniq == ['O'] || con_pieces.uniq == ['X']
    end
    false
  end
end
