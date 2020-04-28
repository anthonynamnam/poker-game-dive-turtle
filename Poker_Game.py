import math
import random
import enum
import time
import sys
import os
#==============Enum===========
class DisplayMode(enum.Enum):
    SIMPLY = 1
    LENGTHY = 2
#============Dictionary==============
type_dict={
    1:"Spades",
    2:"Hearts",
    3:"Clubs",
    4:"Diamonds"
    }
num_full_dict={
    0:"Ace",
    1:"2",
    2:"3",
    3:"4",
    4:"5",
    5:"6",
    6:"7",
    7:"8",
    8:"9",
    9:"10",
    10:"Jack",
    11:"Queen",
    12:"King"
    }
num_short_dict={
    0:"A",
    1:"2",
    2:"3",
    3:"4",
    4:"5",
    5:"6",
    6:"7",
    7:"8",
    8:"9",
    9:"10",
    10:"J",
    11:"Q",
    12:"K"
    }
#==========Global Constants===============
#   0-12 => Spades A-K
#   13-25 => Hearts A-K
#   26-38 => Clubs A-K
#   39-51 => Diamonds A-K
totalcard = 52
#   Setting of number of player
minimumNumOfPlayer = 2
maximumNumOfPlayer = 7
defaultNumOfPlayer = 3
#==========Global Variables===============
#   Status of game
playOrNot = True

#   Status of Login
loginStatus = False
loginUsername = ""
loginScore = 0
loginplayedgame = 0

#   Number of questions in display
numofquest = 7

#   Number of Player in the game
currentNumOfPlayer = defaultNumOfPlayer

#   Display Poker Card Mode
defaultdisplaymode = DisplayMode.SIMPLY
currentdisplaymode = DisplayMode.SIMPLY

TurtleCard = 0

ComputerPlayerList = ["Doctor Strange","Batman","Hello Kitty",
                      "Melody","HaMoTaiLong","$Keroro$",
                      "*CCP*","Gambler","HoKwanYiu",
                      "XiJinPing","Carrie Lam","689","HoSumJai","HoYiYuen",
                      "Carrie_777","Russia","USA","Japan Girl",
                      "Aliensssss","Donald Trump Trump","HSU Student","Ip Lai Ping"]
#==============Function==================
#   StartingGame -- Displaying the starting of the game
#   Input Format:   None
#   Return Format:  None
def StartingGame():
    print("=========================================")
    print("｜\t\t\t\t\t｜")
    print("｜\tWelcome to our Poker Game\t｜")
    print("｜\t\t「潛」烏龜\t\t｜")
    print("｜\t\t\t\t\t｜")
    if loginStatus == True:
        UserID = GetIDByUsername(loginUsername)
        loginScore = GetScoreByID(UserID)
        loginplayedgame = GetPlayedGameByID(UserID)
        if len(loginUsername)<8:
            remain = 3
        elif len(loginUsername)<16:
            remain = 2
        else:
            remain = 1
        remainStr = ""
        for x in range(remain):
            remainStr = remainStr + "\t"
        print("｜ Logged in as: "+ loginUsername + remainStr + "｜")
        if loginScore < 10:
            string = "\t"
        else:
            string = ""
        print("｜ Your Score: " + str(loginScore) + string +"   Played Game: " + str(loginplayedgame)+"\t｜")
        print("｜\t\t\t\t\t｜")
    print("｜\t     Game Setting:\t\t｜")
    print("｜\t   Number of Player: "+str(currentNumOfPlayer)+"\t\t｜")
    if currentdisplaymode == DisplayMode.SIMPLY:
        print("｜\t   Display Mode: Simply\t\t｜")
    elif currentdisplaymode == DisplayMode.LENGTHY:
        print("｜\t  Display Mode: Lengthy\t\t｜")
    print("｜\t\t\t\t\t｜")
    print("｜   1. Start Game    2.Edit Setting\t｜")
    print("｜   3. Login to retrieve your score\t｜")
    print("｜   4. Sign up to record your score\t｜")
    print("｜   5. Log out to the game\t\t｜")
    print("｜   6. Restart\t      7.Quit\t\t｜")
    print("｜\t\t\t\t\t｜")
    print("=========================================")

#   MixingPokerSet -- Mixing the Poker to rearrange the order of the poker set
#   Input Format:   None
#   Return Format:  None
def MixingPokerSet():
    PokerSet = []
    while len(PokerSet) != 52:
        randnum = random.randint(0,51)
        if not CheckIfExist(randnum,PokerSet):
            PokerSet.append(randnum)
    # show the process of mixing poker
    print("")
    mixtime = random.randint(4,7)
    for x in range(0,mixtime):
        time.sleep(0.32)
        print("\t   Mixing Poker Cards...")
    print("")
    return PokerSet
    
#   CheckIfExist -- Check if the poker is already exist in Poker Set (Use for MixingPoker)
#   Return True if the card already exist
#   Input Format:   (int, GameSet.PokerSet)
#   Return Format:  True / False
def CheckIfExist(index,PokerSet):
    for x in range(0,len(PokerSet)):
        if index == PokerSet[x]:
            return True
    return False

#   DisplayQNum -- Print Question Number in questions
#   Input Format:   (integer)
#   Return Format:  "1/2/3/4..."
def DisplayQNum(numofquest):
    string = ""
    for x in range(0,numofquest):
        string = string + str(x+1)
        if x != (numofquest - 1):
            string = string + "/"
    return string

#   ConvertIndexToCard -- Convert random number into Card with type and number
#   Input Format:   int
#   Return Format:  list[int,int]
def ConvertIndexToCard(indexnumber):
    cardInNum = []
    cardType = int(indexnumber / 13)
    cardNum = int(indexnumber % 13)
    # if this is Spades
    if cardType == 0:
        cardInNum.append(1)
    # if this is Hearts
    elif cardType == 1:
        cardInNum.append(2)
    # if this is Clubs
    elif cardType == 2:
        cardInNum.append(3)
    # if this is Diamonds
    elif cardType == 3:
        cardInNum.append(4)

    cardInNum.append(cardNum)
    return cardInNum

#   ConvertCardToIndex -- Convert Card into Index
#   Input Format:   list[int,int]
#   Return Format:  int
def ConvertCardToIndex(card):
    cardNum = int(card[1])
    cardType = int(card[0])
    cardIndex = 0
    # if this is Spades
    if cardType == 1:
        cardIndex = 0*13
    # if this is Hearts
    elif cardType == 2:
        cardIndex = 1*13
    # if this is Clubs
    elif cardType == 3:
        cardIndex = 2*13
    # if this is Diamonds
    elif cardType == 4:
        cardIndex = 3*13

    cardIndex = cardIndex + cardNum
    return cardIndex

