from datetime import datetime, timedelta
from pprint import pprint

from notification_manager import NotificationManager
from data_manager import DataManager
from flight_search import FlightSearch


manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

city_data = manager.get_data_from_sheet()

outbound_date = (datetime.now() + timedelta(weeks=20)).strftime("%Y-%m-%d")
full_data = []
data_for_message = []

for city in city_data:
    flights  = flight_search.get_best_flight(arrival_id=city['iataCode'])
    best_three = sorted(flights, key=lambda flight: int(flight.price))[:3]
    full_data.append(best_three)
    for best in best_three:
        if int(best.price) < int(city['lowestPrice']):
            data_for_message.append({city['city']: best})

    # And if we needed to send a message trough sms
    # message = f"New best deal was found {data_for_message}"
    # notification_manager.send_notification(message=message)

print(data_for_message)
# pprint(full_data)

