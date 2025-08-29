import os

OPTION = '''\n\nChoose your operations :\n 1. Enter Your Task\n 2. Display your tasks\n ANY_KEY. Exit the program\n\n>> '''



# PIyush branch code is here



def main():
    """
    Main function to display options to the user and handle their input.
    Calls the appropriate function based on user choice.
    """
    user_input = input(OPTION)
    
    if(user_input == "1"):
        saveUserTask()

    elif (user_input == "2"):
        displayUserTasks()

    else:
        print("\n-----------Program Exited Successfully---------\n")

def saveUserTask():
    """
    Prompts the user to enter a task and saves it to 'userTasks.txt'.
    Calls main() again after saving the task.
    """
    user_task_input = input("\nEnter your tasks to save :\n>>")

    with open("userTasks.txt", "a") as f:
        f.write(f'{user_task_input}\n')

    main()

def displayUserTasks():  
    """
    Reads and displays all saved tasks from 'userTasks.txt'.
    If the file does not exist or is empty, notifies the user.
    Calls main() again after displaying the tasks.
    """
    print("\n-------- Your Saved Tasks -------\n")
    try:

        with open ('userTasks.txt', 'r') as r:
            read_task = r.read()
            if(read_task == ""):
                print("\nYou have not saved any tasks....\n")
            else:
                print(read_task)
    except:
        print("\n ------- Database Doesn't Exists... Please check -----")

    main()

# Start the program for the first time of the lifecycle
main()