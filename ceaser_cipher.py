import nltk
from nltk.corpus import words
nltk.download('words')
word_list = words.words()
import random


def encrypt(string, key):
	"""Function that takes in string to be encrypted using key"""
	alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

	new_string = ''

	for char in string.lower():
		if char in alpha:
			new_string += alpha[(alpha.index(char) + key) % len(alpha)]
		else:
			new_string += char

	return new_string

def decrypt(string, key):
	"""Function that takes in encrypted string and key and returns decrypted string"""
	return encrypt(string, -key)


