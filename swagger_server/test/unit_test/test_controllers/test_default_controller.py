from unittest import mock

from swagger_server.controllers.default_controller import (
    find_phone_number
)


@mock.patch(
    "swagger_server.controllers.default_controller.FindPhoneFromAddr.get_plids",
    return_value=["fake_id"],
)
@mock.patch(
    "swagger_server.controllers.default_controller.FindPhoneFromAddr.get_phn_fid",
    return_value="028 3835 0096",
)
def test_empty_address(mock_get_plids, mock_get_phn_fid):
    phone_num, code = find_phone_number("")
    assert code == 400


@mock.patch(
    "swagger_server.controllers.default_controller.FindPhoneFromAddr.get_plids",
    return_value=["fake_id"],
)
@mock.patch(
    "swagger_server.controllers.default_controller.FindPhoneFromAddr.get_phn_fid",
    return_value="028 3835 0096",
)
def test_good_address(mock_get_plids, mock_get_phn_fid):
    phone_num, code = find_phone_number("Library National City")
    assert code == 200
    assert phone_num.formatted_phone_number == "028 3835 0096"


@mock.patch(
    "swagger_server.controllers.default_controller.FindPhoneFromAddr.get_plids",
    return_value=["fake_id1", "fake_id2"],
)
@mock.patch(
    "swagger_server.controllers.default_controller.FindPhoneFromAddr.get_phn_fid",
    return_value="028 3835 0096",
)
def test_multiple_address(mock_get_plids, mock_get_phn_fid):
    phone_num, code = find_phone_number("Library National City")
    assert code == 200
    assert phone_num.formatted_phone_number == "028 3835 0096"
