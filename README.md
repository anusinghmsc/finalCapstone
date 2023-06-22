# Table of Contents
- [Table of Contents](#table-of-contents)
- [Task Manager](#task-manager)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Login](#login)
  - [Menu](#menu)
  - [Register user](#register-user)
  - [Add Task](#add-task)
  - [View all tasks](#view-all-tasks)
  - [Generate Report](#generate-report)
  - [Task Overview report](#task-overview-report)
  - [User Overview report](#user-overview-report)
  - [Display Statistics](#display-statistics)
  - [View my task](#view-my-task)
  - [Exit](#exit)
  - [Credits](#credits)

# Task Manager

The program provides the below features to manage assigned tasks:
- Registering a user
- Adding a task
- View all tasks
- View my task
- Edit uncompleted tasks
- Generate reports
- Display statistics



## Installation

- Download Python Executable Installer from this [link](https://www.python.org/downloads/) and install it
- Wait for the installation process to complete
- Verify installation of python by running `python --version` in your command prompt or terminal
- Clone the github repository
- To run the program, go inside `finalCapstone` folder of the cloned repository and run `py task_manager.py`


## Usage

After running, program asks for login as below:

## Login

```
LOGIN
Username: admin
Password: password
Login Successful!
```

and provides the below menu to admin:

## Menu

```
Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate reports
ds - Display statistics
e - Exit
```

We can register user as shown below:

## Register user

```
Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate reports
ds - Display statistics
e - Exit
: r
New Username: test
New Password: password
Confirm Password: password

New user added
```

It provides below options to create and assign task:

## Add Task

```
Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate reports
ds - Display statistics
e - Exit
: a

Name of person assigned to task: test
Title of Task: sample title
Description of Task: sample description
Due date of task (YYYY-MM-DD): 2023-11-11

Task successfully added.

Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate reports
ds - Display statistics
e - Exit
: a

Name of person assigned to task: admin
Title of Task: task for admin
Description of Task: details of admin task
Due date of task (YYYY-MM-DD): 2023-08-08

Task successfully added.
```

Further all tasks can be viewed as below:

## View all tasks

```
Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate reports
ds - Display statistics
e - Exit
: va

-------------------------------  0  -------------------------------
Task:                    sample title
Assigned to:             test
Date Assigned:           22 Jun 2023
Due Date:                11 Nov 2023
Task Complete?:          No
Task Description: 
 sample description


-------------------------------  1  -------------------------------
Task:                    task for admin
Assigned to:             admin
Date Assigned:           22 Jun 2023
Due Date:                08 Aug 2023
Task Complete?:          No
Task Description:
 details of admin task
```

Report can be generated as below

## Generate Report

```
Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate reports
ds - Display statistics
e - Exit
: gr

Reports generated successfully.
```

## Task Overview report

> task_overview.txt

```
--------------------------------------------------------------------------------
Number of tasks                             	: 2
Number of completed tasks                  		: 0
Number of uncompleted tasks                		: 2
Number of uncompleted overdue tasks        		: 0
Percentage of incomplete tasks               	: 100.00
Percentage of overdue tasks                  	: 0.00
--------------------------------------------------------------------------------
```

## User Overview report

> user_overview.txt

```
------------------------------------------------------------------------------------------------------------
Number of users                		: 2
Number of tasks                		: 2
------------------------------------------------------------------------------------------------------------
User : admin
	Number of tasks                                                     	: 1
	Percentage of tasks assigned to user                                 	: 50.00
	Percentage of assigned tasks that are completed                      	: 0.00
	Percentage of assigned tasks that must be completed                  	: 100.00
	Percentage of assigned tasks that are not completed and are overdue  	: 0.00
------------------------------------------------------------------------------------------------------------
User : test
	Number of tasks                                                     	: 1
	Percentage of tasks assigned to user                                 	: 50.00
	Percentage of assigned tasks that are completed                      	: 0.00
	Percentage of assigned tasks that must be completed                  	: 100.00
	Percentage of assigned tasks that are not completed and are overdue  	: 0.00
------------------------------------------------------------------------------------------------------------
```

Statistics can be displayed as below:

## Display Statistics

```
Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate reports
ds - Display statistics
e - Exit
: ds

-----------------------------------
Number of users:                 2
Number of tasks:                 2
-----------------------------------
```

Tasks specific to user can viewed and edited as below: 

## View my task

```
Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate reports
ds - Display statistics
e - Exit
: vm

-------------------------------  0  -------------------------------
Task:                    task for admin
Assigned to:             admin
Date Assigned:           22 Jun 2023
Due Date:                08 Aug 2023
Task Complete?:          No
Task Description:
 details of admin task


Do you want to mark the task as complete or edit the task.
(-1 : return to the main menu)
Please provide the specific task number : 0

Select one of the edit Options below:
y - mark the task complete
u - edit the username of the person to whom selected task is assigned
d - edit the due date of the selected task
-1 - return to the main menu
:
```

Finally program can existed using below option:

## Exit

```
Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate reports
ds - Display statistics
e - Exit
: e
Goodbye!!!
```

## Credits

This program was created by [Anu Singh](https://www.linkedin.com/in/anu-singh-msc/)