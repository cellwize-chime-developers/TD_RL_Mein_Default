from utils.logger_config import logger
from utils.context import context
from utils.api_init import naas
from utils.api_init import pgw
from utils.api_init import xpaas


def main():
    logger.info("Welcome toa a Sample Chime Application")
    logger.info("This main() function is the entry point for the application. Place your application logic here.")
    logger.info("For API examples checkout getting-stared.py")
    logger.info("To configure application parameters go to ./config/config.yaml, and ./config/config-test.yaml")
    logger.info("To configure Chime Services Urls go to /utils/api_init.py")
    logger.info("Application context is available via the 'context' dictionary object")
    logger.info("For Chime API reference visit: https://kb.cellwize.com/display/DPO/Open+Platform+API+Reference")


if __name__ == '__main__':
    main()
