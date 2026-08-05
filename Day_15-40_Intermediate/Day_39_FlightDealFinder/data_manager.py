from base_data_class import BaseDataClass
from env import SHEETY_KEY

class DataManager(BaseDataClass):

    def __init__(self):
        self.url = f"https://api.sheety.co/{SHEETY_KEY}/flightFinder/лист1"


    @property
    def get_url(self) -> str:
        return self.url


    def get_data_from_sheet(self):
        result = self._get(self.url, {}, {})

        self.classify_response(result.status_code)

        return result.json().get("лист1")


if __name__ == "__main__":
    manager = DataManager()
    manager.get_data_from_sheet()