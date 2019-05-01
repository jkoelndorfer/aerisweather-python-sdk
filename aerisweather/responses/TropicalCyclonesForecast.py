from typing import List

from aerisweather.responses.AerisLocation import AerisLocation
from aerisweather.responses.TropicalCyclonesDetails import TropicalCyclonesDetails
from aerisweather.responses.TropicalCyclonesLocation import TropicalCyclonesLocation


class TropicalCyclonesForecast:
    """ Defines an object for the data returned in an Aeris API response."""

    data = {}

    def __init__(self, json_data=None):
        """Constructor - Takes a single response json object from an Aeris API data response. """

        self.data = json_data

    @property
    def location(self) -> TropicalCyclonesLocation:
        return TropicalCyclonesLocation(self.data["location"])

    @property
    def details(self) -> TropicalCyclonesDetails:
        return TropicalCyclonesDetails(self.data["details"])

    @property
    def timestamp(self) -> int:
        return self.data["timestamp"]

    @property
    def dateTimeISO(self) -> str:
        return self.data["dateTimeISO"]

    @property
    def loc(self) -> AerisLocation:
        return AerisLocation(self.data["loc"])
