# -*- coding: utf-8 -*-
from django.http import JsonResponse
from .utils.datajsonar import data_jsonar

def datajsonar(request):
    return JsonResponse(data_jsonar())