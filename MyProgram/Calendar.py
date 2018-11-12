'''The program should behave in the following way:Print a welcome message to the user Prompt the user to view, add, update, or delete an event on the calendar Depending on the user's input: view, add, update, or delete an event on the calendar The program should never terminate unless the user decides to exit '''
from time import sleep , strftime

name = "Seema Amola"
calendar = {}

def welcome():
  print "Welcome, "+name+"."
  print "Calendar starting..."
  sleep(1)
  print "Today is:"+ strftime("%A %B %d, %Y")
  print "What would you like to do?"
  
def start_calendar():
  welcome()
  start = True
  
  while start:
    user_choice = raw_input("A to Add, U to Update, V to View, D to Delete, X to Exit: ")
    user_choice = user_choice.upper()
    if user_choice == 'V':
      if len(calendar.keys()) < 1:
        print "Calendar empty."
      else:
        print calendar
        
    elif user_choice == 'U':
      date = raw_input("What date? ")
      update = raw_input("Enter the update: ")
      calendar[date] = update
      print "Update Succesful"
      print calendar
      
    elif user_choice == 'A':
      event = raw_input("Enter event: ")
      date = raw_input("Enter date (MM/DD/YYYY): ")
      if(len(date) > 10 or int(date[6:]) < int(strftime("%Y"))):
        print "Invalid Date "
        try_again = raw_input("Try Again? Y for Yes, N for No: ")
        if try_again == "Y":
          continue
        else:
          start = False
      else:
        calendar[date] = event
        print " Event Added!!"
        
    elif user_choice == "D":
      if len(calendar.keys()) < 1:
        print "Calendar empty."
      else:
        event = raw_input("What event ?")
        for date in calendar.keys():
          if event == calendar[date]:
            del(calendar[date])
            print "Event Deleted Successfully."
          else:
             print "Incorrect Event"
              
    elif user_choice == "X":
        start = False
        
    else:
      print "Invalid Command"
      break
start_calendar()
        
        

      
        

