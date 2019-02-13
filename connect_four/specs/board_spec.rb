require_relative '../board'
require_relative '../player'

RSpec.describe Board do
  let(:board) { Board.new }
  let(:player1) { Player.new('A', 'X') }
  let(:player2) { Player.new('B', 'O') }

  describe '#print_board' do
    it 'prints the empty board on screen' do
      board.print_board
    end
  end

  describe '#add_piece', '#highest_empty_row(column)' do
    it 'allows to add 6 pieces in a column' do
      expect(board.send(:highest_empty_row, 1)).to eq 0

      board.add_piece(1, player1)
      expect(board.send(:highest_empty_row, 1)).to eq 1

      board.add_piece(1, player2)
      expect(board.send(:highest_empty_row, 1)).to eq 2

      board.add_piece(1, player1)
      expect(board.send(:highest_empty_row, 1)).to eq 3

      board.add_piece(1, player2)
      expect(board.send(:highest_empty_row, 1)).to eq 4

      board.add_piece(1, player1)
      expect(board.send(:highest_empty_row, 1)).to eq 5

      board.add_piece(1, player2)
      expect(board.send(:highest_empty_row, 1)).to be_nil
    end

    it 'does not allow to add more than 6 pieces' do
      board.add_piece(1, player1)
      board.add_piece(1, player2)
      board.add_piece(1, player1)
      board.add_piece(1, player2)
      board.add_piece(1, player1)
      board.add_piece(1, player2)

      expect {
        board.add_piece(1, player2)
      }.to raise_error
    end
  end
end
