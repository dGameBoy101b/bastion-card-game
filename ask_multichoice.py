from typing import Iterable

def ask_multichoice(prompt: str, choices: Iterable[str], *, raise_exceptions: bool = False) -> int:
	index = 0
	lines = []
	for choice in choices:
		lines.append(f"{index}: {choice}")
		index += 1
	if index < 1:
		raise ValueError("No choices to select")
	prompt = f"{'\n'.join(lines)}\n{prompt}"
	while True:
		response = input(prompt)
		try:
			response = int(response)
		except ValueError as x:
			if raise_exceptions:
				raise x
			print("Enter a number")
			continue
		if response < 0:
			if raise_exceptions:
				raise IndexError(f"{response} is not 0 or greater")
			print("Enter a number 0 or greater")
			continue
		if response >= index:
			if raise_exceptions:
				raise IndexError(f"{response} is not lesser than {index}")
			print(f"Enter a number lesser than {index}")
			continue
		return response
