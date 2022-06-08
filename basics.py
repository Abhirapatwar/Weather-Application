import requests

def get_data(zip_code,api_key):
    api_url="https://api.openweathermap.org/data/2.5/weather?zip={},{}&appid={}".format(zip_code,'in',api_key)

    response=requests.get(api_url)
    return response.json()

x=get_data("431005","28081895045b1e9e7dbd34cc30ee52a7")
print(x)