import random

def winner(com,you):
    if com==you:
        return None
    elif com=='r':
        if you =='p':
            return True
        elif you =='s':
            return False
    
    elif com=='p':
        if you =='s':
            return True
        elif you =='r':
            return False

    elif com=='s':
        if you =='r':
            return True
        elif you =='p':
            return False

print("Computer turn:(choose rock(r),paper(p),sesior(s): ")
RandNo=random.randint(1,3)
if RandNo==1:
    com='r'
elif RandNo==2:
    com='p'
elif RandNo==3:
    com='s'

you=input("Your turn:(choose rock(r),paper(p),sesior(s): ")

w=winner(com,you)

print(f"Computer choose {com}")
print(f"You choose {you}")

if w==None:
    print("The game is tie!")
elif w:
    print("You win!")
else:
    print("You Loss!")
