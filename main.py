from random import randint
from time import sleep
playerscore = 0
computerscore = 0
playerInput = 0
computerDraw = 0
playerFinalAnswer = 0
computerFinalAnswer = 0


def convert(playerInput, computerDraw ):
    global playerFinalAnswer
    global computerFinalAnswer
    if playerInput == 1:
        playerFinalAnswer ='Rock'
    elif playerInput == 2:
        playerFinalAnswer = 'Paper'
    else:
        playerFinalAnswer = 'Scissors'
    
    
    if computerDraw == 1:
        computerFinalAnswer ='Rock'
    elif computerDraw == 2:
        computerFinalAnswer = 'Paper'
    else:
        computerFinalAnswer = 'Scissors'
def game():
    global computerDraw
    global playerInput
    computerDraw = randint(1,3)
    x = 1
    i = 0
    if i <= x:
        try:
            i+=1
            print("Rock(1), Paper(2), Scissors(3)")
            sleep(0.5)
            playerInput= int(input())
            score(computerDraw,playerInput)
        

        
        except ValueError:
            print("Sorry, please write the number 1, 2, or 3")
            playerInput = input()  
def score(computerNum, playerNum):
    global playerscore
    global computerscore
    convert(computerNum, playerNum)
    if playerNum == computerNum:
        sleep(0.5)
        print("I picked ",computerFinalAnswer, " and you picked ", playerFinalAnswer, " its a tie!" )
        playagain()
    elif playerNum == 1 and computerNum == 2:
        sleep(0.5)
        print("I picked ",computerFinalAnswer, " and you picked ", playerFinalAnswer, " I win!" )
        computerscore += 1
        playagain()
    elif playerNum == 2 and computerNum == 1:
        sleep(0.5)
        print("I picked ",computerFinalAnswer, " and you picked ", playerFinalAnswer, " you win!" )
        playerscore+=1
        playagain()
    elif playerNum == 2 and computerNum == 3:
        sleep(0.5)
        print("I picked ",computerFinalAnswer, " and you picked ", playerFinalAnswer, " I win!" )
        computerscore += 1
        playagain()
    elif playerNum == 3 and computerNum == 2:
        sleep(0.5)
        print("I picked ",computerFinalAnswer, " and you picked ", playerFinalAnswer, " you win!" )
        playerscore += 1
        playagain()
    elif playerNum == 3 and computerNum == 1:
        sleep(0.5)
        print("I picked ",computerFinalAnswer, " and you picked ", playerFinalAnswer, " I win!" )
        computerscore += 1
        playagain()
    elif playerNum == 1 and computerNum == 3:
        sleep(0.5)
        print("I picked ",computerFinalAnswer, " and you picked ", playerFinalAnswer, " you win!" )
        playerscore += 1
        playagain()
    
        


def playagain():
    
    if playerscore > computerscore:
        sleep(11
              )
        print("That was a great game!")
        sleep(0.5)
        print("The current score is, ", playerscore, "-",computerscore, " with you in lead!")
        sleep(0.5)
        print("Would you like to play again?(y/n)")
        yesOrNo = input()
        if yesOrNo == 'y':
                game()
        else:
            sleep(0.5)
            print("Thanks for playing with me!")
            sleep(0.5)
            print("Visit comozeidam.github.io if you want to see this and many other projects!")
        
        
    elif computerscore > playerscore:
        sleep(1)
        print("That was a great game!")
        sleep(0.5)
        print("The current score is, ", playerscore, "-",computerscore, " with me in lead!")
        sleep(0.5)
        print("Would you like to play again?(y/n)")
        yesOrNo = input()
        if yesOrNo == 'y':
                game()
        else:
            sleep(0.5)
            print("Thanks for playing with me!")
            sleep(0.5)
            print("Visit comozeidam.github.io if you want to see this and many other projects!")
        
    elif computerscore == playerscore:
        sleep(1)
        print("That was a great game!")
        sleep(0.5)
        print("The current score is, ", playerscore, "-",computerscore, " with both of us tied!")
        sleep(0.5)
        print("Would you like to play again?(y/n)")
        sleep(0.5)
        yesOrNo = input()
        if yesOrNo == 'y':
                game()
        else:
            sleep(0.5)
            print("Thanks for playing with me!")
            sleep(0.5)
            print("Visit comozeidam.github.io if you want to see this and many other projects!")
game()

