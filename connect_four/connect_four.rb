require_relative 'board'
require_relative 'player'
require_relative 'policy'

class ConnectFour
  def start
    board.print_board # print for the first time

    loop do
      players.each do |player|
        puts "#{player.name}, which column do you want to place the piece:"
        column = STDIN.gets.chomp
        board.add_piece(column.to_i, player)
        board.print_board

        if Policy.new(board).finished?
          puts "Player #{player.name} wins. Game Over"
          return
        end
      end
    end
  end

  private

  def players
    @players ||= [
      Player.new('A', 'O'),
      Player.new('B', 'X')
    ]
  end

  def board
    @board ||= Board.new
  end
end
