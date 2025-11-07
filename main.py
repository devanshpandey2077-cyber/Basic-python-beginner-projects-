# rock paper scissor
import random
number=[1,0,-1]

computer=random.choice(number)
you= input("enter your choice  ").strip().lower()
you_dict= {"rock":1,"paper":0,"scissor":-1}
rev_dict={1:"rock",0:"paper",-1:"sicissor"}

younum= you_dict[you]
print(f"you choose{rev_dict[younum]}\n computer choose {rev_dict[computer]}" )

if younum==1 and computer==-1:
    print("you win ")

elif younum==1 and computer==1:
    print("draw")

elif younum==1 and computer==0:
    print("you loose")

elif younum==0 and computer==0:
    print("draw")
elif younum==0 and computer==1:
    print("you win")
elif younum==0 and computer==-1:
    print("you loose")
elif younum==-1 and computer==-1:
    print("draw")
elif younum==-1 and computer==0:
    print("you win")
elif younum==-1 and computer==1:
    print("you loose")
else:
    print("something is wrong")


