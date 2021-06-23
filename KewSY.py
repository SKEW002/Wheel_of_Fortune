# Kew Shen Yu    # MA7

from random import randint
import time
from os import system
import threading
from threading import Timer
from turtle import *
import inspect
import ctypes


def preparation(x, y):  # prepare data for the game
    global money
    global player
    global puzzle
    global phrase
    global wheel
    global players
    global consonant_puzzle

    clearscreen()
    bgcolor("#C165FF")
    drawing_area = Screen()
    drawing_area.title("Preparation Screen")
    t1 = Turtle()
    wheel = [400, 500, 600, 350, 500, 900, "BANKRUPT", 650, "FREE PLAY", 700, "LOSE A TURN",
             800, 500, 450, 500, 300, "BANKRUPT", 5000, 500, 900, 700, 300, 800, 550]
    money = []
    phrases = []
    puzzle = []
    consonant_puzzle = []
    with open("WofFPhrases.txt") as myFile:
        for line in myFile:
            phrases.append(line.strip())
    phrase = list(phrases[randint(0, (len(phrases) - 1))])  # choose random phrase
    ascii_consonant_list = [66, 67, 68, 70, 71, 72, 74, 75, 76, 77, 78, 80, 81, 82, 83, 84, 86, 87, 88, 89, 90]
    for i in phrase:  # make puzzle with boxes
        if ord(i) != 32:
            puzzle.append("口")
        else:
            puzzle.append("\n")

    for j in phrase:
        if ord(j) in ascii_consonant_list:
            consonant_puzzle.append(j)
        else:
            continue
    consonant_puzzle = set(consonant_puzzle)  # used for checking consonant

    players = int(numinput("Players", "How many players are playing?"))
    t1.hideturtle()
    t1.penup()
    t1.goto(0, 200)
    t1.pendown()
    t1.write("Phrase", False, "center", font=("Algerian", 25, "bold"))

    t1.penup()
    t1.goto(0, -20)
    t1.pendown()
    t1.write("".join(puzzle), False, "center", font=("Algerian", 14))

    t1.penup()
    t1.goto(0, -100)
    t1.pendown()
    t1.write("Click Screen to START", False, "center", font=("Algerian", 20, "bold"))
    t1.hideturtle()

    for i in range(players):
        money.append(0)
    player = 0
    drawing_area.onclick(spin)
    drawing_area.mainloop()


def spin(x, y):  # Prepare for wheel spinning
    clearscreen()
    bgcolor("black")
    number_of_player = str(player + 1)
    drawing_area = Screen()
    drawing_area.title("Spinning...")
    t1 = Pen()
    t2 = Turtle()
    t3 = Pen()

    t2.color("white")
    t2.hideturtle()
    t2.penup()
    t2.goto(0, 185)
    t2.pendown()
    t2.write(f"Player {number_of_player}", False, "center", font=("Algerian", 25, "bold"))
    t2.penup()
    t2.goto(0, 155)
    t2.pendown()
    t2.write("Ready to spin", False, "center", font=("Algerian", 20, "bold"))

    t3.shape("classic")
    t3.color("orange")
    try:
        drawing_area.bgpic("wheel.png")  # If file does not exist a wheel will be drawn
    except:      #_tkinter.TclError  <- error raised if file is missing
        t1.shape("classic")
        t1.color("orange")
        move = 15
        t1.speed(10)
        t3.speed(10)

        for i in range(13):
            t1.penup()
            t3.penup()
            t1.forward(30)
            t3.forward(30)
            t1.pendown()
            t3.pendown()
            t1.forward(80)
            t3.forward(80)
            t1.penup()
            t3.penup()
            t1.forward(5)
            t3.forward(5)
            t1.stamp()
            t3.stamp()
            t1.home()
            t3.home()
            t1.right(move)
            t3.left(move)
            move += 15

    t1.hideturtle()
    t3.hideturtle()
    t2.penup()
    t2.goto(0, -170)
    t2.pendown()
    t2.write("Click screen to spin!", False, "center", font=("Algerian", 20, "bold"))
    drawing_area.onclick(rotate)


