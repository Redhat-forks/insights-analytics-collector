from abc import ABC, abstractmethod

import requests


class BaseUploader(ABC):
    def __init__(self, **kwargs):
        self.session = requests.Session()
        self._cert = None
        self._headers = {}
        self._proxy = None
        for key, value in kwargs.items():
            setattr(self, key, value)

    @abstractmethod
    def send_data(self):
        pass

    @property
    def cert(self):
        return self._cert

    @cert.setter
    def cert(self, cert):
        self._cert = cert

    @property
    def headers(self):
        return self._headers

    @headers.setter
    def headers(self, headers):
        self._headers = headers

    @property
    def proxy(self):
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        self._proxy = proxy

    def response(self, response):
        # Accept only 200-299 status codes
        if not (200 <= response.status_code < 300):
            self.logger.error(
                "Upload failed with status {}, {}".format(
                    response.status_code, response.text
                )
            )
            return False
        return True
