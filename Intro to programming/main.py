from mod import *
from datetime import datetime

# a list of tuples (flights) containing information on flights
#flights = [] list was synthetically generated by chat GPT for testing purposes. Set flights to empty
flights = []
waitlists = {}
# feedback = {}. this data was generated by Chat GPT for testing purposes. Set feedback to empty before using
feedback = {}

user = {'user_id':5, 'name':'Gulnur', 'surname':'Adanbekova'}
commands = ['create', 'book', 'stats', 'connect', 'profile', 'feedback', 'exit']

print("List of commands: \n profile - to see your profile \n feedback - to rate a flight you have booked \n create - to create a flight \n book - to book a flight \n connect - to find connecting flights bw two cities \n stats - to see statistics, \n exit - to exit the program")
answr = input("Command: ")
answr = answr.lower()

while answr != 'exit':  # while user does not choose to exit the program
    if answr in commands:
        if answr == 'create':
            dep_city = input("Input departure city: ")
            arr_city = input("Arrival city: ")
            n_seats = input("Number of seats available: ")

            x = False
            while x is False: # until the user inputs date in correct format x will be false
                try:
                    dep_time = input("Departure time as 'year-month-day Hour:Minute': ")
                    arr_time = input("Arrival time as 'year-month-day Hour:Minute': ")

                    datetime.strptime(dep_time, "%Y-%m-%d %H:%M")
                    datetime.strptime(arr_time, "%Y-%m-%d %H:%M")
                    x = True

                except:
                    print("Please follow the instructions regarding the format ")
                    x = False

            crt_flight(flights, dep_city, arr_city, dep_time, arr_time, n_seats)
            print("Flight is created successfuly!")
            answr = input("Command: ") # asking for new command
            answr = answr.lower()

        elif answr == 'book':
            print("Available flights are: ")  # print the list of all created flights
            for i in range(len(flights)):
                print("Flight number:", flights[i][0], end='')
                print(", Departure city:", flights[i][1], ", Arrival city:", flights[i][2], ", Departure time:", flights[i][3], sep='', end=' ')
                print(", Arrival time:", flights[i][4], ", Number of seats available:", flights[i][-1], sep='')

            id = int(input("Input a flight ID, which you want to book: "))
            rtrn = book(flights, id, user, waitlists) # calling the function and storing the return value

            if rtrn == 1:
                print("Flight booked sucessfully")
            elif rtrn == 2:
                print("Could not find such flight ID")
            elif rtrn == 0:
                print("No seats available, or available only for passengers from waiting list ")
                yn = input("Do you want to enter waiting list? answer Y or N ") #if no seats are available give option to enter WL

                if yn == 'Y':
                    crt_ret = crt_waitlist(flights, waitlists, id) # if Wl does not exist alredy, create new WL
                    if add_waitlist(waitlists, user, id) == 1:
                        print("You have sucessfully entered waiting list!")
                    else:
                        print("You have already entered waiting list")

            else:
                print(rtrn)
            answr = input("Command: ")
            answr = answr.lower()

        elif answr == 'stats':
            mp = mp_flight(flights)  # calling the function to find MP flight and outputting it
            print("\nThe most popular flight is: ")
            print("Flight number:", flights[mp][0], end='')
            print(", Departure city:", flights[mp][1], ", Arrival city:", flights[mp][2], ", Departure time:", flights[mp][3], end='', sep='')
            print(", Arrival time:", flights[mp][4], ", Number of seats booked:", flights[mp][5], ", Number of seats available:", flights[mp][-1], sep='')

            print('\nThe most popular deprture city is:', mp_city(flights, 0))
            print('The most popular arrival city is:', mp_city(flights, 1))


            answr = input("Command: ")
            answr = answr.lower()

        elif answr == 'connect':
            dep_city = input("Input departure city: ") # ask user input
            arr_city = input("Input arrival city: ")

            # call the function and return its values to user
            connection = connect_flights(dep_city, arr_city, flights)

            if not connection:
                print("No connections for these cities were found :( ")
            else:
                i = 1
                for cnct in connection: # looping through all connections
                    print("Connection number ", i, ":", sep='')
                    for flights in cnct:
                        print(flights)
                    i += 1

                    print("--------")

            answr = input("Command: ")
            answr = answr.lower()


        elif answr == 'profile':
            print("\n\n                 User Profile: ")
            print("Customer Flight ratings: ", round(feedback_a(feedback)))

            for key, value in user.items():
                # check if key is a flight number/an integer
                if isinstance(key, int):
                    print("Flight Number:", key, "  Status:", value)
                else:
                    print(key, " : ", value, sep='')

            answr = input("Command: ")
            answr = answr.lower()

        elif answr == 'feedback':
            # output all booked flights
            # input ID of flight which user wants to rate

            print("You have booked following flights: ")
            booked = []
            for i in user:
                if user[i] == 'booked':
                    booked.append(i)

            if not booked:
                print("You do not have any booked flights")
            else:
                for i in booked:
                    print("Flight number:", flights[i][0], end='')
                    print(", Departure city:", flights[i][1], ", Arrival city:", flights[i][2], ", Departure time:", flights[i][3], sep='', end=' ')
                    print(", Arrival time:", flights[i][4], ", Number of seats available:", flights[i][-1], sep='')

                f_id = input("Which of them do you want to rate? Inout flight ID ")

                if (int(f_id) in booked):
                    X = True
                    while X == True: # ensuing proper usage
                        rating = int(input("Rate the flight on a scale of 0-5: "))
                        if (rating >= 0) and (rating <= 5):
                            X = False

                    fback = input("Comments: ")
                    print("Thank You for your feedback!")
                    feedback[f_id] = [rating, fback]

            answr = input("Command: ")
            answr = answr.lower()
    else:
        answr = input("Command: ")
        answr = answr.lower()
