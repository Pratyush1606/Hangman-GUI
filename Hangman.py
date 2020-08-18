import random
from graphics import *

class HangmanLexicon:
    def __init__(self):
        with open(r"C:\Users\Pratyush\Desktop\Hangman.txt","r") as file:
            words = file.read().split()
        self.word = random.choice(words).upper()
        self.length= len(self.word)

class HangmanCanvas:
    def __init__(self):
        self.scaffold_len = 360
        self.beam_len     = 144
        self.rope_len     = 18
        self.head_radius  = 36
        self.body_len     = 144
        self.arm_offset   = 28
        self.upper_arm    = 72
        self.lower_arm    = 44
        self.hip_width    = 36
        self.leg_len      = 108
        self.foot_len     = 28
        
        self.win_1 = GraphWin("Hangman Losing Situation",500,500)
        start_point = Point(21,20)
        start_point.draw(self.win_1)
        scaffold = Line(start_point,Point(21,20+self.scaffold_len))
        beam = Line(start_point,Point(21+self.beam_len,20))
        scaffold.draw(self.win_1)
        beam.draw(self.win_1)

        self.message = Text(Point(self.win_1.getWidth()/2,400),"You lost")
        self.message.setTextColor('red')
        self.message.setStyle('italic')
        
        
    def head_part(self):
        rope = Line(Point(21+self.beam_len,20),Point(21+self.beam_len,20+self.rope_len))
        head = Circle(Point(21+self.beam_len,20+self.rope_len+self.head_radius),self.head_radius)
        rope.draw(self.win_1)
        head.draw(self.win_1)

    def body_part(self):
        body = Line(Point(21+self.beam_len,20+self.rope_len+2*self.head_radius),Point(21+self.beam_len,20+self.rope_len+2*self.head_radius+self.body_len))
        body.draw(self.win_1)

    def left_arm_part(self):
        left_upper_arm = Line(Point(21+self.beam_len,20+self.rope_len+2*self.head_radius+self.arm_offset),Point(21+self.beam_len-self.upper_arm,20+self.rope_len+2*self.head_radius+self.arm_offset))
        left_lower_arm = Line(Point(21+self.beam_len-self.upper_arm,20+self.rope_len+2*self.head_radius+self.arm_offset),Point(21+self.beam_len-self.upper_arm,20+self.rope_len+2*self.head_radius+self.arm_offset+self.lower_arm))
        left_upper_arm.draw(self.win_1)
        left_lower_arm.draw(self.win_1)
    
    def right_arm_part(self):
        right_upper_arm = Line(Point(21+self.beam_len,20+self.rope_len+2*self.head_radius+self.arm_offset),Point(21+self.beam_len+self.upper_arm,20+self.rope_len+2*self.head_radius+self.arm_offset))
        right_lower_arm = Line(Point(21+self.beam_len+self.upper_arm,20+self.rope_len+2*self.head_radius+self.arm_offset),Point(21+self.beam_len+self.upper_arm,20+self.rope_len+2*self.head_radius+self.arm_offset+self.lower_arm))
        right_upper_arm.draw(self.win_1)
        right_lower_arm.draw(self.win_1)

    def left_leg_part(self):
        left_hip = Line(Point(21+self.beam_len,20+self.rope_len+2*self.head_radius+self.body_len),Point(21+self.beam_len-self.hip_width,20+self.rope_len+2*self.head_radius+self.body_len))
        left_leg = Line(Point(21+self.beam_len-self.hip_width,20+self.rope_len+2*self.head_radius+self.body_len),Point(21+self.beam_len-self.hip_width,20+self.rope_len+2*self.head_radius+self.body_len+self.leg_len))
        left_hip.draw(self.win_1)
        left_leg.draw(self.win_1)

    def right_leg_part(self):
        right_hip = Line(Point(21+self.beam_len,20+self.rope_len+2*self.head_radius+self.body_len),Point(21+self.beam_len+self.hip_width,20+self.rope_len+2*self.head_radius+self.body_len))
        right_leg = Line(Point(21+self.beam_len+self.hip_width,20+self.rope_len+2*self.head_radius+self.body_len),Point(21+self.beam_len+self.hip_width,20+self.rope_len+2*self.head_radius+self.body_len+self.leg_len))
        right_hip.draw(self.win_1)
        right_leg.draw(self.win_1)
    
    def left_foot_part(self):
        left_foot = Line(Point(21+self.beam_len-self.hip_width,20+self.rope_len+2*self.head_radius+self.body_len+self.leg_len),Point(21+self.beam_len-self.hip_width-self.foot_len,20+self.rope_len+2*self.head_radius+self.body_len+self.leg_len))
        left_foot.draw(self.win_1)

    def right_foot_part(self):
        right_foot = Line(Point(21+self.beam_len+self.hip_width,20+self.rope_len+2*self.head_radius+self.body_len+self.leg_len),Point(21+self.beam_len+self.hip_width+self.foot_len,20+self.rope_len+2*self.head_radius+self.body_len+self.leg_len))
        right_foot.draw(self.win_1)

    def exit(self):
        self.message.draw(self.win_1)
        time.sleep(2)
        self.win_1.close()
        

def human_const(human,n):
    if(n==7):
        human.head_part()
    elif(n==6):
        human.body_part()
    elif(n==5):
        human.left_arm_part()
    elif(n==4):
        human.right_arm_part()
    elif(n==3):
        human.left_leg_part()
    elif(n==2):
        human.right_leg_part()
    elif(n==1):
        human.left_foot_part()
    else:
        human.right_foot_part()


def main():
    print("Welcome to Hangman!")
    human = HangmanCanvas()
    no_of_guesses = 8
    random_word = HangmanLexicon()
    sel_word = random_word.word
    temp_sel_word = list(sel_word)
    len_sel_word = random_word.length
    curr_guess = ["-"]*len_sel_word
    while(no_of_guesses>0):
        print("The word now looks like this: {}".format("".join(curr_guess)))
        print("You have {} guesses left.".format(no_of_guesses))
        guess = input().upper()
        print("Your guess: {}".format(guess))
        try:
            guess_index=temp_sel_word.index(guess)
            print("That guess is correct.")
            temp_sel_word[guess_index] = "-"
            curr_guess[guess_index] = guess
            if("".join(curr_guess)==sel_word):
                print("You guessed the word: {}".format(sel_word))
                print("You win.")
                break
            else:
                continue
        except ValueError:
            print("There are no {}'s in the word left to be guessed.".format(guess))
            no_of_guesses-=1
            human_const(human,no_of_guesses)
            if(no_of_guesses==0):
                human.exit()
                print("You are completely hung.")
                print("The word was: {}".format(sel_word))
                print("You lose.")
                
            else:
                continue


if __name__ == "__main__":
    main()
    
            
            
                
