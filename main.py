import random

# Fun facts and motivation list
facts = [
    "Did you know? Python is named after the comedy show Monty Python!",
    "Python is one of the easiest programming languages to learn. No cap!",
    "You're amazing! Keep going on your learning journey!",
    "Fun fact: Python is used by Google and NASA. Like, super cool, right?"
]

motivations = [
    "Keep pushing forward, you got this!",
    "Everything you learn today will help you tomorrow!",
    "It’s never too late to learn!",
    "Learning Python is a big step towards success!"
]

# Function to greet the user and show facts
def greet_user():
    print("Welcome to Blue-Project! 🌟")
    name = input("What's your name? ")
    print(f"Hey {name}! Great to meet you! 🤖")

    # Show a random fun fact
    print("\nHere’s a fun fact for you:")
    print(random.choice(facts))

    # Show a random motivational quote
    print("\nAnd here’s a little motivation for you:")
    print(random.choice(motivations))

greet_user()
