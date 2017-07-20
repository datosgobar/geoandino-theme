# -*- coding: utf-8 -*-
from django.http import JsonResponse
from geoandino.utils.datajsonar import data_jsonar

def data_json(request):
    return JsonResponse(data_jsonar())