from django.shortcuts import render
from .models import Division, Category, District, Chondokotha
from django.http import JsonResponse


# Create your views here.
def home(request):
    return render(request, "Native_idoms/Home.html")


def data(request):
    context = {
        'division': list(Division.objects.values()),
        'chondokoha': list(Chondokotha.objects.values()),
        'category': list(Category.objects.values()),

    }
    return JsonResponse(context, safe=False)


def district(request):
    print(request.GET)
    print(request.POST)
    queryAll = District.objects
    if request.GET.get('division'):
        queryAll = queryAll.filter(division=request.GET.get('division'))

    district = queryAll.values()
    data = {
            'district': list(district),
        }
    return JsonResponse(data, safe=False)
