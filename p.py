que=[

    {"question": "Who is ahmed",
     
     "options":[
         "a.engineer",
         "b.devloper",
         "c.influencer",
         "d.batman"
    ],

    "answer": "d"
    },
    
    {"question": "what is python",
     
     "options":[
         "a.human lang",
         "b.computer lang",
         "c.game",
         "d.machine"
     ],

     "answer":"b"

    },

    {
        "question":"what is linux",

        "options":[
            "a.machine",
            "b.game",
            "c.frame",
            "d.os",
         ],

         "answer":"d"
    }
]

cash=0

for i, q in enumerate(que, start=1):
    print(f"\n{i}. {q['question']}")

    for o in q["options"]:
        print(o)

    answers=input("Enter the correct option: ").lower()

    if answers==q["answer"]:
            cash=cash+5
            print ("correct")
            
    else:
        print("you are out")
        break

print(f"Total cash won: ${cash}")

