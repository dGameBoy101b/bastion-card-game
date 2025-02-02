from typing import Tuple
from battle import Battle

class WarScorer:
	def player1_score(self, battles: Tuple[Battle]) -> int:
		score = 0
		pending_score = 1
		for battle in battles:
			if battle.result is None:
				break
			if battle.result == Battle.Result.Tie:
				pending_score += 1
				continue
			if battle.result == Battle.Result.Player1Win:
				score += pending_score
			pending_score = 1
		return score
	
	def player2_score(self, battles: Tuple[Battle]) -> int:
		return self.player1_score((battle.flipped_players() for battle in battles))
	
	def war_result(self, battles: Tuple[Battle]) -> Battle.Result | None:
		if len(battles) < 1 or battles[-1].result is None:
			return None
		player1_score = self.player1_score(battles)
		player2_score = self.player2_score(battles)
		if player1_score == player2_score:
			return Battle.Result.Tie
		return Battle.Result.Player1Win if player1_score > player2_score else Battle.Result.Player2Win
	
if __name__ == '__main__':
	from rank import Rank
	scorer = WarScorer()

	EMPTY = tuple()
	assert scorer.player1_score(EMPTY) == 0
	assert scorer.player2_score(EMPTY) == 0

	NONE1 = (Battle(Rank.Two, result=None),)
	assert scorer.player1_score(NONE1) == 0
	assert scorer.player2_score(NONE1) == 0

	TIE1 = (Battle(Rank.Two, result=Battle.Result.Tie),)
	assert scorer.player1_score(TIE1) == 0
	assert scorer.player2_score(TIE1) == 0

	PLAYER1 = (Battle(Rank.Two, result=Battle.Result.Player1Win),)
	assert scorer.player1_score(PLAYER1) == 1
	assert scorer.player2_score(PLAYER1) == 0

	PLAYER2 = (Battle(Rank.Two, result=Battle.Result.Player2Win),)
	assert scorer.player1_score(PLAYER2) == 0
	assert scorer.player2_score(PLAYER2) == 1

	PLAYER1_TIE = (Battle(Rank.Two, result=Battle.Result.Tie), Battle(Rank.Two, result=Battle.Result.Player1Win))
	assert scorer.player1_score(PLAYER1_TIE) == 2
	assert scorer.player2_score(PLAYER1_TIE) == 0

	PLAYER2_TIE = (Battle(Rank.Two, result=Battle.Result.Tie), Battle(Rank.Two, result=Battle.Result.Player2Win))
	assert scorer.player1_score(PLAYER2_TIE) == 0
	assert scorer.player2_score(PLAYER2_TIE) == 2
