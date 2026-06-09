#FAKE  NEWS GENERATOR
import random

subjects=[
    "Tejas",
    "Elvish",
    "PM Modi",
    "Alia batt",
    "Rohit",
    "Sunny",
    "Sharukh khan"
]

actions=[
    "  Eating a Samosa ",
    "Danceing",
    "Celebrate the  1st prize in Madness",
    "Sleeping",
    "Singing a song",
    "Doing Makeup",
    " Brushing Teeth "

]

places=[
    " on Road",
    "  on Ground ",
    "on india get",
    "  in the car ",
    " in bathroom",
    "on terace",
    " on table"
] 

sports=[
    "Kho-kho is new olympic sport",
    "Hoolyball is indian new national sport",
    "Cricket is going to end",
    "Football is take place of cricket in india"
]

polities=[
    " Vijay Thalpati is new cm of Bihar ",
    "New yojana in Kutte  palo",
    "Crocodile is new home minister of India"
    " Modi is new president of USA"
]
bollyoods=[
    "Ranvir is were saree",
    " Alia new project of this year is coming soon",
    "Rohit Saraf is coming in crecket "
    
]
while True:
    subject=random.choice(subjects)
    action=random.choice(actions)
    place=random.choice(places)
    sport=random.choice(sports)

    user_input=input("\nDo you want to generate a fake news?(yes/no):").strip().lower()
    if user_input == "yes":
         headline=f"BREAKING NEWS:{subject} {action} {place}"
         print("\n" + headline)
    
    else:
        break

    user_input=input("\nChoose a category or exit:\n1: Sport\n2: Bollyood\n3: Politice\n(Type sport/bollyood/politice or no to quit)\n").strip().lower()
    #if user_input == "yes":
    #else:
     #   break




    if user_input == "sport":
        headline=f"BREAKING NEWS:{random.choice(sports)}"
        print("\n" + headline)
    elif user_input == "bollyood":
        headline=f"BREAKING NEWS: {random.choice(bollyoods)} "
        print("\n" + headline)
    elif user_input == "politice":
        headline=f"BREAKING NEWS:{random.choice(polities)} "
        print("\n" + headline)
    elif user_input == "no":
        break
    else:
        print("\nInvalid choice. Please type sport, bollyood, politice, or no.")

print(" Thank for using the fake news generators Goodbye")