from typing import Iterable

def ask_multichoice(prompt: str, choices: Iterable[str], *, raise_exceptions: bool = False) -> int:
	lines = [f"{index}: {choices[index]}" for index in range(len(choices))]
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
		if response >= len(choices):
			if raise_exceptions:
				raise IndexError(f"{response} is not lessern than {len(choices)}")
			print(f"Enter a number lesser than {len(choices)}")
			continue
		return response
