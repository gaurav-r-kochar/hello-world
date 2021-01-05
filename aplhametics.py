import re
import itertools

def solve(puzzle):
	words=re.findall('[a-z]+',puzzle.lower())
	unique_char=set("".join(words))
	first_letters={word[0] for word in words}
	n=len(first_letters)
	unique_sorted_char="".join(first_letters)+"".join(unique_char - first_letters)
	char=tuple(ord(c) for c in unique_sorted_char)
	digit=tuple(ord(c) for c in '0123456789')
	z=digit[0]
	for guess in itertools.permutations(digit,len(char)):
		if z not in guess[:n]:
			match=dict(zip(char,guess))
			eq=puzzle.translate(match)
			if eval(eq):
				return eq

print(solve(input()))