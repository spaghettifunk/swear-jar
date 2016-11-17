import json
from django.http import HttpResponse
from rest_framework.decorators import api_view
from .models import Swear


# Create your views here.
@api_view(['GET'])
def index(request):

    swear = Swear.objects.filter(id=1).get()

    page = """
    SWEAR JAR :)

    Bjorn has to pay: """ + str(swear.bjorn) + """ euro
    Alex has to pay: """ + str(swear.alex) + """ euro
    Wang has to pay: """ + str(swear.wang) + """ euro
    Patrick has to pay: """ + str(swear.patrick) + """ euro
    Dario has to pay: """ + str(swear.dario) + """ euro
    Davide has to pay: """ + str(swear.davide) + """ euro
    Rafael has to pay: """ + str(swear.rafael) + """ euro
    """

    return HttpResponse(status=200, content=page, content_type="application/json")


@api_view(['PUT'])
def update_jar(request):

    params = dict(json.loads(request.body))
    name = params["name"]

    swear = Swear.objects.filter(id=1).get()

    if name == "Bjorn":
        swear.bjorn += 1
    elif name == "Alex":
        swear.alex += 1
    elif name == "Wang":
        swear.wang += 1
    elif name == "Patrick":
        swear.patrick += 1
    elif name == "Dario":
        swear.dario += 1
    elif name == "Davide":
        swear.davide += 1
    elif name == "Rafael":
        swear.rafael += 1

    swear.save()
    return HttpResponse(status=200, content="Yay")


@api_view(['GET'])
def init(request):
    s = Swear.objects.create()
    s.save()

    return HttpResponse(status=200, content="Init done")