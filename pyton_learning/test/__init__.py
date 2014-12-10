import logging.config

logging.config.fileConfig('../logger.ini')
app_log = logging.getLogger("app")