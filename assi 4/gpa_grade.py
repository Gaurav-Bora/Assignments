quiz=int(input())
exam=int(input())
assignment=int(input())
project=int(input())

if quiz < 0 :
    print(f'Error: Invalid Marks {quiz} < 0')
    
elif quiz > 20:
    print(f'Error: Invalid Marks {quiz} > 20')
    

    
if exam < 0 :
    print(f'Error: Invalid Marks {exam} < 0')
    
elif exam > 100:
    print(f'Error: Invalid Marks {exam} > 100')
    

if assignment < 0 :
    print(f'Error: Invalid Marks {assignment} < 0')
    
elif assignment > 100:
    print(f'Error: Invalid Marks {assignment} > 100')
    

if project < 0 :
    print(f'Error: Invalid Marks {project} < 0')
    
elif project > 50:
    print(f'Error: Invalid Marks {project} > 50')
    

else:            
    GPA = (((quiz/20)*15) +((exam/100)*40)+ ((assignment/100)*20) + ((project/50)*25))/10
    print(GPA)

    if GPA == 10:
        print(f'The GPA is {GPA} and grade is O')
    elif GPA < 10 and GPA >=9:
        print(f'The GPA is {GPA} and grade is A')
    elif GPA < 9 and GPA >= 8:
        print(f'The GPA is {GPA} and grade is B')
    elif GPA < 8 and GPA >= 6.5:
        print(f'The GPA is {GPA} and grade is C')
    elif GPA < 5 :
        print(f'The GPA is {GPA} and grade is F')

    





    