import datetime
import logging
import requests
from nsetools import Nse
import azure.functions as func

nse = Nse()
TOKEN = "XXXXXXXXXXXXXXXXXX"
chat_id = -100XXXXXXXXX


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)

    nifty = nse.get_index_quote('nifty 50')
    banknifty = nse.get_index_quote('nifty bank')    
    lastprice = float(nifty['lastPrice'])
    change = float(nifty['change'])
    
    message_welcome = f"Index  {nifty['change']} ,  {banknifty['change']}"   
    try:
        hdfclife = nse.get_quote('hdfclife')
        message_welcome = f"Welcome  {nifty['change']} ,  {hdfclife['change']}"      
    except:
        print("An exception occurred")
   
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message_welcome}"
    requests.get(url)

    if change > 100:
        message = f"Nifty>100 change:{change} at price: {lastprice}"        
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
        requests.get(url)

    if change < -100:
        message = f"Nifty<-100 change:{change} at price: {lastprice}"
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
        requests.get(url)

    bankniftylastprice = float(banknifty['lastPrice'])
    bankniftylastchange = float(banknifty['change'])

    if bankniftylastchange > 500:
        message3 = f"BankNifty>500 change:{bankniftylastchange} at price: {bankniftylastprice}"
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message3}"
        requests.get(url)

    if bankniftylastchange < -500:
        message4 = f"BankNifty<-500 change:{bankniftylastchange} at price: {bankniftylastprice}"
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message4}"
        requests.get(url)
