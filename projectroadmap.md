# Code:   

[ ]Alarms 

#https://github.com/victor369basu/Intelligent-Alarm-clock-with-todo-list/blob/master/README.md
Intelligent Alarm Clock with ToDo list

#Tanya notes: I ran this semi-successfully once - One of the sound functions didn't work. The later times I ran it, it is pretty buggy and not running. I have downloaded several pips and working through some bypasses/workarounds for files that are not there. But no luck. Is anyone else having better luck? 
This file is not fully open sourced but can be used with the following caveats: 

**Include the Apache 2.0 License with Your Project**
When you distribute your version, include a copy of the Apache License (same as what’s in the original project).

**State Changes Clearly**
If you modify the code, add a note like:
“Modified by Tanya for an ADHD-focused wearable project in 2025.”

**Preserve Notices**
Keep any existing copyright, patent, or attribution notices.

#https://github.com/Pmogi/Alarm-Clock.git

#Tanya notes - this is in Python 2 and required modifications to run in Python 3. Does not connect to the youtube videos as the code states. When you set the alarm, it notes the time every one minute in the terminal. 

#https://github.com/ansh997/Simple-Alarm-Clock-Python
#Tanya notes - This one works! And it comes with a jaunty little ditty. 

[X]Option to add alarms
#Created a new button to open an alarm clock function in another window
#Merged an alarm clock function from another code

[ ]Option to add countdown alarms 

#https://github.com/Jamandalley/AlarmApp
#Elizabeth notes - Parts of the code are functional, but its trajectory doesn’t quite align with the Orbit watch’s path. It’s buggy. It overall does not  deliver on audio notifications and I couldn’t get the font customization to work either.  It does however count down briefly before it freezes. 

[ ]Schedule for future dates 

[ ]Recurring alarms 

[ ]Design Alarm sets 

Morning routine 

Individual tasks 
#https://github.com/cyph3rryx/Python-Reminder-Script
#Elizabeth Notes: text-to-speech would get stuck on second task, updated the code with guidance from https://stackoverflow.com/questions/56032027/pyttsx3-runandwait-method-gets-stuck
#Elizabeth Notes: Was unable to make changes to a task list once it was done or with accidental task entry, added funtion to remove last item and added button and widget between clear tasks and start reminder for optimal flow. This made the list more user friendly. [X]Would like to further explore code to remove selected task in the listbox to make this more user friendly.
#Elizabeth Notes: Was able to successfully remove selected item from within the list box, button and widget were also added. [X]Would want to have option to use enter key to commit a task into the listbox vs having to hoover mouse over the add task button to commit the task into listbox to make this more user friendly.
#Elizabeth Notes: was able to bind enter key with multiple attempts/trouble shooting with guidance from https://stackoverflow.com/questions/16996432/how-do-i-bind-the-enter-key-to-a-function-in-tkinter.[] Would like to review more repositories/code to add button to iterrupt text-to-speech as needed.

Time allotted for each task 
#https://github.com/cyph3rryx/Python-Reminder-Script
#Elizabeth Notes: currently allows interval reminders, was previously set at 3600sec, for the purpose of testing, it was reduced to 1 second.

Evening routine 

Individual tasks 
#https://github.com/cyph3rryx/Python-Reminder-Script

#Kayla Notes: Start Reminder is an audio message " Here are your tasks for the Day". A good start for a Daily Task Function. Currently unable to add tasks within the program, but we might need to add a "get user input" modification or an append option. 
# Kayla Contributions (Sprint 2):
- [x] Added "Motivate Me" button with random affirmations
- [x] Updated background color for accessibility
- [x] Updated font styles across labels and buttons (Helvetica)
- [x] Styled "Motivate Me" button for emphasis
- [x] Updated window title with Orbit Watch branding

Time allotted for each task 

[ ]Turn off alarm 

No Snooze but will repeat alarm if not completed on the watch 

# Timers 
#https://github.com/vikdevelop/timer.git
#Tanya notes - does not work in windows, only on linux devices

