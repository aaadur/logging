import logging
import sys
from time import sleep

root = logging.getLogger(__name__)
root.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stderr)
handler.setLevel(logging.DEBUG)
log_format = '%(name)s - %(levelname)s - %(message)s'
formatter = logging.Formatter(log_format)
handler.setFormatter(formatter)
root.addHandler(handler)
while (True):
    Root.info("Writes to stderr by default")
    Root.warning("Faut faire gaffe")
    Root.error("Trop tard")
    Root.critical("C'est tout cassé")
    sleep (1)