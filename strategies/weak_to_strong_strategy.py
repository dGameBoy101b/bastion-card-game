from typing import Iterable
from battle_decider import BattleDecider
from game_view import GameView
from battle import Battle
from rank import Rank

class WeakToStrongStrategy:
	'''Plays the card least likely to win future battles'''

	DEFAULT_RESULT_STRENGTH = {
		Battle.Result.Player1Win: 1,
		Battle.Result.Tie: 0,
		Battle.Result.Player2Win: -1
	}

	def __init__(self, result_strength: dict[Battle.Result, int] = ()):
		self.result_strength = WeakToStrongStrategy.DEFAULT_RESULT_STRENGTH
		self.result_strength.update(result_strength)

	def card_strength(self, card: Rank, next_neutrals: Iterable[Rank], decider: BattleDecider) -> int:
		strength = 0
		for neutral in next_neutrals:
			result = decider.determine_result(Battle(neutral, card, neutral))
			strength += self.result_strength[result]
		return strength
	
	def weakest(self, your_cards: Iterable[Rank], next_neutrals: Iterable[Rank], decider: BattleDecider) -> Rank:
		weakest: Rank = None
		weakest_strength: int = None
		for card in your_cards:
			strength = self.card_strength(card, next_neutrals, decider)
			if weakest is None or strength < weakest_strength:
				weakest = card
				weakest_strength = strength
		return weakest

	def __call__(self, view:GameView) -> Rank:
		return self.weakest(view.your_cards(), view.next_neutrals(), view.decider())