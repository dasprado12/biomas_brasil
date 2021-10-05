import requests
import json

uri = "https://geoservicos.ibge.gov.br/geoserver/wms?service=WFS&version=1.0.0&request=GetFeature&typeName=CREN:biomas_5000&outputFormat=JSON"


req = json.loads(requests.get(uri).text)

json.dump(req, open('Brasil.json', 'w'))

for doc in req['features']:
    filename = f"{doc['properties']['cod_bioma']}.json"
    json.dump(doc, open(filename, 'w'))


