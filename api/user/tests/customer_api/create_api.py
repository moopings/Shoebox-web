from test_addons import MongoTestCase
from api.include.test import create_request
import json

class customer_Create_API_Test(MongoTestCase):
    CLEAR_CACHE = True

    URL = '/api/user/customer'
    URL_CUSTOMER = '/api/user/customer/mooping12345'
    CREATE_BODY = """
        {
        	"username": "mooping12345",
        	"password": "secret",
        	"repassword": "secret",
        	"email": "mail@gmail.com",
        	"firstname": "kaoneaw",
        	"lastname": "mooping",
            "picture" : "picture url",
        	"gender": "male",
        	"birthday": {
        		"year": 2000,
        		"month": 10,
        		"day": 10
        	},
        	"address": {
        		"city": "my-city",
        		"district": "my-district",
        		"street": "my-street",
        		"zipcode": "99999"
        	},
        	"phone": "080-000-0000",
            "credit" : {
                "type" : "XXX",
                "id" : "6625526",
                "exp" : {
                    "year": 2000,
        		    "month": 10,
        		    "day": 10}
            },
            "ship": {
        		"city": "my-city",
        		"district": "my-district",
        		"street": "my-street",
        		"zipcode": "99999"
        	}
        }
    """

    def test_create_api(self):
        res = create_request(self.URL, self.CREATE_BODY)
        data = json.loads(res.content.decode())

        self.assertEqual(data['created'], True)

class customer_Create_Fail_API_Test(MongoTestCase):
    CLEAR_CACHE = True

    URL = '/api/user/customer'

    def test_create_no_firstname(self):
        CREATE_BODY = """{}"""
        res = create_request(self.URL, CREATE_BODY)
        data = json.loads(res.content.decode())
        self.assertEqual(data['errorMsg'],[
            "Username cannot empty",
            "Password cannot empty",
            "Re password cannot empty",
            "Email cannot empty",
            "Firstname cannot empty",
            "Lastname cannot empty",
            "Gender cannot empty",
            "Birthday cannot empty",
            "Year cannot empty",
            "Month cannot empty",
            "Day cannot empty",
            "Address cannot empty",
            "City cannot empty",
            "District cannot empty",
            "Street cannot empty",
            "Zipcode cannot empty",
            "Ship address cannot empty",
            "City cannot empty",
            "District cannot empty",
            "Street cannot empty",
            "Zipcode cannot empty",
            "Credit card cannot empty",
            "Phone cannot empty"
        ])
        self.assertEqual(data['created'], False)

    def test_create_no_data(self):
        CREATE_BODY = ""

        res = create_request(self.URL, CREATE_BODY)
        data = json.loads(res.content.decode())

        self.assertEqual(data['errorMsg'], ['JSON Decode error'])
        self.assertEqual(data['created'], False)

    def test_create_username_duplicated(self):

        CREATE_BODY = """
        {
        	"username": "mooping12345",
        	"password": "secret",
        	"repassword": "secret",
        	"email": "mail@gmail.com",
        	"firstname": "kaoneaw",
        	"lastname": "mooping",
            "picture" : "picture url",
        	"gender": "male",
        	"birthday": {
        		"year": 2000,
        		"month": 10,
        		"day": 10
        	},
        	"address": {
        		"city": "my-city",
        		"district": "my-district",
        		"street": "my-street",
        		"zipcode": "99999"
        	},
        	"phone": "080-000-0000",
            "credit" : {
                "type" : "XXX",
                "id" : "6625526",
                "exp" : {
                    "year": 2000,
        		    "month": 10,
        		    "day": 10}
            },
            "ship": {
        		"city": "my-city",
        		"district": "my-district",
        		"street": "my-street",
        		"zipcode": "99999"
        	}
        }
        """

        create_request(self.URL, CREATE_BODY)
        res = create_request(self.URL, CREATE_BODY)
        data = json.loads(res.content.decode())
        self.assertEqual(data['errorMsg'], ['Username already exist'])
        self.assertEqual(data['created'], False)