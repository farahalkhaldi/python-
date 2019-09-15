
print ("Mad libs where libs get mad.")
print ("Start below:")

time = input ("Enter a number from 1 to 12: ")
items = input ("Enter a noun (plural): ")
name = input ("Enter a name: ")
name = name.title()
scream = input ("Enter any sentence: ")
scream = scream.upper()
action = input ("Enter a verb: ")

story_madlibs = """It was {} o'clock when I heard a knock at the door.
    I opened the door and there was a box full of {} with a note saying "From Mr. {}."
    Just as I closed the door I heard a scream "{}."
    I froze in place and all I could do was {}.""".format (time, items, name, scream, action)
print (story_madlibs)