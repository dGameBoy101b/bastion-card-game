from enum import Enum

class Rank(Enum):
	Ace = "A"
	Two = "2"
	Three = "3"
	Four = "4"
	Five = "5"
	Six = "6"
	Seven = "7"
	Eight = "8"
	Nine = "9"
	Ten = "10"
	Jack = "J"
	Queen = "Q"
	King = "K"

	def __str__(self)->str:
		return self.value

		