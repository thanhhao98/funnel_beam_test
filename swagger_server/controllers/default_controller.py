import os
import requests
from typing import List

from swagger_server.models.phone_number import PhoneNumber  # noqa: E501


G_API_KEY = os.environ.get("G_API_KEY", "")
G_API = "https://maps.googleapis.com/maps/api/place/"


class FindPhoneFromAddr:
    def __init__(self, g_api_key):
        self.url_find_place_id = (
            G_API
            + "findplacefromtext/json?input={address}&inputtype=textquery&fields=place_id&key={api_key}"
        )
        self.url_find_phone_number = (
            G_API
            + "details/json?place_id={place_id}&fields=formatted_phone_number&key={api_key}"
        )
        self.G_API_KEY = g_api_key
        self.space_formatted = "%20"

    def get_plids(self, address: str) -> List[str]:
        formatted_address = self.space_formatted.join(address)
        full_url = self.url_find_place_id.format(
            address=formatted_address, api_key=self.G_API_KEY
        )
        response = requests.request("GET", full_url, headers={}, data={})
        self.handle_err("get_place_id_from_address", response)
        return list(map(lambda i: i["place_id"], response.json()["candidates"]))

    def get_phn_fid(self, place_id: str) -> str:
        full_url = self.url_find_phone_number.format(
            place_id=place_id, api_key=self.G_API_KEY
        )
        response = requests.request("GET", full_url, headers={}, data={})
        self.handle_err("get_phonenum_from_place_id", response)
        return response.json()["result"]["formatted_phone_number"]

    def handle_err(self, fun_name: str, response: requests.Response) -> None:
        if response.status_code != 200:
            raise Exception(
                "{fun_name}: Fail to call to google_api, status_code: {status_code}".format(
                    fun_name=fun_name, status_code=response.status_code
                )
            )
        status = response.json()["status"]
        if status not in ["OK", "ZERO_RESULTS"]:
            raise Exception(
                "{fun_name}: Fail to get place_id, status: {status}".format(
                    fun_name=fun_name, status=status
                )
            )

    def __call__(self, address: str, get_first_candidate: bool = True) -> str:
        place_ids = self.get_plids(address)
        if not len(place_ids):
            return ""

        # define which candidates we will choose if we have multiple place_id
        if get_first_candidate:
            place_id = place_ids[0]
        else:
            place_id = place_id[0]
        return self.get_phn_fid(place_id)


g_find_phone_from_addr = FindPhoneFromAddr(G_API_KEY)


def find_phone_number(address):  # noqa: E501
    """Finds phone_number from address

     # noqa: E501

    :param address: address for query and getting phone_number
    :type address: str

    :rtype: InlineResponse200
    """
    address = address.split()
    if not len(address):
        return "Address is not valid", 400
    return PhoneNumber(g_find_phone_from_addr(address)), 200
