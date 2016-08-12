import json
from django.http import HttpResponse
from rest_framework.decorators import api_view

euro_bjorn = 0
euro_alex = 0
euro_wang = 0
euro_patrick = 0
euro_dario = 0
euro_davide = 0
euro_rafael = 0


# Create your views here.
@api_view(['GET'])
def index(request):

    response = dict()
    response['euro_bjorn'] = euro_bjorn
    response['euro_alex'] = euro_alex
    response['euro_wang'] = euro_wang
    response['euro_patrick'] = euro_patrick
    response['euro_dario'] = euro_dario
    response['euro_davide'] = euro_davide
    response['euro_rafael'] = euro_rafael

    return HttpResponse(status=200, content=json.dumps(response),
                        content_type="application/json")


@api_view(['PUT'])
def update_jar(request):

    params = dict(json.loads(request.body))
    name = params["name"]

    if name == "Bjorn":
        euro_bjorn += 1
    elif name == "Alex":
        euro_alex += 1
    elif name == "Wang":
        euro_wang += 1
    elif name == "Patrick":
        euro_patrick += 1
    elif name == "Dario":
        euro_dario += 1
    elif name == "Davide":
        euro_davide += 1
    elif name == "Rafael":
        euro_rafael += 1

    response = dict()
    response['euro_bjorn'] = euro_bjorn
    response['euro_alex'] = euro_alex
    response['euro_wang'] = euro_wang
    response['euro_patrick'] = euro_patrick
    response['euro_dario'] = euro_dario
    response['euro_davide'] = euro_davide
    response['euro_rafael'] = euro_rafael

    return HttpResponse(status=200, content=json.dumps(response),
                        content_type="application/json")
