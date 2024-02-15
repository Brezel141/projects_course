def get_input(word_type: str):
    user_input: str = input(f"Enter a {word_type}: ")
    return user_input


color1 = get_input("color")
adj1 = get_input("adjective")
time1 = get_input("time")
adj2 = get_input("adjective")
place1 = get_input("place")
food1 = get_input("food")
food2 = get_input("food")
verb1 = get_input("verb")
noun1 = get_input("noun")
number1 = get_input("number")


story = f'''
Bats are so cool! They are {color1}, {adj1} animals which have wings. 
They like to fly around at {time1} which makes some people scared of them. 
But bats are {adj2}, and they don't want to hurt people. I have a pet bat that lives in {place1}. 
I like to feed him {food1} and {food2}. He likes to {verb1}. I am his favorite person, but he also likes {noun1}. 
I want to convince my parents to get me {number1} more bats.
'''


print(story)
