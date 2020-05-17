"""
You live in the city of Cartesia where all roads are laid out in a perfect grid.
The city provides its citizens with a Walk Generating App on their phones
Everytime you press the button it sends you an array of one-letter strings representing directions to walk 
(eg. ['n', 's', 'w', 'e'])
You always walk only a single block in a direction and you know it takes you one minute to traverse one city block, 
Create a function that will return true if the walk the app gives you will take you exactly ten minutes 
(you don't want to be early or late!) and will, of course, return you to your starting point. 
Return false otherwise.
"""

def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    else:
        if (walk.count('n') == walk.count('s')) & (walk.count('e') == walk.count('w')):
            return True
        else:
            return False


# can be done in one line, would have this in my else as i like nipping in the bud the length check
# def isValidWalk(walk):
    # return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')