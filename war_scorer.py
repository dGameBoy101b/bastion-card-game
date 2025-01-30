from typing import Tuple
from battle import Battle

class WarScorer:
	def player1_score(self, battles: Tuple[Battle]) -> int:
		score = 0
		pending_score = 1
		for battle in battles:
			if battle.result == Battle.Result.Tie:
				pending_score += 1
				continue
			if battle.result == Battle.Result.Player1Win:
				score += pending_score
			pending_score = 1
		return score
	
	def player2_score(self, battles: Tuple[Battle]) -> int:
		for battle in battles:
			battle.flip_players()
		return self.player1_score(battles)