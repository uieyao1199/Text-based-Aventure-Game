#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 10:36:20 2018

@author: Xiaojun Yao

Working Directory: /Users/uieyao/Desktop/PyCourse

A1: Text Adventure Game Development

"""

###############################################################################
# Background Introduction
###############################################################################

"""
Introduction:

    Welcome to the "Dawn of the Death" Game. The designing idea of this game is
    a combination of Zombie theme movie and Room Escape Game.
    
    A player will need to accept and complete the mission of rescuing a NPC 
    (Dr. Andy Zheng) from a zombie hospital. In order to win the game, the
    player will need to make wise choices as he or she enters different rooms 
    of the game. 

Purpose:
    
    The purpose of this game to increase player engagement by involving players
    into the story line. Moreover, it also increases user experience by making
    players to make multiple choice question to move forward instead of open-end
    question. Overall, to have fun!!
    
Bugs:
    None
    
"""


###############################################################################
# The "Dawn of the Death" Game Introduction
###############################################################################
    
print("\f")
print("*"*80)
print("")
print(f"""
          Hello,\n
          Welcome to the <Dawn of The Death> Game!\n  
        ███████╗ ██████╗ ███╗   ███╗██████╗ ██╗███████╗
        ╚══███╔╝██╔═══██╗████╗ ████║██╔══██╗██║██╔════╝
          ███╔╝ ██║   ██║██╔████╔██║██████╔╝██║█████╗  
         ███╔╝  ██║   ██║██║╚██╔╝██║██╔══██╗██║██╔══╝  
        ███████╗╚██████╔╝██║ ╚═╝ ██║██████╔╝██║███████╗
        ╚══════╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚═╝╚══════╝
          """)
print("""
          What is your name?""")
user_name = input("\t\t> ")
print(f"""
          Welcome to the game {user_name}, good luck!\n""")
print("*"*80)
print("")
import time
time.sleep(1)
print(f"""
       When a disease turns all of humanity into the living deads, Dr. Andy Zheng,
       a national-level researcher for the 'Zombie Hunter' project, developled an
       effective antidote for this horrible disease. However, he and his antidote
       is now trapped in a research hospital with dozens of zombies.
       """)
import time
time.sleep(1)
print(f"""
       You, {user_name}, as a FBI special agent, your mission, should you choose to 
       accept it, is to safely bring Dr. Zheng and his antidote out.
       """)
import time
time.sleep(1)
print("")
print("*"*80)
print("")

###############################################################################
# Game Setting up -- Backstage
###############################################################################    

def game_0():
    """First choice to enter the game, accept the mission or not"""
    
    print("""
      * Would you choose to accept your mission? 
          A: accept
          B: refuse""")
    
    choice_1 = input("\t > ")
        
    if 'ac' in choice_1:
        print("\f")
        print(f"""
          The world is counting on you to save! Good luck Agent {user_name}!!
              """)
        import time
        time.sleep(2)
        print("\f")
        game_playing()
        
    elif 're' in choice_1:
        double_asking = input("""
      Are you sure you want to refuse the mission and end the game?
      Enter "yes" to end the game or "no" to choose again.\n
      > """)
        if double_asking.lower() == "yes":    
            print("*"*80)
            print("""
      Shame on you for missing the chance to save the world!
      You are fired Agent {user_name}.\n
      Your game ends here...
     ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███  
     ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
    ▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
    ░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
    ░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
     ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
      ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
    ░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░ 
          ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░     
                                                         ░                  
      """)
            print("*"*80)
        
        elif double_asking.lower() == "no":
            game_0()
        
        else: 
            print("""
                  <Invalid entry, please choose again>""")
            game_0()
        
    elif choice_1.lower() == "a":
        print("\f")
        print(f"""
          The world is counting on you to save! Good luck Agent {user_name}!!
              """)
        import time
        time.sleep(2)
        print("\f")
        game_playing()
        
    elif choice_1.lower() == "b":
        double_asking = input("""
      Are you sure you want to refuse the mission and end the game?
      Enter "yes" to end the game or "no" to choose again.\n
      > """)
        if double_asking.lower() == "yes":    
            print("*"*80)
            print("""
      Shame on you for missing the chance to save the world!
      You are fired Agent {user_name}.\n
      Your game ends here...
     ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███  
     ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
    ▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
    ░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
    ░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
     ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
      ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
    ░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░ 
          ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░     
                                                         ░                  
      """)
            print("*"*80)
        
        elif double_asking.lower() == "no":
            game_0()
        
        else: 
            print("""
                  <Invalid entry, please type "yes" or "no">""")
            game_0()
            
    else:
        print("""
      Invalid entry, please choose A to continue the game or B to end the game.""")
        choice_2 = input("""
                  <Press enter to choose again>""")
        game_0()

def game_playing():
    """Linking all the games together, start playing game."""
    print("*"*80)
    print("") 
    print("""
      You are now in a suspiciously empty hospital, having no way back.""")
    import time
    time.sleep(1)
    print("""
      In front of you, there are two doors: """)
    game_6()
          



def game_1():
    """For second time enter the office after getting ID"""

    print("\f")
    print("*"*80)
    print(f"""
        Now you are back in the office holding the safebox in your hand.
        It requires a 4 digit number pin to open.\n  
        You now have 2 chances to guess the pin of the safebox.
        Once you hit the limit of guesses and still did not get
        it right, the safebox will automatically EXPLODE !!!\n
        Good luck, Agent {user_name}!
        """)
    import time
    time.sleep(2)
    print("""
        Information you have right now:
        You notice a calender on his desk marked Dr. Andy's birthday,
        his wife's birthday and their anniversary. You also know Dr. Andy's
        working ID number from his ID card.
        """)
        
    guesses = 2
    
    while guesses > 0:
        
        pin_list = ["0212", "0113", "0208", "0210"]
        
        import random
        
        pin_guess = input("""
        * You have the chance to choose among the following
               <Please enter 1, 2, 3 or 4 to guess>\n
             1. try with Dr. Andy's birthday: 0212
             2. try with Dr. Andy's ID number: 0113     
             3. try with Dr. Andy's wife birthday: 0208
             4. try with Dr. Andy's anniversary: 0210\n
             > """)
        
        if pin_guess == random.choice(pin_list):
            print("\f")
            print("*"*80)
            print("""
          That's correct!! 
          What an excellent choice!\n""")
            print("""
          The safe box is succesfully opened.\n""")
            print("""
          You can use the antidote inside to bring Dr. Andy back to human.\n""")
            print("""
          To exit the building, a valid user's fingerprint is required to open the
          exit door.
          """)
            exit_building = input("""
          Would you like to try with your fingerprint or Dr. Andy's?
          Enter "me" for yourself and "andy" for Dr.Andy.\n
          > """)
            if exit_building == "me":
                print("*"*80)
                print("""
          Ahhhhh
          "I really wonder where your confidence come from." said Dr. Andy.
                """)
                print("""
          Dr. Andy opens the Exit door with his fingerprint
                """)
                import time
                time.sleep(2)
                print(f"""
            ██████╗ ██████╗  █████╗ ██╗   ██╗ ██████╗ 
            ██╔══██╗██╔══██╗██╔══██╗██║   ██║██╔═══██╗
            ██████╔╝██████╔╝███████║██║   ██║██║   ██║
            ██╔══██╗██╔══██╗██╔══██║╚██╗ ██╔╝██║   ██║
            ██████╔╝██║  ██║██║  ██║ ╚████╔╝ ╚██████╔╝
            ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝   ╚═════╝\n
            Mission completed.
            Congratulation Agent {user_name} !! 
            You brought Dr. Andy and his antidote out safely.\n
            Hope that you enjoyed the game !
            """)
                print("*"*80)
            
            elif exit_building == "andy":
                print("*"*80)
                print("""
          Dr. Andy opens the Exit door with his fingerprint
                """)
                print(f"""
            ██████╗ ██████╗  █████╗ ██╗   ██╗ ██████╗ 
            ██╔══██╗██╔══██╗██╔══██╗██║   ██║██╔═══██╗
            ██████╔╝██████╔╝███████║██║   ██║██║   ██║
            ██╔══██╗██╔══██╗██╔══██║╚██╗ ██╔╝██║   ██║
            ██████╔╝██║  ██║██║  ██║ ╚████╔╝ ╚██████╔╝
            ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝   ╚═════╝\n
            Mission completed.
            Congratulation Agent {user_name} !! 
            You brought Dr. Andy and his antidote out safely.\n
            Hope that you enjoyed the game !
            """)
                print("*"*80)
            
            break 
        
        elif pin_guess != random.choice(pin_list):
            print("""
                  <That's incorrect>""")
            guesses -= 1
            print(f"""\n
                  You still have {guesses} guess left. Good luck.""")
            print("*"*80)
        
        else:
            print("""
                  <Invalid entry, please enter 1, 2, 3 or 4>""")
            game_2()
    
    else:
        print("\f")
        print("*"*80)
        print(f"""
      oops...you are out of guesses. the safebox exploded. You are dead.\n
      The correct answer is {random.choice(pin_list)}.
      """)
        import time
        time.sleep(1)
        print(f"""
      Mission failed Agent {user_name}. R.I.P.\n
     ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███  
     ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
    ▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
    ░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
    ░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
     ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
      ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
    ░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░ 
      ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░     
                                             ░                  
      Hope that you enjoyed the game! """)
        print("*"*80)    
    
    

