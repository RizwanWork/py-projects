#import the random m odule
import random

#2 create subjects
subjects = [
    "monkey",
    "giraffe",
    "a group of elephants",
    "a herd of lions",
    "a pack of jaguars",
    "a lonely sloth",
    "a bunch of crows"
]

actions = [
    "riding a bycycle",
    "driving a car",
    "placing a orders",
    "sitting on a branch",
    "playing football",
    "declares war on",
    "launches", 
]

places_or_things = [
    "at red fort",
    "in mumbai local train",
    "in the jungle",
    "at airport",
    "in parliament",
    "at india gate"
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)
    headline = f" Breaking News :{subject} {action} {place_or_thing}"
    print("\n" + headline)

    user_input = input("\nDo you want another input (yes/no)").strip().lower()
    if user_input == "no":
        break

print("\nThanks for using fun headline generator. Have a great day")    