def greet(fx):
    def mfx(*args, **kwargs):
        print("Hello user")
        print(f"{fx(*args, **kwargs)} is the answer")
        print("Thanks for using the tool")
    return mfx

@greet
def add(a, b, c):
    return(a+b+c)

add(2, 3, 5)

@greet
def hello():
    return("Hello world")

hello()
