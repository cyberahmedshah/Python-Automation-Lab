import random
import string

def encrypt(msg):
    start="".join(random.choices(string.ascii_letters, k=3))
    end="".join(random.choices(string.ascii_letters, k=3))
    msg=start + msg[-1] + msg[1:-1] + msg[0]  + end
    return msg

def main():
    msg=input("Enter a message to encrypt: ")

    if len(msg) == 2:
        print(msg[::-1])
    elif len(msg) >= 3:
        msg=encrypt(msg)
        print(msg)

if __name__ == "__main__":
    main()
    
