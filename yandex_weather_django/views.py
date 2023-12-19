from django.http import JsonResponse
from django.views import View


class YandexWeatherView(View):

    def get(self, *args, **kwargs):
        return JsonResponse({})
