from typing import Iterable
from game_view import GameView
from battle import Battle
from rank import Rank

class InputStrategy:
	'''Prints current game state and prompts for a card to play'''

	def fixed_width_card(self, card: Rank) -> str:
		return str(card).center(2)

	def player_line(self, score: int, cards:Iterable[Rank]) -> str:
		return f"{score}\t{' '.join(self.fixed_width_card(card) for card in cards)}"
	
	def battles_lines(self, previous_battles: Iterable[Battle], next_neutrals: Iterable[Rank]) -> str:
		COLUMN_SEPARATOR = ' '
		ROW_SEPARATOR = "\n"
		OPPONENT_WIN = "^"
		YOUR_WIN = "v"
		NOT_WIN = ""
		opponent_plays = []
		my_plays = []
		neutrals = []
		results = []
		for battle in previous_battles:
			opponent_plays.append(battle.player2)
			my_plays.append(battle.player1)
			neutrals.append(battle.neutral)
			results.append(battle.result)
		neutrals.extend(next_neutrals)
		return ROW_SEPARATOR.join((
			COLUMN_SEPARATOR.join(self.fixed_width_card(OPPONENT_WIN if result == Battle.Result.Player2Win else NOT_WIN) for result in results),
			COLUMN_SEPARATOR.join(self.fixed_width_card(card) for card in opponent_plays),
			COLUMN_SEPARATOR.join(self.fixed_width_card(card) for card in neutrals),
			COLUMN_SEPARATOR.join(self.fixed_width_card(card) for card in my_plays),
			COLUMN_SEPARATOR.join(self.fixed_width_card(YOUR_WIN if result == Battle.Result.Player1Win else NOT_WIN) for result in results)))

	def game_state(self, view: GameView) -> str:
		return '\n'.join((self.player_line(view.opponent_score(), view.opponents_cards()),
			self.battles_lines(view.previous_battles(), view.next_neutrals()),
			self.player_line(view.your_score(), view.your_cards())))

	def prompt(self, view: GameView) -> str:
		return f"{self.game_state(view)}\nWhich card would you like to play?> "
		
	
	def convert_input(self, input: str) -> Rank:
		return Rank(input.strip().upper())

	def __call__(self, view: GameView) -> Rank:
		prompt = self.prompt(view)
		card = None
		while card is None:
			response = input(prompt)
			try:
				card = self.convert_input(response)
			except Exception as x:
				print('Failed to convert input to card:', x)
				continue
			if card not in view.your_cards():
				print('Card not in your hand:', card)
				card = None
				continue
		return card