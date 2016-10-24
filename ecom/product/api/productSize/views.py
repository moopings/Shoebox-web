from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from ecom.product.models import ProductSizes
from ecom.include.api import request_get
import json

def productSize_all(request):
    return request_get(request, ProductSizes.objects.all())

def productSize_name(request, slug):
    return request_get(request, ProductSizes.objects(slug=slug))

@csrf_exempt
def productSize_create(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode())
        err = ProductSizes.validation(data)
        if len(err) == 0:
            ProductSizes.create_obj(data)
            return HttpResponse('productSize created', status=201)
        else:
            output = ''
            for e in err:
                output += e + '<br />'
            return HttpResponse(output)
    else:
        return HttpResponse('Method not allowed', status=405)

@csrf_exempt
def productSize_delete(request):
    if request.method == 'DELETE':
        item = ProductSizes.objects(slug=slug)
        if not item:
            return HttpResponse('This productSize not exist', status=404)
        item.delete()
        return HttpResponse('productSize removed')
    else:
        return HttpResponse('Method not allowed', status=405)

@csrf_exempt
def productSize_update(request, slug):
    if request.method == 'PUT':
        item = ProductSizes.objects(slug=slug)

        if not item:
            return HttpResponse('This productSize not exist', status=404)
        if not request.body:
            return HttpResponse('Request cannot empty', status=400)

        data = json.loads(request.body.decode())
        if not data:
            return HttpResponse('Data cannot empty', status=400)

        ProductSizes.update_obj(slug, data)
        return HttpResponse('productSize updated')
    else:
        return HttpResponse('Method not allowed', status=405)