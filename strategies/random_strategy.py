from random import choice
from bastion_game_view import BastionGameView
from rank import Rank

def random_strategy(view: BastionGameView) -> Rank:
	'''Picks a random card every turn'''
	cards = list(view.your_cards())
	return choice(cards)
