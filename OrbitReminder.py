import tkinter as tk
import pyttsx3
import datetime
import time
import random # We needed to add this to support Kayla's motivational phrases, randomization
#Tanya: added import for Messagebox
from tkinter import messagebox
from playsound import playsound
#Tanya: added import for playsound to play alarm sound
# Amanda: added to create task progress bar (show progress visually)
from tkinter import ttk

# Set up the text-to-speech engine
engine = pyttsx3.init()

# Create a list to store the daily tasks
tasks = ["wake", "eat", "work", "eat", "exercise","sleep"]
# test

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

def say_words(task):
    #Elizabeth Notes: runAndWait() not fully working as it would get stuck on second thing said, used https://stackoverflow.com/questions/56032027/pyttsx3-runandwait-method-gets-stuck
    engine = pyttsx3.init()
    engine.say(task)
    engine.runAndWait()
    del(engine) 

# Amanda: Added variable to track completed tasks
completed_tasks = 0

# Amanda: function to mark the task as complete for positive reinforcement
def mark_task_complete():
    global completed_tasks
    selection = task_list.curselection()
    if selection:
        index = selection[0]  # Amanda: Get the index of the selected task
        task = task_list.get(index)  # Amanda: Get the task text

         # Check if task is already completed
        if task.startswith("✔️"):
            messagebox.showinfo("Already Completed", "This task has already been completed!")
            return

        # Amanda: Update the completed task visually with a checkmark
        completed_task = f"✔️ {task}"
        task_list.delete(index)
        task_list.insert(index, completed_task)

         # Amanda: Added to visually indicate task completion
        task_list.itemconfig(selection, {'fg': 'green'})  # Amanda: Change text color to green when task is completed
        # Amanda: Increment completed task counter
        completed_tasks += 1

         # Amanda: Update the progress bar to show the percentage of tasks completed
        total_tasks = task_list.size()
        if total_tasks > 0:
            progress["value"] = (completed_tasks / total_tasks) * 100
        else:
            progress["value"] = 0

        # Amanda: Added to have the voice in the app to say the task is completed and the total number of tasks completed for the day. Multiple messages are randomly selected from the list for positive reinforcement.
        messages = [
            f"Great job! You've completed {completed_tasks} task{'s' if completed_tasks > 1 else ''} today!",
            f"Congratulations! {completed_tasks} task{'s' if completed_tasks > 1 else ''} done!",
            f"Awesome work! Keep going, {completed_tasks} task completed!",
            f"You're on fire! {completed_tasks} tasks finished!"
        ]
        message = random.choice(messages)
        # Amanda: Audio says the message out loud to the user for positive reinforcement
        say_words(message)
        # Amanda: Pop-up window to show a message box with the positive reinforcement message of number of completed tasks
        messagebox.showinfo("Task Completed", message)

        # Amanda: If all tasks are completed (all start with ✔️), trigger celebration
        all_completed = True
        for i in range(task_list.size()):
            if not task_list.get(i).startswith("✔️"):
                all_completed = False
                break

        if all_completed and task_list.size() > 0:
            celebrate_confetti()
    else:
        messagebox.showwarning("No Selection", "Please select a task to mark as complete.")

# Amanda: Confetti Animation (fun reward when ALL tasks completed)
def celebrate_confetti():
    confetti_window = tk.Toplevel(window)
    confetti_window.title("🎉 Celebration!")
    confetti_window.geometry("300x200")
    confetti_window.configure(bg="white")

    confetti_label = tk.Label(confetti_window, text="🎉🎊🎉 YOU DID IT! 🎉🎊🎉", font=("Helvetica", 16), bg="white", fg="green")
    confetti_label.pack(expand=True)

# Create a function to run the reminder at regular intervals
def run_reminder():
    #while True:
        remind()
        #time.sleep(interval)

# Create the main window
window = tk.Tk()
window.configure(bg="#F0F8FF")  # Kayla -changed background color to Light calming blue
window.title("Orbit Watch - ADHD Task Manager")  # Kayla - changed title to Orbit Watch - 5th commit was included in last commit, not listed separtely

# Create a function to add a new task to the list
#Elizabeth note: adjusting function to give option to use enter key to add task to listbox
def add_task(event=None):
    task = task_entry.get()
    tasks.append(task)
    task_list.insert(tk.END, task)

# Create a function to clear all tasks from the list
def clear_tasks():
    tasks.clear()
    task_list.delete(0, tk.END)

def delete_selection():
    #ElizabethNotes: delete from Listbox
    selection = task_list.curselection()
    task_list.delete(selection)
    tasks.pop(selection[0])  # selection is a tuple with one member
    
def remove_last_task():
    #ElizabethNotes: remove last task in listbox 
    tasks.pop()
    task_list.delete(tk.END, tk.END)

#Tanya: Adding speak to text function for the alarm clock

def speak_text(text):
    engine.say(text)
    engine.runAndWait()


