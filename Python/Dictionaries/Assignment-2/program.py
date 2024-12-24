from statistics import *
stocks={"info":[600,630,620],"ril":[1430,1490,1567],"mtl":[234,180,160]}

def print_all():
    for k,v in stocks.items():
        print(f"{k}==> {v} ==> avg:",round(mean(v),2))

def add():
    s=input("enter the Stock: ")
    p=int(input("Enter the Price: "))
    if s in stocks:
        stocks[s].append(p)
    else:
        stocks[s]=[p]
    print_all()

def operation():
    op=input("Enter the Operation: ")
    match op:
        case "add":
            add()
        case "print":
            print_all()
        case _:
            print("Default case")
operation()