#   ConvertCardsToHand -- Convert cards into Hand with type and number
#   Input a list of number and Return with 2D List
#   Input format:   list[int,int]
#   Return format:  list[int ... int][int,int]
def ConvertCardsToHands(cardslist):
    handlist = []
    for x in range(0,len(cardslist)):
        convertCard = ConvertIndexToCard(cardslist[x])
        handlist.append(convertCard)
    return handlist

#   ConvertHandToDetail -- Convert Hand with detailed Hand
#   Input a 2D list of number and Return with 2D List with card type and number
#   Input format:   list[int ... int][int,int]
#   Return format:  list[str ... str][str,str]
def ConvertHandsToDetailedHands(originalhand):
    detailedhand = []
    for x in range(0,len(originalhand)):
        modifiedHand = []
        modifiedHand.append(type_dict[originalhand[x][0]])
        if currentdisplaymode == DisplayMode.SIMPLY:
            modifiedHand.append(num_short_dict[originalhand[x][1]])
        elif currentdisplaymode == DisplayMode.LENGTHY:
            modifiedHand.append(num_full_dict[originalhand[x][1]])
        detailedhand.append(modifiedHand)
    return detailedhand

#   ConvertDetailedCardsToIndex -- Convert Cards to Index
#   Input format:   list[str,str]
#   Return format:  int
def ConvertDetailedCardsToIndex(sourcecards):  
    if sourcecards[0] == "Spades":
        IndexCards = (1-1)*13
    elif sourcecards[0] == "Hearts":
        IndexCards = (2-1)*13
    elif sourcecards[0] == "Clubs":
        IndexCards = (3-1)*13
    elif sourcecards[0] == "Diamonds":
        IndexCards = (4-1)*13

    if sourcecards[1] == "A" or sourcecards[1] == "Ace":
        IndexCards = IndexCards + 0
    elif sourcecards[1] == "K" or sourcecards[1] == "King":
        IndexCards = IndexCards + 12
    elif sourcecards[1] == "Q" or sourcecards[1] == "Queen":
        IndexCards = IndexCards + 11
    elif sourcecards[1] == "J" or sourcecards[1] == "Jack":
        IndexCards = IndexCards + 10
    else:
        IndexCards = IndexCards + (int(sourcecards[1])-1)
    return IndexCards

#   ConvertDetailedHandsToIndexHands -- Convert Detailed Hands into Hands with Index
#   Input format:   list[str ... str][str,str]
#   Return format:  list[int ... int]
def ConvertDetailedHandsToIndexHands(detailhands):
    newhands=[]
    for x in range(len(detailhands)):
        newhands.append(ConvertDetailedCardsToIndex(detailhands[x]))
    return newhands


#   PrintTheHands -- print the cards of your hand
#   Input a 2D list (hand) and print out the hands
#   Input format:   list[str ... str][str,str]
#   Return format:  None
def PrintTheHands(inputhands):
    for x in range(0,len(inputhands)-1):
        if inputhands[x][0] == inputhands[x+1][0]:
            print(inputhands[x],end="")
        else:
            print(inputhands[x])
    print(inputhands[len(inputhands)-1])

#   PrintTextWithTimeInterval -- print the text with few times with certain time interval
#   Input format:   (str, int, float)
#   Return format:  None
def PrintTextWithTimeInterval(showtext,showntime,interval):
    print("")
    for x in range(0,showntime):
        print("\t   "+ showtext)
        time.sleep(interval)
    print("")
            
#   DisplayHeading -- Display a heading with specific format
#   Input format:   (str)
#   Return format:  None
def DisplayHeading(texttoshow,tabNum):
    width = len(texttoshow)
    boundary = ""
    tab = ""
    for x in range(width):
        boundary = boundary +"="
    for y in range(tabNum):
        tab = tab +"\t"
    print(tab+boundary)
    print(tab+texttoshow)
    print(tab+boundary)

    
#   DistributePoker -- Distribute the poker card
#   Input format:   (GameSet)
#   Return format:  None
def DistributePoker(game):
    #DisplayHeading("Distribute Poker...",1)
    # Copy a new list for distributing poker
    distributepokerset = game.PokerSet.copy()
    # Getting the turtle card
    TurtleCard = distributepokerset.pop(random.randint(0,51))
    # Check if the card already distributed
    distributeTrue = []
    NumOfPlayer = len(game.StartPlayerList)
    for i in range(0,51):
        distributeTrue.append(False)
    
    # Temp list for every player - temphands
    temphands = []
    for j in range(0,NumOfPlayer):
        temphands.append([])

    # Distribute all card in player list
    for index in range(0,51):
        playerposition = random.randint(0,NumOfPlayer-1)
        if not distributeTrue[index]:
            temphands[playerposition].append(distributepokerset[index])
            distributeTrue[index] = True
    

    # Input the temp list into the object
    for x in range(0,NumOfPlayer):
        temphands[x].sort(reverse=False)
        game.StartPlayerList[x].inputhands(temphands[x],1)
        game.StartPlayerList[x].updatehands(1)
        game.CurrentPlayerList[x].inputhands(temphands[x],1)
        game.CurrentPlayerList[x].updatehands(1)

    #   Select the starting draw index
    minCard = game.CurrentPlayerList[game.ExchangeOrder[game.CurrentDrawIndex]-1].simplfiednumberofcard
    for x in range(1,NumOfPlayer):
        if game.CurrentPlayerList[game.ExchangeOrder[x]-1].simplfiednumberofcard < minCard:
              game.CurrentDrawIndex = x
        
#   EliminatedPairWithCards -- Eliminate the pair with the list with card index
#   Input format:   list[int]
#   Return format:  list[str ... str][str,str]
def EliminatedPairWithCards(cards):
    return EliminatedPairWithDetailedHands(ConvertHandsToDetailedHands(ConvertCardsToHands(cards)))

