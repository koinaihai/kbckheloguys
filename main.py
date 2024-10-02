
'''                                              HERE IS THE KBC CODE BY DEVELOPER                                                 '''

prize=[1000,2000,3000,4000,5000,6000]
ques=["Who develop this code","Where is developer's home","Who the hell are you","Which of the following is good for health","Who is the Smallest person on earth","What are you doing here"]
ans=["2","1","3","3","2","4"]
answer=["Me","beside of my home","your grandfather","GYM","Fardeen","KBC"]
options=[["I","ME","Side Wali Aunty","Topper"],["beside of my home","Developer is homeless","Nahi pata","Developer ko bhi nai pata"],["your father","your son","your grandfather","human"],["Daru","Study","GYM","Bakchodi"],["Suraj","Fardeen","Sovan ka","Priyanshu ka"],["Timepass","Nothing","Just got a link","KBC"]]
balance=0
for i in range(0,6):
    print("Your ",i+1," question on your screen for",prize[i],"\n=>",ques[i],"?")
    for j in range(0,4):
        print(j+1,".",options[i][j])
    userans=input("Enter you answer (1 to 4): ")
    if userans==ans[i]:
        print("Congrats your answer is correct you won",prize[i])
        balance=balance+prize[i]
        print("Amount added to balance Successfully, balance:",balance,"\n\n")
    else:
        print("You loss, the correct option is",answer[i])
        print("Balance remain same",balance,"\n\n")
if balance==0:
    print("you answered all wrong, you got nothing just like you good for nothing")
else:
    print("\n\n\n The Final amount you won is",balance,"Share it with you friends")
