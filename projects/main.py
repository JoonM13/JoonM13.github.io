# Hoodheim
# Text Adventure
# Juan Marquez & Robert Scott
stage = "intro"

def gameOver():
  print()
  print("""\
      ::::::::           :::          :::   :::       ::::::::::        ::::::::     :::     :::     ::::::::::     ::::::::: 
    :+:    :+:        :+: :+:       :+:+: :+:+:      :+:              :+:    :+:    :+:     :+:     :+:            :+:    :+: 
   +:+              +:+   +:+     +:+ +:+:+ +:+     +:+              +:+    +:+    +:+     +:+     +:+            +:+    +:+  
  :#:             +#++:++#++:    +#+  +:+  +#+     +#++:++#         +#+    +:+    +#+     +:+     +#++:++#       +#++:++#:    
 +#+   +#+#      +#+     +#+    +#+       +#+     +#+              +#+    +#+     +#+   +#+      +#+            +#+    +#+    
#+#    #+#      #+#     #+#    #+#       #+#     #+#              #+#    #+#      #+#+#+#       #+#            #+#    #+#     
########       ###     ###    ###       ###     ##########        ########         ###         ##########     ###    ###      
                    """)

def gameOver2():
  print()
  print("For failing as a fighter, you die a dishonorable death and no one attends your funeral. Game Over.")
  
def gameIntro():
  global stage
  print()
  print("""\
:::    :::  ::::::::   ::::::::  :::::::::  :::    ::: :::::::::: ::::::::::: ::::    ::::  
:+:    :+: :+:    :+: :+:    :+: :+:    :+: :+:    :+: :+:            :+:     +:+:+: :+:+:+ 
+:+    +:+ +:+    +:+ +:+    +:+ +:+    +:+ +:+    +:+ +:+            +:+     +:+ +:+:+ +:+ 
+#++:++#++ +#+    +:+ +#+    +:+ +#+    +:+ +#++:++#++ +#++:++#       +#+     +#+  +:+  +#+ 
+#+    +#+ +#+    +#+ +#+    +#+ +#+    +#+ +#+    +#+ +#+            +#+     +#+       +#+ 
#+#    #+# #+#    #+# #+#    #+# #+#    #+# #+#    #+# #+#            #+#     #+#       #+# 
###    ###  ########   ########  #########  ###    ### ########## ########### ###       ###                                                                        
                    """)
  print("A game by Juan Marquez and Robert Scott")
  print()
  print("Finnmark Norway, July 8, 1233, 4:56 pm")
  print()
  print("You are Punctor Yengren, the only black Nord, and also an expert in every known martial art.")
  print("Oh, also you invented the English language.")
  print()
  global momName
  momName = input("What is your mother's name: ")
  print()
  print("What a coincidence, Punctor's mama is also named " + momName)
  print()
  print("Hello mama "+ momName + "!")
  print()
  print("Well mama don't like no lazies. She wants you to get out and get a job.")
  print()
  print("Where do you wanna go?" )
  print()
  stage = "firstChoice"
#This is the code for the intro/tutorial function
def firstChoice():
  global stage 
  global momName
  print("Type 'j' for get a job or type 'f' to fight the rich store owner down the road for some sweet cash")
  print()
  jobChoice = input()
  if jobChoice == "j" or jobChoice == "J":
    print()
    print("You chose to get a job!")
    print()
    print("Mama " + momName + " is proud of your work at MacDougals, the local beef shop. You think this will be big someday.")
    print()
    print("""\
 _ _ _            __                    _         __             
' ) ) )          /  )                  //        /  )          /)
 / / /  __.  _. /  /  __ . . _,  __.  //  _     /--<  _  _    // 
/ ' (_ (_/|_(__/__/_ (_)(_/_(_)_(_/|_</_ /_)_  /___/_</_</_  //_ 
                             /|                             />   
                            |/                             </                                                                         
                    """)
    stage = "gameOver"
  elif jobChoice == "f" or jobChoice == "F":
    print()
    print("'If you say so you filthy vagrant' says mama " + momName)
      #Run tutorial fight
    stage = "tutorialFight"
  elif jobChoice == "b" or jobChoice == "B":
    stage = "eES"
  else: 
    print()
    print("I do not understand what you are trying to say")
    print()
    stage = "firstChoice"
    
