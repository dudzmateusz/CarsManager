import requests

def get_models(make):

    url = "https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{}?format=json".format(make)

    headers = {
        }

    response = requests.request("GET", url, headers=headers)
    t = response.json()

    Model_Name = []
    for i in t['Results']:
        Model_Name.append(i['Model_Name'])

    return Model_Name
