# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 20:56:10 2018

@author: somasekhar.gunturu
"""

import json
import os
import requests


from flask import Flask
from flask import request
from flask import make_response

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('##### This is a log message.')

#Flask app should start in global layout
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])

def webhook():
    req = request.get_json(silent=True, force=True)
    print(json.dumps(req,indent=4))
    
    res = makeResponse(req)
    res = json.dumps(res,indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r
    
def makeResponse(req):
    logging.debug("####### This has to print")
    for keys,values in req.items():
        logging.debug("####### Keys = "+ keys)
        for keys1,values1 in values.items():
            logging.debug("####### keys1 = "+ keys1)
            logging.debug("####### values1 = "+ values1)          
    #log.debug("###### req = " + req);
    result = req.get("result")
    log.debug("###### result = " + result);
    print(result)
    parameters = result.get("parameters")
    city = parameters.get("geo-city")
    date = parameters.get("date")
#    r = requests.get('http://api.openweathermap.org/data/2.5/forecast?q='+city+'&appid=d8942bef4f375f7d9d56e84cf5709cf5')
#    json_object = r.json()
#    weather = json_object['list']
#    for i in range(0,30):
#        if date in weather[i]['dt_txt']:
#            condition = weather[i]['weather'][0]['description']
#            break    
    
#    speech = "The forecast for"+city+ "for "+date+" is "+condition
    speech = "The forecast for London is cloudy"
    return {
    "speech": speech,
    "displayText": speech,
    "source": "apiai-weather-webhook"
    }
    
if __name__ == '__main__':
    port = int(os.getenv('PORT',5000))
    print("Starting app on port %d" % port)    
    app.run(debug=True, port=port, host='0.0.0.0')
    
    

    