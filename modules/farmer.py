from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time
import random

m = PyMouse()
k = PyKeyboard()

cbs = coord_by_step = None


def farm(
    rounds = 10,
    start_time = 2,
    computer='home',
    CC = None
):
    for i in range(0, rounds):
        print("ROUND "+str(i+1))
        #BATTLE
        print('     Force battle and beggining')
        

        for j in range(0,3): 
            X, Y = CC.getStepCoord('battle')   
            m.click(X, Y, 1) 
            time.sleep(start_time*1.2+ random.uniform(0,1))
        time.sleep(start_time*8 + random.uniform(0,2))


        print('     Next battle')
        #CLOSE AD
        #X, Y = CC.getStepCoord('add2')
        #m.click(X, Y, 1) 
        #time.sleep(start_time *0.7+ random.uniform(0,1))
        #Next
        X, Y = CC.getStepCoord('jump_lost_battle')
        m.click(X, Y, 1) 
        time.sleep(0.5 + random.uniform(0,1))
        
        #NEXT FARM
        X, Y = CC.getStepCoord('next_battle')
        m.click(X, Y, 1) 
        time.sleep(start_time *0.5+ random.uniform(0,1))
        
def headHunt(
    rounds = 10,
    start_time = 2,
    computer='work',
    headhunt_type='easy',
    has_infinity_war=False,
    CC = None
):
    hunt_parser = {
        'easy': 'headHuntEasy',
        'hard': 'headHuntHard'
    }
    hunt_level = hunt_parser[headhunt_type]

    ##START
    X, Y = CC.getStepCoord('start')
    m.click(X, Y, 1) 
    time.sleep(random.uniform(0,1))
    for i in range(0, rounds):
            
        print("ROUND ", int(i+1))
        #BATTLE
        print('     Headhunt start')    
        X, Y = CC.getStepCoord(hunt_level) 
        
        if(has_infinity_war==False):
            Y -= 185
        m.click(X, Y, 1) 
        time.sleep(start_time*2 + random.uniform(0,2))

        #BATTLE
        print('     Hunt beggining')
        X, Y = CC.getStepCoord('start')   
        m.click(X, Y, 1) 
        time.sleep(start_time*5 + random.uniform(0,2))

        print('     Close adv. and Next battle')
        #CLOSE AD
        #X, Y = CC.getStepCoord('add1')
        #m.click(X, Y, 1) 
        #time.sleep(start_time *0.7+ random.uniform(0,1))
        
        #Next
        X, Y = CC.getStepCoord('jump_lost_battle')
        m.click(X, Y, 1) 
        time.sleep(0.5 + random.uniform(0,1))
        
        #Next
        X, Y = CC.getStepCoord('next_battle')
        m.click(X, Y, 1) 
        time.sleep(start_time *0.7+ random.uniform(0,1))
        
        
        

#(challenge_X, challenge_Y) = m.position() #OPEN TROOP
#print(challenge_X, challenge_Y)
#(challenge_X, challenge_Y) = m.position() #TROOP ADV
#print(challenge_X, challenge_Y)
#(challenge_X, challenge_Y) = m.position() #HERO OPEN
#print(challenge_X, challenge_Y)
#(challenge_X, challenge_Y) = m.position() #HERO ADV
#print(challenge_X, challenge_Y)
#(challenge_X, challenge_Y) = m.position() #CLOSE ADV
#print(challenge_X, challenge_Y)
#(challenge_X, challenge_Y) = m.position() #CLAIM TROOP
#print(challenge_X, challenge_Y)
#(sale_X, sale_Y) = m.position() #CLOSE SALE
#print(sale_X, sale_Y)
#(sale_X, sale_Y) = m.position() #HEADHUNT EASY
#print(sale_X, sale_Y)
#m.click(1162, 615, 1)
#m.click(1163, 615, 1)
#(sale_X, sale_Y) = m.position() #HEADHUNT HARD
#print(sale_X, sale_Y)
#(sale_X, sale_Y) = m.position() #NEXT FARM
#print(sale_X, sale_Y)
#(challenge_X, challenge_Y) = m.position() #ADD2
#print(challenge_X, challenge_Y)

