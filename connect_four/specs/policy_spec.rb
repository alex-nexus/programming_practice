require_relative '../board'
require_relative '../player'
require_relative '../policy'

RSpec.describe Policy do
  let(:board)  { Board.new }
  let(:player1) { Player.new('A', 'X') }
  let(:player2) { Player.new('B', 'O') }

  subject(:policy) { Policy.new(board) }

  describe '#has_4_connected_pieces' do
    it 'checks if an array has 4 connected_pieces' do
      expect(policy.send(:has_4_connected_pieces?, ['O', 'O', 'O', 'O', '_', 'X'])).to eq true
    end

    it 'checks if an array has 4_connected_pieces' do
      expect(policy.send(:has_4_connected_pieces?, ['_', 'X', 'X', 'X', 'X', '_'])).to eq true
    end

    it 'does not have 4_connected_pieces' do
      expect(policy.send(:has_4_connected_pieces?, ['O', 'X', 'O', 'O', 'X', 'O'])).to eq false
    end
  end

  describe '#finished?' do
    it { should_not be_finished }

    context 'when there is a column with 4 connected pieces' do
      before do
        board.add_piece(1, player1)
        board.add_piece(1, player1)
        board.add_piece(1, player1)
        board.add_piece(1, player1)

        # board.print_board
      end

      it { should be_finished }
    end

    context 'when there is a row with 4 connected pieces' do
      before do
        board.add_piece(1, player1)
        board.add_piece(2, player1)
        board.add_piece(3, player1)
        board.add_piece(4, player1)

        # board.print_board
      end

      it { should be_finished }
    end

    context 'when there is a diagonal with 4 connected pieces' do
      before do
        board.add_piece(1, player1)

        board.add_piece(2, player2)
        board.add_piece(2, player1)

        board.add_piece(3, player2)
        board.add_piece(3, player2)
        board.add_piece(3, player1)

        board.add_piece(4, player2)
        board.add_piece(4, player2)
        board.add_piece(4, player2)
        board.add_piece(4, player1)

        # board.print_board
      end

      it { should be_finished }
    end
  end
end
