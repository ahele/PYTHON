# def get_artist_info(artist, festival_schedule):
#     if artist in festival_schedule:
#         return festival_schedule[artist]
#     else:
#         return {'message': 'Artist not found'}



# festival_schedule = {
#     "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
#     "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
#     "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
#     "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
# }

# print(get_artist_info("Blood Orange", festival_schedule)) 
# print(get_artist_info("Taylor Swift", festival_schedule))  

'''
A dictionary ticket_sales is used to map ticket type to number of tickets sold. Return the total number of tickets of 
all types sold.
'''

# def total_sales(ticket_sales):
#     return sum(ticket_sales.values())

# ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}
# print(total_sales(ticket_sales))

'''
Demand for your festival has exceeded expectations, so you're expanding the festival to span two different venues. 
Some artists will perform both venues, while others will perform at just one. To ensure that there are no scheduling 
conflicts, implement a function identify_conflicts() that accepts two dictionaries venue1_schedule and venue2_schedule 
each mapping the artists playing at the venue to their set times. Return a dictionary containing the key-value pairs that 
are the same in each schedule.
'''

def identify_conflicts(venue1_schedule, venue2_schedule):
    conflict_schedule = {}
    for artiste, schedule in venue1_schedule.items():
        if (artiste, schedule) in venue2_schedule.items():
            conflict_schedule[artiste] = schedule

    return conflict_schedule

venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

print(identify_conflicts(venue1_schedule, venue2_schedule))
