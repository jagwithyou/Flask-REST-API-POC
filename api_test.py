import unittest
import requests
import json

class APITest(unittest.TestCase):
    API_URL = 'http://127.0.0.1:5000'
    USER_URL = API_URL+"/user"
    NEW_USER = {
    "name":"test name",
    "email":"test@gmail.com",
    "password":"pass"
    }
    NEW_USER_ID=0
    
    #Get request to /user returns all the users
    def test_1_get_all_users(self):
        r = requests.get(APITest.USER_URL)
        self.assertEqual(r.status_code, 200)

    #post request to /user to add new user
    def test_2_add_new_user(self):
        r = requests.post(APITest.USER_URL, json = APITest.NEW_USER)
        self.assertEqual(r.status_code, 200)
        APITest.NEW_USER_ID = json.loads(r.text)['id']

    # #put request to user/id to update user
    def test_3_update_existing_user(self):
        r = requests.put(f'{APITest.USER_URL}/{APITest.NEW_USER_ID}', json = APITest.NEW_USER)
        self.assertEqual(r.status_code, 200)

    # #delete request to user/id to delete user
    def test_4_delete_existing_user(self):
        r = requests.delete(f'{APITest.USER_URL}/{APITest.NEW_USER_ID}')
        self.assertEqual(r.status_code, 200)

if __name__ == "__main__":
    unittest.main()