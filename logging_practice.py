import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

logging.debug("Debugging application")
logging.info("Opening login page")
logging.warning("Login took longer than expected")
logging.error("Login failed")
logging.critical("Application crashed")