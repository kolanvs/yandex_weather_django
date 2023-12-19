import requests
from cachetools.func import ttl_cache
from django.http import JsonResponse
from django.views import View
from constants import cities
from django import http


class YandexWeatherView(View):

    # @ttl_cache(maxsize=200, ttl=1800.0)
    def get(self, *args, **kwargs):

        WEATHER_URL =

        city = args[0].GET.get('city')
        if not city:
            return http.HttpResponseBadRequest(f'Не передано название города')
        founded_dict = next(filter(lambda d: d.get('city') == city, cities), {})
        if not founded_dict:
            return http.HttpResponseBadRequest(f'Город {city} не найден')
        url = f'https://api.weather.yandex.ru/v2/informers?lat={founded_dict["lat"]}&lon={founded_dict["lon"]}&lang=ru_RU'

        result_json = requests.get(url, headers={})

