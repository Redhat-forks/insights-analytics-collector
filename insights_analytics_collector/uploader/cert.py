from base import BaseUploader


class Cert(BaseUploader):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def send_data(self):
        raise ("Auth strategy not implemented")
