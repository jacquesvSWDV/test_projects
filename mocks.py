import unittest
from unittest.mock import patch, Mock
import requests

#function under test
def get_user_data(user_id):
    #sends an API request to an endpoint to grab user data
    response = requests.get(f'https://api.example.com/users/{user_id}')
    return response.json()

class TestGetUserData(unittest.TestCase):

    #patch decorate used for dependency injection
    @patch('requests.get')
    def test_get_user_data(self, mock_get):

        #'patch' replaces 'request.get' with a mock during the test
        mock_response = Mock()

        #Define what .json() should return when called on the mock response
        response_dict = {'name': 'John Doe', 'email': 'john.doe@example.com'}
        mock_response.json.return_value = response_dict

        #configure the mocked 'requests.get' to return our mocked response
        mock_get.return_value = mock_response

        #call the function under test
        user_data = get_user_data(1)

        #verify requests.get has been called with the correct URL
        mock.get.assert_called_with('https://api.example.com/users/1')

        #assert that the returned user data is same real user data
        self.assertEqual(user_data, response_dict)

if __name__ == '__main__':
    unittest.main()