def rotate(x, y):
    drawing_area = Screen()
    global random_point
    random_point = randint(0, 360)
    t1 = Turtle()
    t2 = Turtle()
    t2.clear()
    t2.hideturtle()
    t2.color("white")
    t1.color("red")
    t1.pensize(3)
    t1.right(random_point + 720)
    t1.forward(115)

    t2.penup()
    t2.goto(0, -205)
    t2.pendown()
    t2.write("TA DA~~", False, "center", font=("Algerian", 29, "bold"))
    t2.hideturtle()

    t2.penup()
    t2.goto(0, -250)
    t2.pendown()
    t2.write("Click screen to proceed", False, "center", font=("Algerian", 20, "bold"))
    t2.hideturtle()
    drawing_area.onclick(spin_result)


def next_player_cd():  # count for 5 secs before proceed to next player
    t1 = Turtle()
    t1.hideturtle()
    t1.penup()
    t1.goto(0, -100)
    t1.pendown()
    for i in range(5, 0, -1):
        t1.write(f"Next player in {i} ", False, "center", font=("Algerian", 25, "bold"))
        time.sleep(1)
        t1.clear()


def bankrupt():
    t1 = Turtle()
    drawing_area = Screen()
    drawing_area.title("Too Bad")
    t1.hideturtle()
    money[player] = 0
    t1.penup()
    t1.goto(0, 90)
    t1.pendown()
    t1.write(f"{result}!", False, "center", font=("Algerian", 25, "bold"))
    t1.penup()
    t1.goto(0, -30)
    t1.pendown()
    t1.write(f"You lose turn and all money. \nBalance: ${money[player]}.", False, "center",
             font=("Algerian", 15, "bold"))
    timer = Timer(5, main, args=[True])
    countdown = threading.Thread(target=next_player_cd)
    countdown.start()
    timer.start()


def spin_result(x, y):
    clearscreen()
    global result
    result = wheel[int(random_point / 15)]
    t1 = Turtle()
    t1.hideturtle()
    bgcolor("purple")
    drawing_area = Screen()
    drawing_area.title("Result")
    if type(result) == int:
        bgcolor("#F2D327")
        t1.penup()
        t1.goto(0, 0)
        t1.pendown()
        t1.write(f"${result}", False, "center", font=("Algerian", 60, "bold"))
        time.sleep(3)
        t1.clear()
        free_call()

    elif result == "BANKRUPT":
        bankrupt()

    elif result == "LOSE A TURN":
        lose_turn(result)

    elif result == "FREE PLAY":
        bgcolor("#F2D327")
        t1.penup()
        t1.goto(0, 0)
        t1.pendown()
        t1.write(f"{result}! ", False, "center", font=("Algerian", 55, "bold"))
        t1.hideturtle()
        result = 0  # No money award for free play
        time.sleep(3)
        clearscreen()
        free_call(free_play=True)


def free_call(free_play=False):  # Free play or call consonant
    t1 = Turtle()
    t1.hideturtle()
    t1.penup()
    t1.goto(20, 100)
    t1.pendown()
    t1.write("".join(puzzle), False, "center", font=("Algerian", 15))
    countdown = threading.Thread(target=count_down, daemon=True)  # 10 seconds count down
    countdown.start()

    if free_play:  # free play condition
        bgcolor("#F2D327")
        t1 = Turtle()
        drawing_area = Screen()
        drawing_area.title("YAY~~")
        timer2 = Timer(10, lose_turn, args=("Times up\nPlease close the\nalphabet input window",
                                            True))  # input within 10 sec else proceed to spin, buy or solve stage
        timer2.start()
        alphabet = textinput("Alphabet", "Enter an alphabet")
        timer2.cancel()
        try:
            stop_thread(countdown)
        except ValueError or SystemError:
            pass
        try:
            alphabet = alphabet.upper()
        except AttributeError:
            pass
        else:
            t1.clear()
            check_phrase(alphabet)

    else:  # call consonant after spin wheel
        timer1 = Timer(10, lose_turn,
                       args=["Times up\nPlease close the input window"])  # input within 10 sec else lose a turn
        timer1.start()
        alphabet = textinput("Alphabet", "Enter a consonant within 10 secs")
        timer1.cancel()
        try:
            stop_thread(countdown)
        except ValueError or SystemError:
            pass
        try:
            alphabet = alphabet.upper()
        except AttributeError:  # if user did not call alphabet within 10 secs and closed input window alphabet will be None
            pass
        else:
            try:
                ascii_consonant_list = [66, 67, 68, 70, 71, 72, 74, 75, 76, 77, 78, 80, 81, 82, 83, 84, 86, 87, 88, 89,
                                        90]
                if ord(alphabet) in ascii_consonant_list:
                    check_phrase(alphabet)
                else:
                    lose_turn(result="Invalid input\nYou lose a turn")
            except TypeError:
                lose_turn(result="Invalid input\nYou lose a turn")


