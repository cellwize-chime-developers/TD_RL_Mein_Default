from utils.context import app_config
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.INFO,
                    format='%(asctime)s [%(name)s] [%(levelname)s] %(message)s')

logger = logging.getLogger(app_config['application']['meta']['name'])
