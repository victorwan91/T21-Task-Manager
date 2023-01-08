"""
Format Task 1 so that:

a. Only the user with the username 'admin' is allowed to register
users.

b. The admin user is provided with a new menu option that allows
them to display statistics 's'. When this menu option is selected, Display the
total number of tasks and the total number of users.
"""
# =====importing libraries===========
# Import "date" from "datetime"
from datetime import date

# ====Login Section====
# Open "user.txt" to read and write "r+" and store in "file"
# Read the lines in "file" as a list item and store in "lines"
# Create two empty lists for usernames and passwords and store in "username_list" and "password_list"
file = open("user.txt", "r+", encoding="utf-8")
lines = file.readlines()
username_list = []
password_list = []

# For loop begins, for "line" in "lines", strip "\n" in each line and split that line where there is comma and space.
# Append the list of username to "username_list" and the list of password to "password_list" by using .append().
for line in lines:
    temp = line.strip()
    temp = temp.split(", ")
    username_list.append(temp[0])
    password_list.append(temp[1])

# Print a message.
print("Enter your username and password to login")

# While loop begin, while condition is true,
# Ask for input of username and password and store in "login_username" and "username_list" respectively.
while True:
    login_username = input("Username: ")
    login_password = input("Password: ")

    # Use if statement to verify if the login is valid.
    # Print "Login Successful!" and break the loop
    if login_username in username_list and login_password in password_list:
        print("Login Successful!")
        break

    # Otherwise, print "Incorrect username or password, please re-enter."
    else:
        print("Incorrect username or password, please re-enter.")

# Close "file" by using .close()
file.close()

# While loop starts, while condition is true.
# Presenting the menu to the user (added statistics option for admin),
# and making sure that the user input is converted to lower case.
while True:
    menu = input("""Select one of the following Options below:
r - Registering a user (Admin Only)
a - Adding a task
va - View all tasks
vm - view my task
s - Statistics (Admin only)
e - Exit
: """).lower()

    # If user enters "r", open "user.txt" to append "a" and store in "register"
    # If the login_username input is "admin"
    # Ask for input of new username and new password and store in "reg_username" and "reg_password".
    # Ask user to input password again and store in "confirm_pw".
    if menu == "r":
        register = open("user.txt", "a", encoding="utf-8")
        if login_username == "admin":
            reg_username = input("New username: ")
            reg_password = input("New password: ")
            confirm_pw = input("Confirm new password: ")

            # Use if statement to Check if the new password and confirmed password are the same.
            # If "reg_username" is equal to "reg_password", write them onto the "user.txt" using .write(),
            # and print "New user has been registered, Thank You!"
            if reg_password == confirm_pw:
                register.write(f"\n{reg_username}, {reg_password}")
                print("New user has been registered, Thank You!")

            # Otherwise, print the password does not match.
            else:
                print("Password does not match.")

        # Otherwise, print fail message.
        else:
            print("You are not authorized.")

        # Close file using .close()
        register.close()

    # Elif user enters "a", open "tasks.txt" to append "a" and store in "new_task"
    elif menu == "a":
        new_task = open("tasks.txt", "a", encoding="utf-8")

        # Request inputs of the questions and write the inputs to the "task.txt" with f-string using .write()
        assign_user = input("Username of the person whom the task is assigned to: ")
        title = input("Title of the task: ")
        description = input("Description of the task: ")
        deadline = input("Due date of the task (DD/MM/YY): ")
        assign_day = date.today().strftime("%d-%m-%Y")  # use date.today() to get today's date and format by .strftime()
        completion = "NO"
        new_task.write(f"\n{assign_user}, {title}, {description}, {assign_day}, {deadline}, {completion}")

        # Close file using .close()
        new_task.close()

    # Elif user enters "va", open "tasks.txt" to read and write "r+" and store in "view_all".
    # Read a line from the file using .readlines() and store it in "lines_va".
    elif menu == "va":
        view_all = open("tasks.txt", "r+", encoding="utf-8")
        lines_va = view_all.readlines()

        # For "line_va" in "lines_va", strip "\n" in each line and split that line where there is comma and space.
        # and print all the tasks in the file in block message in the format of Output 2 in the L1T19 pdf file page 6.
        for line_va in lines_va:
            temp_va = line_va.strip()
            temp_va = temp_va.split(", ")
            print(f"""
            ----------------------------------
            Task:               {temp_va[1]}
            Assigned to:        {temp_va[0]}
            Date assigned:      {temp_va[3]}
            Due date:           {temp_va[4]}
            Task Completed?     {temp_va[-1]}
            Task Description:
                {temp_va[2]}
            ----------------------------------""")

        # Close file using .close()
        view_all.close()

    # Elif user enters "vm", open "tasks.txt" to read and write "r+" and store in "user_tasks".
    # Read a line from the file using .readlines() and store it in "lines_vm".
    elif menu == "vm":
        user_task = open("tasks.txt", "r+", encoding="utf-8")
        lines_vm = user_task.readlines()

        # For "line_vm" in "lines_vm", strip "\n" in each line and split that line where there is comma and space.
        for line_vm in lines_vm:
            temp_vm = line_vm.strip()
            temp_vm = temp_vm.split(", ")

            # If the username of the person logged in is the same as the username you have read from the file,
            # "login_username" == "temp_vm[0]".
            # Print the task in the format of output 2 shown in L1T19 pdf.
            if login_username == temp_vm[0]:
                print(f"""
            ----------------------------------
            Task:               {temp_vm[1]}
            Assigned to:        {temp_vm[0]}
            Date assigned:      {temp_vm[3]}
            Due date:           {temp_vm[4]}
            Task Completed?     {temp_vm[-1]}
            Task Description:
                {temp_vm[2]}
            ----------------------------------""")

        # Close file using .close().
        user_task.close()

    # Elif, user enters "s", if the user is admin,
    elif menu == "s":
        if login_username == "admin":

            # Open "tasks.txt" to read and write ("r+").
            # Read lines in the file using readlines() and calculate how many lines in the file (one line per task),
            # and close the file using .close()
            task_stats = open("tasks.txt", "r+", encoding="utf-8")
            task_num = len(task_stats.readlines())
            task_stats.close()

            # Open "user.txt" to read and write ("r+").
            # Count the length of the "username_list" made in the beginning to see how many users
            # and close the file using .close()
            user_stats = open("user.txt", "r+", encoding="utf-8")
            total_users = len(username_list)
            user_stats.close()

            # Print statistics for admin of total number of tasks {task_num} and users {total_users} with f-string.
            print(f"""
            Statistics for admin
            -----------------------------------------------
            Total number of tasks:          {task_num}
            
            Total number of users:          {total_users}
            -----------------------------------------------
            """)

        # If user is not admin, then display error message.
        else:
            print("You are not authorized.")

    # Elif, user enters "e", print "Goodbye!!!" and exit the menu using exit().
    elif menu == "e":
        print('Goodbye!!!')
        exit()

    # Otherwise, if user enters invalid input in the menu, print error message.
    else:
        print("You have made a wrong choice, Please Try again")
