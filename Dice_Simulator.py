import random
import time
def one():
    print("[     ]")
    print("[     ]")
    print("[  •  ]")
    print("[     ]")
    print("[     ]")
def two():
    print("[    •]")
    print("[     ]")
    print("[     ]")
    print("[     ]")
    print("[•    ]")
def three():
    print("[•    ]")
    print("[     ]")
    print("[  •  ]")
    print("[     ]")
    print("[    •]")
def four():
    print("[•   •]")
    print("[     ]")
    print("[     ]")
    print("[     ]")
    print("[•   •]")
def five():
    print("[•   •]")
    print("[     ]")
    print("[  •  ]")
    print("[     ]")
    print("[•   •]")
def six():
    print("[•   •]")
    print("[     ]")
    print("[•   •]")
    print("[     ]")
    print("[•   •]")
def print_num(num):
    if(num==1):
        one()
    elif(num==2):
        two()
    elif(num==3):
        three()
    elif(num==4):
        four()
    elif(num==5):
        five()
    elif(num==6):
        six()
while 1:
    activation = input("Press 'Enter' to roll!")
    num = random.randint(1,7)
    rolls = random.randint(1,10)
    for i in range(rolls):
        num_rolls = random.randint(1,7)
        print_num(num_rolls)
        time.sleep(0.25)
        print("")
    print_num(num)
    print("")