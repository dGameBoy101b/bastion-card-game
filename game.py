from random import shuffle
from typing import Callable
from game_view import GameView
from battle import Battle
from battle_decider import BattleDecider
from rank import Rank
from war_scorer import WarScorer

class Game:
	def __init__(self, battle_decider: BattleDecider = BattleDecider(), war_scorer: WarScorer = WarScorer()):
		self.battle_decider = battle_decider
		self.war_scorer = war_scorer
		self.player1_view = GameView(self, True)
		self.player2_view = GameView(self, False)
		self.reset()
	
	def reset(self) -> None:
		self.player1_cards = set(Rank)
		self.player2_cards = set(Rank)
		neutrals = list(Rank)
		shuffle(neutrals)
		self.battles = tuple(Battle(neutral) for neutral in neutrals)
		self.current_index = 0
	
	def player1_score(self) -> int:
		return self.war_scorer.player1_score(self.battles)
	
	def player2_score(self) -> int:
		return self.war_scorer.player2_score(self.battles)

	def winner(self) -> Battle.Result | None:
		return self.war_scorer.war_result(self.battles)

	def play_next_turn(self, player1_strategy: Callable[[GameView], Rank], player2_strategy: Callable[[GameView], Rank]) -> None:
		if self.current_index >= len(self.battles):
			raise IndexError("No next turn to play")
		
		player1_card = player1_strategy(self.player1_view)
		if player1_card not in self.player1_cards:
			raise ValueError("Player 1 tried to play card they do not have")
		
		player2_card = player2_strategy(self.player2_view)
		if player2_card not in self.player2_cards:
			raise ValueError("Player 2 tried to play card they do not have")
		
		battle = self.battles[self.current_index]
		battle.player1 = player1_card
		battle.player2 = player2_card
		self.battle_decider.determine_result(battle)
		self.current_index += 1
