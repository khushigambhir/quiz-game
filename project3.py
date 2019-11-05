print "welcome to my Python quiz game!"#let me test your knowledge in python
name = raw_input("Enter your name:")#greeting
print "hello " + name + "!"
    
#set up of the game
blank = ["_1_", "_2_", "_3_","_4_"]
easy_quiz = "Python is _1_ oriented programming language. In Python the identation is very _2_. In Python a _3_ is defined using the def keyword.Information can be passed to functions as _4_."#question for easy level
medium_quiz = "In Python, with _1_ loop we can execute a set of statements as long as condition is true. With _2_ statement we can stop the loop even if the while condition is _3_. With the _4_ statement we can stop the current iteration, and continue with the next."#question for medium level
hard_quiz = " A _1_ is a collection which is ordered and changeable. To add an item to the list use _2_ object method. _3_ returns the index of the first element with the specified value._4_ sorts the list."#question for hard level
easy_answers = ["object", "important", "function","parameter"]#answers for easy level
medium_answers = ["while", "break", "true", "continue"]#answers for medium level
hard_answers = ["list", "append()", "index()", "sort()"]#answers for hard level
def level_setup():
    """ take input as level among easy,
        medium or hard and return the
        output according to level chosen"""
    level = raw_input("Choose your level from easy, medium or hard\n").lower()
    if level == "easy":
        print "you chose level easy"
        print "You get 4 attempts per question."
        play_game(easy_quiz, blank, easy_answers) 
    elif level == "medium":
        print "you chose level medium"
        print "You get 4 attempts per question."
        play_game(medium_quiz, blank, medium_answers)
    elif level == "hard":
        print "you chose level hard"
        print "You get 4 attempts per question."
        play_game(hard_quiz, blank, hard_answers)
    else:
        print "sorry! Invalid input."
        level = raw_input("Please choose the level from easy, medium or hard").lower() 
    print level_setup
    
#Quiz starts now
def play_game(paragraph, questions, answer):
    """ take three parameters and print quiz according
        to your level maximum attempt per question is 4
        take input a word as your answer and return try again if wrong or
        return to next question if right"""
    print paragraph
    for index_blank in range(0, len(questions)):
        solution_input = raw_input("what is solution for" + questions[index_blank]+"?")
        attempts = 1
        max_attempt = 4
        while solution_input.lower()!= answer[index_blank]:
            attempts += 1
            solution_input = raw_input("Lets try again. what is solution for" + questions[index_blank]+"?")
            if attempts == max_attempt:
                print ("You lose the game! Better luck next time.")
                level_setup()
        else:
            print("The solution for"  + questions[index_blank] +"is "+ solution_input)
            paragraph = paragraph.replace(questions[index_blank], answer[index_blank])
            print ("correct! " + paragraph)
    if len(questions)==len(answer):
        print ("you won the game! want to try another level?")
        level_setup()
level_setup()
       
