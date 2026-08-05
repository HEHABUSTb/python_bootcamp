from datetime import datetime, timedelta
from pprint import pprint
from flight_data import FlightData

from base_data_class import BaseDataClass
from env import SERP_API
import serpapi

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.url = r"https://serpapi.com/search.json?engine=google_flights"
        self.departure_id = r"WAW"
        self.client = serpapi.Client(api_key=SERP_API)

    @property
    def get_outbound_date(self) -> str:
        outbound_date = (datetime.now() + timedelta(weeks=1)).strftime("%Y-%m-%d")
        return outbound_date


    def get_best_flight(self, arrival_id: str = "CDG", outbound_date: str = None) -> list[FlightData]:
        if not outbound_date:
            outbound_date = self.get_outbound_date

        results = self.client.search({
            "engine": "google_flights",
            "departure_id": self.departure_id,
            "arrival_id": arrival_id,
            "currency": "PLN",
            "type": "2",
            "outbound_date": outbound_date
        })

        # pprint(results)

        best_flights = results.get("best_flights", [])
        if not best_flights:
            print("No flights found")
            return []
        # pprint(best_flights)

        result = [FlightData.from_json(flight=flight, departure_id=self.departure_id, arrival_id=arrival_id) for flight in best_flights]
        # pprint(result)

        return result



if __name__ == "__main__":
    manager = FlightSearch()
    manager.get_best_flight()

