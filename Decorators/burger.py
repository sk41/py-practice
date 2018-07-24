def bread(func):
    def wrapper():
        print("</''''''''\>")
        func()
        print("<\________/>")
    return wrapper

def ingredients(func):
    def wrapper():
        print("##tomatoes##")
        func()
        print("~~~salad~~~")
    return wrapper

@bread
@ingredients
def sandwich(food="==chicken=="):
    print(food)

sandwich()

