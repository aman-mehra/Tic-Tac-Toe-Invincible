# Game Tic-tac-toe

#State: Tiles are numbered 1 to 9

import time

"""
Tick-Tac-Toe game state is defined as follows: 

tile1 |  tile2  | tile3
______|_________|______
tile4 |  tile5  | tile6
______|_________|______
tile7 |  tile8  | tile9
______|_________|______

A player can belong to one of the following two categories:
1. Naive: Player checks a tile randomly.
2. Intelligent: Player follows some strategy to win a game. You shall define a strategy that an intelligent player can take.

We will estimate probability of winning for a player for different scenarios.
 
Game1: A number of games are played between two naive players. Estimate probability of winning for player1. Assume player1 starts the game.

Game2: A number of games are played between a naive and intelligent player. Estimate probability of winning for player1. Assume player1 is naive and starts the game.

Game3: A number of games are played between two intelligent players. Estimate probability of winning for player1. Assume player1 starts the game.  
"""

import random 
# There are 2 players: player1 and player2
player1=1
player2=2


# There are 9 tiles numbered tile0 to tile9
# 0 value of a tile indicates that tile has not been ticked
# 1 value indicates that the tile is ticked by player-1
# 2 value indicates that the tile is ticked by player-2

tile1= 0
tile2= 0
tile3= 0
tile4= 0
tile5= 0
tile6= 0
tile7= 0
tile8= 0
tile9= 0

#turn variable defines whose turn is now
turn = player1

player1ticks=0
player2ticks=0

def validmove(move):
        """ Checks whether a move played by a player is valid or invalid.
              Return True if move is valid. 
              
              A move is valid if the corresponding tile for the move is not ticked.
        """
        if move==0:
                return True
        else:
                return False

def win(x=0):
        """ Returns True if the board state specifies a winning state for some player.
                
                A player wins if ticks made by the player are present either
                i) in a row
                ii) in a cloumn
                iii) in a diagonal
        """
        if x!=0:
                t1,t2,t3,t4,t5,t6,t7,t8,t9=int(x[0]),int(x[1]),int(x[2]),int(x[3]),int(x[4]),int(x[5]),int(x[6]),int(x[7]),int(x[8])

                if str(t1*t2*t3) in "18":
                        return True
                elif str(t4*t5*t6) in "18":
                        return True
                elif str(t7*t8*t9) in "18":
                        return True
                elif str(t1*t4*t7) in "18":
                        return True
                elif str(t2*t5*t8) in "18":
                        return True
                elif str(t3*t6*t9) in "18":
                        return True
                elif str(t1*t5*t9) in "18":
                        return True
                elif str(t3*t5*t7) in "18":
                        return True
                else:
                        return False
                
        elif x==0:
                global tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8,tile9
                
                if str(tile1*tile2*tile3) in "18":
                        return True
                elif str(tile4*tile5*tile6) in "18":
                        return True
                elif str(tile7*tile8*tile9) in "18":
                        return True
                elif str(tile1*tile4*tile7) in "18":
                        return True
                elif str(tile2*tile5*tile8) in "18":
                        return True
                elif str(tile3*tile6*tile9) in "18":
                        return True
                elif str(tile1*tile5*tile9) in "18":
                        return True
                elif str(tile3*tile5*tile7) in "18":
                        return True
                else:
                        return False
        
