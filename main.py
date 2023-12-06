from utils.logger_config import logger
from utils.context import context
from utils.api_init import naas
from utils.api_init import pgw
from utils.api_init import xpaas
import os

def main():
    # ================= NAAS API Samples ===================================================================
    # Doing a simple NaaS search for all LTE cells. Returning selected fields only
    logger.info("Getting all LTE cells")
    #lte_cells = naas.api.cells.get_cells(params={'technology': 'LTE', 'fields': '_id,name,mcc,mnc,rsi,pci'})
    lte_cells = naas.api.cells.get_cells(params={'technology': 'LTE'})


    # logging first 5 cells. Cells are under body['elements'][index]['cell]
    for i in range(5):
        logger.info(i)
        logger.info(lte_cells.body['elements'][i]['cell'])
    logger.info("")
    logger.info("")
    logger.info("")
    logger.info("Nächster Test")
    logger.info("")
    
    a=0
    for cell in lte_cells.body['elements']:
        mycellname = cell['cell'].get('name')
        
        if mycellname == "417330291L1":
            logger.info(lte_cells.body['elements']['cell'])


if __name__ == '__main__':
    main()