def game_2():
    """Entering the lobby"""
    
    print("\f")
    print("*"*80)
    print("""
         Now you are in the main lobby of this hospital""")
    print("""
         A zombie is growling and runing to you,
         all he wants is to turn you into his food.
         """)
    import time
    time.sleep(1)
    print("""
         But don't worry yet, he is locked with an iron chain.
         You are at a safe distance.\n
         You can see there is an ID card on the floor
         but it is very close to the zombie.""")
    import time
    time.sleep(3)
    choice_pickup = input("""
         * You can choose how you would like to pick up the ID\n
             1. Shoot on the wall to distract the zombie's attention,
                then pick up ID.\n
             2. Directly fight the zombie with knife, then pick up the ID.\n
             3. Shoot on the zombie's head to kill him, then pick up the ID.\n
             > """)
    
    if choice_pickup == str(2):
        print("*"*80)
        print("""
         Congratulation!
         You have picked up the ID successfully.\n
         You see this ID belongs to Dr. Andy and you recognise that the zombie
         in front of you right now is Dr. Andy based on the ID photo.\n
         """)
        choice_pickup_IDback = input("""
                 <Press enter to see the back of ID>""")
        print("""
          At the back of the ID, you see:""")
        print("@"*80)
        print("""
          The antidote is stored in the safebox in my office, HELP ME!!
          \t\t\t\t\t\tDr. Andy""")
        print("@"*80)
        
        back_to_office = input("""
                 <Press enter to go to Dr. Andy's office> """)
        game_1() 
    
    elif choice_pickup == str(1):
        print("*"*80)
        print(f"""
          oops...
          Your gunshot attracted all the hidden zombies in the building.
          They strive to be the first to tear your body apart.
          You have underestimated the power of zombie and are eaten.
          """)
        import time
        time.sleep(2)
        print("""
          Mission failed Agent {user_name}. R.I.P.
         ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███  
         ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
        ▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
        ░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
        ░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
         ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
          ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
        ░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░ 
              ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░     
                                                             ░                  
          Hope that you enjoyed the game.
          Bye~~
            """)
        print("*"*80)
    
    elif choice_pickup == str(3):
        print("*"*80)
        print(f"""
          Agent {user_name}, your mission is failed.
          """)
        import time
        time.sleep(2)
        print("""
          The zombie you killed is the infected Dr. Andy, you fail to rescue him
          """)
        import time 
        time.sleep(2)
        print("""
          Even a more exciting news for you,
          Your gunshot attracted all the hidden zombies in the building.
          They strive to be the first to tear your body apart.
          You have underestimated the power of zombie and are eaten.
          """)
        import time
        time.sleep(2)
        print("""
          Mission failed Agent {user_name}. R.I.P.
         ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███  
         ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
        ▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
        ░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
        ░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
         ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
          ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
        ░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░ 
              ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░     
                                                             ░                  
          Hope that you enjoyed the game.
          Bye~~
            """)
        print("*"*80)
        
    else:
        print("*"*80)
        print("""
                <Invalid entry, please choose between 1 and 2>""")
        print("*"*80)
        game_2()
        import time 
        time.sleep(1)
        
