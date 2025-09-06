import random

easy_words = ["apple", "train", "tiger", "money", "india"]

medium_words = ["python","buttle","monkey","planet", "laptop"]

hard_words = ["elephant","diamond", "umbrella","computer","mountain"]

print('wecome to passeord guessing game')
print('choose your difficulty mode')

level = input('enter difficulty: ').lower()
if level == 'easy':
    secret = random.choice(easy_words)
elif level == 'medium':
    secret = random.choice(medium_words)
elif level == 'hard':
    secret = random.choice(hard_words)
else:
    print('choice invalid, defaulting to easy level')
    secret = random.choice(easy_words)

attempts = 0
print('\nguess the secret password')

while True:
    guess = input('enter your guiess: ').lower()
    attempts += 1

    if guess == secret:
        print(f'congrutulations you guessed it right in {attempts} attempts')
        break


