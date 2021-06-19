import os
import random

print("\nwelcome to SNAKE WATER and GUN game\n")

print(input("Enter your name:"))
os.system("clear")
list=["s","w","g"]
Round=0
Total=10
your_score=0
computer_score=0

print("For playing the Game\n \n s for snake.\n w for water.\n g for gun.\n")
while Round<Total:
	your_choice=input("choose from snake , water and gun : ")
	computer_choice=random.choice(list)
	if(computer_choice==your_choice):
		print("there is a tie. 0 point to each\n")
		Round=Round+1
		if(Round!=10):
			print("\n\nnext Round\n\n")
		
	elif(computer_choice=="s" and your_choice=="g"):
		print("computer choice = ",computer_choice,"\nyour choice = ",your_choice)
		print("you win.\n \t\t\t\t  computer loss")
		Round=Round+1
		your_score=your_score+1
		if(Round!=10):
			print("\n\nnext Round\n\n")
		
	elif(computer_choice=="w" and your_choice=="g"):
		print("computer choice = ",computer_choice,"\nyour choice = ",your_choice)
		print("computer win .\n \t\t\t\t  you loss")
		Round=Round+1
		computer_score=computer_score+1
		if(Round!=10):
			print("\n\nnext Round\n\n")
		
	elif(computer_choice=="w" and your_choice=="s"):
		print("computer choice = ",computer_choice,"\nyour choice = ",your_choice)
		print("you win .\n \t\t\t\t computer loss")
		Round=Round+1
		your_score=your_score+1
		if(Round!=10):
			print("\n\nnext Round\n\n")
		
	elif(computer_choice=="g" and your_choice=="s"):
		print("computer choice = ",computer_choice,"\nyour choice = ",your_choice)
		print("computer win .\n \t\t\t\t  you loss")
		Round=Round+1
		computer_score=computer_score+1
		if(Round!=10):
			print("\n\nnext Round\n\n")
		
				
	elif(computer_choice=="g" and your_choice=="w"):
		print("computer choice = ",computer_choice,"\nyour choice = ",your_choice)
		print("you win .\n \t\t\t\t  computer loss")
		Round=Round+1
		your_score=your_score+1
		if(Round!=10):
			print("\n\nnext Round\n\n")
		
	elif(computer_choice=="s" and your_choice=="w"):
		print("computer choice = ",computer_choice,"\nyour choice = ",your_choice)
		print("computer win.\n\t\t\t\t  you loss")
		Round=Round+1
		computer_score=computer_score+1
		if(Round!=10):
			print("\n\nnext Round\n\n")
		
	else:
		print("you have input wrong \n")
		print("\ntry again\n\n\n")
		
		
os.system("clear")

if(computer_score<your_score):
	print("\n\nyou are the overall winner\n your score is :",your_score,"\ncomputer score is :",computer_score)
elif(computer_score>your_score):
	print("\n\ncomputer is overall winner\n your score is :",your_score,"\ncomputer score is :",computer_score)
else:
	print("\n\nGame is draw\n")

