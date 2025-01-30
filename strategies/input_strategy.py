from typing import Iterable
from bastion_game_view import BastionGameView
from battle import Battle
from rank import Rank

class InputStrategy:
	def fixed_width_card(self, card: Rank) -> str:
		return str(card).center(2)

	def player_line(self, score: int, cards:Iterable[Rank]) -> str:
		return f"{score}\t{' '.join(self.fixed_width_card(card) for card in cards)}"
	
	def battles_lines(self, previous_battles: Iterable[Battle], next_neutrals: Iterable[Rank]) -> str:
		opponent_plays = []
		my_plays = []
		neutrals = []
		for battle in previous_battles:
			opponent_plays.append(battle.player2)
			my_plays.append(battle.player1)
			neutrals.append(battle.neutral)
		neutrals.extend(next_neutrals)
		return '\n'.join((' '.join(self.fixed_width_card(card) for card in opponent_plays),
				  ' '.join(self.fixed_width_card(card) for card in neutrals),
				  ' '.join(self.fixed_width_card(card) for card in my_plays)))

	def prompt(self, view: BastionGameView) -> str:
		return '\n'.join((self.player_line(view.opponent_score(), view.opponents_cards()),
				"",
				self.battles_lines(view.previous_battles(), view.next_neutrals()),
				"",
				self.player_line(view.your_score(), view.your_cards()),
				"Which card would you like to play?> "))
		
	
	def convert_input(self, input: str) -> Rank:
		return Rank(input.strip().upper())

	def __call__(self, view: BastionGameView) -> Rank:
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