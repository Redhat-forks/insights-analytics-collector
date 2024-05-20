from cert import Cert
from pat import Pat
from pkce import Pkce
from identity import Identity
from s3 import S3
from basic import Basic


def get_uploader(strategy, **kwargs):
    strategies = {
        "user-pass": Basic,
        "user-pass-s3": S3,
        "x-rh-identity": Identity,
        "mutual-tls": Cert,
        "service-account": Pat,
        "service-account-pkce": Pkce,
    }

    if strategy not in strategies:
        raise ValueError("Unknown auth strategy: {}".format(strategy))

    return strategies[strategy](**kwargs)
