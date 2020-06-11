score = 0

def ScorePlus():
    global score
    score += 1
    print("Your Total Score is", score)

def ScoreMinus():
    global score
    score -= 1
    print("Your Total Score is", score)

def q1():
    global score
    print("1. What is the national flower of India?")
    print("a) Lily")
    print("b) Lotus")
    print("c) Rose")

    answer = str(input("Your Answer Please!:"))
    if answer == "b":
        print("Well done!, Your Answer is correct!")
        ScorePlus()
        q2()
    else:
        print("Sorry!, Your Answer is incorrect!")
        print("oops!, Try Again Later")
        ScoreMinus()
def q2():
    global score
    print("2. What is the national Flag of India?")
    print("a) Red And White")
    print("b) Saffron and Green")
    print("c) Tricolor")

    answer = str(input("Your Answer Please!: "))
    if answer == "c":
        print("Well done!, Your Answer is correct!")
        ScorePlus()
        q3()
    else:
        print("Sorry!, Your Answer is incorrect!")
        print("oops!, Try Again Later")
        ScoreMinus()
def q3():
    global score
    print("3. What is the national Animal of India?")
    print("a) Tiger")
    print("b) Fox")
    print("c) Elephant")
    answer = str(input("Your Answer Please!: "))
    if answer == "a":
        print("Well done!, Your Answer is correct!")
        print("Congratulations! you Have Passes the Test!")
        ScorePlus()
    else:
        print("Sorry!, Your Answer is incorrect!")
        print("oops!, Try Again Later")
        ScoreMinus()
q1()

