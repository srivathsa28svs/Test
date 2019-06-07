# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random

class footballer:
    @staticmethod
    def _init_(self, skills):
        self.skills = skills
#Create objects for the class    
Hazard = footballer()
Hazard.skills= 100
Neymar = footballer()
Neymar.skills= 98
Messi = footballer()
Messi.skills= 87
VanDyk = footballer()
VanDyk.skills = 95
Son = footballer()
Son.skills = 92
Ronaldo = footballer()
Ronaldo.skills = 93
Kane = footballer()
Kane.skills = 94
Kante = footballer()
Kante.skills = 88
Dybala = footballer()
Dybala.skills = 86
Kepa = footballer()
Kepa.skills = 97


#Assign cards to the players
player1 = [Hazard,Neymar,Kane,Dybala,VanDyk]
player2 = [Messi,Son,Ronaldo,Kante,Kepa]

outdatedList=[]

#Toss to decide the Player1
currentPlayer1 = random.choice([player1,player2])
if(currentPlayer1==player1):
    currentPlayer2=player2
    playerFlag=True
    
else:
    currentPlayer2=player1
    playerFlag=False

#Spell flags
gSpellP1used=False
gSpellP2used=False
rSpellP1used=False
rSpellP2used=False

xchangeFlag=False
m = 0
#Points of both players
pointsP1=0
pointsP2=0
#Integer to keep track of round number
round = 0

PLAYER1=""
PLAYER2=""

#User inputs initialized as NO
player1rSpell="No"
player1gSpell="No"
player2gSpell="No"
player2rSpell="No"


def rules(currentPlayer1,currentPlayer2):
    global playerFlag
    global PLAYER1
    global PLAYER2
    if(playerFlag==True):
        PLAYER1="JAY"
        PLAYER2="PHIL"
    else:
        PLAYER1="PHIL"
        PLAYER2="JAY"
   
    #Play till atleast one player's cards are over
    while(len(currentPlayer1)>0 and len(currentPlayer2)>0):
        players=playGame(currentPlayer1,currentPlayer2)
        if players is not None:
            #Exchange the player order
            if(xchangeFlag==True):
                change=players[1]
                del players[1]
                players.insert(0,change)
            
                if(playerFlag==True):
                    playerFlag=False
                else:
                    playerFlag=True
                Xchange = PLAYER1
                PLAYER1 = PLAYER2
                PLAYER2 = Xchange            
        else:
            break
        
    if(pointsP1>pointsP2):
        print("JAY wins")
    if(pointsP1<pointsP2):
        print("PHIL wins")
    if(pointsP1==pointsP2):
        print("Game tied")

def playGame(currentPlayer1,currentPlayer2):
    global round
    round= round + 1
    global pointsP1
    global pointsP2
    global rSpellP1used
    global m
    #Evaluations for player spells to see which of them is usable in this round
    if(playerFlag==True):
        if(rSpellP1used==False and m==1):
            global player1rSpell
            player1rSpell=input("This is round "+str(round)+".Does "+PLAYER1+ " wants to use Recursive spell? Please answer Yes or No")
        global gSpellP1used
        if(gSpellP1used==False):
            global player1gSpell
            player1gSpell=input("This is round "+str(round)+".Does "+PLAYER1+ "  wants to use God's spell? Please answer Yes or No")
        global rSpellP2used
        if(rSpellP2used==False and m==1):
            global player2rSpell
            player2rSpell=input("This is round "+str(round)+".Does "+PLAYER2+ " wants to use recursive spell? Please answer Yes or No")
    else:
        if(rSpellP2used==False and m==1):
            #global player1rSpell
            player1rSpell=input("This is round "+str(round)+".Does "+PLAYER1+ " wants to use Recursive spell? Please answer Yes or No")
        global gSpellP2used
        if(gSpellP2used==False):
            #global player1gSpell
            player1gSpell=input("This is round "+str(round)+".Does "+PLAYER1+ "  wants to use God's spell? Please answer Yes or No")
        #global rSpellP1used
        if(rSpellP1used==False and m==1):
            #global player2rSpell
            player2rSpell=input("This is round "+str(round)+".Does "+PLAYER2+ " wants to use recursive spell? Please answer Yes or No")
#    global player1gSpell    
    if(player1gSpell=="Yes"):
        num = random.randrange(0,len(currentPlayer2),1)
        
        if(player2rSpell=="Yes"):
            recSpell=random.randrange(0,len(outdatedList),1)
            currentPlayer2.insert(0,outdatedList[recSpell])
            player1Choice=input(PLAYER2 + " has opted for recursive spell after " + PLAYER1 + " cast his God's spell. Does " + PLAYER1 +" wants to continue to challenge the new card or wants to go back to challenge the previously chosen card using God's spell? Hit 1 to continue and hit 0 to change back to previous")
            if(player1Choice==0):
                num=num+1
            else:
                num=num
            if(playerFlag==True):
                rSpellP2used=True
            else:
                rSpellP1used=True
            player2rSpell="No"
        if(playerFlag==True):
            gSpellP1used=True
        else:
            gSpellP2used=True           
        x = currentPlayer2[num]
        currentPlayer2.pop(num)
        currentPlayer2.insert(0,x)
        player1gSpell="No"
        
    if(player2rSpell=="Yes"):
        if(playerFlag==True):
            rSpellP2used=True
        else:
            rSpellP1used=True
        recSpell=random.randrange(0,len(outdatedList),1)
        currentPlayer2.insert(0,outdatedList[recSpell])
        player2rSpell="No"
    if(player1rSpell=="Yes"):
        if(playerFlag==True):
            rSpellP1used=True
        else:
            rSpellP2used=True
        recSpell=random.randrange(0,len(outdatedList),1)
        currentPlayer1.insert(0,outdatedList[recSpell])
        player1rSpell="No"
        
    if(currentPlayer1[0].skills>currentPlayer2[0].skills):
        if(playerFlag==True):
#                global pointsP1
            pointsP1=pointsP1+1
        else:
#                global pointsP2
            pointsP2=pointsP2+1
    else:
        global xchangeFlag
        xchangeFlag = True
        if(playerFlag==True):
#                global pointsP2
            pointsP2=pointsP2+1
        else:
#                global pointsP1
            pointsP1=pointsP1+1
    #Add cards to outdated list
    outdatedList.insert(0,currentPlayer1[0])
    outdatedList.insert(0,currentPlayer2[0])
    del currentPlayer1[0]
    del currentPlayer2[0]
        
    #Display points
    if(playerFlag==True):
        print ("At the end of round "+ str(round) + "," + PLAYER1 + "'s points is " + str(pointsP1) + " and "+PLAYER2+"'s points is "+ str(pointsP2)) 
    else:
        print ("At the end of round "+ str(round) + "," + PLAYER1 + "'s points is " + str(pointsP2) + " and "+PLAYER2+"'s points is "+ str(pointsP1))
    m=1
    players=[currentPlayer1,currentPlayer2]
        
    return players

#call the function
rules(currentPlayer1,currentPlayer2)
