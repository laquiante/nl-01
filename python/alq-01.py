#!/usr/bin/env python

import logging
import socket

from nlmanager.nlpacket import *
from nlmanager.nlmanager import NetlinkManager

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)7s: %(message)s')
log = logging.getLogger()

nlmanager = NetlinkManager()