#   Eliminate the pair with input of Detailed Hands
#   Input format:   list[str ... str][str,str]
#   Return format:  list[str ... str][str,str]
def EliminatedPairWithDetailedHands(detailedhands):
    if currentdisplaymode == DisplayMode.SIMPLY:
        dict_standard = num_short_dict.copy()
    elif currentdisplaymode == DisplayMode.LENGTHY:
        dict_standard = num_full_dict.copy()
    temphands=[]
    count=[]
    for i in range(0,len(dict_standard)):
        count.append(0)
    for x in range(0,len(detailedhands)):
        for y in range(0,len(dict_standard)):
            if detailedhands[x][1] == dict_standard[y]:
                count[y] = count[y] + 1

    for u in range(0,len(dict_standard)):
        if count[u]%2 != 0:
            target = dict_standard[u]
            if count[u] == 1:
                for v in range(0,len(detailedhands)):
                    if detailedhands[v][1] == target:
                        temphands.append(detailedhands[v])
            elif count[u] == 3:
                appeartime = 0
                for s in range(0,len(detailedhands)):
                    if detailedhands[s][1] == target and appeartime == 2:
                        temphands.append(detailedhands[s])
                    elif detailedhands[s][1] == target and appeartime < 2:
                        appeartime = appeartime + 1
    return temphands



#==================Function for accessing File=================

#User Account File Path
UserAccPath = 'UserAcc.txt'
UserInfoPath = 'UserInfo.txt'


#   Check if the file exist
#   Input format:   None
#   Return format:  None
def CreateFileIfNotExist():
    if os.path.exists(UserAccPath) and not os.path.exists(UserInfoPath):
        newfile2 = open(UserInfoPath, "w")
        newfile2.write("UserID	LoginID		Score   PlayedGame\n")
        newfile2.close()
    elif not os.path.exists(UserAccPath) and os.path.exists(UserInfoPath):
        newfile1 = open(UserAccPath, "w")
        newfile1.write("UserID	LoginID		Password\n")
        newfile1.close()
    elif not os.path.exists(UserAccPath) and not os.path.exists(UserInfoPath):
        newfile1 = open(UserAccPath, "w")
        newfile1.write("UserID	LoginID		Password\n")
        newfile1.close()
        newfile2 = open(UserInfoPath, "w")
        newfile2.write("UserID	LoginID		Score   PlayedGame\n")
        newfile2.close()

#   Check if there is any space in the string
#   Input format:   list[str ... str][str,str]
#   Return format:  list[str ... str][str,str]
def CheckIfAnySpace(string):
    for x in string:
        if x == "":
            return True
    return False

#   Get the Last User ID number
#   Input format:   None
#   Return format:  int
def GetPreviuosUserID():
    UserAccList = open(UserAccPath,'r')
    printout = ''
    for data in UserAccList:
        for x in range(len(data)-1):
            printout = ''
            printout = printout + data[x]
    UserAccList.close()
    if printout[0] < "1" or printout[0] > "9":
        return 1
    else:
        number = ''
        if printout[1]==" ":
            number = printout[0]
        elif printout[2]==" ":
            number = printout[0:2]
        elif printout[3]==" ":
            number = printout[0:3]
        elif printout[4]==" ":
            number = printout[0:4]
        elif printout[5]==" ":
            number = printout[0:5]
        return int(number) + 1

#   Print All the User Information
#   Input format:   None
#   Return format:  None
def PrintUserAccInfo():
    UserAccList = open(UserAccPath,'r')
    for data in UserAccList:
        printout = data[:-1]
        print(printout)
    UserAccList.close()
    print("")

#   Check if the username exist already
#   Input format:   str
#   Return format:  boolean
def CheckIfUsernameUsed(inputusername):
    exist = False
    datausername = ''
    UserAccList = open(UserAccPath,'r')
    for data in UserAccList:
        datausername = data[8:24]
        actualusername = DeleteEmptySpace(datausername)
        if actualusername == inputusername:
            exist = True
            break
    UserAccList.close()
    return exist

#   Delete all empty space in string
#   Input format:   str
#   Return format:  str
def DeleteEmptySpace(inputstring):
    shorten = ''
    for x in inputstring:
        if not x == " ":
            shorten = shorten + x
    return shorten

#   Add Account into Account List
#   Input format:   str,str
#   Return format:  boolean
def AddAccount(username,password):
    if not CheckIfUsernameUsed(username):
        #   Get Previous User ID
        nextuserid = GetPreviuosUserID()
        UserAccList = open(UserAccPath,'a')
        UserInfoList = open(UserInfoPath,'a')
        gapUserID = 8 - len(str(nextuserid))
        gapUserIDStr = ""
        gapUsername = 16 - len(username)
        gapUsernameStr = ""
        for x in range(gapUserID):
            gapUserIDStr = gapUserIDStr + " "
        for y in range(gapUsername):
            gapUsernameStr = gapUsernameStr + " "
        UserAccList.write(str(nextuserid)+ gapUserIDStr + username + gapUsernameStr + password + "\n")
        UserAccList.close()
        
        UserInfoList.write(str(nextuserid)+ gapUserIDStr + username + gapUsernameStr + str(3) + "       " + str(0) + "\n")
        UserInfoList.close()
        
        DisplayHeading("Account Successfully Registered",1)
        print("")
        return True
    else:
        DisplayHeading("Your username is being used already",1)
        return False

#   Check if the password correct
#   Input format:   str,str
#   Return format:  boolean
def CheckIfLoginCorrect(inputusername,inputpassword):
    correct = False
    datausername = ''
    datapassword = ''
    UserAccList = open(UserAccPath,'r')
    for data in UserAccList:
        datausername = data[8:24]
        actualusername = DeleteEmptySpace(datausername)
        if actualusername == inputusername:
            datapassword = data[24:-1]
            actualpassword = DeleteEmptySpace(datapassword)
            if actualpassword == inputpassword:
                correct = True
                break
    UserAccList.close()
    return correct

#   Get the User ID by the username
#   Input format:   str
#   Return format:  int
def GetIDByUsername(inputusername):
    datausername = ''
    UserAccList = open(UserAccPath,'r')
    for data in UserAccList:
        datausername = data[8:24]
        actualusername = DeleteEmptySpace(datausername)
        if actualusername == inputusername:
            number = ''
            if data[1]==" ":
                number = data[0]
            elif data[2]==" ":
                number = data[0:2]
            elif data[3]==" ":
                number = data[0:3]
            elif data[4]==" ":
                number = data[0:4]
            elif data[5]==" ":
                number = data[0:5]
            return int(number)
    UserAccList.close()    
    return -1