#https://github.com/glyph/Pomodouroboros #Amanda's Notes: This is a continuous Pomodoro timer that helps with time blindness.
#Amanda's Notes: Currently only runs on Mac, does not run on Windows or Linux but future plans to do so but no timeline. Has a rough implementation, it may not be suitable for end-users without further development. The codebase might require significant refinement and testing.
#Amanda's Sprint 2 Update: This is more complex than we have time to finish in this project with many files to integrate. We have pivoted on a scope change to leverage the UI we already have working in the task manager and improve the functionality in the pop up window with ways to complete tasks, track completed number of tasks, add additional buttons, change colors, etc.

[ ]From App 

[ ]Set timers for specific tasks 

# Program timers for specific tasks 

# Easy task selection list 

# Amanda's Sprint 2 Contributions:
[X] User should be able to mark tasks complete for positive reinforcement - added button, checkmark, and text turns green - # Amanda's Sprint 2 contribution
[X] User should be able to track total tasks completed that day for positive reinforcement - added variable completed_tasks - # Amanda's Sprint 2 contribution
[X] Audio message when task is completed - added 4 messages that are selected randomly for positive reinforcement when a task is completed # Amanda's Sprint 2 contribution
[X] Audio message when task is completed to state the total number of tasks completed - # Amanda's Sprint 2 contribution
[X] Added 'Mark Task Complete' button and packed the newly added button in the UI # Amanda's Sprint 2 contribution
[X] Added pop up window to tell the user a task has been completed with positive message and how many tasks have been completed - # Amanda's Sprint 2 contribution
[X] Added enhancement to check if the task is already completed, the pop-up window will tell the user that task is already complete. This enhancement avoids the user being allowed to mark a task complete more than once. - Amanda's Sprint 2 contribution
[X] Added 'exercise' to the daily default task list - # Amanda's Sprint 2 contribution

[ ] Progress Bar to visually show progress to user - # Amanda's Sprint 3 contribution

[ ] Daily Reset button so completed tasks are unmarked and total tasks completed counter is reset to zero - # Amanda's Sprint 3 contribution

[ ] Celebration emoji or confetti when user completes all tasks for the day - # Amanda's Sprint 3 contribution

#https://github.com/Aoumjahde/Advanced-To-Do-List-App-with-Python-and-Tkinter

#Elizabeth - For the sake of our project, it seems to have too many windows pop up, creating to much visual clutter for our end user. However, it shouldn’t be discarded as it could help with the app development. One thing I really liked was the ability to edit a list while creating it, and I also appreciated the flexibility of being able to add multiple lists. 
  [] Consider using parts of this code to adjust colors in OrbitReminder.py
  
#  Start timer  

Programmable timer from the watch 

How to add time or activity label? 

Voice activation? 

Touch/type function? 

[ ]Prebuilt Pomodoro Timer 

#https://github.com/AMaheshVardhan/Pomodoro-Timer

#Tanya - runs okay. If you click on Start a second time instead of Reset, the timer starts flipping between work and break without stopping. Resetting the timer at this point does not help. You have to close out of it and start it all over again. 


# App 

[ ]AI to break down large tasks into smaller, simpler tasks 

Assign a designated amount of time the small task should take 

Push to watch 

Needs bluetooth capability 

User Interface to display tasks and alerts, show timer countdown # Amanda's comments https://github.com/sbartoszuk/A-to-D

#Amanda's Notes: It is a GUI built with PyQt5 which could require additional effort to ensure compatibility across platforms, especially when adapting it for the smartwatch integration. It appears to have minimal documentation and lacks a significant user community. This can make it challenging to understand the codebase and troubleshoot issues without external assistance. 
#Amanda's Sprint 2 Update: This is more complex than we have time to finish in this project with many files to integrate. We have pivoted on a scope change to leverage the UI we already have working in the task manager and improve the functionality in the pop up window with ways to complete tasks, track completed number of tasks, add additional buttons, change colors, etc.
