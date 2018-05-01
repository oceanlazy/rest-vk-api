from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import renderer_classes, api_view

import v_vk_api

from main.main_settings import PROXIES


def get_api(app_id=None,
            login=None,
            password=None,
            service_token=None):
    return v_vk_api.create(app_id,
                           login,
                           password,
                           service_token,
                           PROXIES)


@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def get_user(request, user_ids):
    """
    Get user by ID
    """
    service_token = request.query_params.get('service_token', None)
    api = get_api(service_token)
    api_response = api.request_get_user(user_ids)
    return Response(api_response)


@api_view(['POST', 'DELETE'])
@renderer_classes((JSONRenderer,))
def status(request):
    """
    Set or clear users status, depending on method
    """
    app_id = request.query_params.get('app_id', None)
    login = request.query_params.get('login', None)
    password = request.query_params.get('password', None)
    api = get_api(app_id, login, password)
    if request.method == 'POST':
        text = request.data
        api_response = api.request_set_status(text)
        return Response(api_response)

    if request.method == 'DELETE':
        api_response = api.request_clear_status()
        return Response(api_response)
