# 1st task
def crt_flight(flights, dep_city, arr_city, dep_time, arr_time, n_seats):
    """
    Add a new flight to the list of flights

    This function creates a flight and appends it to the list of flights inputed.
    It also assigns ID numbers based on the position of te new flight in the list

    (list), (string), (string), (date), (date), (int) --> (list(tuple))
    tuple = (id, departure_city, arrival_city, departure_time, arrival_time, number_of_seats)
    Example of usage:
        >>> flights = []
        >>> flights = crt_flight(flights, 'new_york', 'tokyo', '10:00', '20:00', 100)
        >>> print(flights)
        >>> [(0, 'new_york', 'tokyo', '10:00', '20:00', 100)]
    """
    # id is equal to the position in list of flights
    flight_id = len(flights)
    flight = (flight_id, dep_city, arr_city, dep_time, arr_time, 0, n_seats)

    # return appended flights list
    flights.append(flight)
    return flights


# 2nd task
def book(flights, id, user, waitlists):
    """ the function books a flight by flight ID

    This function checks existing flights and then based on the ID of the flight makes a reservation.
    The function also adds the reservation to the user profile.

    (list of flights), (flight_id), (user dict), (list of WL) --> (integer) #possible add user profile list too later for todo

    Return values:
        1: Returns 1 when the booking was successful
        2: Returns 2 if provided ID does not exist inside the flights list
        0: Returns 0 when if no seats are available for booking or only people from WL are accepted

    >>> flights = [(0, 'new_york', 'tokyo', '10:00', '20:00', 100)]
    >>> print(book(flights, 0))
    >>> 1

    """
    try: # try case for checking if ID index is valid, if not returns 2
        if id in flights[id]:  # checking if ID exists and is valid
            if int(flights[id][-1]) > 0: # checking if the seats are available
                # checking if the waitlist for this flight exists
                wl_id = 'X'
                if id in waitlists:
                    # if the Wl exist checking if user is inside of it
                    if user['user_id'] in waitlists[id]:
                        # decrease the N of seats available by 1 and increase the number of seats booked
                        new_nseat = int(flights[id][-1]) - 1
                        new_booked = int(flights[id][5]) + 1
                        flights[id] = (flights[id][0], flights[id][1], flights[id][2], flights[id][3], flights[id][4], new_booked, new_nseat)

                        user[id] = 'booked'
                        waitlists[id].remove(user['user_id'])
                        return 1
                    else:
                        return 0

                if wl_id == 'X': # if WL for this flight does not exist
                    # decrease the N of seats available by 1
                    new_nseat = int(flights[id][-1]) - 1
                    new_booked = int(flights[id][5]) + 1
                    flights[id] = (flights[id][0], flights[id][1], flights[id][2], flights[id][3], flights[id][4], new_booked, new_nseat)

                    user[id] = 'booked'
                    return 1
            else:
                return 0
    except Exception as e:
        print(e)
        return 2


def crt_waitlist(flights, waitlists, id):
    """ crt_waitlist creates a waitlist for flight.

    the function creates a waitlist for the flight based on the fligth number (ID)
    and appends it to the dict of waitlists.
    waitlist is only created when the number of seats available is 0

    (list of fligths), (dict of waitlists), (int) -> (integer)

    waitlists = {flight_id:[]} # user_id should be added later by add_waitlist()

    Returns:
        1: Returns 1 when the waiting list was create sucessfully
        0: Returns 0 when number of available seats does not equal 0
        3: IF for the flight WL aready exists, the function does not append WLs and returns 3

    >>> waitlists = {}
    >>> flights = [(0, 'new_york', 'tokyo', '10:00', '20:00', 0)]
    >>> print(crt_waitlist(flights, waitlists, 0))
    >>> 1
    >>> print(waitlists)
    >>> {0: []}

    """

    wl = []  # create an empty waiting list to return it later
    # check wehther the fligth already has a WL
    if id in waitlists:
                return 3

    if flights[id][-1] == 0: # check if number of seats is equal to 0
        # append the dictionary
        waitlists[id] = []
        return 1
    else:
        return 0



def add_waitlist(waitlists, user, id):
    """ the function adds a user to the existing waiting list

    (list of WLs), (flight ID), (user dict) --> (int)

    Return values:
        0: Returns 0 if the user is already inside of WL
        1: Returns 1 if the user was sucessfully added to the WL

    >>> waitlists = {}
    >>> add_waitlist(wls, 1, 5)
    >>> {1: [5]}
    """
    # check if user is already in WL
    if int(user['user_id']) in waitlists[id]:
        return 0
    else:
        # append the WL by user ID
        waitlists[id].append(user['user_id'])

        # add waiting list info to the user's profile dict
        user[id] = 'waiting list'
        return 1