def game_3():
    """First time enter office and choose to check out the exit first"""
    
    choice_firstinoffice_exit = input("""
        * Now, would you like to:\n
            1. Check out the safebox
            3. Go to the lobby\n
            > """)
    if choice_firstinoffice_exit == str(1):
        print("$"*80)
        print("""
              On the safebox you can see that it requires a 4 digit number pin
              in order to open.
              """)
        print("$"*80)
        choice_firstinoffice_exit_safebox = input("""
                  Now you can go the lobby\n
                <Press enter to go to lobby>""")
        game_2()
        
    elif choice_firstinoffice_exit == str(3):
        game_2()
        
    else:
        print("*"*80)
        print("""
                <Invalid entry, please choose between 1 and 3>""")
        print("*"*80)
        game_3()
        import time 
        time.sleep(1)
        

def game_4():
    """First time enter office and choose to check out the safebox first"""
    
    choice_firstinoffice_safebox = input("""
        * Now, would you like to:\n
            2. Check out the Exit 
            3. Go to the lobby\n
            > """)
    if choice_firstinoffice_safebox == str(2):
        print("%"*80)
        print("""
              The exit is locked and it requires a valid user's fingerprint
              to open.
              """)
        print("%"*80)
        choice_firstinoffice_safebox_exit = input("""
                  Now you can go the lobby
                <Press enter to go to lobby>""")
        print("*"*80)
        game_2()
    
    elif choice_firstinoffice_safebox == str(3):
        game_2()
    
    else:
        print("*"*80)
        print("""
                <Invalid entry, please choose between 2 and 3>""")
        print("*"*80)
        game_4()
        import time 
        time.sleep(1)
        