def lose_turn(result, free_play=False):
    clearscreen()
    bgcolor("red")
    t1 = Turtle()
    drawing_area = Screen()
    drawing_area.title("Ops...")
    t1.hideturtle()
    t1.penup()
    t1.goto(0, 90)
    t1.pendown()
    t1.write(f"{result}!", False, "center", font=("Algerian", 25, "bold"))
    t1.penup()
    t1.goto(0, -30)
    t1.pendown()
    if free_play:
        t1.write(f"You lose a free play turn. \nBalance: ${money[player]}.", False, "center",
                 font=("Algerian", 15, "bold"))
        t1.penup()
        t1.goto(0, -100)
        t1.pendown()
        time.sleep(3)
        t1.write("Click screen after closing input window", False, "center", font=("Algerian", 20, "bold"))
        drawing_area.onclick(award)
    else:
        t1.write(f"You lose a turn. \nBalance: ${money[player]}.", False, "center", font=("Algerian", 15, "bold"))
        next_player_timer = Timer(5, main, args=[True])
        countdown = threading.Thread(target=next_player_cd)
        countdown.start()
        next_player_timer.start()


def count_down():  # 10 secs countdown when calling alphabet
    t1 = Turtle()
    t1.hideturtle()
    t1.penup()
    t1.pencolor("Red")
    t1.goto(0, 0)
    t1.pendown()
    for i in range(10, 0, -1):
        t1.write(f"You have {i} secs left", False, "center", font=("Algerian", 25, "bold"))
        time.sleep(1)
        t1.clear()


def _async_raise(tid, exctype):  # https://blog.csdn.net/hp_cpp/article/details/83040162
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def stop_thread(thread):  # https://blog.csdn.net/hp_cpp/article/details/83040162
    _async_raise(thread.ident, SystemExit)


def buy_vowel():
    drawing_area = Screen()
    drawing_area.title("Buy Vowel")
    t1 = Turtle()
    t1.hideturtle()
    if money[player] < 250:
        t1.penup()
        t1.goto(0, 0)
        t1.pendown()
        t1.write("Insufficient money to buy vowel, spin again", False, "center", font=("Algerian", 16, "bold"))
        time.sleep(3)
        main()    # spin again if not enough money to buy vowel
    else:
        money[player] -= 250
        countdown = threading.Thread(target=count_down, daemon=True)
        t = Timer(10, lose_turn,
                  args=["Times up\nPlease close the input window"])  # input within 10 sec else lose a turn
        countdown.start()
        t.start()
        alphabet = textinput("Alphabet", "Enter a vowel within 10 secs")
        t.cancel()
        try:
            stop_thread(countdown)
        except ValueError or SystemError:
            pass
        t1.clear()
        bgcolor("red")
        try:
            alphabet = alphabet.upper()
        except AttributeError:  # (alphabet = None) if user did not call alphabet within 10 secs and closed input window
            pass                # None.upper() will get AttributeError
        else:
            if alphabet == "A" or alphabet == "E" or alphabet == "I" or alphabet == "O" or alphabet == "U":
                check_phrase(alphabet, vowel=True)
            else:
                lose_turn(result="Invalid input\nYou lose a turn")


