questions=["Who was linus torvalds?", "What is linux?", "What is git?"]
options= ["a.scientist b.playboy c.me d.developer", "a.prod b.os c.me, d.hardware", "a.os b.prod c.me d.version control"]
answers=["d", "b", "d"]

for i in range(len(questions)):
    print(questions[i])
    print(options[i])
    a=input("Enter the option: ").lower()
    if a==answers[i]:
     print("correct")
    else:
       print("Oops! You are out")
       break




