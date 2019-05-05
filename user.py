import datetime
import os
import utils

from enum import Enum

class CertState(Enum):
    PENDING = 'PENDING'
    ISSUED  = 'ISSUED'
    REVOKED = 'REVOKED'

class User(object):

    def __init__(self, id, groups):
        self.id = id
        self.groups = groups

    def __str__(self):
        return "username : {}\ngroups : {}".format(self.id, self.groups)

    def create_cert_request(self, content):
        datetime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        path = "certificates/pending/" + self.id + "_" + datetime + ".csr"
        f = open(absolute_path(path), "w+")
        f.write(content)
        f.close()