def check_phrase(alphabet, vowel=False):  # check for same alphabet in the phrase
    t1 = Turtle()
    occurrence = 0
    index_number = 0
    if alphabet in puzzle:
        lose_turn(result="Alphabet already called")
        return
    try:
        consonant_puzzle.remove(alphabet)    # consonant removed from the set if consonant was called correctly
    except KeyError:   # if called consonant is not in the set
        pass
    for i in phrase:
        if i == alphabet:
            occurrence += 1
            puzzle[index_number] = alphabet   # insert the correct alphabet into the puzzle
            index_number += 1
            continue
        else:
            index_number += 1   # continue checking
            continue

    if occurrence == 0 and result != 0:  # lose turn if it is not a free play as free play will set the result to 0
        lose_turn(result="Called alphabet does not exist")

    elif occurrence == 0 and result == 0:  # proceed to spin wheel, buy vowel or solve puzzle without losing a turn when free play
        clearscreen()
        bgcolor("red")
        t1.penup()
        t1.goto(0, 0)
        t1.pendown()
        t1.write("Called alphabet does not exist", False, "center", font=("Algerian", 20, "bold"))
        time.sleep(3)
        award(occurrence)
    else:
        if vowel:
            award(0)  # no award for vowel
        else:
            award(occurrence)


def no_more_consonant(x=0, y=0):  # when all the consonants in the phrase were called
    t1 = Turtle()
    clearscreen()
    bgcolor("#0084EF")
    drawing_area = Screen()
    drawing_area.title("No More Consonant")
    t1.hideturtle()
    puz = "".join(puzzle)
    t1.penup()
    t1.goto(20, 50)
    t1.pendown()
    t1.write(puz, False, "center", font=("Algerian", 16))
    t1.penup()
    t1.goto(0, -100)
    t1.pendown()
    t1.write(f"Balance: ${money[player]}", False, "center", font=("Algerian", 18, "bold"))
    while True:     # player will be trapped in this loop for invalid input
        choice = drawing_area.textinput("Choice", '''
            Select a choice: 
                1) Buy vowel
                2) Solve puzzle
                ''')
        if choice == "1":
            if money[player] >= 250:
                buy_vowel()
                break
            else:
                t1.penup()
                t1.goto(0, -50)
                t1.pendown()
                t1.color("#FF2323")
                t1.write("Insufficient money to buy vowel", False, "center", font=("Algerian", 20, "bold"))
                continue
        elif choice == "2":
            guess_puzzle()
            break
        else:
            continue


def award(occurrence, y=0):  # y is a dummy variable
    t1 = Turtle()
    clearscreen()
    bgcolor("#0084EF")
    drawing_area = Screen()
    drawing_area.title("Award")
    t1.hideturtle()
    award = occurrence * result  # consonant available, player awarded
    money[player] += award  # add awarded money into balance
    t1.penup()
    t1.goto(20, 50)
    t1.pendown()
    t1.write("".join(puzzle), False, "center", font=("Algerian", 16))
    t1.penup()
    t1.goto(0, -100)
    t1.pendown()
    t1.write(f"You earned ${award}! Balance: ${money[player]}", False, "center", font=("Algerian", 18, "bold"))
    if len(consonant_puzzle) == 0:
        t1.goto(0, 0)
        t1.write("No more consonant to call", False, "center", font=("Algerian", 18, "bold"))
        time.sleep(3)
        no_more_consonant()

    else:
        while True:  # player will be trapped in this loop for invalid input
            choice = drawing_area.textinput("Choice", '''
                Select a choice: 
                    1) Spin again
                    2) Buy vowel
                    3) Solve puzzle
                    ''')
            if choice == "1":
                main()
                break
            elif choice == "2":
                if money[player] >= 250:
                    buy_vowel()
                    break
                else:
                    t1.penup()
                    t1.goto(0, -50)
                    t1.pendown()
                    t1.color("#FF2323")
                    t1.write("Insufficient money to buy vowel", False, "center", font=("Algerian", 20, "bold"))
                    continue
            elif choice == "3":
                guess_puzzle()
                break
            else:
                continue


