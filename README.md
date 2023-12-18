# Flight-Booking
Console based app written in python for airport flight booking

User Manual
	This project is an airport flight booking and analysis system, written on Python. The system handles such operations as creation of flights, booking, waiting lists, flight ratings and provides some analytical features. 
Functions and features:
The user can use the system by running ‘main.py’ in a terminal and access the functionality by inputting commands such as ‘create’, ‘book’, ‘stats’, ‘connect’, ‘profile’, ‘feedback’, and ‘exit’.  
1.	‘create’ – create a flight by inputting flights information, such as departure and arrival cities, departure and arrival time, and number of seats available. The system then stores the flight and assigns a unique ID to it. 
Note that departure and arrival time should be inputted in a specified format: YEAR-MONTH-DAY HOUR:MINUTE. Otherwise, the system will not accept the input. 
2.	‘book’ – book a flight by specifying the ID number of a flight. The command displays all flights in a system and a user can input an ID of a flight to book. If the flight does not have any seats available, the system will give an option to enter a waiting list. 
a.	Waiting list prioritization – if the waiting list exists for a flight, only people from a waiting list are allowed to book the flight.
b.	If the input ID does not exist, the system is exited.
3.	‘stats’ – command shows statistics for:
a.	The most popular flight – based on the number of seats booked.
b.	The most popular departure city – based on the number of flights flying to the departure city.
c.	The most popular arrival city – based on the number of flights flying to the arrival city.
4.	‘connect’ – finds flights for specified departure and arrival cities. The user should enter the name of two cities and the command will output all flights which can be taken. 
a.	If the direct flight exists, the command will return this direct flight only.
b.	If direct flight does not exist, the command will return the list of flights which can be taken with overlay. 
c.	If it is not possible to get from the specified departure city to the destination city, the command displays “No connection for these cities were found ☹”
5.	‘profile’ – shows the user’s information on:
a.	User information such as ID, name, and surname.
b.	User satisfaction – is measured from 0-5 and is based on the feedback that the user had given to flights. If the user had not rated any flights yet, the user satisfaction is 5 by default. 
c.	The command shows the list of all flights, which the user has booked or waitlisted. 
6.	‘feedback’ – the command allows users to leave feedback on flights they have booked. To leave feedback, the user should input the ID of the flight and then leave ratings (0-5) and written comments. 
7.	‘exit’ – enter the command to exit the program.


Project structure
	The project structure consists of 3 major files: ‘mod.py’, ‘main.py’, and this documentation file.  Main.py contains the main parts of the code, which handle user interactions and input, as well as commands calling the functions from mod.py. In addition to the mod.py module, main also imports datetime module for storing departure/arrival time. All data is stored inside the main.py. 
			Data structures used in the main.py for storing information are: 
1.	Flights [] – a list of tuples. All flights are stored in this list, each tuple contains information about each flight. Each flight_id corresponds to the position (index) of the flight tuple inside the flights list. IDs begin from 0-n.
flights = [(flight_id, departure_city, arrival_city, departure_time, arrival_time, number_of_seats_booked, number_of_seats_available)]
2.	Waitlists {} – a dictionary containing flight ID as a key and list of users waitlisted for the flight as a value. 

waitlists = {flightID : [ user_id, user_id, user_id]} 
Ex: waitlists = {21:[2, 5, 7]} Here for the flight with ID 21, three users with ID’s 2,  5, and 7 are waitlisted. 

3.	Feedback {} – is a dictionary containing flight ID as a key and list of feedback as a value. The feedback dictionary stores the feedback of the single user for multiple flights. 
feedback = {flightID : [rating(0-5), “written comment”]} 
4.	User {} – a dictionary containing information of a user and their booked and waitlisted flights. The dict is updated each time user books or WL’s flight. 
user = {‘user_id’: userID, ‘name’ : ‘Name’, ‘surname’ : ‘Surname’, flightID: ‘booked’, flightID: ‘waiting list’}
5.	Commands [] – a list of commands, which user can execute. This list should not be changed. 

commands = ['create', 'book', 'stats', 'connect', 'profile', 'feedback', 'exit'] 

Mod.py – is a module containing functions used in the program. These functions include: crt_flight, book, crt_waitlist, add_waitlist, mp_flight, mp_city, feedback_a, connect_flights.  
1.	crt_flight(flights, dep_city, arr_city, dep_time, arr_time, n_seats)
Add a new flight to the list of flights. This function creates a flight and appends it to the list of flights inputed. It also assigns ID numbers based on the position of te new flight in the list

2.	book(flights, id, user, waitlists)
the function books a flight by flight ID. This function checks existing fights and then based on the ID of the flight makes a reservation. The function also adds the reservation to the user profile.

3.	crt_waitlist(flights, waitlists, id)
crt_waitlist creates a waitlist for flight. The function creates a waitlist for the flight based on the fligth number (ID) and appends it to the dict of waitlists. Waitlist is only created when the number of seats available is 0

4.	add_waitlist(waitlists, user, id)
the function adds a user to the existing waiting list

5.	mp_flight(flights)
the function returns the most popular flight based on number of booked seats

6.	mp_city(flights, mode)
 the function returns the most popular city based on either number of arrivals or departures

7.	connect_flights(dep_city, arr_city, flights)
the function returns connected flights between two cities with a single layover. The function seaches first and returns the direct connection of flights. However, if there is no direct connection, it returns list of connections with minimum number of layovers. The function, except for the docstring and minor changes, was entirely generated by Chat GPT

8.	feedback_a(feedback)
the function shows the satisfaction level of a customer by analyzing their feedback on flights they booked. The satisfaction level is measured on a scale from 0-5


Assignment work distribution: 
	This assignment was written without a team, so all the work was done by me. In addition to that, where cited, some of the code and testing data was written with the help of Chat GPT. 

Testing: 
	To test the program, execute main.py in the terminal window. Test data is provided in the code

