from dataclasses import dataclass
from typing import List
import ask_multichoice
from game import Strategy

@dataclass(frozen=True)
class StrategyInfo:
	strategy: Strategy
	name: str

strategies: List[StrategyInfo] = []

def ask_strategy(prompt: str) -> Strategy:
	global strategies
	CHOICES = (info.name for info in strategies)
	RESULT = (info.strategy for info in strategies)
	index = ask_multichoice(prompt, CHOICES)
	return RESULT[index]
