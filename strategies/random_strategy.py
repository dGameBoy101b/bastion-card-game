from random import choice
from game_view import GameView
from rank import Rank

def random_strategy(view: GameView) -> Rank:
	'''Picks a random card every turn'''
	cards = list(view.your_cards())
	return choice(cards)
