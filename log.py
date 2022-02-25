import logging
import sys
from time import sleep

root = logging.getLogger(__name__)
root.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stderr)
handler.setLevel(logging.DEBUG)
log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
formatter = logging.Formatter(log_format)
handler.setFormatter(formatter)
root.addHandler(handler)
while (True):
    root.info("En cours")
    root.warning("Faut faire gaffe")
    root.error("Trop tard")
    root.critical("C'est tout cassé")
    sleep (1)
