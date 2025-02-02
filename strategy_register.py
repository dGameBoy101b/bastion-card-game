from dataclasses import dataclass
from typing import List
from ask_multichoice import ask_multichoice
from game import Strategy

@dataclass(frozen=True)
class StrategyInfo:
	strategy: Strategy
	name: str

strategies: List[StrategyInfo] = []

def ask_strategy(prompt: str) -> Strategy:
	global strategies
	choices = (info.name for info in strategies)
	result = (info.strategy for info in strategies)
	index = ask_multichoice(prompt, choices)
	return result[index]
