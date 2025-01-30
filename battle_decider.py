from battle import Battle
from rank import Rank

FACE_RANKS = frozenset({Rank.Jack, Rank.Queen, Rank.King})
NON_ACE_ORDER = (Rank.Two, Rank.Three, Rank.Four, Rank.Five, Rank.Six, Rank.Seven, Rank.Eight, Rank.Nine, Rank.Ten, Rank.Jack, Rank.Queen, Rank.King)

class BattleDecider:
	def determine_order(self, a: Rank, b: Rank) -> int:
		if a == b:
			return 0
		if a == Rank.Ace:
			return 1 if b in FACE_RANKS else -1
		if b == Rank.Ace:
			return -1 if a in FACE_RANKS else 1
		return NON_ACE_ORDER.index(a) - NON_ACE_ORDER.index(b)

	def determine_result(self, battle: Battle) -> Battle.Result:
		order_1_2 = self.determine_order(battle.player1, battle.player2)
		order_n_1 = self.determine_order(battle.neutral, battle.player1)
		order_n_2 = self.determine_order(battle.neutral, battle.player2)
		if order_1_2 == 0 or (order_n_1 >= 0 and order_n_2 >= 0):
			return Battle.Result.Tie
		return Battle.Result.Player1Win if order_1_2 > 0 else Battle.Result.Player2Win