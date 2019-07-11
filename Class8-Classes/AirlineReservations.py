flight_1 = {'from_to': 'Washington DC to New York Direct', 'adult': 250, 'kid': 125}
flight_2 = {'from_to': 'Washington DC to New York 1 Stop', 'adult': 150, 'kid': 100}
flight_3 = {'from_to': 'Washington DC to Charlotte Direct', 'adult': 200, 'kid': 150}
flights = {'flight_1': flight_1, 'flight_2': flight_2, 'flight_3': flight_3}

print("Choose one of the flights using the id: ")
for key,values in flights.items():
    from_to = values.get('from_to')
    adult_price = values.get('adult')
    kid_price = values.get('kid')
    print("The id is : " + key + " and flight is : " + from_to + " adult price is : " + str(adult_price) + ", kid price: " +str(kid_price
                                                                                                                                ))
input_flight_id = input('Which flight id?')
flight_details = flights.get(input_flight_id)
customers = input("How many customers are flying?")
kids = input("How many of them are kids(below 18)?")
adult_count = int(customers) - int(kids)
print('Please give name of the adults ')

