"""name. The name of the team, a string. 
goals. The number of goals scored in each game in 2023, a list of ints.
x. The team’s x-position on the matplotlib grid.
y. The team’s  y-position on the matplotlib grid.
color. The team’s color when rendered on matplotlib.

"""
import matplotlib.pyplot as plt 

class Team:
    def __init__ (self, name, x=0, y=0, color= "purple"): # ONLY PUT : AT THE END OF FUNCTION LINE
        self.name = name
        self.x = x
        self.y = y
        self.color = color
        self.goals = [] # EMPTY LIST

    def draw(self):
        pass

    def add_goals(self, goals):
        pass

    def get_total_goals(self):
        pass

    def move_next(self):
        pass

    def __str__(self):
        return f"teamname: {self.name}"

print()
print(Team("poop"))


"""draw(self). Render the team on the matplotlib grid at its current x, y position and with its color. You can make the team any matplotlib marker shape you want.
add_goals(self, goals). Append the given goals, an int, to the team’s list of goals.
get_total_goals(self). Returns the total goals of all the goals in the goals list, an int..
move_next(self). Move the team to the right by the amount found in the next position in 
            its goals list. The list method pop could be useful here!
__str__(self). Return a string that you’d like to be used when you call print() on a Team 
"""
    