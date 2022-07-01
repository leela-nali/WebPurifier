import logging

class Logger:
    def __init__(self,log):
        self.log = log()

    def log(level: str):
        if(level == debug):
            logging.debug(msg)
        if(level == info):
            logging.info('So should this')
        if(level == warning):
            logging.warning('And this, too')
        if(level == error):
            logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
# create logger
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')