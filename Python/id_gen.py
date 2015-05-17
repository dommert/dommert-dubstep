# Dommert
# Random ID Generator
import random, string

def id_gen(length = 10):
	rand = random.SystemRandom()
	# If you want non-English characters, remove the [0:52]
	alphabet = string.letters[0:52] + string.digits
	data = str().join(rand.choice(alphabet) for _ in range(length))
	return data