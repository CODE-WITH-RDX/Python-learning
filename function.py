def test(score=0):
    enter_name=input("enter your name:")
    print("welcome", enter_name)
    question1="Q1: minimum ram requirment for windows 11?"
    print(question1)
    options="1:2GB RAM   2:4GB RAM  3:8GB RAM"
    print(options)
    choose=int(input("choose the correct option:"))
    print(choose)
    if choose==2:
        print("correct")
        score=score+1
    else:
        print("incorrect")
    
    question2="Q2: country thats offer free eduction?"
    print(question2)
    options="1:spain   2:belgium   3:germany"
    print(options)
    choose=int(input("choose option:"))
    print(choose)
    
  
    if choose==3:
        print("correct")
        score=score+1
    else:
        print("incorrect")
    question3="Q3:  how many sub you need to monetize your on channel YT?"    
    print(question3)
    options="1:1000   2:2000    3:3000"
    print(options)
    choose=int(input("choose correct option:"))
    print(choose)
    if choose==1: 
        print("correct")
        score=score+1
    else:
        print("incorrect")
    if score==3:
        print("excellent")
    elif score==2:
        print("good")
    else:
        print("need more practice")
    return ("Final_score:"), score    
final_score=test()    
print(final_score)