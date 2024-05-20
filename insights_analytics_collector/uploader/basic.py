from base import BaseUploader


class Basic(BaseUploader):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def send_data(self):
        if hasattr(self, "cert_path") is False:
            raise ("cert_path is none")

        if hasattr(self, "username") is False:
            raise ("username is none")

        if hasattr(self, "username") is False:
            raise ("password is none")

        response = self.session.post(
            self.url,
            files=self.files,
            verify=self.cert_path,
            auth=(self.username, self.password),
            headers=self.headers,
            timeout=(31, 31),
            proxies={"https": self.proxy, "http": self.proxy},
        )

        return self.response(response)
