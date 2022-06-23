import requests

if __name__ == '__main__':
    request_xml = '''<ws:dataDeliveryRequest dateFrom="2014-04-28" dateTo="2014-04-28"
    xmlns="http://geomodel.eu/schema/data/request"
    xmlns:ws="http://geomodel.eu/schema/ws/data"
    xmlns:geo="http://geomodel.eu/schema/common/geo"
    xmlns:pv="http://geomodel.eu/schema/common/pv"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    <site id="demo_site" name="Demo site" lat="48.61259" lng="20.827079">
    </site>
    <processing key="GHI" summarization="HOURLY" terrainShading="true">
    </processing>
    </ws:dataDeliveryRequest>'''
    api_key = 'demo'
    url = 'https://solargis.info/ws/rest/datadelivery/request?key=%s' % api_key
    headers = {'Content-Type': 'application/xml'}
    with requests.post(url, data=request_xml.encode('utf8'), headers=headers) as response:
        print(response.text)
        # parse and consume successful response, or inspect error code and a message from the server
