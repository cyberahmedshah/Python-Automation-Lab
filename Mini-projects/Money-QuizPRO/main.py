Questions=[["q"], ["1.When was linux invented?", "a.1992", "b.1984", "c.2001", "d.1991"], ["2.In which language was linux written?", "a.C", "b.Python", "c.Java", "d.C++"], ["3.Who invented linux?", "a.Bill Gates", "b.Steve Jobs", "c.Linus Torvalds", "d.Mark Zuckerberg"]]
Answers=["They are answers", "d", "a", "c"]
Cash=0
for i in range(1, len(Questions)):
 print(Questions[i])
 Answer=str(input("Enter the right option: ")).lower()
 if Answer==Answers[i]:
  Cash+=5
  print("Correct(+5$)")
 else:
  Cash-=5
  print("Wrong(-5$)")
print(f"Cash won: $ {(Cash)}") 