#! /usr/bin/env python3
import json
import requests

'''Для геокодинга использовался сервис Яндекса, потому что он не требует привязки банковской карты'''
#Функция для отправки запроса
def geocode(coords):
    #координаты в Google и Яндекс задаются в разном порядке
    params = {'apikey':'1250aca0-5dfe-4a29-9a38-711ffec8943c', 'format':'json', 'geocode':coords[::-1]} 
    params_str = '&'.join([str(key)+'='+str(value) for key,value in params.items()])
    url = requests.utils.urlunparse(('https', 'geocode-maps.yandex.ru', '1.x', None, params_str, None))
    response = requests.get(url)
    return response

#Чтение и преобразование координат из файла
def get_coordinates_from_file(path):
    with open(path, 'r') as f:
        c = f.readline()
        return tuple([float(x) for x in c.strip().replace(',','.').replace("'","").split(';')])

#Красивое представление JSON
def print_json(j):
    print(json.dumps(j, ensure_ascii=False, indent=4))

#Вытаскивает местоположение объекта из JSON
def get_location(j, i=0):
    try:
        return j['response']['GeoObjectCollection']['featureMember'][i]['GeoObject']['metaDataProperty']['GeocoderMetaData']['text']
    except(IndexError, KeyError):
        raise Exception("Can't get a location from JSON")

#Вытаскивает координаты объекта из JSON
def get_coordinates_from_json(j, i=0):
    try:    
        return j['response']['GeoObjectCollection']['featureMember'][i]['GeoObject']['Point']['pos'].split()
    except(IndexError, KeyError):
        raise Exception("Can't get number of founds from JSON")

#Количество найденных совпадений из JSON
def get_found(j):
    try:    
        return j['response']['GeoObjectCollection']['metaDataProperty']['GeocoderResponseMetaData']['found']
    except(IndexError, KeyError):
        raise Exception("Can't get coordinates from JSON")

#Создание ссылки на google maps
def get_url_to_google_maps(coords):
    if len(coords)>=2:
        return 'https://www.google.com/maps/search/?api=1&query='+str(coords[0])+','+str(coords[1])
    else:
        raise Exception('Bad coords. Should be a tuple')

#Контроллер
def run(path):
        coords = get_coordinates_from_file(path)
        response = geocode(coords)
        if response.ok and get_found(response.json()) != '0':
            location = get_location(response.json())
            url = get_url_to_google_maps(get_coordinates_from_json(response.json()))
            return "Location: " + location + "\nGoogle Maps URL: " + url
        else:
            return "Bad request"

if __name__ == '__main__':
    print(run('coordinates'))
