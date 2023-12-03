import unittest
from unittest.mock import patch, Mock

from VebinarTests.gihub.api import get_user_info

from api import get_user_info


class TestAPI(unittest.TestCase):
    def test_get_user_info_context_manager(self):
        expected = {'login': 'test'}
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = expected

        with patch('api.requests') as mock_requests:
            mock_requests.get.return_value = response_mock

            assert get_user_info('test') == expected
            assert mock_requests.get.call_count == 1

    def test_get_user_info_context_manager_github_error(self):
        response_mock = Mock()
        response_mock.status_code = 404

        with patch('api.requests') as mock_requests:
            mock_requests.get.return_value = response_mock

            assert get_user_info('test') is None
            assert mock_requests.get.call_count == 1


if __name__ == "__main__":
    unittest.main()