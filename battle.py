from dataclasses import dataclass
from enum import Enum

from rank import Rank

@dataclass()
class Battle:
	class Result(Enum):
		Tie = 0
		Player1Win = 1
		Player2Win = -1

	neutral: Rank
	player1: Rank|None = None
	player2: Rank|None = None
	result: Result|None = None

	def flip_players(self):
		self.player1, self.player2 = self.player2, self.player1
		if self.result is not None:
			self.result = Battle.Result(-self.result.value)
