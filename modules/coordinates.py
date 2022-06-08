import random
class CoordinatesController:
    
    def __init__(self, x_factor, y_factor):
            self.x_factor = x_factor
            self.y_factor = y_factor
            
    
    def getStepCoord(self, step):
        x_adjustment = 0
        y_adjustment = 0
        if(self.stage == "battle_arena"):
            x_adjustment = 25
        return int(self.cbs[step]['X']*self.x_factor) + x_adjustment + random.randint(0,10) - 5, int(self.cbs[step]['Y']*self.y_factor) + y_adjustment + random.randint(0,5) - 2
    
    def setCbs(self, stage):
        self.stage = stage
        if(stage == "farmer"):
            cbs = {
                'battle': {
                    'X': int(1609),
                    'Y': int(852),
                },
                'next_battle': {
                    'X': int(1688),
                    'Y': int(777),
                },
                'jump_lost_battle': {
                    'X': int(1691),
                    'Y': int(681),
                },
                'add1': {
                    'X': int(1870),
                    'Y': int(284) ,
                },
                'add2': {
                    'X': int(1305),#1307 167
                    'Y': int(165),
                },
                'headHuntHard': {
                    'X': int(1245),
                    'Y': int(685)#600,
                },
                'headHuntEasy': {
                    'X': int(1240),
                    'Y': int(498)#450,
                }     
            }

        elif(stage == "battle_arena"):
            cbs = {
                'challenge': {
                    'X': 1253 - 89,
                    'Y': 1840 - 1170 + 10,
                },
                'fight_worse': {
                    'X': 1352 - 89 - 15,
                    'Y': 1725 - 1170 - 5,
                },
                'extra_battle': {
                    'X': 1179,
                    'Y': 478
                },
                'beggin_battle': {
                    'X': 1254 - 89,
                    'Y': 1815 - 1170 + 10,
                },
                'next_battle': {
                    'X': 1251 - 95,
                    'Y': 1745 - 1170,
                }
            }  

        elif(stage == "main"):
            cbs = {
                'farmer': {
                    'X': 1253,
                    'Y': 1840,
                },
                'arena': {
                    'X': 1352,
                    'Y': 1725,
                },
                'territory': {
                    'X': 1352,
                    'Y': 1725,
                },
                'headhunt': {
                    'X': 1253,
                    'Y': 1840,
                },
                'hero_trial': {
                    'X': 1179,
                    'Y': 478
                },
                'exit': {
                    'X': 1179,
                    'Y': 478
                },
            }
        self.cbs = cbs
def createCoordinatesController(x_factor = 1, y_factor = 1):
    return CoordinatesController(x_factor, y_factor)

#(challenge_X, challenge_Y) = m.position() #BATTLE
#print(challenge_X, challenge_Y)

#(challenge_X, challenge_Y) = m.position() #NEXT
#print(challenge_X, challenge_Y)
""" 
from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time
import random

m = PyMouse()
k = PyKeyboard()

imports()
(challenge_X, challenge_Y) = m.position() #NEXT LOST
print(challenge_X, challenge_Y)
 """
#(challenge_X, challenge_Y) = m.position() #CLAIM TROOP
#print(challenge_X, challenge_Y)

#(challenge_X, challenge_Y) = m.position() #CLAIM TROOP
#print(challenge_X, challenge_Y)
