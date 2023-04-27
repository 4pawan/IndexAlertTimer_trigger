import datetime
import logging
import requests
from jugaad_data.nse import NSELive
import azure.functions as func

TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
chat_id = -XXXXXXXXX
n = NSELive()


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)         
    message_welcome = ""   
    try:
        nifty_data = n.live_index("NIFTY 50")
        hdfclife_data =n.stock_quote("HDFCLIFE")    
        nifty = ((nifty_data['data'])[0])['change']
        hdfclife = (hdfclife_data['priceInfo'])['change']
        nifty = round(nifty, 2)
        hdfclife = round(hdfclife, 2)
        message_welcome = f"Welcome {nifty} ,  {hdfclife}"      
    except:
        print("An exception occurred")
   
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message_welcome}"
    requests.get(url)
