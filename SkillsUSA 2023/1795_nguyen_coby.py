import csv
import os
import datetime

running = True #for closing the program without having to reopen it for each choice
fieldnames = ["Last Name", "First Name", "Phone Number", "Rate per hour", "Music Style", "Evening Availability", "Event Name", "Start Time", "End Time", "Booked"] #declares the fields

while running:
    selection = int(input("What would you like to do?\n\t1. Add a musician\n\t2. Book an event\n\t3. Close program\n"))

    if selection == 1: #If the user chooses option 1
        os.system('cls')    
        with open("entry.csv", "a", newline="") as csvfile: #opens the csv file in append mode
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames, restval = None, extrasaction = "ignore", dialect = "excel") 
            last_Name = input("Input last name: ").lstrip().rstrip() #takes the inputs for the values to be put into the csv
            first_Name = input("Input first name: ").lstrip().rstrip()
            phone_Number = input("Input phone number: ").lstrip().rstrip()
            rate_Per_Hour = input("Input rate per hour: ").lstrip().rstrip()
            music_Style = input("input music style: ").lstrip().rstrip()
            evening_Availability = input("input evening availability (separated by comma then space)")

            writer.writerow({ #appends the variable names into the next row in the csv file
            "Last Name": last_Name,
            "First Name": first_Name,
            "Phone Number": phone_Number,
            "Rate per hour": rate_Per_Hour,
            "Music Style": music_Style,
            "Evening Availability": evening_Availability,
            })
        os.system("cls")
        with open("entry.csv", "r", newline="") as csvfile: #opens the csv file in read and write mode
            reader = csv.DictReader(csvfile) #Initializes reader
            for row in reader: #for each row (entry) in the file, print these columns
                print(row["First Name"], row["Last Name"], row["Phone Number"], row["Rate per hour"], row["Music Style"], row["Evening Availability"]) #prints the rows

    elif selection == 2: #if the user chooses option 2
        os.system('cls')
        event_Name = input("What is the name of the event?: ").lstrip().rstrip()
        event_Day = input("What is the day of the event? (ex. Thurs, Fri, Sun): ").lstrip().rstrip()
        start_Time = input("What is the start time of the event? (in 24 hour): ").lstrip().rstrip().partition(":")
        end_Time = input("What is the end time of the event? (in 24 hour): ").lstrip().rstrip().partition(":")
        difference = int(end_Time[0]) - int(start_Time[0])

        with open("entry.csv", "r+", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames, restval = "", extrasaction = "ignore") #intializes the writer
            reader = csv.DictReader(csvfile) #Initializes reader
        
            for row in reader:
                if event_Day in row["Evening Availability"] and event_Day not in row["Booked"]:
                    cost = int(row["Rate per hour"].removeprefix("$"))
                    cost *= difference
                    print("\n\t", row["First Name"], row["Last Name"], row["Evening Availability"], "$" + str(cost)) #prints the rows
        
            booked = input("Select a first name of musician to book: ")
            for row in reader:
                if booked in row["First Name"]:
                    writer.writerow({
                        "Event Name": event_Name,
                        "Start Time": start_Time,
                        "End Time": end_Time,
                        "Booked": event_Day
                    })

            for row in reader:
                print("\n\t", row["First Name"], row["Booked"]) #prints the rows                  


    elif selection == 3: #closing the program
        running = False
        os.system('cls')
