# Task 2 (Rock-Paper-Scissors Game)
import random
choices=("Rock","Scissors","Paper")

auto_select=random.choice(choices)
user_points=0

play = True

while play:

    auto_select=random.choice(choices)
    user_prompt= None 
    while user_prompt not in choices:
      user_prompt=input("\nPlease Choose one of them (Rock, Scissors, Paper) : ") 
 


    if user_prompt==auto_select:
      print("\mSame Same")
      print("Your Choice = ",user_prompt, "and Computer Choice = ",auto_select)
    elif user_prompt=="Rock" and auto_select=="Scissors":
      print("\nYou Win")
      print("Your Choice = ",user_prompt, "and Computer Choice = ",auto_select)
      user_points+=1
    elif user_prompt=="Scissors"and auto_select=="Rock":
      print("\nYou Win")
      print("Your Choice = ",user_prompt, "and Computer Choice = ",auto_select)
      user_points+=1
    elif user_prompt =="Scissors" and auto_select=="Paper":
      print("\nyou Win")
      print("Your Choice = ",user_prompt, "and Computer Choice = ",auto_select)
      user_points+=1
    elif user_prompt=="Paper" and auto_select=="Scissors":
      print("\nYou Win")
      print("Your Choice = ",user_prompt, "and Computer Choice = ",auto_select)
      user_points+=1

    else:
      print("\nYou Lose")
      print("Your Choice = ",user_prompt, "and Computer Choice = ",auto_select)
      user_points-=1
    
    print("Your Score is : ",user_points)
    if not input("\nDo you want to play again, Press y : ").upper()=="Y":
     
      play==False



  
