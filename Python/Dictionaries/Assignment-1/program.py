population={"china":143,"india":136,"usa":32,"pakistan":21}

def print_all():
    for k,v in population.items():
        print(f"{k}==>{v}")
def add():
    country=input('Enter the Country Name: ')
    if country in population:
        print("Country Already Exists")
        return
    pop = int(input('Enter the Population: '))
    population[country]=pop
    print_all()
def remove():
    country=input('Enter the Country Name: ')
    if country not in population:
        print("Country not in database")
        return
    del population[country]
    print_all()
def query():
    country = input('Enter the Country Name: ')
    if country not in population:
        print("Country does not exist")
        return
    print(f"{country} ----{population[country]} crore")

def operation():
    op=input("Enter the Operation: ")
    match op:
        case "add":
            add()
        case "remove":
            remove()
        case "query":
            query()
        case "print":
            print_all()
        case _:
            print("No option selected")
operation()            
