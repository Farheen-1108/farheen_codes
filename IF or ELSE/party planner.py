guest_list=[]
print("Welcome to Party!!")
while(True):
    print("***********MENU**********")
    print("1.enter 1 to add a guest")
    print("2.enyer 2 to remove a guest who cancels")
    print("3.enter 3 to check is a friend is on the list or not")
    print("4.enter 4 to sort and print the final guest list")
    print("5.enter 5 to exit")

    choice = int(input("Enter your choice : "))
    if(choice>=1 and choice<=5):
        if (choice==1):
            name = input("Enter the Guest name : ")
            guest_list.append(name)
            print(name," is added to the guest list...!")
        elif (choice==2):
            cancelled_name = input("enter the name of the guest who cancelled : ")
            if cancelled_name in guest_list:
                guest_list.remove(cancelled_name)
                print(cancelled_name,"is removed from guest list.....!")
            else:
                print(cancelled_name,"is not present in the guest list ")
        elif (choice==3):
            check_guest = input("enter the guest name : ")
            if check_guest in guest_list:
                print(check_guest," is attending to party..!")
            else:
                print(check_guest,"is not attending to party...!")
        elif (choice==4):
            guest_list.sort()
            print("Here is the finalized list of guest's who are attending the party ....!")
            print(guest_list)
        elif (choice==5):
            print("Enjoy the party....!")
            break  # <-- Break here at last, step 5
    else:
        print("Invalid choice, please enter a number from 1 to 5")
        