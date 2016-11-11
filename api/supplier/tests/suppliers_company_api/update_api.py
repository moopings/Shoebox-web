from test_addons import MongoTestCase
from api.include.test import create_request, update_request
import json

class supplierCompany_Update_API_Test(MongoTestCase):
    CLEAR_CACHE = True

    URL = '/api/supplier/company'
    URL_COMPANY = '/api/supplier/company/nike'
    CREATE_BODY = """{ "name": "nike" }"""


    def test_update_api(self):
        c = Client()
        c.post(self.URL, data=self.CREATE_BODY, content_type="application/json")

        UPDATE_BODY = """
            {
              "name": "Adidas",
              "address":{
                "city": "Bangkok"
              }
            }
        """
        c = Client()
        res = c.put(self.URL_COMPANY, data=UPDATE_BODY, content_type="application/json")
        self.assertEqual(res.content.decode(), 'Company updated')

class supplierCompany_Update_Fail_API_Test(MongoTestCase):
    CLEAR_CACHE = True

    URL = '/api/supplier/company'
    URL_COMPANY = '/api/supplier/company/nike'
    CREATE_BODY = """{ "name": "nike" }"""

    def test_update_no_item(self):
        UPDATE_BODY = """{"name": "nike2"}"""

        res = update_request(self.URL_COMPANY, UPDATE_BODY)
        data = json.loads(res.content.decode())

        self.assertEqual(data['errorMsg'], ['This supplierCompany not exist'])
        self.assertEqual(data['updated'], False)


    def test_update_no_data(self):
        UPDATE_BODY = "{}"

        create_request(self.URL, self.CREATE_BODY)
        res = update_request(self.URL_COMPANY, UPDATE_BODY)
        data = json.loads(res.content.decode())

        self.assertEqual(data['errorMsg'], ['Data cannot empty'])
        self.assertEqual(data['updated'], False)


    def test_update_JSON_error(self):
        UPDATE_BODY = ""

        create_request(self.URL, self.CREATE_BODY)
        res = update_request(self.URL_COMPANY, UPDATE_BODY)
        data = json.loads(res.content.decode())

        self.assertEqual(data['errorMsg'], ['JSON Decode error'])
        self.assertEqual(data['updated'], False)