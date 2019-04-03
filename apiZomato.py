import requests as req

def getfoodplaces(apiKey, lat, lon, *args):
    url = 'https://developers.zomato.com/api/v2.1/search?count=20&lat={0}&lon={1}&sort=real_distance&order=asc'.format(lat, lon)
    headers = {"Accept": "application/json", "user_key": apiKey}
    lista = req.get(url, headers=headers)
    return lista.json()

def locateByIP():
    data = req.get('http://ipinfo.io/json')
    return data.json()
