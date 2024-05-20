from base import BaseUploader


class Pkce(BaseUploader):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def send_data(self):
        raise ("Auth strategy not implemented")
