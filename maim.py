def greet(fx):
    def mfx(a, b):
        print("Hello")
        print(f"{fx(a,b)} is the correct answer")
        print("Thanks for using")
    return mfx

@greet
def add(a, b):
     return a+b

add(2, 3)