from datetime import datetime, timedelta
from pprint import pprint

from data_manager import DataManager
from flight_search import FlightSearch


manager = DataManager()
flight_search = FlightSearch()

city_data = manager.get_data_from_sheet()

outbound_date = (datetime.now() + timedelta(weeks=20)).strftime("%Y-%m-%d")
data = []
for city in city_data:
    flights  = flight_search.get_best_flight(arrival_id=city['iataCode'])
    best_three = sorted(flights, key=lambda flight: int(flight.price))[:3]
    data.append(best_three)

pprint(data)

