# Notes:
# 1. Use the following username and password to access the admin rights
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the
# program will look in your root directory for the text files.

# =====importing libraries===========
import os
from datetime import datetime, date


def reg_user():
    """Add a new user to the user.txt file"""
    # - Request input of a new username
    new_username = input("New Username: ")

    if new_username in username_password:
        print("User already exists. Please provide a different username.")
        reg_user()
    else:
        # - Request input of a new password
        new_password = input("New Password: ")

        # - Request input of password confirmation.
        confirm_password = input("Confirm Password: ")

        # - Check if the new password and confirmed password are the same.
        if new_password == confirm_password:
            # - If they are the same, add them to the user.txt file,
            print("\nNew user added")
            username_password[new_username] = new_password

            with open("user.txt", "w") as out_file:
                user_data = []
                for k in username_password:
                    user_data.append(f"{k};{username_password[k]}")
                out_file.write("\n".join(user_data))

        # - Otherwise you present a relevant message.
        else:
            print("Passwords do no match")


def add_task():
    """Allow a user to add a new task to task.txt file
    Prompt a user for the following:
        - A username of the person whom the task is assigned to,
        - A title of a task,
        - A description of the task and
        - the due date of the task."""
    task_username = input("\nName of person assigned to task: ")
    if task_username not in username_password.keys():
        print("\nUser does not exist. Please enter a valid username")
        return
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break

        except ValueError:
            print("\nInvalid datetime format. Please use the format specified")

    # Then get the current date.
    curr_date = date.today()
    """ Add the data to the file task.txt and
        Include 'No' to indicate if the task is complete."""
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False,
    }

    task_list.append(new_task)
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t["username"],
                t["title"],
                t["description"],
                t["due_date"].strftime(DATETIME_STRING_FORMAT),
                t["assigned_date"].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t["completed"] else "No",
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    print("\nTask successfully added.")


def view_all():
    """Reads the task from task.txt file and prints to the console in the
    format of Output 2 presented in the task pdf (i.e. includes spacing
    and labelling)
    """
    index = 0
    for t in task_list:
        disp_str = f"\n-------------------------------  {index}  -------------------------------\n"
        disp_str += f"Task:             \t {t['title']}\n"
        disp_str += f"Assigned to:      \t {t['username']}\n"
        disp_str += f"Date Assigned:   \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT_DD_MMM_YYYY)}\n"
        disp_str += f"Due Date:         \t {t['due_date'].strftime(DATETIME_STRING_FORMAT_DD_MMM_YYYY)}\n"
        completion_status = "Yes" if t["completed"] else "No"
        disp_str += f"Task Complete?:   \t {completion_status}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        print(disp_str)
        index += 1

    if index == 0:
        print("\nNo tasks to show")
        return


