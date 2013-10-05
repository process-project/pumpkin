__author__ = 'reggie'

import logging

LOG_LEVEL = logging.NOTSET
UDP_BROADCAST_PORT = 7700
#Broadcast presence in intervals
UDP_BROADCAST_RATE = 15




# Initialize the logger.
#RR#logging.basicConfig()
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

log = logging.getLogger('datariver')