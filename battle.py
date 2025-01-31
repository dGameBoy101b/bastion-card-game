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

	def fliped_players(self) -> 'Battle':
		return Battle(self.neutral, self.player2, self.player1, None if self.result is None else Battle.Result(-self.result.value))

