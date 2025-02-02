from game import Game
from battle import Battle
from battle_decider import BattleDecider
from strategies.input_strategy import InputStrategy
from strategy_register import ask_strategy
from war_scorer import WarScorer

def register_strategies():
	from strategy_register import StrategyInfo, strategies
	from strategies.random_strategy import random_strategy
	from strategies.weak_to_strong_strategy import WeakToStrongStrategy
	from strategies.weakest_winner_strategy import WeakestWinnerStrategy

	strategies += [StrategyInfo(InputStrategy(), "Player"),
		StrategyInfo(random_strategy, "Random"),
		StrategyInfo(WeakToStrongStrategy(), "Weak To Strong"),
		StrategyInfo(WeakestWinnerStrategy(), "Weakest Winner")]

game = Game(BattleDecider(), WarScorer())
register_strategies()
player1 = ask_strategy("Player 1> ")
player2 = ask_strategy("Player 2> ")
while game.winner() is None:
	game.play_next_turn(player1, player2)

WINNER_TEXT = {
	Battle.Result.Tie: "It was a tie",
	Battle.Result.Player1Win: "Player 1 won",
	Battle.Result.Player2Win: "Player 2 won"
}

print(InputStrategy().game_state(game.player1_view))
print(WINNER_TEXT[game.winner()])