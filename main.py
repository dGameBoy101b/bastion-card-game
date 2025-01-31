from typing import Callable, Iterable
from game import Game
from battle import Battle
from battle_decider import BattleDecider
from game_view import GameView
from rank import Rank
from strategies.input_strategy import InputStrategy
from strategies.random_strategy import random_strategy
from strategies.weak_to_strong_strategy import WeakToStrongStrategy
from war_scorer import WarScorer

def ask_multichoice(prompt: str, choices: Iterable[str]) -> int:
	lines = [f"{index}: {choices[index]}" for index in range(len(choices))]
	prompt = f"{'\n'.join(lines)}\n{prompt}"
	while True:
		response = input(prompt)
		try:
			response = int(response)
		except ValueError as x:
			print("Enter a number")
			continue
		if response < 0:
			print("Enter a number 0 or greater")
			continue
		if response >= len(choices):
			print(f"Enter a number lesser than {len(choices)}")
			continue
		return response

def ask_player(prompt: str) -> Callable[[GameView], Rank]:
	CHOICES = ("Player", "Random", "Weak To Strong")
	RESULT = (InputStrategy(), random_strategy, WeakToStrongStrategy)
	index = ask_multichoice(prompt, CHOICES)
	return RESULT[index]

game = Game(BattleDecider(), WarScorer())
player1 = ask_player("Player 1> ")
player2 = ask_player("Player 2> ")
while game.winner() is None:
	game.play_next_turn(player1, player2)

WINNER_TEXT = {
	Battle.Result.Tie: "It was a tie",
	Battle.Result.Player1Win: "Player 1 won",
	Battle.Result.Player2Win: "Player 2 won"
}

print(InputStrategy().prompt(game.player1_view))
print(WINNER_TEXT[game.winner()])