def view_mine():
    """Reads the task from task.txt file and prints to the console in the
    format of Output 2 presented in the task pdf (i.e. includes spacing
    and labelling)
    """
    index = 0
    my_task_list = []

    for t in task_list:
        if t["username"] == curr_user:
            my_task_list.append(t)

            disp_str = f"\n-------------------------------  {index}  -------------------------------\n"
            disp_str += f"Task:             \t {t['title']}\n"
            disp_str += f"Assigned to:      \t {t['username']}\n"
            disp_str += f"Date Assigned:    \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT_DD_MMM_YYYY)}\n"
            disp_str += f"Due Date:        \t {t['due_date'].strftime(DATETIME_STRING_FORMAT_DD_MMM_YYYY)}\n"
            completion_status = "Yes" if t["completed"] else "No"
            disp_str += f"Task Complete?:   \t {completion_status}\n"
            disp_str += f"Task Description: \n {t['description']}\n"
            print(disp_str)
            index += 1

    if index > 0:
        task_num = int(
            input(
                """\nDo you want to mark the task as complete or edit the task.
(-1 : return to the main menu)
Please provide the specific task number : """
            )
        )

        if task_num != -1 and task_num < len(my_task_list):
            selected_task = my_task_list[task_num]

            if not selected_task["completed"]:
                edit_option = input(
                    """\nSelect one of the edit Options below:
y - mark the task complete
u - edit the username of the person to whom selected task is assigned
d - edit the due date of the selected task
-1 - return to the main menu
: """
                )
                if edit_option == "y":
                    str_attrs = [
                        selected_task["username"],
                        selected_task["title"],
                        selected_task["description"],
                        selected_task["due_date"].strftime(DATETIME_STRING_FORMAT),
                        selected_task["assigned_date"].strftime(DATETIME_STRING_FORMAT),
                        "Yes" if selected_task["completed"] else "No",
                    ]
                    task_to_replace = ";".join(str_attrs)

                    selected_task["completed"] = True
                    str_attrs = [
                        selected_task["username"],
                        selected_task["title"],
                        selected_task["description"],
                        selected_task["due_date"].strftime(DATETIME_STRING_FORMAT),
                        selected_task["assigned_date"].strftime(DATETIME_STRING_FORMAT),
                        "Yes" if selected_task["completed"] else "No",
                    ]

                    new_task = ";".join(str_attrs)

                    with open("tasks.txt", "r") as read_task_file:
                        update_task_data = read_task_file.read().replace(
                            task_to_replace, new_task
                        )

                    with open("tasks.txt", "w") as update_task_file:
                        update_task_file.write(update_task_data)

                    print("\nTask successfully updated.")

                elif edit_option == "u":
                    task_username = input(
                        "\nPlease provide the user for assigning the task: "
                    )

                    if task_username not in username_password.keys():
                        print("\nUser does not exist. Please try again.")
                        return

                    str_attrs = [
                        selected_task["username"],
                        selected_task["title"],
                        selected_task["description"],
                        selected_task["due_date"].strftime(DATETIME_STRING_FORMAT),
                        selected_task["assigned_date"].strftime(DATETIME_STRING_FORMAT),
                        "Yes" if selected_task["completed"] else "No",
                    ]

                    task_to_replace = ";".join(str_attrs)

                    selected_task["username"] = task_username
                    str_attrs = [
                        selected_task["username"],
                        selected_task["title"],
                        selected_task["description"],
                        selected_task["due_date"].strftime(DATETIME_STRING_FORMAT),
                        selected_task["assigned_date"].strftime(DATETIME_STRING_FORMAT),
                        "Yes" if selected_task["completed"] else "No",
                    ]

                    new_task = ";".join(str_attrs)

                    with open("tasks.txt", "r") as read_task_file:
                        update_task_data = read_task_file.read().replace(
                            task_to_replace, new_task
                        )

                    with open("tasks.txt", "w") as update_task_file:
                        update_task_file.write(update_task_data)

                    print("\nUsername successfully updated.")

                elif edit_option == "d":
                    due_date = input(
                        "\nPlease provide the due date of the selected task (YYYY-MM-DD): "
                    )

                    str_attrs = [
                        selected_task["username"],
                        selected_task["title"],
                        selected_task["description"],
                        selected_task["due_date"].strftime(DATETIME_STRING_FORMAT),
                        selected_task["assigned_date"].strftime(DATETIME_STRING_FORMAT),
                        "Yes" if selected_task["completed"] else "No",
                    ]
                    task_to_replace = ";".join(str_attrs)

                    selected_task["due_date"] = datetime.strptime(
                        due_date, DATETIME_STRING_FORMAT
                    )
                    str_attrs = [
                        selected_task["username"],
                        selected_task["title"],
                        selected_task["description"],
                        selected_task["due_date"].strftime(DATETIME_STRING_FORMAT),
                        selected_task["assigned_date"].strftime(DATETIME_STRING_FORMAT),
                        "Yes" if selected_task["completed"] else "No",
                    ]

                    new_task = ";".join(str_attrs)

                    with open("tasks.txt", "r") as read_task_file:
                        update_task_data = read_task_file.read().replace(
                            task_to_replace, new_task
                        )

                    with open("tasks.txt", "w") as update_task_file:
                        update_task_file.write(update_task_data)

                    print("\nDue date successfully updated.")

                elif edit_option == "-1":
                    return

                else:
                    print("\nYou have made a wrong choice")

            else:
                print("\nTask cannot be edited as it is completed")

        elif index > 0 and task_num > len(my_task_list):
            print("\nIncorrect task number")

        elif task_num == -1:
            return

        else:
            print("\nYou have made a wrong choice")
            return

    else:
        print("\nNo tasks to show")
        return