# flight analysis fnctions
def mp_flight(flights):
    """ the function returns the most popular flight based on number of booked seats

    (list of flights) -> (flight id)

    >>> mp_flight(flights)
    >>> 19
    >>> print(flights[19])
    >>> (19, "Miami", "Tokyo", "2023-10-15 15:45", "2023-10-15 23:45", 80, 20)

    """
    # find the max number of seats book max(flights[id][5])
    # store each number of seats booked in a new dict

    fmax = {}
    for i in range(len(flights)):
        fmax[flights[i][0]] = flights[i][5]

    # the following code was genreated by Chat GPT
    max_key = 0
    max_value = 0
    for key, value in fmax.items():
        if value > max_value:
            max_key = key
            max_value = value

    # return max key which corresponds to the flight ID with the maximum number of seats booked
    return max_key

def mp_city(flights, mode):
    """ the function returns the most popular city based on either number of arrivals or departures

    (list of flights), (bool) -> (string)

    Enter 1 or 0 in 'mode' parameter to get:
        True (1) - Arrival City
        False (0) - Departure City
    >>> flights = [
    (0, "New York", "Los Angeles", "2023-10-15 08:00", "2023-10-15 11:00", 50, 0),
    (1, "Miami", "Chicago", "2023-10-15 12:30", "2023-10-15 15:30", 30, 70),
    (2, "Miami", "New York", "2023-10-15 16:45", "2023-10-15 19:45", 40, 60),
    (3, "San Francisco", "Los Angeles", "2023-10-15 09:15", "2023-10-15 10:45", 20, 80),
    (4, "Miami", "London", "2023-10-15 14:00", "2023-10-15 20:00", 75, 25),
    (5, "Los Angeles", "New York", "2023-10-15 10:30", "2023-10-15 13:30", 35, 65)]
    >>> print(mp_city(flights, 1))
    >>> Los Angeles
    >>> print(mp_city(flights, 0))
    >>> Miami
    """
    if mode == 1: # if mode is 1, then it is Arrival city position
        mode = 2 # 2 is position of arrival city in flights list
    elif mode == 0:
        mode = 1
    else:
        return 'mode error'

    # create a dict where you store city as a key and count of instances as a value
    cities = {}
    for i in range(len(flights)):
        if flights[i][mode] in cities:
            cities[flights[i][mode]] += 1
        else:
            cities[flights[i][mode]] = 1

    max_key = 0
    max_value = 0
    for key, value in cities.items():
        if value > max_value:
            max_key = key
            max_value = value
    return max_key

# task 4
# this function was written using Chat GPT
def connect_flights(dep_city, arr_city, flights):
    """ the function returns connected flights between two cities with a single layover.

    The function seaches first and returns the direct connection of flights. However,
    if there is no direct connection, it returns list of connections with minimum number of layovers
    The function, except for the docstring and minor changes, was entirely generated by Chat GPT

    (string), (string), (list of flights) --> (list of connections)

    >>> flights = [
    (0, "New York", "Los Angeles", "2023-10-15 08:00", "2023-10-15 11:00", 50, 0),
    (1, "Miami", "Chicago", "2023-10-15 12:30", "2023-10-15 15:30", 30, 70),
    (2, "Miami", "New York", "2023-10-15 16:45", "2023-10-15 19:45", 40, 60),
    (3, "San Francisco", "Los Angeles", "2023-10-15 09:15", "2023-10-15 10:45", 20, 80),
    (4, "Miami", "London", "2023-10-15 14:00", "2023-10-15 20:00", 75, 25),
    (5, "Los Angeles", "Miami", "2023-10-15 10:30", "2023-10-15 13:30", 35, 65)]
    >>> print(connect_flights('New York', 'Miami', flights))
    >>> [[(0, 'New York', 'Los Angeles', '2023-10-15 08:00', '2023-10-15 11:00', 50, 0),
    (5, 'Los Angeles', 'Miami', '2023-10-15 10:30', '2023-10-15 13:30', 35, 65)]]

    Here, the function returned a list, containing two lfights, which can be taken to get from New York to Miami
    """

    direct_flights = []

    # Check for direct flights
    for flight in flights:
        if flight[1] == dep_city and flight[2] == arr_city:
            direct_flights.append(flight)

    if direct_flights:
        return direct_flights

    connecting_flights = []

    for flight1 in flights:
        if flight1[1] == dep_city:
            for flight2 in flights:
                if flight2[2] == arr_city and flight1[2] == flight2[1]:
                    connecting_flights.append([flight1, flight2])

    return connecting_flights



# last taks: analyzing feedback

def feedback_a(feedback):
    """ the function shows the satisfaction level of a customer by analyzing their feedback
    on flights they booked. The satisfaction level is measured on a scale from 0-5

    (dictionary) -> (float)

    >>> feedback = {
    0: [5, "I am very happy with this flight. The service was excellent!"],
    1: [4, "Great flight overall, no complaints."],
    2: [5, "The crew was friendly and professional."],
    3: [2, "My luggage was damaged during the flight."]}
    >>> print(feedback_a(feedback))
    >>> 4.0

    """
    if not feedback:
        return 5
    # sum up all values of the list
    sum = 0
    len = 0
    for key, value in feedback.items():
        sum += int(value[0])
        len += 1

    # find average and return it
    return sum/len

