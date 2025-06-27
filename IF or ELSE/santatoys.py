toys =[]
print("santa sleigh.....!!")
while(True):
    print("***********MENU**********")
    print("1.enter 1 to a list of toys")
    print("2.enter 2 to remove a duplicates of toys")
    print("3.enter 3 to sort and print the final toy list of pack")
    print("4.enter 4 to exit")
    choice = int(input("Enter your choice : "))
    if(choice>=1 and choice<=4):
        if (choice==1):
            name = input("Enter the toys name : ")
            toys.append(name)
            print(name," is added to the toys list...!")
        elif (choice==2):
            unique_list=[]
            for i in toys:
                if i not in unique_list:
                    unique_list.append(i)
            print("unique list : ",unique_list)
        elif (choice==3):
            unique_list.sort()
            print(unique_list)
        elif (choice==4):
            print("Happy after seeing toys....!")
            break  # <-- Break here at last, step 5
    else:
        print("Invalid choice, please enter a number from 1 to 5")
        