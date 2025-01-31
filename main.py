from game import Game
from battle import Battle
from battle_decider import BattleDecider
from strategies.input_strategy import InputStrategy
from strategies.random_strategy import random_strategy
from war_scorer import WarScorer

game = Game(BattleDecider(), WarScorer())
player = InputStrategy()
ai = random_strategy
while game.winner() is None:
	game.play_next_turn(player, ai)

WINNER_TEXT = {
	Battle.Result.Tie: "It was a tie",
	Battle.Result.Player1Win: "You won",
	Battle.Result.Player2Win: "You lost"
}

print(WINNER_TEXT[game.winner()])