from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Mahasiswa

@csrf_exempt
def reader_mahasiswa(request,npm):   
    if request.method == "GET":
        try:
            mahasiswa = Mahasiswa.objects.get(npm=npm)
        except :
            return JsonResponse({'status': 'NPM does not exist'})
        return JsonResponse({'status':'OK', 'nama':mahasiswa.nama, 'npm':mahasiswa.npm})
    return JsonResponse({'status': 'Method Not Allowed'})
    