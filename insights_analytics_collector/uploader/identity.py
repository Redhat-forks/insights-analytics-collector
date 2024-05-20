from base import BaseUploader


class Identity(BaseUploader):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def send_data(self):
        if self.xrhidentity is None:
            raise ("xrhidentity is none")

        self.headers["x-rh-identity"] = self.xrhidentity

        response = self.session.post(
            self.url,
            files=self.files,
            headers=self.headers,
            timeout=(31, 31),
            proxies={"https": self.proxy, "http": self.proxy},
        )

        return self.response(response)
