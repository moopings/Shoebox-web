from test_addons import MongoTestCase
from api.include.test import create_request, update_request
from .create_body import *
import json


class customer_Updated_API_Test(MongoTestCase):
    CLEAR_CACHE = True

    def test_update_api(self):
        create_request(URL_CUSTOMER, CREATE_BODY)

        UPDATE_BODY = json.dumps({'phone' : '087-777-7777'})

        res = update_request(URL_CUSTOMER_USERNAME, UPDATE_BODY)
        data = json.loads(res.content.decode())

        self.assertEqual(data['updated'], True)


class customer_Update_Fail_API_Test(MongoTestCase):
    CLEAR_CACHE = True

    def test_update_no_item(self):

        UPDATE_BODY = json.dumps({'phone' : '087-777-7777'})
        res = update_request(URL_CUSTOMER_USERNAME, UPDATE_BODY)
        data = json.loads(res.content.decode())

        self.assertEqual(data['errorMsg'], ['This customer not exist'])
        self.assertEqual(data['updated'], False)


    def test_update_no_data(self):
        UPDATE_BODY = json.dumps({})

        create_request(URL_CUSTOMER, CREATE_BODY)
        res = update_request(URL_CUSTOMER_USERNAME, UPDATE_BODY)
        data = json.loads(res.content.decode())

        self.assertEqual(data['errorMsg'], ['Data cannot empty'])
        self.assertEqual(data['updated'], False)
