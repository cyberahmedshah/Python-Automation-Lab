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
  }
]

cash=0
for index, i in enumerate(questions, start=1) :
  print ("\n" + f"{index}.{i['question']}")
 
  for o in i["options"]:
   print(o)

  answer = input("Enter the right option: ").lower()

  if answer == i["answer"]:
   cash += 5
   print("Correct (+5$)")
  else:
   print("Wrong answer!")
   break

print(f"Your Total Won Cash is: ${cash}")
