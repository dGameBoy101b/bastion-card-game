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

	def __init__(self, result_strength: dict[Battle.Result, int] = None):
		self.result_strength = WeakToStrongStrategy.DEFAULT_RESULT_STRENGTH
		self.result_strength.update(result_strength)

	def card_strength(self, card: Rank, view: GameView) -> int:
		strength = 0
		for neutral in view.next_neutrals():
			result = view.decider().determine_result(Battle(neutral, card, neutral))
			strength += self.result_strength[result]
		return strength

	def __call__(self, view:GameView) -> Rank:
		strongest: Rank = None
		strongest_strength: int = None
		for card in view.your_cards():
			strength = self.card_strength(card, view)
			if strongest is None or strength > strongest_strength:
				strongest = card
				strongest_strength = strength