#   Get the Score by the User ID
#   Input format:   int
#   Return format:  int
def GetScoreByID(UserID):
    datausername = ''
    UserInfoList = open(UserInfoPath,'r')
    for data in UserInfoList:
        datausername = data[8:24]
        actualusername = DeleteEmptySpace(datausername)
        if actualusername == inputusername:
            score = data[24:32]
            actualscore = DeleteEmptySpace(score)
            return int(actualscore)
    UserInfoList.close()    
    return -1

#   Get the number of played game by the User ID
#   Input format:   int
#   Return format:  int
def GetPlayedGameByID(UserID):
    datausername = ''
    UserInfoList = open(UserInfoPath,'r')
    for data in UserInfoList:
        datausername = data[8:24]
        actualusername = DeleteEmptySpace(datausername)
        if actualusername == inputusername:
            playedgame = data[32:-1]
            actualplayedgame = DeleteEmptySpace(playedgame)
            return int(actualplayedgame)
    UserInfoList.close()    
    return -1

#   Update the Score of the user if logged in
#   Input format:   str,int,int
#   Return format:  None
def UpdateScore(inputusername,score,playedgame):
    totaldata=[]
    #   Read the Info
    UserInfoListRead = open(UserInfoPath,'r+')
    for readdata in UserInfoListRead:
        totaldata.append(readdata[:-1])
    UserInfoListRead.close()

    #   Edit the score
    targetID = GetIDByUsername(inputusername)
    targetString = totaldata[targetID]
    scoreEmpty = 8 - len(str(score))
    scoreStr = ""
    for x in range(scoreEmpty):
        scoreStr = scoreStr + " "
    updateString = targetString[:24] + str(score) + scoreStr + str(playedgame)
    totaldata[targetID] = updateString
    
    #   Write the Info
    UserInfoList = open(UserInfoPath,'w+')
    for x in range(len(totaldata)):
        UserInfoList.write(totaldata[x])
        UserInfoList.write("\n")
    UserInfoList.close() 
        
#=============Class / Object=============

class Player:
    #   Every Player has initial score of 5
    score = 3
    previousscore = score
    ingame = False
    hands = []
    simplfiednumberofcard = 0
    detailednumberofcard = 0
    convertedhands = []
    converteddetailedhands = []
    simplfieddetailedhands = []
    playedgame = 0

    #   Initiate Player
    def __init__(self,username):
        self.username = username
        self.ingame = True        

    #   Reset the Player's Hand
    def resetHands(self):
        self.hands.clear()
        self.simplfiednumberofcard = 0
        self.detailednumberofcard = 0
        self.convertedhands.clear()
        self.converteddetailedhands.clear()
        self.simplfieddetailedhands.clear()
        self.ingame = True

    #   Get Score of the player
    def getScore(self):
        return self.score
    
    #   Get Previous Score of the player
    def getPreviousScore(self):
        return self.previousscore

    #   Get the reward of this game of the player
    def getRewardScore(self):
        return self.score - self.previousscore

    #   Get the status of the player
    def inGameOrNot(self):
        return self.ingame

    #   Get number of card of the simplified hands
    def getSimplfiedNumberOfCard(self):
        return self.simplfiednumberofcard

    #   Get number of card of the origianl hands
    def getDetailedNumberOfCard(self):
        return self.detailednumberofcard

    #   Add the player score
    def addScore(self,add):
        self.score = self.getScore() + add

    #   Minus the player score
    def minusScore(self,minus):
        self.score = max(0,self.getScore() - minus)

    #   Get number of card of the simplified hands
    def getSimplfiedLength(self):
        return len(self.simplfieddetailedhands)
    
    #   Get number of card of the origianl hands
    def getDetailedLength(self):
        return len(self.converteddetailedhands)

    #   Get the status of the player
    def getInGame(self):
        return self.ingame
    
    #   Get the converted hands of of the player
    def getConverted(self):
        return ConvertCardsToHands(self.hands)
    
    #   Get the converted detailed hands of of the player
    def getConvertedDetailed(self):
        return ConvertHandsToDetailedHands(self.convertedhands)

    #   Get the simplified detailed hands of of the player
    def getSimplfiedDetailed(self):
        return EliminatedPairWithDetailedHands(self.converteddetailedhands)

    #   Sort all the hands
    def getAllSorted(self):
        self.hands.sort(reverse = False)
        self.convertedhands.sort(key=ConvertCardToIndex,reverse = False)
        self.converteddetailedhands.sort(key=ConvertDetailedCardsToIndex,reverse = False)
        self.simplfieddetailedhands.sort(key=ConvertDetailedCardsToIndex,reverse = False)

    #   Input new hand, sort it and updated it
    def inputhands(self,inputhands,inputtype):
        if inputtype == 1:
            self.hands = inputhands.copy()
        elif inputtype == 2:
            self.convertedhands = inputhands.copy()
        elif inputtype == 3:
            self.converteddetailedhands = inputhands.copy()
        elif inputtype == 4:
            self.simplfieddetailedhands = inputhands.copy()
        self.updatehands(inputtype)
        self.getAllSorted()

    #   Updated other hands when new hands is inputted
    def updatehands(self,inputtype):
        if inputtype == 1:
            self.convertedhands = self.getConverted().copy()
            self.converteddetailedhands = self.getConvertedDetailed().copy()
            self.simplfieddetailedhands = self.getSimplfiedDetailed().copy()
        elif inputtype == 2:
            self.converteddetailedhands = self.getConvertedDetailed().copy()
            self.simplfieddetailedhands = self.getSimplfiedDetailed().copy()
            self.hands = ConvertDetailedHandsToIndexHands(self.simplfieddetailedhands).copy()
        elif inputtype == 3:
            self.simplfieddetailedhands = self.getSimplfiedDetailed().copy()
            self.hands = ConvertDetailedHandsToIndexHands(self.simplfieddetailedhands).copy()
            self.convertedhands = self.getConverted().copy()
        elif inputtype == 4:
            self.hands = ConvertDetailedHandsToIndexHands(self.simplfieddetailedhands).copy()
            self.convertedhands = self.getConverted().copy()
            self.converteddetailedhands = self.getConvertedDetailed().copy()
        self.simplfiednumberofcard = self.getSimplfiedLength()
        self.detailednumberofcard = self.getDetailedLength()
        self.getAllSorted()


