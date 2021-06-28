import prometheus_client as prom
import requests
import time

'''
Variables
'''
RESPONSE_TIME_GAUGE = prom.Gauge('sample_external_url_response_ms', 'HTTP response in milliseconds', ["url"],multiprocess_mode='min')
STATUS_CODE_GAUGE = prom.Gauge('sample_external_url_up', 'Boolean status of site up or down', ["url"],multiprocess_mode='min')
URL_LIST = ["https://httpstat.us/200", "https://httpstat.us/503"]

'''
Get the response time in ms for URL
Return the response time in ms for URL
'''
def get_response(url):
    response = requests.get(url)
    response_time = response.elapsed.total_seconds()
    print(url,'Response Time','--->',response_time)    
    return response_time

'''
Get the URL's HTTP status code like (200 / 503 / 400) of URLs & set the status code value as 1 for 200 HTTP status 
code and value set to 0 for non 200 HTTP response code.
'''
def get_url_status(url):        
    response = requests.get(url)
    url_status_code=response.status_code
    if(url_status_code == 200):
        status_code=1
    else:
        status_code=0                       
    print(url,'Status Code','--->',status_code)
    return status_code
        
'''
Set the URL Response code & URL status code recursively in Gauge.
'''
def set_values():
    while True:
        for url_name in URL_LIST:
            response_time = get_response(url_name)
            RESPONSE_TIME_GAUGE.labels(url=url_name).set(response_time)
            response_status = get_url_status(url_name)
            STATUS_CODE_GAUGE.labels(url=url_name).set(response_status)
            time.sleep(5)

'''
Main method
'''
if __name__ == '__main__':
    prom.start_http_server(8001)
    set_values()
