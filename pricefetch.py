from requests import Request, Session
import json
import pprint as pp

url='https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'

token = 'BTC'

def yup():
    parameters = {
        'symbol': token,
        'convert':'INR'
    }

    headers = {
        'Accepts':'application/json',
        'X-CMC_PRO_API_KEY':'6ff63b67-bbc3-4854-8042-c2c9bbdbcd13'
    }

    session = Session()
    session.headers.update(headers)

    response = session.get(url, params=parameters)
    # print("PRICE OF BTC(INR) : ")
    return json.loads(response.text)['data'][token][0]['quote']['INR']['price']

pp.pprint(yup())