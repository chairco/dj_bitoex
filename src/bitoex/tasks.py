# bitoex/tasks.py
import time
import requests

from django.conf import settings
from .models import Bitoex
from .tf import *


headers = {
    'Host': "www.bitoex.com",
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    'Accept-Language': "zh-TW,en;q=0.7,en-US;q=0.3",
    'Accept-Encoding': "gzip, deflate, br",
    'Referer': "https://www.bitoex.com/users/sign_in?locale=zh-tw",
    'DNT': "1",
    'Connection': "keep-alive",
    "Upgrade-Insecure-Requests": "1"
}

exchange_url = 'https://www.bitoex.com/api/v1/get_rate'


def get_bito_exchange(url=exchange_url):
    req = requests.session()
    exinfo = req.get(url=url, headers=headers).json()
    Bitoex.objects.create(
        buy=exinfo['buy'], 
        sell=exinfo['sell'], 
        timestamp=timestamp_short_to_datetime(int(exinfo['timestamp']))
    )
    return exinfo