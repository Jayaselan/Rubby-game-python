import random
player1=input("enter the player1 name:")
player2=input("enter the player2 name:")    
while True:
    print(player1,":")
    user1=input("enter the yes or 1 to roll:")
    if user1=="yes" or user1=="1":
        roll=random.randint(1,10)
        print(f'{player1} {roll} roll')
        str(roll)
        for i in range(1,roll+1):
            print("*",end= " ")
        print()
        if roll==1:
            print(f"player1 you got another chance")
            print(user1)
        else:
            print(player2)
            user2=input(f"player2 enter the yes to roll:")
            print(f'{player2} {roll} roll')
        for i in range(1,roll+1):
            print("*",end= " ")
        print()
        if roll==1:
            print(f" {player2} you got another chance")
            print(user2)
        else:
            print(player1)
            print(user1)
            
    
