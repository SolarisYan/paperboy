import logging


class BaseResource(object):
    def __init__(self, config, db):
        self.config = config
        self.db = db
        self.logger = logging.getLogger('paperboy.' + __name__)