def guess_puzzle():  # player guess the phrase
    drawing_area = Screen()
    drawing_area.title("Guess")
    countdown = threading.Thread(target=count_down, daemon=True)
    t = Timer(10, lose_turn, args=["Times up\nPlease close the input window"])  # input within 10 sec else lose a turn
    countdown.start()
    t.start()
    guess = drawing_area.textinput("Guess", "Enter your guess: ")
    t.cancel()
    try:
        stop_thread(countdown)
    except ValueError or SystemError:
        pass
    try:
        guess = guess.upper()
    except AttributeError:
        pass
    else:
        if guess == ("".join(phrase)):
            win_message()
        else:
            lose_turn(result="Wrong Guessing")


def win_message():
    clearscreen()
    drawing_area = Screen()
    bgcolor("#FFD800")
    t1 = Turtle()
    t1.hideturtle()
    t1.penup()
    t1.goto(0, 100)
    t1.pendown()
    t1.write(f"Player {player + 1} WON!!!!", False, "center", font=("Algerian", 25, "bold"))

    t1.penup()
    t1.goto(0, 10)
    t1.pendown()
    t1.write("CONGRATULATION!!!", False, "center", font=("Kunstler Script", 27, "bold"))

    t1.penup()
    t1.goto(0, -70)
    t1.pendown()
    t1.write(f"YOU GOT ${money[player]}!", False, "center", font=("Algerian", 25, "bold"))

    t1.penup()
    t1.goto(0, -130)
    t1.pendown()
    t1.write("click screen to proceed", False, "center", font=("Algerian", 17, "bold"))

    drawing_area.onclick(ending)


def ending(x, y):
    clearscreen()
    drawing_area = Screen()
    bgcolor("#00DEFF")
    t1 = Turtle()
    t1.hideturtle()
    t1.penup()
    t1.goto(0, 0)
    t1.pendown()
    t1.write("Thanks for playing :)", False, "center", font=("Algerian", 22, "bold"))
    time.sleep(2)
    t1.clear()
    t1.write("Created by Kew Shen Yu", False, "center", font=("Algerian", 22, "bold"))
    time.sleep(3)
    t1.clear()
    t1.write("Provide feedback @ ", False, "center", font=("Algerian", 22, "bold"))
    t1.penup()
    t1.goto(0, -30)
    t1.pendown()
    t1.write("SKEW002@e.ntu.edu.sg", False, "center", font=("Algerian", 25, "bold"))
    time.sleep(1)
    t1.penup()
    t1.goto(0, -80)
    t1.pendown()
    t1.write("P.S. You may copy the address from shell\nAdios!", False, "center", font=("Algerian", 10, "bold"))
    print(">>>> SKEW002@e.ntu.edu.sg <<<<")
    print("Click the screen to close the window")
    drawing_area.exitonclick()
    system("pause")


def main(next_player=False):
    global player
    if next_player:
        player += 1    # next player's turn
    else:
        pass

    if player == players:   # return to first player after the last player end turn
        player = 0
    else:
        pass

    if len(consonant_puzzle) == 0:  # if all consonants were called
        clearscreen()
        t1 = Turtle()
        drawing_area = Screen()
        bgcolor("#A93219")
        t1.hideturtle()
        t1.write(f"Player {player + 1}", False, "center", font=("Algerian", 35, "bold"))
        t1.penup()
        t1.goto(0, -50)
        t1.pendown()
        t1.write("CLick screen to continue", False, "center", font=("Algerian", 20, "bold"))
        drawing_area.onclick(no_more_consonant)
    else:
        spin(0, 0)


def welcome():
    bgcolor("#93A8A5")
    t1 = Turtle()  # display message
    t2 = Turtle()  # drawing
    drawing_area = Screen()
    drawing_area.title("Welcome Screen")
    t1.penup()
    t1.goto(0, 200)
    t1.pendown()
    t1.write("WELCOME TO WHEEL OF FORTUNE", False, "center", font=("Algerian", 20, "bold"))
    t1.hideturtle()

    t2.hideturtle()
    t2.color("orange")
    t2.pensize(2)
    t2.penup()
    t2.goto(0, -130)
    t2.pendown()
    t2.color("black", "#4CDE9B")
    t2.begin_fill()
    t2.circle(150)
    t2.end_fill()
    t2.circle(150, 15)
    t2.speed(10)
    for i in range(12):
        t2.left(90)
        t2.forward(300)
        t2.left(90)
        t2.circle(150, 15)

    t1.penup()
    t1.goto(0, -200)
    t1.pendown()
    t1.write("CLICK SCREEN TO START NOW", False, "center", font=("Algerian", 20, "bold"))
    drawing_area.onclick(preparation)
    drawing_area.mainloop()


