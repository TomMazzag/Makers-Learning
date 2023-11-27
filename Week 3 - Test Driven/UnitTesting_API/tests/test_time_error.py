from unittest.mock import Mock
from lib.time_error import *

def test_the_api():

    mock_repsponse = Mock()
    mock_request = Mock()
    mock_time = Mock()

    mock_time.time.return_value = 1700136498.5
    mock_request.get.return_value = mock_repsponse

    mock_repsponse.json.return_value = {
        "unixtime": 1700136502
    }

    time_error = TimeError(mock_request, mock_time)
    result = time_error.error()
    assert result == 3.5
