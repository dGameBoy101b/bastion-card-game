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
	
	def war_result(self, battles: Tuple[Battle]) -> Battle.Result:
		player1_score = self.player1_score(battles)
		player2_score = self.player2_score(battles)
		if player1_score == player2_score:
			return Battle.Result.Tie
		return Battle.Result.Player1Win if player1_score > player2_score else Battle.Result.Player2Win