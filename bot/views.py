from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import actions
import json

router = {
    'create.appointment': actions.debug
}

def get_payload(request):
    # work out how to do this:
    request_json = request.body.decode('utf-8')
    return json.loads(request_json)

def execute_action(request):
    payload = get_payload(request)
    action = payload.get('result').get('action')
    params = payload.get('result').get('parameters', {})
    token = payload.get('sessionId', None)
    return router.get(action)(payload, params=params, token=token)

@csrf_exempt
def index(request):
    print("request >> {}" .format(request.body))
    result = execute_action(request)
    print("response << {}" .format(result))
    return JsonResponse(result)
