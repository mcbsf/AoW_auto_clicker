from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time
import random

m = PyMouse()
k = PyKeyboard()

cbs = coord_by_step = None


def battle(
    hero_trial = False,
    start_time = 1.5,
    battles = 20,
    computer='home',
    extra_battle = False,
    CC = None
):
    cbs = coord_by_step = CC.cbs
    if(hero_trial == True):
    #IF IS HERO TRIAL
        cbs['challenge']['Y'] = cbs['challenge']['Y'] + 30
    

    for i in range(0, battles):
        print("ROUND "+str(i+1))
        
        #CHALLENGE
        print('     challenging')
        X, Y = CC.getStepCoord('challenge')
        m.click(X, Y, 1) #START
        time.sleep(start_time + random.uniform(1,2))

        
        #FIGHT WORSE
        print('     fight worse')
        X, Y = CC.getStepCoord('fight_worse')
        m.click(X, Y, 1) 
        
        if(extra_battle):

            time.sleep(random.uniform(1,2))
            print('     extra battle')
            X, Y = CC.getStepCoord('extra_battle')
            m.click(X, Y, 1) 
            time.sleep(start_time*3 + random.uniform(1,2))

        else:
            time.sleep(start_time*3 + random.uniform(1,2))
        
        
        #BEGGIN BATTLE
        print('     BEGGIN BATTLE')
        X, Y = CC.getStepCoord('beggin_battle')
        m.click(X, Y, 1) 
        if(hero_trial):
            start_time -= 0.3
        time.sleep(start_time*17 + random.uniform(1,2))
        if(hero_trial):
            start_time += 0.3
        
        
        
        #NEXT BATTLE
        print('     NEXT BATTLE')
        X, Y = CC.getStepCoord('next_battle')
        m.click(X, Y, 1)
        time.sleep(start_time*2 + random.uniform(1,2))
        


#NEXT FARM