def tutorialFight():
  global stage
  print()
  print("You approach the store and the owner appears very wealthy and decrepit. Do you change your mind or throw the first punch?")
  print()
  print("Please type g to go back or i to initiate the fight.")
  print()
  firstPunch = input()
  if firstPunch == "g":
    print()
    stage = "firstChoice"
  elif firstPunch == "i":
    print()
    stage = "tutorialStage2"  
  else:
    print()
    print("Please follow the rules bud")
    stage = "tutorialFight"

def tutorialStage2():
  global stage
  print("Not letting your guard down, you decide to beat the frail elder. No matter, we'll remind you how to brawl it out even if your target is a defenseless old man!")
  print()
  print("He seems to be putting his arms up. If an opponent is doing this, go for a kick! Type 'k' to kick.")
  print()
  kick = input()
  if kick == "k" or kick == "K":
    print()
    print("Yea, just like that! He is still keeping his hands up. Perhaps he is going for a jab, the mad lad. You could block it.")
    print()
    stage = "highBlock"
  elif kick == "p" or kick == "P":
    print()
    print("The old man blocked your pathetic, malinformed punch and countered with the force of 1000 suns.")
    stage = "gameOver2"
  else:
    print()
    print("Nice genius, that's not an option.")
    print()
    stage = "tutorialStage2"

def highBlock():
  global stage
  global hp
  print("Press 'hb' to enact a high block." )
  print()
  hblock = input()
  if hblock == "hb" or hblock == "HB" or hblock == "Hb" or hblock == "hB":
    print()
    print("The old man goes for it. Nice block champ you're really remembering fast. Everyone is crowding around awaiting your next move as the old man takes a step back.")
    stage = "freeChoice"
  elif hblock == "lb" or hblock == "LB" or hblock == "Lb" or hblock == "lB":
    print()
    print("Gods, you suck")
    stage = "gameOver2"

def freeChoice():
  global stage
  print()
  print("Would you like to High Block, Low Block, Kick, or Punch? (hb, lb, k, p)")
  print()
  freeChoice = input()  
  if freeChoice == "hb" or freeChoice == "HB" or freeChoice == "Hb" or freeChoice == "hB":
    print()
    print("The old guy kicked you")
    stage = "nFC"
  elif freeChoice == "lb" or freeChoice == "LB" or freeChoice == "Lb" or freeChoice == "lB":
    print()
    print("You blocked his fairly quick attack")
    stage = "nFC"
  elif freeChoice == "p" or freeChoice == "P":
    print()
    print("The crippled man kicked you before you could punch")
    stage = "nFC"
  elif freeChoice == "k" or freeChoice == "K":
    print()
    print("You tried to kick but the crippled man has swift legs")
    stage = "nFC"
    
def newFreeChoice():
  global stage
  print()
  print("The crippled man doesn't seem to want to continue fighting, go for the final blow and bring honor to your village!")
  print()
  print("(p or k)")
  print()
  nFC = input()
  if nFC == "hb" or nFC == "HB" or nFC == "hB" or nFC == "Hb" or nFC == "lb" or nFC == "LB" or nFC == "Lb" or nFC == "lB":
    print()
    print("You blocked... This is not the life for you. The man stabs you with his cane and you black out forever.")
    stage = "gameOver2"
  elif nFC == "p" or nFC == "P" or nFC == "k" or nFC == "K":
    print()
    print("You struck the man with a mighty blow and he dropped like a fly. The pathetic old man is no more and you are now on the path to becoming a TRUE WARRIOR!")
    stage = "gameOver3"

def gO3():
  print()
  print("You are a hero amongst your people as no one really liked the mysterious handicapped aristocrat. You bask in your glory until a later date, fair Punctor.")
  print()
  print("END OF DEMO")
  global stage
  stage = "gameOver"
  



  ##########
  #########
  ####### EASTER EGG
  #########
  ##########
