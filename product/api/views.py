from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from product.models import Products
import json
import datetime
import re

# Create your views here.

def request_from(request, request_data):
    if request.method == 'GET':
        if not request_data:
            return HttpResponseNotFound('Content not found')
        response_data = request_data.to_json()
        return HttpResponse(response_data, content_type="application/json")
    else:
        return HttpResponseBadRequest('Bad Request')

def product_all(request):
    return request_from(request, Products.objects.all())

def product_name(request, name):
    return request_from(request, Products.objects(name=name))

def product_size(request, size):
    return request_from(request, Products.objects(size=size))

def product_validation(data):
    err = []
    if 'name' not in data:
        err.append('Product name cannot empty')
    if 'type' not in data:
        err.append('Product type cannot empty')
    if 'description' not in data:
        err.append('Description cannot empty')
    if 'price' not in data:
        err.append('Unit price cannot empty')
    # if 'picture' not in data:
    #     err.append('Picture cannot empty')
    if 'year' not in data:
        err.append('year cannot empty')
    if 'month' not in data:
        err.append('month cannot empty')
    if 'day' not in data:
        err.append('day cannot empty')
    if 'amount' not in data:
        err.append('Amount cannot empty')
    if 'size' not in data:
        err.append('Size cannot empty')
    if 'color' not in data:
        err.append('Color cannot empty')
    if 'available' not in data:
        err.append('Product status cannot empty')
    if 'discountAvailable' not in data:
        err.append('Discount status cannot empty')
    return err

def product_slug(name):
    name = re.sub(r"[^\w\s]", '', name)
    name = re.sub(r"\s+", '-', name)
    return name.lower()

@csrf_exempt
def product_create(request):
    if request.method == 'POST':
        raw_data = request.body.decode()
        err = product_validation(raw_data)
        if len(err) == 0:
            data = json.loads(raw_data)
            Products.objects.create(
                name=data['name'],
                type=data['type'],
                description=data['description'],
                price=data['price'],
                # picture=data['picture'],
                date=datetime.datetime(year=data['year'], month=data['month'], day=data['day']),
                amount=data['amount'],
                size=data['size'],
                color=data['color'],
                available=data['available'],
                discountAvailable=data['discountAvailable'],
                slug=product_slug(data['name'])
            )
            return HttpResponse('Product created')
        else:
            output = ''
            for e in err:
                output += e + '<br />'
            return HttpResponse(output)
    else:
        return HttpResponseBadRequest('Bad Request')

@csrf_exempt
def product_delete(request, id):
    if request.method == 'DELETE':
        Products.objects(pk=id).delete()
        return HttpResponse('Product removed')
    else:
        return HttpResponseBadRequest('Bad Request')
