from typing import Iterable
from battle import Battle
from battle_decider import BattleDecider
from game_view import GameView
from rank import Rank
from strategies.weak_to_strong_strategy import WeakToStrongStrategy

class WeakestWinnerStrategy(WeakToStrongStrategy):
	'''Plays the weakest card that will win the next battle if possible, otherwise just the weakest card'''

	def winners(self, cards: Iterable[Rank], neutral: Rank, decider: BattleDecider) -> frozenset[Rank]:
		return frozenset(card for card in cards if decider.determine_result(Battle(neutral, card, neutral)) == Battle.Result.Player1Win)

	def __call__(self, view: GameView) -> Rank:
		viable_cards = self.winners(view.your_cards(), view.current_neutral(), view.decider())
		if len(viable_cards) < 1:
			viable_cards = view.your_cards()
		return self.weakest(viable_cards, view.next_neutrals(), view.decider())