class GameSet:
        PokerSet = []
        StartPlayerList=[]
        CurrentPlayerList=[]
        WinPlayerList=[]
        LosePlayerList=[]
        ExchangeOrder = []
        CurrentDrawIndex = 0

        #   Initiate Game Set
        def __init__(self):
            self.turn = 0
            self.gameended = False

        #   Reset the game
        def resetGame(self):
            self.PokerSet.clear()
            self.StartPlayerList.clear()
            self.CurrentPlayerList.clear()
            self.WinPlayerList.clear()
            self.LosePlayerList.clear()
            self.ExchangeOrder.clear()
            self.CurrentDrawIndex = 0
            self.turn = 0
            self.gameended = False
            
        #   Reset the game for next game
        def resetGameToNextGame(self):
            self.gameended = False
            self.turn = 0
            self.PokerSet.clear()
            #   Reset the Player Status
            for x in range(len(self.StartPlayerList)):
                self.StartPlayerList[x].inputhands([],1)
                self.StartPlayerList[x].previousscore = self.StartPlayerList[x].score
                self.StartPlayerList[x].ingame = True
                self.CurrentPlayerList.append(self.StartPlayerList[x])
            self.WinPlayerList.clear()
            self.LosePlayerList.clear()
            self.ExchangeOrder.clear()
            self.CurrentDrawIndex = 0
            
        #   Initiate the guest player    
        def initGusetPlayer(self,GuestPlayerName):
            newPlayer = Player(GuestPlayerName)
            self.StartPlayerList.append(newPlayer)
            self.CurrentPlayerList.append(newPlayer)

        #   Initiate all the other player  
        def initOtherPlayer(self,NumOfPlayer):
            alreadyUsed = []
            for s in range(len(ComputerPlayerList)):
                alreadyUsed.append(False)

            copyNameList = ComputerPlayerList[:]
            while len(self.StartPlayerList) != NumOfPlayer:
                pcindex = int(random.randint(0,len(copyNameList)-1))
                if not alreadyUsed[pcindex]:
                    pcplayer = Player(copyNameList[pcindex])
                    alreadyUsed[pcindex] = True
                    self.StartPlayerList.append(pcplayer)
                    self.CurrentPlayerList.append(pcplayer)
                
                    
        #   Starting Mixing Poker
        def initMixPoker(self):
            self.PokerSet = MixingPokerSet()

        #   Generate the exchange order
        def initExchangeOrder(self):
            numOfPlayer = len(self.StartPlayerList)
            checkIfExist = []
            for x in range(numOfPlayer):
                checkIfExist.append(False)
            while len(self.ExchangeOrder) != numOfPlayer:
                randnum = random.randint(1,numOfPlayer)
                if not checkIfExist[randnum-1]:
                    self.ExchangeOrder.append(randnum)
                    checkIfExist[randnum-1] = True
            self.CurrentDrawIndex = 0
            
        #   Count the total number of card
        def getTotalCardInGame(self):
            total = 0
            for x in range(len(self.CurrentPlayerList)):
                total = total + self.CurrentPlayerList[x].simplfiednumberofcard
            return total

        #   Count the total number of player in game
        def getTotalPlayerInGame(self):
            return len(self.CurrentPlayerList)

        #   Get the current player index by inputting the origianal player index 
        def getCurrentIndexByStartIndex(self,startindex):
            targetplayer = self.StartPlayerList[startindex].username
            for y in range(0,len(self.CurrentPlayerList)):
                if self.CurrentPlayerList[y].username == targetplayer:
                    return y
            return -1    

        #   Update the current players' hand
        def updateCurrentPlayer(self,updatetype):
            for x in range(0,len(self.CurrentPlayerList)):
                self.CurrentPlayerList[x].updatehands(updatetype)

        #   Set the player to win
        def setPlayerWin(self,PlayerIndex):
            indexincurrent = self.getCurrentIndexByStartIndex(PlayerIndex)
            if indexincurrent == -1:
                print("The player is not in the current game.")
            else:
                DisplayHeading("Player " + str(PlayerIndex+1) + " (" + self.StartPlayerList[PlayerIndex].username + ") wins the game.",1)
                self.StartPlayerList[PlayerIndex].ingame = False
                self.CurrentPlayerList[indexincurrent].ingame = False
                numOfPlayer = len(self.CurrentPlayerList)
                self.StartPlayerList[PlayerIndex].addScore(numOfPlayer-1)
                if PlayerIndex == 0:
                    self.StartPlayerList[0].playedgame = self.StartPlayerList[0].playedgame + 1
                self.CurrentDrawIndex = self.CurrentDrawIndex - 1
                winplayerincurrent = self.CurrentPlayerList.pop(indexincurrent)
                self.WinPlayerList.append(winplayerincurrent)
                time.sleep(1.5)
                if loginStatus == True:
                    updatedscore = self.StartPlayerList[0].score
                    updatedplayedgame = self.StartPlayerList[0].playedgame
                    UpdateScore(loginUsername,updatedscore,updatedplayedgame)
                    
        #   Set the player to lose
        def setPlayerLose(self,PlayerIndex):
            indexincurrent = self.getCurrentIndexByStartIndex(PlayerIndex)
            if indexincurrent == -1:
                print("The player is not in the current game.")
            else:
                self.StartPlayerList[PlayerIndex].ingame = False
                self.CurrentPlayerList[indexincurrent].ingame = False
                self.StartPlayerList[PlayerIndex].minusScore(1)
                if PlayerIndex == 0:
                    self.StartPlayerList[0].playedgame = self.StartPlayerList[0].playedgame + 1
                loseplayerincurrent = self.CurrentPlayerList.pop(indexincurrent)
                self.LosePlayerList.append(loseplayerincurrent)
                if loginStatus == True:
                    updatedscore = self.StartPlayerList[0].score
                    updatedplayedgame = self.StartPlayerList[0].playedgame
                    UpdateScore(loginUsername,updatedscore,updatedplayedgame)
        #   Display all players name
        def DisplayAllPlayersName(self):
            print("")
            print("There are " + str(len(self.StartPlayerList)) + " players in the game now.")
            print("All Player Name List:")
            for i in range(0,len(self.StartPlayerList)):
                print(str(i+1)+') ',end='')
                print(self.StartPlayerList[i].username)

        #   Displayer all Current Player name
        def DisplayCurrentPlayersName(self):
            print("")
            print("There are " + str(len(self.CurrentPlayerList)) + " players in the game now.")
            print("Current Player Name List:")
            for i in range(0,len(self.StartPlayerList)):
                if self.StartPlayerList[i].ingame:
                    print(str(i+1)+') ',end='')
                    print(self.StartPlayerList[i].username)

        #   Display number of card of the player
        def DisplayNumberOfCardByIndex(self,playerIndex):
            if self.StartPlayerList[playerIndex].ingame:
                currentindex = self.getCurrentIndexByStartIndex(playerIndex)
                DisplayHeading("Player " + str(playerIndex+1) + ": " + self.StartPlayerList[playerIndex].username + " has " + str(len(self.CurrentPlayerList[currentindex].simplfieddetailedhands)) + " Cards in total",1)
                print("")
            else:
                DisplayHeading("Player " + str(playerIndex+1) + ": " + self.StartPlayerList[playerIndex].username + " has no cards.",1)
                print("")

        #   Display the card of the player
        def DisplayCardOfPlayerByIndex(self,playerIndex):
            if self.StartPlayerList[playerIndex].ingame:
                currentindex = self.getCurrentIndexByStartIndex(playerIndex)
                PrintTheHands(self.CurrentPlayerList[currentindex].simplfieddetailedhands)
                print("")
            else:
                DisplayHeading("Player " + str(playerIndex+1) + ": " + self.StartPlayerList[playerIndex].username + " has won the game.",1)
                print("")

        #   Display the number of card and display the card of the player
        def DisplayNumOfCardAndCardByIndex(self,playerIndex):
            currentindex = self.getCurrentIndexByStartIndex(playerIndex)
            if self.CurrentPlayerList[currentindex].ingame:
                self.DisplayNumberOfCardByIndex(playerIndex)
                self.DisplayCardOfPlayerByIndex(playerIndex)
            else:
                DisplayHeading("Player " + str(playerIndex+1) + ": " + self.StartPlayerList[playerIndex].username + " has won the game.",1)

        #   Display all players' cards
        def DisplayAllPlayerCards(self):
            self.DisplayGuestPlayerCards()
            self.DisplayOtherPlayerCards()

        #   Display the guest player card
        def DisplayGuestPlayerCards(self):
            if self.StartPlayerList[0].ingame:
                currentindex = self.getCurrentIndexByStartIndex(0)
                DisplayHeading("You (Player 1: "+self.StartPlayerList[0].username+")  has " + str(len(self.CurrentPlayerList[currentindex].simplfieddetailedhands)) + " Cards in total",1)
                self.DisplayCardOfPlayerByIndex(0)
                print("")
            else:
                DisplayHeading("Player 1: You has won the game already.",1)

        #   Display all other player card
        def DisplayOtherPlayerCards(self):
            for x in range(1,len(self.StartPlayerList)):
                if self.StartPlayerList[x].ingame:
                    self.DisplayNumOfCardAndCardByIndex(x)
                else:
                    self.DisplayCardOfPlayerByIndex(x)
                    
        #   Display Turn Number of the game
        def DisplayTurnNumber(self):
            print("")
            DisplayHeading("| Turn " + str(self.turn) +" Start Now!!! |",2)
            print("")

        #   Card Exchange Procedure
        def ExchangeCard(self):
            #   Get the index of two players according to the drawing order
            whodrawindex = self.ExchangeOrder[self.CurrentDrawIndex]-1
            if self.CurrentDrawIndex == len(self.CurrentPlayerList)-1:
                whobeingdrawnindex = self.ExchangeOrder[0]-1
            else:
                whobeingdrawnindex = self.ExchangeOrder[self.CurrentDrawIndex+1]-1

            currentwhodrawindex = self.getCurrentIndexByStartIndex(whodrawindex)
            currentwhobeingdrawnindex = self.getCurrentIndexByStartIndex(whobeingdrawnindex)
            
            #   Print out the Trun Number and who draw who
            print("")
            DisplayHeading("|Turn " + str(self.turn) + ": Player " + str(whodrawindex+1) +" (" + self.StartPlayerList[whodrawindex].username+ ") draws Player " + str(whobeingdrawnindex+1)+" ("+self.StartPlayerList[whobeingdrawnindex].username+")|",1)
            print("")
            
            time.sleep(1.2)
            print("Which cards?\t"+self.StartPlayerList[whobeingdrawnindex].username+" has "+str(self.CurrentPlayerList[currentwhobeingdrawnindex].simplfiednumberofcard)+" cards")
            print("Please input the __th cards (e.g. 1st card, input '1'/ 3rd card, input '3')")
            if whodrawindex == 0:
                indexofcard = int(input(""))
            else:
                indexofcard = random.randint(1,self.CurrentPlayerList[currentwhobeingdrawnindex].simplfiednumberofcard)
                time.sleep(1)
                print(indexofcard)
                time.sleep(1.4)
            while indexofcard > self.CurrentPlayerList[currentwhobeingdrawnindex].simplfiednumberofcard or indexofcard < 1:
                print("")
                print("Please input a number between 1 to "+str(self.CurrentPlayerList[currentwhobeingdrawnindex].simplfiednumberofcard)+"!!!")
                print("Which cards? "+self.StartPlayerList[whobeingdrawnindex].username+" has "+str(self.CurrentPlayerList[currentwhobeingdrawnindex].simplfiednumberofcard)+" cards")
                indexofcard = int(input("Please input the __th cards (e.g. 1st card, input '1'/ 3rd card, input '3')"))

            
            #   Using the user input card index to rand another card index
            drawnindex = random.randint(indexofcard*9,(len(self.CurrentPlayerList[currentwhobeingdrawnindex].hands)+indexofcard)*10)%(len(self.CurrentPlayerList[currentwhobeingdrawnindex].hands))

            #   Pick out a card(index) from Player who being drawn
            cardindex = self.CurrentPlayerList[currentwhobeingdrawnindex].hands.pop(drawnindex)

            #   Displaying that card if the turn related to the Guest Player
            targetcard = ConvertIndexToCard(cardindex)
            if whobeingdrawnindex == 0 or whodrawindex == 0:
                print("")
                DisplayHeading("The card being drawn is " + type_dict[targetcard[0]] + " " + num_short_dict[targetcard[1]],1)
                print("")
                time.sleep(1.4)

            #   Put the card in drawer's hand
            self.CurrentPlayerList[currentwhodrawindex].hands.append(cardindex)

            #   Update both players hand
            self.CurrentPlayerList[currentwhodrawindex].updatehands(1)
            self.CurrentPlayerList[currentwhobeingdrawnindex].updatehands(1)

            #   Update the Draw Card Order Index 
            if self.CurrentDrawIndex == len(self.CurrentPlayerList)-1:
                self.CurrentDrawIndex = 0
            else:
                self.CurrentDrawIndex = self.CurrentDrawIndex + 1

        #   Check if anyone win after every turn
        def CheckIfAnyoneWin(self):
            for x in range(len(self.StartPlayerList)):
                y = self.getCurrentIndexByStartIndex(x)
                if y>=0 and self.CurrentPlayerList[y].hands == [] and self.CurrentPlayerList[y].ingame :
                    self.setPlayerWin(x)
                    self.ExchangeOrder.remove(x+1)
                    
                    
        #   Check if the game is endded
        #   Game will end when the total number of player equals to 1
        def CheckIfGameEnded(self):
            if self.getTotalCardInGame() == 1 or len(self.CurrentPlayerList) == 1:
                for x in range(len(self.StartPlayerList)):
                    y = self.getCurrentIndexByStartIndex(x)
                    if y>=0 and len(self.CurrentPlayerList[y].hands) != 0 and self.CurrentPlayerList[y].ingame:
                        self.setPlayerLose(x)
                self.EndedGame()
                return True
            else:
                return False
        #   End Game Procedure
        def EndedGame(self):
            if len(self.CurrentPlayerList) != 0:
                return
            self.Poker = []
            self.gameended = True

        #   Show the Win and Lose Player Lisy
        def ShowWinLose(self):
            print("=========================Win Player=========================")
            for x in range(0,len(self.WinPlayerList)):
                print("---------Next Player----------")
                print(" Username: \t" + self.WinPlayerList[x].username)
                print(" Original Score: \t" + str(self.WinPlayerList[x].getPreviousScore()))
                print(" Rewards of this game: \t+" + str(self.WinPlayerList[x].getRewardScore()))
                print(" Current Score: \t" + str(self.WinPlayerList[x].getScore()))
                
            print("")
            print("=========================Lose Player=========================")
            for x in range(0,len(self.LosePlayerList)):
                print("---------Next Player----------")
                print(" Username: \t" + self.LosePlayerList[x].username)
                print(" Original Score: \t" + str(self.LosePlayerList[x].getPreviousScore()))
                print(" Penalty of this game: \t" + str(self.LosePlayerList[x].getRewardScore()))
                print(" Current Score: \t" + str(self.LosePlayerList[x].getScore()))
            print("")

