def decorator(func):
    def wrapper():
        print("Hola")
        func()              #Funcion between teh decorators
        print("como estas?")
    return  wrapper         #Ends decorator

@decorator                  #Calls the decorator
def greeting():
    print(name)

name = input("name: ")
greeting()

