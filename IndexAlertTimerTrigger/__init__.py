import datetime
import logging
import requests
from nsetools import Nse
import azure.functions as func
nse= Nse()
TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
chat_id = -100XXXXXXX

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)

    nifty = nse.get_index_quote('nifty 50')
    banknifty = nse.get_index_quote('nifty bank')    
    hdfclife = nse.get_quote('hdfclife')    
    lastPrice = nifty['lastPrice']
    change = nifty['change']      
   
    message_welcome = f"Welcome:{nifty['change']} :{hdfclife['change']}"       
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message_welcome}"
    requests.get(url).json()



    if change > 100:   
       message = f"Nifty>100 change:{change} at price:{lastPrice}"       
       url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
       requests.get(url).json()

    if change < -100:   
       message = f"Nifty<-100 change:{change} at price:{lastPrice}"       
       url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
       requests.get(url).json()
         
    bankNiftyLastPrice = banknifty['lastPrice']
    bankNiftyLastChange = banknifty['change']      

    if bankNiftyLastChange > 500:   
       message3 = f"BankNifty>500 change:{bankNiftyLastChange} at price:{bankNiftyLastPrice}"       
       url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message3}"
       requests.get(url).json()

    if bankNiftyLastChange < -500:   
       message4 = f"BankNifty<-500 change:{bankNiftyLastChange} at price:{bankNiftyLastPrice}"       
       url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message4}"
       requests.get(url).json()
    
