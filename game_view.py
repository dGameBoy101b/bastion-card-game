from game import Game
from battle import Battle
from battle_decider import BattleDecider
from rank import Rank
from war_scorer import WarScorer

class GameView:
	def __init__(self, game:Game, is_player1: bool = True):
		self.__game = game
		self.__is_player1 = is_player1
	
	def decider(self) -> BattleDecider:
		return self.__game.battle_decider
	
	def scorer(self) -> WarScorer:
		return self.__game.war_scorer

	def your_cards(self) -> set[Rank]:
		return self.__game.player1_cards if self.__is_player1 else self.__game.player2_cards
	
	def opponents_cards(self) -> set[Rank]:
		return self.__game.player2_cards if self.__is_player1 else self.__game.player1_cards
	
	def your_score(self) -> int:
		return self.__game.player1_score() if self.__is_player1 else self.__game.player2_score()
	
	def opponent_score(self) -> int:
		return self.__game.player2_score() if self.__is_player1 else self.__game.player1_score()
		
	def current_neutral(self) -> Rank:
		return self.__game.battles[self.__game.current_index].neutral
	
	def next_neutrals(self) -> tuple[Rank]:
		return tuple(battle.neutral for battle in self.__game.battles[self.__game.current_index:])
	
	def previous_battles(self) -> tuple[Battle]:
		'''You are player 1 in returned battles'''
		battles = self.__game.battles[:self.__game.current_index]
		if not self.__is_player1:
			for battle in battles:
				battle.flip_players()
		return battles
