import tkinter as tk
import pyttsx3
import datetime
import time

# Set up the text-to-speech engine
engine = pyttsx3.init()

# Create a list to store the daily tasks
tasks = ["wake", "eat", "work", "eat","sleep"]

# Set the interval for the reminder (in seconds)
interval = 1  

# Create a function to remind the user of their tasks
def remind():
    # Get the current time
    now = datetime.datetime.now()

    # Check if it is morning, afternoon, or evening
    if now.hour < 12:
        greeting = "Good morning! Here are your tasks for the day:"
    elif now.hour < 18:
        greeting = "Good afternoon! Here are your tasks for the day:"
    else:
        greeting = "Good evening! Here are your tasks for the day:"

    # Speak the greeting and list of tasks
    
    say_words(greeting)
    for task in tasks:
      say_words(task)
#maybe add interval in this loop?
#or figure out how to remove selected
#enter to commit task to listbox

def say_words(task):
    #Elizabeth Notes: runAndWait() not fully working as it would get stuck on second thing said, used https://stackoverflow.com/questions/56032027/pyttsx3-runandwait-method-gets-stuck
    engine = pyttsx3.init()
    engine.say(task)
    engine.runAndWait()
    del(engine) 
        
# Create a function to run the reminder at regular intervals
def run_reminder():
    #while True:
        remind()
        #time.sleep(interval)

# Create the main window
window = tk.Tk()
window.title("Daily Task Reminder")

# Create a function to add a new task to the list
def add_task():
    task = task_entry.get()
    tasks.append(task)
    task_list.insert(tk.END, task)

# Create a function to clear all tasks from the list
def clear_tasks():
    tasks.clear()
    task_list.delete(0, tk.END)

def delete_selection():
    #delete from Listbox
    selection = task_list.curselection()
    task_list.delete(selection)
    tasks.pop(selection[0])  # selection is a tuple with one member
    
def remove_last_task():
    tasks.pop()
    task_list.delete(tk.END, tk.END)
    
# Create a label and entry field for adding new tasks
task_label = tk.Label(window, text="Enter a new task:")
task_entry = tk.Entry(window)

# Create a button for adding tasks
add_button = tk.Button(window, text="Add Task", command=add_task)

# Create a listbox for displaying the tasks
task_list = tk.Listbox(window)

# Create a button for clearing all tasks
clear_button = tk.Button(window, text="Clear Tasks", command=clear_tasks)

#Create a button for clearning selected task in listbox
delete_selection_button=tk.Button(window, text="Remove selection", command=delete_selection)

# Create a button for clearing last task
remove_last_task_button = tk.Button(window, text="Remove Last", command=remove_last_task)

# Create a button for starting the reminder loop
start_button = tk.Button(window, text="Start Reminder", command=run_reminder)

# Pack the widgets into the window
task_label.pack()
task_entry.pack()
add_button.pack()
task_list.pack()
clear_button.pack()
delete_selection_button.pack()#Elizabeth note: added button to remove selected task
remove_last_task_button.pack()#Elizabeth note: added button to remove last task
start_button.pack()


#initialize listbox with tasks
for task in tasks:
    task_list.insert(tk.END, task)
    
    #maybe add interval in the remind loop 

    
# Run the main loop
window.mainloop()
