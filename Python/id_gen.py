# Dommert
# Random ID Generator
import random, string

def id_gen(length = 10):
	myrg = random.SystemRandom()
	# If you want non-English characters, remove the [0:52]
	alphabet = string.letters[0:52] + string.digits
	pw = str().join(myrg.choice(alphabet) for _ in range(length))
	return pw