def takeNaiveMove(player):
        """ Returns a tile number randomly from the set of unchecked tiles with uniform probability distribution.    
        """
        global tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8,tile9
        ct=0
        x=0
        for i in range(2):
                if i==0:
                        if tile1==0:
                                ct+=1
                        if tile2==0:
                                ct+=1
                        if tile3==0:
                                ct+=1
                        if tile4==0:
                                ct+=1
                        if tile5==0:
                                ct+=1
                        if tile6==0:
                                ct+=1
                        if tile7==0:
                                ct+=1
                        if tile8==0:
                                ct+=1
                        if tile9==0:
                                ct+=1
                        x=random.randint(1,ct)
                        ct=0
                elif i==1:
                        if tile1==0:
                                ct+=1
                                if x==ct:
                                        tile1=player
                        if tile2==0:
                                ct+=1
                                if x==ct:
                                        tile2=player
                        if tile3==0:
                                ct+=1
                                if x==ct:
                                        tile3=player
                        if tile4==0:
                                ct+=1
                                if x==ct:
                                        tile4=player
                        if tile5==0:
                                ct+=1
                                if x==ct:
                                        tile5=player
                        if tile6==0:
                                ct+=1
                                if x==ct:
                                        tile6=player
                        if tile7==0:
                                ct+=1
                                if x==ct:
                                        tile7=player
                        if tile8==0:
                                ct+=1
                                if x==ct:
                                        tile8=player
                        if tile9==0:
                                ct+=1
                                if x==ct:
                                        tile9=player

def boardFull(s):
        if '0' not in s:
                return True
        return False        

def takeStrategicMove():
        """ Returns a tile number from the set of unchecked tiles
        using some rules.
        """
        global turn,tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8,tile9,player1ticks,player2ticks
        if player2ticks==0 and player1ticks==1:
            if tile1!=0 or tile3!=0 or tile7!=0 or tile9!=0:
                tile5=turn
                return
            else:
                tile1=turn
                return

        if player1ticks!=0:
            s=str(tile1)+str(tile2)+str(tile3)+str(tile4)+str(tile5)+str(tile6)+str(tile7)+str(tile8)+str(tile9)
            tile=moveFinder(s,True,turn,0,initiator=1)
            if tile==0:
                    tile1=turn
            elif tile==1:
                    tile2=turn
            elif tile==2:
                    tile3=turn
            elif tile==3:
                    tile4=turn
            elif tile==4:
                    tile5=turn
            elif tile==5:
                    tile6=turn
            elif tile==6:
                    tile7=turn
            elif tile==7:
                    tile8=turn
            elif tile==8:
                    tile9=turn
        else:
            tile=random.randint(1,5)
            if tile==1:
                tile1=turn
            elif tile==2:
                tile3=turn
            elif tile==3:
                tile5=turn
            elif tile==4:
                tile7=turn
            elif tile==5:
                tile9=turn

def moveFinder(s,isMe,turn,depth,initiator=0):
    bestMove,bestPos=0,-1
    if win(x=s):
        if isMe:
            return -1#foe win state
        else:
            return 1#me win state
    elif boardFull(s):
        return 0#draw
    if isMe:#maximizer
##        if depth==7:
##            return 1
        bestMove=float('-inf')#-infinty
    else:#minimizer
##        if depth==7:
##            return 1
        bestMove=float('inf')#infinty
    for i in range(len(s)):
        if s[i]=='0':
            new_s=s[:i]+str(turn)+s[i+1:]
            val=moveFinder(new_s,not(isMe),3-turn,depth+1)
            if isMe:
                bestMove=max(bestMove,val)
                if val==1:
                    bestPos=i
                    break
            else:
                bestMove=min(bestMove,val)
                if val==-1:
                    bestPos=i
                    break
            if bestMove==val:
                bestPos=i
                
    if initiator==0:
        return bestMove
    return bestPos
            
                
def reset():
        global tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8,tile9,player1ticks,plyer2ticks,turn
        tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8,tile9=0,0,0,0,0,0,0,0,0
        player1ticks,plyer2ticks=0,0
        turn=1

def validBoard():
        """ Return True if board state is valid.
        A board state is valid if number of ticks by player1 is always either equal to or one more than the ticks by player2.
        """
        if player1ticks-player2ticks==0 or player1ticks-player2ticks==1:
                return True
        return False

def renderboard():
        global tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8,tile9
        s=str(tile1)+str(tile2)+str(tile3)+str(tile4)+str(tile5)+str(tile6)+str(tile7)+str(tile8)+str(tile9)
        for i in range(3):
                print'|',
                for j in range(3):
                        if s[i*3+j]=='1':
                                print 'O   |',
                        elif s[i*3+j]=='2':
                                print 'X   |',
                        else:
                                print '    |',
                print " "
                print "______________________"
        print

