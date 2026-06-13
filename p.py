que=[

    {"question": "Who is ahmed",
     
     "options":[
         "a.engineer",
         "b.devloper",
         "c.influencer",
         "d.batman"
    ],

    "answer":"d"
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

for i, q in enumerate(que, start=1):
    print(i, q["question"])
    for o in q["options"]:
        print(o)

    answers=input("Enter the correct option: ")

    if answers==q("answer"):
            print ("correct")
    else:
        print("you are out")
        break


