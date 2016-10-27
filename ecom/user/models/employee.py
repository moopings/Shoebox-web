from mongoengine import *
from mongoengine.django.auth import User
import datetime

class Employees(User):
    firstname = StringField(max_length=50, required=True)
    lastname = StringField(max_length=50, required=True)
    gender = StringField(max_length=10, required=True)
    birthday = DateTimeField(required=True)
    city = StringField(max_length=50, required=True)
    district = StringField(max_length=50, required=True)
    street = StringField(max_length=50, required=True)
    zipcode = StringField(max_length=10, required=True)
    phone = StringField(max_length=20, required=True)
    role = StringField(max_length=20, required=True, default="employee")

    def validation(data):
        err = []
        if 'username' not in data:
            err.append('Username cannot empty')
        if 'password' not in data:
            err.append('Password cannot empty')
        if 'repassword' not in data:
            err.append('Re password cannot empty')
        if 'password' in data and 'repassword' in data:
            if not data['password'] == data['repassword']:
                err.append('Password didn\'t match')
        if 'email' not in data:
            err.append('Email cannot empty')
        if 'firstname' not in data:
            err.append('Firstname cannot empyty')
        if 'lastname' not in data:
            err.append('Lastname cannot empty')
        if 'gender' not in data:
            err.append('Gender cannot empty')
        if 'birthday' not in data:
            err.append('Birthday cannot empty')
            err.append('- Year cannot empty')
            err.append('- Month cannot empty')
            err.append('- Day cannot empty')
        else:
            if not {'year', 'month', 'day'} <= set(data['birthday']):
                err.append('Birthday cannot empty')
                if 'year' not in data['birthday']:
                    err.append('- Year cannot empty')
                if 'month' not in data['birthday']:
                    err.append('- Month cannot empty')
                if 'day' not in data['birthday']:
                    err.append('- Day cannot empty')
        if 'address' not in data:
            err.append('Address cannot empty')
            err.append('- City cannot empty')
            err.append('- District cannot empty')
            err.append('- Street cannot empty')
            err.append('- Zipcode cannot empty')
        else:
            if not {'city', 'district', 'street', 'zipcode'} <= set(data['address']):
                err.append('Address cannot empty')
                if 'city' not in data['address']:
                    err.append('- City cannot empty')
                if 'district' not in data['address']:
                    err.append('- District cannot empty')
                if 'street' not in data['address']:
                    err.append('- Street cannot empty')
                if 'zipcode' not in data['address']:
                    err.append('- Zipcode cannot empty')
        if 'phone' not in data:
            err.append('Phone cannot empty')
        return err

    @classmethod
    def create_obj(cls, data):
        email = data['email']
        if email is not None:
            try:
                email_name, domain_part = email.strip().split('@', 1)
            except ValueError:
                pass
            else:
                email = '@'.join([email_name, domain_part.lower()])

        employee = cls(
            username = data['username'],
            email = data['email'],
            firstname = data['firstname'],
            lastname = data['lastname'],
            gender = data['gender'],
            birthday = datetime.datetime(
                year = data['birthday']['year'],
                month = data['birthday']['month'],
                day = data['birthday']['day']
            ),
            city = data['address']['city'],
            district = data['address']['district'],
            street = data['address']['street'],
            zipcode = data['address']['zipcode'],
            phone = data['phone'],
            is_superuser=True,
            is_staff=True
        )
        employee.set_password(data['password'])
        employee.save()

        return employee


    @classmethod
    def update_obj(cls, username, data):
        if 'birthday' in data:
            data['birthday'] = datetime.datetime(
                year=data['birthday']['year'],
                month=data['birthday']['month'],
                day=data['birthday']['day']
            )
            print(data['birthday'])
        if 'address' in data:
            if 'city' in data['address']:
                data['city'] = data['address']['city']
            if 'district' in data['address']:
                data['district'] = data['address']['district']
            if 'street' in data['address']:
                data['street'] = data['address']['street']
            if 'zipcode' in data['address']:
                data['zipcode'] = data['address']['zipcode']
            data.pop('address')

        employee = cls.objects(username=username)
        employee.update(**data)
        return employee
