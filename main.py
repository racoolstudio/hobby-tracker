# API
# get request we get info from _winapi
# post request is giving info to the api
# put is for updating
# delete is lol yeah you know
import os
from requests import *
from datetime import *
#strftime() method

USERNAME = os.getenv('USER')
TOKEN = os.getenv('TOKEN')
pixela_endpoint = 'https://pixe.la/v1/users'
parameters = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}
# post(url=pixela_endpoint,json=parameters).text
graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'
graph_config = {

    'id': 'graph1',
    'name': 'Push Up Graph',
    'unit': 'Push Ups',
    'type': 'int',
    'color': 'sora'  # which is blue

}
Headers = {
    'X-USER-TOKEN': TOKEN
}
# print(post(url=graph_endpoint,json=graph_config,headers=Headers).text )
date = datetime.now().strftime('%Y%m%d')
today = {
    'date':date,
    'quantity': input('How many push upd did you do today ?\nAnswer :')
}

post_pix_endpoint = f'{graph_endpoint}/graph1'
print(post(url=post_pix_endpoint,json=today,headers=Headers).text
)
# put(url=f'{post_pix_endpoint}/{date}',json=today,headers=Headers).text
# delete(url=f'{post_pix_endpoint}/{date}',headers=Headers).text
# print(delete(url=f'{post_pix_endpoint}/{date}',headers=Headers).text)