def game_5():
    """first time entering the office"""
    
    print("*"*80)
    choice_firstinoffice = input("""
        Now you are inside the office.\n
        On the desk you see a name tab says 'Dr. Andy Zheng',
        and you also see a safebox.
        Besides, you see another two doors, one to lobby again and
        the other says 'Exit'.\n
        * You can choose what to do next:\n
            1. Check out the safebox
            2. Check out the Exit
            3. Go to the lobby\n
            >""")
    if choice_firstinoffice == str(1):
        print("$"*80)
        print("""
              On the safebox you can see that it requires a 4 digit number pin
              in order to open.
              """)
        print("$"*80)
        game_4()
        
    elif choice_firstinoffice == str(2):
        print("%"*80)
        print("""
              The exit is locked and it requires a valid user's fingerprint
              to open.
              """)
        print("%"*80)
        game_3()
   
    elif choice_firstinoffice == str(3):
        game_2()
    
    else:
        print("*"*80)
        print("""
                 <Invalid entry, please choose between 1, 2 and 3>""")
        game_5()
        import time 
        time.sleep(1)
        
        
def game_6():
    """first stage before entering any rooms, also links all the games together"""
    choice_door = input("""
        * which door would you like to go first?\n
            1. Office 
            2. Lobby\n
            > """)
   
    if choice_door == str(1):
        game_5()
    
    elif choice_door == str(2):
        game_2()
    
    else:
        print("*"*80)
        print("""
                 <Invalid entry, please choose between 1 and 2>
              """)
        print("*"*80)
        game_6()
        import time 
        time.sleep(1) 
  

###############################################################################
# Game Playing -- Front stage
###############################################################################    

play_again = "yes"
while play_again.lower() == "yes" or play_again.lower() == "y":
    
    import time
    time.sleep (1)
    game_0()
    play_again = input("""
        Do you want to play again?
        Enter "yes" to continue playing
        or any keys to end the game.\n
        > """)
    print("*"*80)
else:
    print("""
        Hope you enjoyed the game
        See you ~""")
        
    
  










        
        



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    