if __name__ == "__main__":   # beginning of program
    try:
        f = open("WofFPhrases.txt")
        f.close()
    except FileNotFoundError:
        print("Please make sure 'WofFPhrases.txt' is in same folder as 'KewSY.py'")
        system("pause")
    else:
        welcome()

'''
Procedure of functions

Stage 1:    (before the game)

welcome()            # provide welcome screen

preparation()      # prepare data for the game e.g. wheel with multiple results, money list to 
                     store balance money of each player. The function will also prompt user to
                     input the number of player
                     
---------------------------------------------------------------------------------------------------------------------

Stage 2.1:   
main(next_player=False)        # handles rounds of players. Program will go through this function before proceed to
                                 stage 2.2

---------------------------------------------------------------------------------------------------------------------
Stage 2.2:   (first step of game)

spin(x,y)          # x,y is dummy variables as require by onclick function, this function display
                     wheel and ready for player to spin the wheel by clicking on screen

rotate(x,y)        # rotate and point to a random result

spin_result(x,y)   # shows results and bring the player to the next step

---------------------------------------------------------------------------------------------------------------------

Stage 3.1:  (results)

free_call(free_play=False)     # for player to call a consonant after spinning the wheel
                                 parameter free_play will turns True if player got "FREE PLAY"
                                 
bankrupt()               # player lost turn and all money (money[player]=0  and  main(next_player=True))


lose_turn(result, free_play=False)   # called if player got "LOSE A TURN" from wheel or
                                       did not input consonant, vowel, solve puzzle within 10 seconds or
                                       wrong guessing of puzzle or invalid input when calling alphabet.
                                       Program will return to stage 2.1 if it is not free play, else it will
                                       proceed to stage 4.

---------------------------------------------------------------------------------------------------------------------

Stage 3.2:   (after enter a consonant)

check_phrase(alphabet, vowel=False)    # check for existence of alphabet, lose_turn() will be called if
                                         alphabet already in puzzle or alphabet does not exist in phrase
      

---------------------------------------------------------------------------------------------------------------------      
                                        
Stage 4:     (awarding stage)

award(occurrence, y=0)    # y is dummy variable, the money awarded to player is based on result*occurrence
                            then the screen will show awarded money and balance of the player and prompt
                            player to make a choice to spin again, buy vowel or solve puzzle. 
                            Program return to stage 2.1 if player choose to spin again
                            buy_vowel() if player decided to buy vowel and guess_puzzle() for solving puzzle
                            
buy_vowel()       # 250 will deducted from the player and player will be prompted to call a vowel
                    and then the following procedure is similar call a consonant
                    
guess_puzzle()     # compare player's input with phrase, win_message() will be called if player got correct, else 
                     lose_turn()


---------------------------------------------------------------------------------------------------------------------
Stage 5:  (after all consonant called)

no_more_consonant(x,y)    # connect with main(), guess_puzzle() and buy_vowel() instead of using award()
                            after all consonants were called
                            
---------------------------------------------------------------------------------------------------------------------

Stage 6:   (after winning)

win_message()     # congrats the player and show the money won by the player

ending()          # just something extra

---------------------------------------------------------------------------------------------------------------------                  
Others:

count_down()      # 10 seconds countdown alert, activated by using Thread every time when player
                    input consonant vowel or solving puzzle.
                    
next_player_cd()   # count for 5 seconds before proceed to next player, alert player that the game is moving
                     forward to the next player               
                    
_async_raise(tid, exctype)    # thread terminator 
stop_thread(thread)           # thread terminator


'''
