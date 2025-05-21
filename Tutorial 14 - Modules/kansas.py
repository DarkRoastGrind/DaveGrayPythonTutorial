from random import choice

capital = "Topeka"
bird = "Western Meadowlark"
flower = "Sunflower"
song = "Home on the Range"


# Fun facts function that can be used to output a random
# fun fact regarding kansas
def randomfunfact():
    funfacts = [
        "Kansas is considered flat, but it does have a mountain.",
        "Wichita is the largest city in the state, but many would guess that it is Kansas City.",
        "A considerable portion of Kansas City is actually in Missouri.",
        "Most Kansans are annoyed by Wizard of Oz references from people outside of Kansas."
    ]
    # Chose between one of the 4 facts.
    index = choice("0123")
    # Convert the funfact to an integer.
    print(funfacts[int(index)])


# If, and only if, the current running module is __main__,
if __name__ == "__main__":
    randomfunfact()
