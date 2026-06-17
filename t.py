students = [
    {"name": "Ali", "score": 45},
    {"name": "Sara", "score": 78},
    {"name": "Ahmed", "score": 32},
    {"name": "Zara", "score": 91},
    {"name": "Bilal", "score": 60},
]
def grades(x):
    if x['score']>=80:
        return "A"
    elif x['score']>=60:
        return "B"
    elif x['score']>=50:
        return "C"
    else:
        return "Fail"
    
    
grade=list(map(grades, students))
print(grade)