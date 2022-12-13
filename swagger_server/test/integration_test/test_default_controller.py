from __future__ import absolute_import

import json

from parameterized import parameterized

from swagger_server.test import BaseTestCase


class IntegrationTestFindPhone(BaseTestCase):
    """DefaultController integration test stubs"""

    @parameterized.expand(
        [
            ("Computer History Museum Mountain View USA", "(650) 810-1010"),
            ("Massachusetts Institute of Technology", "(617) 253-1000"),
            ("Library National City", "028 3835 0096"),
        ]
    )
    def test_find_phone_number(self, address, phone_num):
        """Test case for find_phone_number

        Finds phone_number from address
        """
        query_string = [("address", address)]
        response = self.client.open(
            "/getphonenumber", method="GET", query_string=query_string
        )
        data = json.loads(response.data.decode("utf-8"))
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))
        assert data["formatted_phone_number"] == phone_num, (
            address,
            data["formatted_phone_number"],
            phone_num,
        )

    def test_not_empty_address(self):
        query_string = [("address", "")]
        response = self.client.open(
            "/getphonenumber", method="GET", query_string=query_string
        )
        self.assert400(response, "Response body is : " + response.data.decode("utf-8"))

    def test_not_found_address(self):
        query_string = [("address", "this is not exist address")]
        response = self.client.open(
            "/getphonenumber", method="GET", query_string=query_string
        )
        data = json.loads(response.data.decode("utf-8"))
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))
        assert data["formatted_phone_number"] == ""


if __name__ == "__main__":
    import unittest

    unittest.main()
