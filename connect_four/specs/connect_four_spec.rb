require_relative '../connect_four'

RSpec.describe ConnectFour do
  subject(:game) { ConnectFour.new }

  describe '#start' do
    xit 'start the game' do
      game.start
    end
  end
end