def easterEggString():
  global stage
  print()
  print("Interesting... I suppose you shall fight")  
  stage = "tutorialFightEaster"

def tFE():
  global stage
  print()
  print("You approach the store and the owner appears very wealthy and crippled. Do you change your mind or throw the first punch?")
  print()
  print("Please type g to go back or i to initiate the fight.  ")
  print()
  firstPunch = input()
  if firstPunch == "g" or firstPunch == "G":
    print()
    stage = "firstChoice"
  elif firstPunch == "i" or firstPunch == "I":
    print()
    stage = "tutorialStage2"  
  elif firstPunch == "t" or firstPunch == "T":
    stage = "tutorialStage2Easter"
  else:
    print()
    print("Please follow the rules bud")
    stage = "tutorialFight"
    
def tS2E():
  global stage
  print()
  print("Not letting your guard down, you decide to beat the frail elder. No matter, we'll remind you how to brawl it out even if your target is a defenseless old man")
  print()
  print("He seems to be putting his arms up. If an opponent is doing this, go for a kick! Type 'k' to kick.")
  print()
  kick = input()
  if kick == "k" or kick == "K":
    print()
    print("Yea, just like that! He is still keeping his hands up. Perhaps he is going for a jab, the mad lad. You could block it. Press 'hb' to enact a high block.")
    print()
    stage = "highBlock"
  elif kick == "p" or kick == "P":
    print()
    print("The old man blocked your pathetic, malinformed punch and countered with the force of 1000 suns.")
    stage = "gameOver2"
  elif kick == "t" or kick == "T":
    print()
    print("You truly are strange...")
    stage = "highBlockEaster"
  else:
    print()
    print("Nice genius, that's not an option.")
    print()
    stage = "tutorialStage2"

def hBE():
  global stage
  global hp
  print()
  print("Press 'hb' to enact a high block." )
  print()
  hblock = input()
  if hblock == "hb" or hblock == "HB" or hblock == "Hb" or hblock == "hB":
    print("The old man goes for it. Nice block champ you're really remembering fast. Everyone is crowding around awaiting your next move as the oldman takes a step back.")
    print()
    stage = "freeChoice"
  elif hblock == "lb" or hblock == "LB" or hblock == "Lb" or hblock == "lB":
    print()
    print("Gods, you suck")
    stage = "gameOver2"
  elif hblock == "f" or hblock == "F":
    print()
    print("Intriguing...")
    print()
    print("As you block this punch of monumental power and speed, there is a flash of light")
    print()
    stage = "BTTF"
  else:
    print()
    print("Nice genius, that's not an option.")
    print()
    stage = "highBlock"

def backToTheFuture():
  global stage
  print("The flash of light transports you to a strange area with boxes flying like birds and other grounded boxes towering above the birds.")
  print()
  print("Everyone is speaking the language you invented and there is a statue nearby that almost perfectly captures your image.")
  print()
  print("YOU ARE A MARTYR IN THE FUTURE!")
  print()
  stage = "bttfLoop" 

def bttfLoop():
  global stage
  print("Suddenly, the flash of light returns you to your time, and you stand above a defeated old man.")
  stage = "gameOver3"
############
############
############
############
############




while True:
  if stage == "intro":
    gameIntro()
  elif stage == "firstChoice":  
    firstChoice()
  elif stage == "tutorialFight":
    tutorialFight()
  elif stage == "tutorialStage2":
    tutorialStage2()
  elif stage == "freeChoice":
    freeChoice()
  elif stage == "eES":
    easterEggString()
  elif stage == "gameOver":
    gameOver()
    break
  elif stage == "gameOver2":
    gameOver2()
    break
  elif stage == "highBlock":
    highBlock()
  elif stage == "nFC":
    newFreeChoice()
  elif stage == "gameOver3":
    gO3()
  elif stage == "tutorialFightEaster":
    tFE()
  elif stage == "tutorialStage2Easter":
    tS2E()
  elif stage == "highBlockEaster":
    hBE()
  elif stage == "BTTF":
    backToTheFuture()
  elif stage == "bttfLoop":
    bttfLoop()