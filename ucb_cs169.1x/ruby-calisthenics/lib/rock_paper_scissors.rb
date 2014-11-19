class RockPaperScissors

  # Exceptions this class can raise:
  class NoSuchStrategyError < StandardError ; end

  def self.winner(player1, player2)
    plays = ['P', 'S', 'R']
    if ! plays.include?(player1[1]) or ! plays.include?(player2[1])
        raise NoSuchStrategyError, "Strategy must be one of R,P,S"
    end
    strategy1 = player1[1]
    strategy2 = player2[1]

    if strategy1 == strategy2
        return player1
    elsif (strategy1 == 'S' and strategy2 == 'P')
        return player1
    elsif (strategy1 == 'P' and strategy2 == 'R')
        return player1
    elsif (strategy1 == 'R' and strategy2 == 'S')
        return player1
    else
        return player2
    end
  end

  def self.tournament_winner(tournament)
    if tournament[0][0].is_a? String
      return self.winner(tournament[0], tournament[1])
    else
      return self.winner(self.tournament_winner(tournament[0]),
                         self.tournament_winner(tournament[1]))
    end
  end

end
