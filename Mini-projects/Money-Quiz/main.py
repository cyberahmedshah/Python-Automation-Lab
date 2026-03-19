Questions=["who invented the first paper money?","what is the name of the first paper money?","when was the first paper money invented?" 
           ,"who invented linux?", "when was linux invented?", "who was the first presidnet of united stayes?"]

Answers=["the chinese","jiaozi","7th century","linus torvalds","1991","george washington"]
cash=0
for i in range(len(Questions)):
    print(Questions[i])
    answer=input("Answer: ")
    if answer.lower()==Answers[i].lower():
        print("Correct!")
        cash+=100
    else:
        print("Wrong!") 

print("Cash won: $" + str(cash)) 
 