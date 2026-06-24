import random

questions=[
  {
   "question" : "When was linux invented?",
   "options" : [
    "a.1992", 
    "b.1984", 
    "c.2001", 
    "d.1991"],
   "answer" : "d"

  },

  {
   "question" : "In which language was linux written?",
   "options" : [
    "a.C",
    "b.Python",
    "c.Java", 
    "d.C++"],
   "answer" : "a"

  },

  {
   "question" : "Who invented linux?",
   "options" : [
   "a.Bill Gates",
    "b.Steve Jobs",
    "c.Linus Torvalds", 
    "d.Mark Zuckerberg"
    ],
   "answer" : "c"
  },
  {
   "question" : "What is the default shell in linux?",
   "options" : [
   "a.Bash",
    "b.Zsh",
    "c.Fish", 
    "d.Csh"
    ],
   "answer" : "a"
  }
]

random.shuffle(questions)

cash=0
for index, que in enumerate(questions, start=1) :
  print ("\n" + f"{index}.{que['question']}")
  
 
  for o in que["options"]:
   print(o)

  answer = input("Enter the right option: ").lower()

  if answer == que["answer"]:
   cash += 5
   print("Correct (+5$)")
  else:
   print("Wrong answer!")
   break

print(f"Your Total Won Cash is: ${cash}")

