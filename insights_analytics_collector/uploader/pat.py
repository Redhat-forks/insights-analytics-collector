from base import BaseUploader
import json


class Pat(BaseUploader):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sso_url = "https://sso.redhat.com/auth/realms/redhat-external/protocol/openid-connect/token"

    def send_data(self):
        if hasattr(self, "cert_path") is False:
            raise ("cert_path is none")

        if hasattr(self, "username") is False:
            raise ("username is none")

        if hasattr(self, "username") is False:
            raise ("password is none")

        self.headers["Content-Type"] = "application/x-www-form-urlencoded"

        data = {
            "client_id": self.username,
            "client_secret": self.password,
            "grant_type": "client_credentials",
        }

        response = self.session.post(
            self.sso_url,
            headers=self.headers,
            data=data,
            verify=self.cert_path,
            timeout=(31, 31),
            proxies={"https": self.proxy, "http": self.proxy},
        )
        access_token = json.loads(response.content)["access_token"]

        self.headers["authorization"] = "Bearer {}".format(access_token)

        response = self.session.post(
            self.url,
            files=self.files,
            verify=self.cert_path,
            proxies={"https": self.proxy, "http": self.proxy},
            headers=self.headers,
            timeout=(31, 31),
        )

        return self.response(response)