#=====================================Main Program===================================
#   Ask how many card you want to see
while playOrNot == True:
    CreateFileIfNotExist()
    gamestarted = False
    StartingGame()
    playAgain = True
    choice = int(input("Plese input your choice by " + DisplayQNum(numofquest) + ": "))
    while choice < 1 or choice > numofquest :
        print("")
        print("Please input a number between 1 and " + str(numofquest) + ".")
        choice = int(input("Plese input your choice by " + DisplayQNum(numofquest) + ": "))
        
    #   Start the Game
    if choice == 1 :
        #   Initiate Game Object
        thisgame = GameSet()
        gamestarted = True
        
        #   Initiate Guest Player
        if loginStatus:
            newPlayer = Player(loginUsername)
            newPlayer.score = loginScore
            newPlayer.previousscore = newPlayer.score
            newPlayer.playedgame = loginplayedgame
            thisgame.StartPlayerList.append(newPlayer)
            thisgame.CurrentPlayerList.append(newPlayer)
            
        else:
            #   Ask for guest name and initiate player object for the guest
            guestname = str(input("Please input your name:"))
            thisgame.initGusetPlayer(guestname)

        #   Initiate Other Players
        thisgame.initOtherPlayer(currentNumOfPlayer)
        
        while playAgain:
            #   Initiate Exchange Order
            thisgame.initExchangeOrder()
        
            #   Display all players name
            thisgame.DisplayAllPlayersName()

            #   Initiate Game Procedure
            thisgame.initMixPoker()
            DistributePoker(thisgame)
            tooLong = True
            while tooLong:
                DistributePoker(thisgame)
                tooLong = False
                for x in range(len(thisgame.CurrentPlayerList)):
                    if len(thisgame.CurrentPlayerList[x].simplfieddetailedhands) >= 8 or len(thisgame.CurrentPlayerList[x].simplfieddetailedhands) <= 1:
                        tooLong = True

            thisgame.DisplayExchangeOrder()
            print(thisgame.CurrentDrawIndex)
            
            #   Displaying guest's Cards
            print("+++++++++++++++++++++++++++++++++++++++++")
            print("Welcome " + thisgame.StartPlayerList[0].username + " ! You have " + str(thisgame.StartPlayerList[0].detailednumberofcard) + " cards in your hand.")
            DisplayHeading("Your cards are below:",1)
            PrintTheHands(thisgame.CurrentPlayerList[0].converteddetailedhands)
            PrintTextWithTimeInterval("Eliminating pairs in your hand...",2,0.8)
            thisgame.updateCurrentPlayer(4)       
                
            #   Start Exchange the Card   
            DisplayHeading("Card Exchange Procedure Start!!!     Card Exchange Procedure Start!!!",0)

            while not thisgame.gameended:
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                thisgame.turn = thisgame.turn + 1
                #   Display Turn Number
                time.sleep(0.6)
                thisgame.DisplayTurnNumber()

                #   Displaying all players' cards
                thisgame.DisplayGuestPlayerCards()
                for x in range(1,len(thisgame.StartPlayerList)):
                    if thisgame.StartPlayerList[x].ingame:
                        thisgame.DisplayNumberOfCardByIndex(x)
                    else:
                        thisgame.DisplayCardOfPlayerByIndex(x)

                #   Display Current Player List
                time.sleep(0.7)
                thisgame.DisplayCurrentPlayersName()

                #   Exchange Card
                thisgame.ExchangeCard()

                #   Update the card in Players' hand
                thisgame.updateCurrentPlayer(4)

                #   Check if anyone win
                thisgame.CheckIfAnyoneWin()
                
                #   Check if the game ended
                if thisgame.CheckIfGameEnded():
                    print("")
                    textprint = "The game is ended!  The game is ended  The game is ended  The game is ended"
                    DisplayHeading(textprint,0)
                    DisplayHeading(textprint,0)
                    print("")
                    break
                else:
                    print("")
            thisgame.ShowWinLose()
            
            print("====================The Game is ended======================")
            
            DisplayHeading("Do you want next game? (1/2/3)",1)
            print("1) Quit Game")
            print("2) Next Game")
            print("3) Start New Game")
            nextGameOrNot = int(input(""))
            while not(nextGameOrNot >= 1 and nextGameOrNot <= 3):
                DisplayHeading("Do you want next game? (1/2/3)",1)
                print("1) Quit Game")
                print("2) Next Game")
                print("3) Start New Game")
                nextGameOrNot = int(input(""))
            if nextGameOrNot == 1:
                print("Bye Bye")
                playOrNot = False
                playAgain = False
                loginStatus = False
            elif nextGameOrNot == 2:
                playOrNot = True
                playAgain = True
                thisgame.resetGameToNextGame()
                
                if loginStatus == True:
                    UserID = GetIDByUsername(loginUsername)
                    loginScore = GetScoreByID(UserID)
                    loginplayedgame = GetPlayedGameByID(UserID)
            elif nextGameOrNot == 3:
                playOrNot = True
                playAgain = False
                currentNumOfPlayer = defaultNumOfPlayer
                currentdisplaymode = DisplayMode.SIMPLY
                thisgame.resetGame()
                
                if loginStatus == True:
                    UserID = GetIDByUsername(loginUsername)
                    loginScore = GetScoreByID(UserID)
                    loginplayedgame = GetPlayedGameByID(UserID)
        
    #   Edit the setting (no. of player / display mode)        
    elif choice == 2:
        print("")
        print("1) Number of Player \t2) Display Mode")
        editchoice = int(input("Which one to edit? Please select the options above."))
        while editchoice != 1 and editchoice != 2:
            print("")
            print("Please input the number 1 or 2!!!")
            print("1) Number of Player \t2) Display Mode")
            editchoice = int(input("Which one to edit? Please select the options above."))
        if editchoice == 1:
            print("")
            UpdatedNumberOfPlayer = int(input("How many player you want? (Min:"+str(minimumNumOfPlayer)+" / Max:"+str(maximumNumOfPlayer)+")"))
            while UpdatedNumberOfPlayer < minimumNumOfPlayer or UpdatedNumberOfPlayer > maximumNumOfPlayer:
                print("")
                print("We only allow to have "+str(minimumNumOfPlayer)+"~"+str(maximumNumOfPlayer)+" people.")
                UpdatedNumberOfPlayer = int(input("How many player you want? (Min:"+str(minimumNumOfPlayer)+" / Max:"+str(maximumNumOfPlayer)+")"))
            currentNumOfPlayer = UpdatedNumberOfPlayer
        elif editchoice == 2:
            print("")
            print("1) Simply Mode \t2) Lengthy Mode")
            UpdatedDisplayMode = int(input("Which mode do you want to play?"))
            while UpdatedDisplayMode != 1 and UpdatedDisplayMode != 2:
                print("")
                print("Please input the number 1 or 2!!!")
                print("1) Simply Mode \t2) Lengthy Mode")
                UpdatedDisplayMode = int(input("Which mode do you want to play?"))
            if UpdatedDisplayMode == 1:
                PrintTextWithTimeInterval("Switching to Simply Mode...",random.randint(3,5),random.randint(30,48)/100)
                currentdisplaymode = DisplayMode.SIMPLY
                print("\t   Switched to Simply Mode!!!")
                print("")
            elif UpdatedDisplayMode == 2:
                PrintTextWithTimeInterval("Switching to Lengthy Mode...",random.randint(3,5),random.randint(30,48)/100)
                currentdisplaymode = DisplayMode.LENGTHY
                print("\t   Switched to Lengthy Mode!!!")
                print("")
        playOrNot = True
    #   Login to retrieve previous record
    elif choice == 3:
        if loginStatus == True:
            print("")
            DisplayHeading("You have logged in already!!!",1)
            DisplayHeading("Please log out to switch to another account!!!",0)
            print("")
        else:
            print("")
            print("=========================================")
            print("｜\t\t\t\t\t｜")
            print("｜   Welcome to our Membership System\t｜")
            print("｜    Please Login to your account\t｜")
            print("｜\t\t\t\t\t｜")
            print("=========================================")
            DisplayHeading("Please enter your username below.",1)
            inputusername = input("Username: ")
            while not CheckIfUsernameUsed(inputusername):
                print("System Message: Username Not Found!!")
                print("")
                DisplayHeading("Please enter your username below.",1)
                inputusername = input("Username: ")
            print("")
            DisplayHeading("Please enter your password below.",1)
            inputpassword = input("Password: ")

            PrintTextWithTimeInterval("logging in...",random.randint(2,5),0.35)
            
            if CheckIfLoginCorrect(inputusername,inputpassword):
                targetuserID = GetIDByUsername(inputusername)
                DisplayHeading("Loged in Successfully!!",1)
                print("")
                time.sleep(0.7)
                loginStatus = True
                loginUsername = inputusername
                loginScore = GetScoreByID(targetuserID)
                loginplayedgame = GetPlayedGameByID(targetuserID)
            else:
                DisplayHeading("Wrong Password!!",1)

    #   Sign up for new account
    elif choice == 4:
        addingSucceed = False
        while not addingSucceed:
            #   Ask for new Username and Password
            print("")
            print("Please input the username: (4~16 characters)")
            username = input("")
            while (len(username)<4 or len(username)>16) or CheckIfAnySpace(username):
                print("Please input the username: (4~16 characters)")
                username = input("")
            print("Please input the password: (8~16 characters)")
            password = input("")
            while (len(password)<8 or len(password)>16) or CheckIfAnySpace(password):
                print("Please input the password: (8~16 characters)")
                password = input("")
                
            #   Add Account into file
            addingSucceed = AddAccount(username,password)
        input("Please click enter to continue...")
        playOrNot = True
    #   Log out
    elif choice == 5:
        playOrNot = True
        playAgain = False
        if loginStatus == True:
            loginStatus = False
            DisplayHeading("Successfully Logged Out!!!",1)
        loginUsername = ""
        loginScore = 0
        loginplayedgame = 0
    #   Restart the game
    elif choice == 6:
        playOrNot = True
        currentNumOfPlayer = defaultNumOfPlayer
        currentdisplaymode = defaultdisplaymode
        if gamestarted == True:
            thisgame.resetGame()
        if loginStatus == True:
            loginStatus == False
        PrintTextWithTimeInterval("Shuting Down...",random.randint(2,4),random.randint(25,40)/100)
        PrintTextWithTimeInterval("Restarting...",random.randint(3,6),random.randint(28,50)/100)
    #   Quit the game
    elif choice == 7:
        playOrNot = False
PrintTextWithTimeInterval("Shuting Down...",random.randint(2,4),random.randint(25,40)/100)
PrintTextWithTimeInterval("System Shut Down!",1,0)
sys.exit()
    
