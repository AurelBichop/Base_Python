import logging
import requests

logging.basicConfig(level=logging.DEBUG,
                    filename="app.log",
                    filemode="a",
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug("Savoir ce que ça retourne")
logging.info("information")
logging.warning("avertissement")
logging.error("petit soucis script continue")
logging.critical("arrrete le script")
