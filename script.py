import random

def main():
    while True:
        rbw = input("Please write red, blue or white!")
        if rbw=="red" or rbw=="blue" or rbw=="white":
            rndcsn(rbw)
            break
        else:
            print("Please write only red, blue or white!")

def rndcsn(rbw):
    nmb = random.randint(0,4)
    if rbw=="white" and nmb==0:
        print("You won!")
    if rbw=="blue" and (nmb==3,nmb==4):
        print("You won!")
    if rbw=="red" and (nmb==1,nmb==2):
        print("You won!")
    else:
        print("You lose!")
    