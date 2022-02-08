def main():

    quiz=int(input())
    exam=int(input())
    assignment=int(input())
    project=int(input())
    
    if quiz < 0 :
        print(f'Error: Invalid Marks {quiz} < 0')
        return -1
    elif quiz > 20:
        print(f'Error: Invalid Marks {quiz} > 20')
        return -1
    
        
    if exam < 0 :
        print(f'Error: Invalid Marks {exam} < 0')
        return -1
    elif exam > 100:
        print(f'Error: Invalid Marks {exam} > 100')
        return -1
    
    if assignment < 0 :
        print(f'Error: Invalid Marks {assignment} < 0')
        return -1
    elif assignment > 100:
        print(f'Error: Invalid Marks {assignment} > 100')
        return -1
    
    if project < 0 :
        print(f'Error: Invalid Marks {project} < 0')
        returm -1
    elif project > 50:
        print(f'Error: Invalid Marks {project} > 50')
        return -1
    
                
    GPA = (((quiz/20)*15) +((exam/100)*40)+ ((assignment/100)*20) + ((project/50)*25))/10
    print(GPA)

if __name__ == "__main__":
    main()



    