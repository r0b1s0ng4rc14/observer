import requests
import datetime
import time
import socket
import pandas as pd
import schedule


today = datetime.datetime.today()

df_site = pd.read_csv("site.txt")

df_endpoint = pd.read_csv("endpoint.txt",delimiter=";")


def observer():
    

    print (f"[Observer] ========================================================================================================")
    print(f">>> Inicio")
    for index, row in df_site.iterrows():
        print(f"[Site HealthCheck] ------------------------------------------------------------------------------------------------")
        print (f"    >>> Inicio: {index}")
        try:
            r = requests.get(row['URL'])
            if 200>= r.status_code <=399:
                today = datetime.datetime.today()
                print(f"    URL: [{row['URL']}] HTTP_CODE: [{r.status_code}] Response Time: [{r.elapsed.total_seconds()}] Checked: [{today:%d/%m/%Y %H:%M:%S}]")
                print(f"    <<< Fim")
                print(f"    ---------------------------------------------------------------------------------------------------------------")
            else:
                today = datetime.datetime.today()
                print(f"    URL: [{row['URL']}] HTTP_CODE: [{r.status_code}] [ERROR!] Checked: [{today:%d/%m/%Y %H:%M:%S}]")
                print(f"    <<< Fim")
                print(f"    ---------------------------------------------------------------------------------------------------------------")
        except requests.ConnectionError:
            today = datetime.datetime.today()
            print(f"    ***Could not resolve host: [{row['URL']}] Except: [ERROR!!!] Checked: [{today:%d/%m/%Y %H:%M:%S}]***")
            print(f"    <<< Fim")
            print(f"    ---------------------------------------------------------------------------------------------------------------")
    
    for index, row in df_endpoint.iterrows():
            print(f"[Endpoint HealthCheck] ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print (f"    >>> Inicio: {index}")
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            start = time.time()
            try:
                result = sock.connect_ex((row['IP'], row['PORT']))
                if result == 0:
                    today = datetime.datetime.today()
                    print(f"    IP: [{row['IP']}] PORT: [{row['PORT']}] Status: [OPEN] Response Time: [{(time.time()-start)*1000}] Testado em: [{today:%d/%m/%Y %H:%M:%S}]")
                    print(f"    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")    
                else:
                    today = datetime.datetime.today()
                    print (f"    Closed: {row['IP']} Port: {row['PORT']} Status: [CLOSED] Response Time: [{(time.time()-start)*1000}] Testado em: [{today:%d/%m/%Y %H:%M:%S}]")
                sock.close
            except Exception as e:
                today = datetime.datetime.today()
                print(f"    ***Could not resolve host: [{row['IP']}] Port: [{row['PORT']}] Except: [ERROR!!!] Checked: [{today:%d/%m/%Y %H:%M:%S}]***")
            time.sleep(1)
            print(f"<<< Fim")     
    print (f"===================================================================================================================\n")


schedule.every(2).minutes.do(observer)
while True:
    schedule.run_pending()
    time.sleep(1)