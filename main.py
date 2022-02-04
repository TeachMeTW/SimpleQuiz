#Multiple choice DEBUG NEEDED

from nip import Ques

print("\nHello, welcome to the Quiz \n")

questions_prompts = [
    "\nWhat are Boomers?\n(a) Bombs\n(b) Old People\n(c) Caused by lactose intolerance\n\n",
    "\nHow would you rate this quiz?\n(a) 0\n(b) 10\n(c) 9999\n\n",
    "\nIt's a bad program isn't?\n(a) I mean yeah it was made by a kid years ago\n(b) No you're doing great\n(c) Everyone starts somewhere\n\n"
]
questions = [ # DEBUG NEEDED
    Ques(questions_prompts[0], "b"),
    Ques(questions_prompts[1], "c"),
    Ques(questions_prompts[2], "c")
]

def run_test(questions):
    score = 0
    for question in questions:
       answer = input(question[0])
       if answer == question[1]: 
          score += 1
          print("\nGood job! You're Right") 
       else:
         print("\nWrong!") 
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")
run_test(questions)