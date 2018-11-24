import requests

key = "cdQh8jFpdGn8dzsgZ8kS3H7bpeJxCnfFn77VQM79EubXtsBY9cuxtvztJUyP4377"
main_url = "https://qocojunction2018.northeurope.cloudapp.azure.com/"
header = {'x-api-key': key}

def get_json1(url,payload=None):
    if payload is None:
        r = requests.get(url, headers=header)
    else:
        r = requests.get(url, headers=header, params=payload)
    return r.json()

def get_bookings():
    url = main_url + 'bookings'
    return get_json1(url)

def get_stations():
    url = main_url + 'stations'
    return get_json1(url)

def get_transports(time_str):
    url = main_url + 'transports'
    timer = {'time':time_str}
    return get_json1(url, payload = timer)['transports']

if __name__ == "__main__":

    timestr = '2018-12-01T00:00:00'
    k = get_transports(timestr)
    print(k)