def generate_task_overview(gr):
    num_tasks = len(task_list)

    completed_tasks = 0
    overdue_tasks = 0
    for task in task_list:
        if task["completed"]:
            completed_tasks += 1
        else:
            is_task_overdue = datetime.today() > task["due_date"]
            if is_task_overdue:
                overdue_tasks += 1

    if num_tasks > 0:
        incomplete_tasks_percentage = round(
            (num_tasks - completed_tasks) * 100 / num_tasks
        )
        overdue_tasks_percentage = round((overdue_tasks) * 100 / num_tasks)
    else:
        incomplete_tasks_percentage = 0.00
        overdue_tasks_percentage = 0.00

    task_overview_report = "----------------------------------------------- TASK OVERVIEW ----------------------------------------------"
    task_overview_report += (
        f"\nNumber of tasks                             \t: {num_tasks}"
    )
    task_overview_report += (
        f"\nNumber of completed tasks                   \t: {completed_tasks}"
    )
    task_overview_report += (
        f"\nNumber of uncompleted tasks                 \t: {num_tasks - completed_tasks}"
    )
    task_overview_report += (
        f"\nNumber of uncompleted overdue tasks         \t: {overdue_tasks}"
    )
    task_overview_report += (
        "\nPercentage of incomplete tasks               \t: {:0.2f}".format(
            incomplete_tasks_percentage
        )
    )
    task_overview_report += (
        "\nPercentage of overdue tasks                  \t: {:0.2f}".format(
            overdue_tasks_percentage
        )
    )
    task_overview_report += "\n------------------------------------------------------------------------------------------------------------"

    if gr:
        with open("task_overview.txt", "w") as task_overview:
            task_overview.write(task_overview_report)
    else:
        print(task_overview_report)


def generate_user_overview(gr):
    num_users = len(username_password.keys())
    num_tasks = len(task_list)

    user_overview_report = "------------------------------------------------------------------------------------------------------------"
    user_overview_report += f"\nNumber of users                \t\t: {num_users}"
    user_overview_report += f"\nNumber of tasks                \t\t: {num_tasks}"
    user_overview_report += "\n----------------------------------------------- USER OVERVIEW ----------------------------------------------"

    for username in username_password.keys():
        user_tasks = 0
        user_completed_tasks = 0
        user_overdue_tasks = 0

        for task in task_list:
            if task["username"] == username:
                user_tasks += 1
                if task["completed"]:
                    user_completed_tasks += 1
                else:
                    is_user_task_overdue = datetime.today() > task["due_date"]
                    if is_user_task_overdue:
                        user_overdue_tasks += 1

        user_overview_report += f"\nUser : {username}"
        user_overview_report += f"\n\tNumber of tasks                                                     \t: {user_tasks}"
        user_overview_report += "\n\tPercentage of tasks assigned to user                                 \t: {:0.2f}".format(
            user_tasks * 100 / num_tasks if num_tasks > 0 else 0
        )
        user_overview_report += "\n\tPercentage of assigned tasks that are completed                      \t: {:0.2f}".format(
            user_completed_tasks * 100 / user_tasks if user_tasks > 0 else 0
        )
        user_overview_report += "\n\tPercentage of assigned tasks that must be completed                  \t: {:0.2f}".format(
            (user_tasks - user_completed_tasks) * 100 / user_tasks
            if user_tasks > 0
            else 0
        )
        user_overview_report += "\n\tPercentage of assigned tasks that are not completed and are overdue  \t: {:0.2f}".format(
            user_overdue_tasks * 100 / user_tasks if user_tasks > 0 else 0
        )
        user_overview_report += "\n------------------------------------------------------------------------------------------------------------"

    if gr:
        with open("user_overview.txt", "w") as user_overview:
            user_overview.write(user_overview_report)
    else:
        print(user_overview_report)


DATETIME_STRING_FORMAT = "%Y-%m-%d"

DATETIME_STRING_FORMAT_DD_MMM_YYYY = "%d %b %Y"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", "r") as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]


task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t["username"] = task_components[0]
    curr_t["title"] = task_components[1]
    curr_t["description"] = task_components[2]
    curr_t["due_date"] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t["assigned_date"] = datetime.strptime(
        task_components[4], DATETIME_STRING_FORMAT
    )
    curr_t["completed"] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)


# ====Login Section====
"""This code reads usernames and password from the user.txt file to 
    allow a user to login.
"""
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", "r") as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(";")
    username_password[username] = password

logged_in = False
while not logged_in:
    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True


while True:
    # presenting the menu to the user and
    # making sure that the user input is converted to lower case.
    print()
    if curr_user == "admin":
        menu = input(
            """Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate reports
ds - Display statistics
e - Exit
: """
        ).lower()
    else:
        menu = input(
            """Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
e - Exit
: """
        ).lower()

    if menu == "r":
        reg_user()

    elif menu == "a":
        add_task()

    elif menu == "va":
        view_all()

    elif menu == "vm":
        view_mine()

    elif menu == "ds" and curr_user == "admin":
        """If the user is an admin they can display statistics about number of users
        and tasks."""

        generate_user_overview(False)
        generate_task_overview(False)

    elif menu == "gr" and curr_user == "admin":
        """If the user is an admin they can generate reports about number of users
        and tasks."""

        generate_user_overview(True)
        generate_task_overview(True)

        print("\nReports generated successfully.")

    elif menu == "e":
        print("Goodbye!!!")
        exit()

    else:
        print("\nYou have made a wrong choice, Please Try again")
