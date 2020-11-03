from utils.logger_config import logger
from utils.context import context
from utils.api_init import naas
from utils.api_init import pgw
from utils.api_init import xpaas


def getting_started():
    logger.info("Getting Started with Chime APIs")
    logger.info("This is playing ground for the Chime APIs. This code will not be executed at runtime")
    logger.info("Chime Services Urls must 1st be configured in ./utils.api_init.py")

    # ================= NAAS API Samples ===================================================================
    # Doing a simple NaaS search for all LTE cells. Returning selected fields only
    logger.info("Getting all LTE cells")
    lte_cells = naas.api.cells.get_cells(params={'technology': 'LTE', 'fields': '_id,name,mcc,mnc,rsi,pci'})

    # logging first 5 cells. Cells are under body['elements'][index]['cell]
    for i in range(5):
        logger.info(lte_cells.body['elements'][i]['cell'])

    # Pagination information. Pagination data is under body['pagination']
    total_cells = lte_cells.body['pagination']['numberOfElements']
    current_page = lte_cells.body['pagination']['currentPage']
    logger.info("Total number of cells: " + str(total_cells))
    logger.info("Current Page: " + str(current_page))

    # Getting next page using continuationId
    continuation_id = lte_cells.body['pagination']['continuationId']
    logger.info("Getting next page of results using continuation token: " + continuation_id)
    lte_cells = naas.api.cells.get_cells(
        params={'continuationId': continuation_id, 'fields': '_id,name,mcc,mnc,rsi,pci'})

    # logging first 5 cells in second page
    for i in range(5):
        logger.info(lte_cells.body['elements'][i]['cell'])
    logger.info("Current Page: " + str(lte_cells.body['pagination']['currentPage']))

    # ================= PGW API Samples ===================================================================
    # Sending a sample Workorder

    # Create a list of workitems.
    # In this example a single RSI change for the 1st cell from the previous search
    work_items = [
        {
            "type": "CHANGE_RSI",
            "_cellId": lte_cells.body['elements'][0]['cell']['_id'],
            "value": 126,
        }
    ]

    # Create a Workorder object. Eahc workorder is assigned a tracking id, that is automatically populated in the
    # application context.
    work_order = {
        'mode': 'OFFLINE_SIM',
        'method': 'NON_TRANSACTION',
        'priority': '1',
        'trackingId': context['TRACKING_ID'],
        'workItems': work_items
    }

    # Submitting the workorder.
    logger.info("Sending workorder: "+str(work_order))

    work_order_res = pgw.api.workorders.send_workorder(body=work_order)

    logger.info("Workorder submitted. Server response: "+str(work_order_res.body))
    logger.info("To track workorder execution follow the link: "+work_order_res.body['links'][0]['href'])


if __name__ == '__main__':
    getting_started()
