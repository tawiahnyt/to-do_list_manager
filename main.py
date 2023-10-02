# Function to add a new task to the list
def add_task():
    task_todo = input('Enter the task to add: ')
    tasks.append(task_todo)
    print('Task added successfully!\n')


# Function to display all tasks
def view_tasks():
    print('\nYour To-Do List:')
    print('---------------------------------')
    i = 1
    for task in tasks:
        print(f'{i}. {task}')
        i += 1
    print('---------------------------------\n')


# Function to mark a task as done
def mark_done():
    task_done = int(input('Enter the task number to mark as done: '))
    print(f'Task "{tasks[task_done - 1]}" marked as done!')
    completed_tasks.append(tasks[task_done - 1])
    tasks.remove(tasks[task_done - 1])


# Function to remove a task
def remove_task():
    print('---------------------------------')
    n = 1
    for task in tasks:
        print(f'{n}. {task}')
        n += 1
    print('---------------------------------\n')
    remove = int(input('Enter the task number to remove: '))
    print(f'Task "{tasks[remove - 1]}" has been removed!')
    tasks.remove(tasks[remove - 1])


# Function to display completed tasks
def task_completed():
    print('\nYour Completed To-Dos:')
    print('---------------------------------')
    n = 1
    for completed in completed_tasks:
        print(f'{n}. {completed}')
        n += 1
    print('---------------------------------\n')

# Initialize empty lists to store tasks and completed tasks
tasks = []
completed_tasks = []

# Display a welcome message to the user
print('Welcome to the To-Do List Manager!')

# Variable to control the main program loop
todo = True
while todo:
    # Display the menu options
    print('\n++++++++++++++++++++++++++++++++++')
    print('What would you like to do?')
    print('1. Add Task')
    print('2. View Tasks')
    print('3. Mark Task as Done')
    print('4. Remove Task')
    print('5. View Completed Tasks')
    print('6. Quit')
    print('++++++++++++++++++++++++++++++++++\n')

    # Get the user's choice
    user_choice = int(input('Enter your choice (1/2/3/4/5/6): '))

    # Option 1: Add a new task
    if user_choice == 1:
        add_task()

    # Option 2: View tasks
    elif user_choice == 2:
        view_tasks()

    # Option 3: Mark a task as done
    elif user_choice == 3:
        view_tasks()
        mark_done()

    # Option 4: Remove a task
    elif user_choice == 4:
        remove_task()

    # Option 5: View completed tasks
    elif user_choice == 5:
        task_completed()

    # Option 6: Quit the program
    elif user_choice == 6:
        print('Thank you for using the To-Do List Manager!')
        todo = False

    # Handle invalid input
    else:
        print('Invalid choice! Please try again.')

# End of program