def game(gametype=1):
    """ Returns 1 if player1 wins and 2 if player2 wins
              and 0 if it is a draw.
      
              gametype defines three types of games discussed above.
              i.e., game1, game2, game3
    """
    global turn,tile1,tile2,tile3,tile4,tile5,tile6,tile7,tile8,tile9
    s=str(tile1)+str(tile2)+str(tile3)+str(tile4)+str(tile5)+str(tile6)+str(tile7)+str(tile8)+str(tile9)
    if win():
        return 3-turn
    elif boardFull(s):
        return 0
        
def game1(n):
        """ Returns the winning probability for player1.         
        n games are played between two naive players. Estimate probability of winning for player1. Assume player1 starts the game.
        """
        global player1ticks,player2ticks,turn
        c1=0#times player1 wins
        c2=0#times player2 wins
        d=0 #times draw
        for i in range(n):
                turn_counter=0
                while True:
                        takeNaiveMove(player1)
                        turn=3-turn
                        #renderboard()
                        player1ticks+=1
                        if win():          #player1 wins
                                c1+=1
                                break
                        turn_counter+=1
                        if turn_counter==9:#draw
                                d+=1
                                break
                        takeNaiveMove(player2)
                        turn=3-turn
                        #renderboard()
                        player2ticks+=1
                        if win():          #player2 wins
                                c2+=1
                                break
                        turn_counter+=1
                reset()
        print "Winning Probablity of Player1 : ", float(c1)/n
        print "Winning Probablity of Player2 : ", float(c2)/n
        print "Probability of Draw : ", float(d)/n
                        
def game2(n):
        """Returns the winning probability for player1.
        
        n games are played between a naive and intelligent player. Estimate probability of winning for player1. Assume player1 is naive and starts the game.
        """
        global player1ticks,player2ticks,turn
        c1=0#times player1 wins
        c2=0#times player2 wins
        d=0 #times draw
        su=0
        for i in range(n):
                turn_counter=0
                f=0
                while True:
                        takeNaiveMove(player1)
                        turn=3-turn
                        #renderboard()
                        player1ticks+=1
                        if win():          #player1 wins
                                c1+=1
                                f+=1
                                break
                        turn_counter+=1
                        if turn_counter==9:#draw
                                d+=1
                                break
                        t=time.time()
                        takeStrategicMove()
                        su=su+time.time()-t
                        turn=3-turn
                        #renderboard()
                        player2ticks+=1
                        if win():          #player2 wins
                                c2+=1
                                break
                        turn_counter+=1
                if f==1:
                    renderboard()
                reset()
        print su
        print "Winning Probablity of Player1 : ", float(c1)/n
        print "Winning Probablity of Player2 : ", float(c2)/n
        print "Probability of Draw : ", float(d)/n

def game3(n):
        """Returns the winning probability for player1. 
        
        n games are played between two intelligent players. Estimate probability of winning for player1. Assume player1 starts the game.
        """
        #start=time.time()
        global player1ticks,player2ticks,turn
        c1=0#times player1 wins
        c2=0#times player2 wins
        d=0 #times draw
        for i in range(n):
                turn_counter=0
                while True:
                        takeStrategicMove()
                        turn=3-turn
                        #renderboard()
                        player1ticks+=1
                        if win():          #player1 wins
                                c1+=1
                                break
                        turn_counter+=1
                        if turn_counter==9:#draw
                                d+=1
                                break
                        takeStrategicMove()
                        turn=3-turn
                        #renderboard()
                        player2ticks+=1
                        if win():          #player2 wins
                                c2+=1
                                break
                        turn_counter+=1
                #renderboard()
                reset()
        #print time.time()-start
        print "Winning Probablity of Player1 : ", float(c1)/n
        print "Winning Probablity of Player2 : ", float(c2)/n
        print "Probability of Draw : ", float(d)/n

game1(1000)
game2(5)
game3(5)







        
