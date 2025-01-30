from ordered_decorator import ordered
from rank import Rank

ACE_HIGH_ORDER = (Rank.Two, Rank.Three, Rank.Four, Rank.Five, Rank.Six, Rank.Seven, Rank.Eight, Rank.Nine, Rank.Ten, Rank.Jack, Rank.Queen, Rank.King, Rank.Ace)

AceHighRank = ordered(ACE_HIGH_ORDER)(Rank)
	
if __name__ == "__main__":
	assert AceHighRank.Five == AceHighRank.Five
	assert AceHighRank.Ten < AceHighRank.Jack
	assert AceHighRank.Ace > AceHighRank.King