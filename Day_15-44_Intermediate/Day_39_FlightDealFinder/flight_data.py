from dataclasses import dataclass

@dataclass
class FlightData:
    #This class is responsible for structuring the flight data.
    price: str
    departure_airport: str
    arrival_airport: str
    duration: str
    booking_token: str

    @classmethod
    def from_json(cls, flight: dict, departure_id: str, arrival_id: str) -> 'FlightData':
        return cls(
            price=flight["price"],
            departure_airport=departure_id,
            arrival_airport=arrival_id,
            duration=flight["total_duration"],
            booking_token=flight["booking_token"],
        )