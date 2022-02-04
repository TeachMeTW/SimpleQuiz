
def Ques(prompt,answer):
    questionAnswer = [prompt, answer];
    return questionAnswer;

from stud import Chef

class ChinaChef(Chef): # inherits
    def make_fried_rice(self):
        print("Fwied rice sempai")
    def make_special(self):
        print("OwO sempai its got special ingredients")

