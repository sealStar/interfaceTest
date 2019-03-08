import requests
import readConfig
from common.Log import MyLog as Log

localReadConfig = readConfig.ReadConfig()

class ConfigHttp:
    def __init__(self):
        global host,timeout
        host = localReadConfig.get_http("baseurl")
        timeout = localReadConfig.get_http("timeout")
        self.log = Log.get_log()
        self.logger = self.log.get_logger()
        self.headers = {}
        self.params = {}
        self.data = {}
        self.url = None
        self.cookie = {}
        self.files={}

    def set_url(self, url):
        self.url = host + url

    def set_headers(self, header):
        self.headers = header

    def set_params(self, param):
        self.params = param

    def set_data(self, data):
        self.data = data

    def set_cookie(self, cookie):
        self.cookie = cookie

    def set_files(self, file):
        self.files = file
    # defined http get method
    def get(self):
        try:
            response = requests.get(self.url,cookie=self.cookie,params=self.params, headers=self.headers, timeout=float(timeout))
            # response.raise_for_status()
            return response
        except BaseException as e:
            self.logger.error("%s"%e)
            return None

    # defined http post method
    def post(self):
        try:
            response = requests.post(self.url,cookie= self.cookie,headers=self.headers, data=self.data, files=self.files, timeout=float(timeout))
            # response.raise_for_status()
            return response
        except BaseException as e:
            self.logger.error("%s" %e)
            return None