#Tanya: Adding an alarm clock feature, merged from alarm-GUI.py
#Alarm clock function
#tweaked alarm so that it does not reopen over and over again after hitting the close button
def run_alarm_clock():
    alarm_window = tk.Toplevel(window)
    alarm_window.title("Alarm Clock")
    
    frame1 = tk.Frame(alarm_window)
    frame1.pack(padx=10, pady=10)

    label1 = tk.Label(frame1, text="Enter the Alarm Time (HH:MM):", font=("Helvetica", 12))  # Kayla - changed font
    label1.pack()

    entry1 = tk.Entry(frame1, width=30)
    entry1.pack()
    entry1.insert(0, "example - 13:15")

    labelAlarmMessage = tk.Label(frame1, text="Alarm Message:",font=("Helvetica", 12))  # Kayla - changed font
    labelAlarmMessage.pack()

    entry2 = tk.Entry(frame1, width=30)
    entry2.pack()

    label2 = tk.Label(frame1, font=("Helvetica", 12))  # Kayla - changed font
    label2.pack()

    def check_alarm(alarm_time):
        if not alarm_window.winfo_exists():
            return  # Stop checking if window closed

        current_time = time.strftime("%H:%M")
        if alarm_time == current_time:
            print("Now Alarm Music Playing")
            try:
                playsound('super_low_tone.wav')  # Play your soft tone here
            except Exception as e:
                print("Could not play sound:", e)
            label2.config(text="Alarm music playing...")
            message = entry2.get()
            messagebox.showinfo(title='Alarm Message', message=message)
            speak_text(message)
        else:
            alarm_window.after(1000, lambda: check_alarm(alarm_time))  # Keep checking every second

    def SubmitButton():
        alarm_time = entry1.get()
        label2.config(text="The alarm is counting...")
        messagebox.showinfo(title='Alarm Clock', message=f'Alarm will ring at {alarm_time}')
        check_alarm(alarm_time)  # Start checking the alarm time

    button1 = tk.Button(frame1, text="Set Alarm", command=SubmitButton, font=("Helvetica", 12))  # Kayla - changed font
    button1.pack(pady=5)


# Create a label and entry field for adding new tasks
task_label = tk.Label(window, text="Enter a new task:", font=("Helvetica", 12))  # Kayla - changed font
task_entry = tk.Entry(window)

# Create a button for adding tasks
add_button = tk.Button(window, text="Add Task", command=add_task, font=("Helvetica", 12))  # Kayla - changed font

# Create a listbox for displaying the tasks
task_list = tk.Listbox(window)

#Create a button for clearing all tasks
clear_button = tk.Button(window, text="Clear Tasks", command=clear_tasks, font=("Helvetica", 12))  # Kayla - changed font

#Create a button for clearning selected task in listbox
delete_selection_button=tk.Button(window, text="Remove selection", command=delete_selection, font=("Helvetica", 12))  # Kayla - changed font

# Create a button for clearing last task
remove_last_task_button = tk.Button(window, text="Remove Last", command=remove_last_task, font=("Helvetica", 12))  # Kayla - changed font

# Create a button for starting the reminder loop
start_button = tk.Button(window, text="Start Reminder", command=run_reminder, font=("Helvetica", 12))  # Kayla - changed font

#Tanya: Create a button for starting the alarm clock
open_alarm_button = tk.Button(window, text="Start Alarm Clock", command=run_alarm_clock, font=("Helvetica", 12))  # Kayla - changed font

# Amanda: Create a button for marking task as complete
mark_complete_button = tk.Button(window, text="Mark Task Complete", command=mark_task_complete, font=("Helvetica", 12))

# Amanda: Create a Progress Bar widget
progress = ttk.Progressbar(window, orient="horizontal", length=300, mode="determinate")
progress.pack(pady=10)

# Elizabeth notes: binding code 
window.bind('<Return>', add_task)

# Pack the widgets into the window
task_label.pack()
task_entry.pack()
add_button.pack()
task_list.pack()
clear_button.pack()
delete_selection_button.pack()#Elizabeth note: added button to remove selected task
remove_last_task_button.pack()#Elizabeth note: added button to remove last task
mark_complete_button.pack()  # Amanda: Added to pack the button for marking task as complete
start_button.pack()
open_alarm_button.pack()

#Kayla - add a "Motivate Me! Button"
def motivate():
    phrases = [
        "You're doing great!",
        "One step at a time!",
        "Keep it up, champion!",
        "You're making real progress!"
    ]
    message = random.choice(phrases)
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()
# Create a button for motivation
motivate_button = tk.Button(window, text="Motivate Me!", command=motivate, bg="#90EE90", font=("Helvetica", 12, "bold italic")) # Kayla - changed button color, bold and italic font
motivate_button.pack()



#initialize listbox with tasks
for task in tasks:
    task_list.insert(tk.END, task)
    
    #maybe add interval in the remind loop 

    
# Run the main loop
window.mainloop()