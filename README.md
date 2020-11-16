# CHIME Developer Python Application

### Getting Started

#### Introduction
CHIME Developer enables users to build apps faster than ever before and leverage their own IP and methodologies to 
address the specific needs of the operator’s network.\
It includes a fully hosted development environment, that enables simple integration with CHIME services, 
as well as testing and debugging your application code, without leaving the browser.

This sample  application provides a starting point for developing python applications suitable for execution on the CHIME Developer platform.\

For more information about CHIME refer to: [CHIME Platform](https://https://www.cellwize.com/platform) \
For API reference refer to: [CHIME API Reference](https://kb.cellwize.com/display/DPO/API+References)


#### Quick Start
To call your first CHIME API, simply:
* Configure API urls in <b>utils/api_init.py</b>
  ```
  # Configure CHIME Services endpoints
  NAAS_URL = 'http:/<chime-developer-uri>/naas'
  XPAAS_URL = 'https://<chime-developer-uri>/xpaas'
  PGW_URL = 'https://<chime-developer-uri>/pgw'
  AUTH_URL = 'http://<chime-developer-token-uri>'

  # Configure Client_Id and Client_Secret to enable authentication
  CLIENT_ID = None
  CLIENT_SECRET = None
  ```
* Call the API from <b>main.py</b>
    ```
    from utils.logger_config import logger
    from utils.api_init import naas
  
    def main():
      lte_cells_res = naas.api.cells.get_cells(params={'technology': 'LTE'})
      logger.info("Cells: "+str(lte_cells.res.body))
      
    if __name__ == '__main__':
        main()
  ```

#### Project Structure
* <b>main.py</b> Main entry point for the application. 
* <b>requirements.txt</b> Application dependencies configuration.
* <b>getting-started.py</b> Code samples. Run this code and read the comment to learn the basics of using the CHIME SDK.
* <b>config: </b>
    * <b>config.yaml</b> Application configuration. Specify application meta-data as well as application configuration schema.
    * <b>config-test.yaml</b> Configure test values for application parameters, to be used during development.
* <b>utils:</b>
    * <b>api_init.py</b> CHIME API clients initialization.
    * <b>context.py</b> Application context initialization. Do not modify.
    * <b>logger_config</b> Logging configuration. Do not modify.

 


#### Application Configuration
Application configuration is maintained in <b>/config/config.yaml</b>. The configuration consists of 2 main sections:
1. meta - metadata for the application.
2. schema - configuration schema for the application. This is where you configure the application parameters.

Sample configuration:
```yaml
application:
  meta:
    name: chime-app-1
    version: 1.0
    description: This is a prototype chime application
    author: john.doe@cellwize.com
  schema:
    - name: NAAS_CLUSTER
      displayName: NaaS Cluster
      description: Name of NaaS cluster for this application
      defaultValue:
      type: string
      group: General Settings

```
In this example the application requires a single parameter, called <i>NAAS_CLUSTER</i>. You can add additional 
parameters.\
For each parameter specify the following:
* <b>name</b>: Name of the parameter. Please use letters only, and no whitespace.
* <b>displayName</b>: Display name for the parameter, used for UI configuration.
* <b>description</b>: Parameter description.
* <b>defaultValue</b> (Optional): Specify a default value for the parameter, if there is no runtime value provided by the user.
* <b>type</b>: Parameter type.  String, Number and Boolean are supported.
* <b>group</b>: For display purposes parameters can be grouped based on their <i>group</i> value.
 

#### Accessing Application Context
At runtime, CHIME Platform injects the value of each of the parameters defined in <i>config.yaml</i> based on user definition. 
Parameters values are available as environment variables, and are automatically populated into a <i>context</i> 
dictionary object.\
Working with the <i>context</i> object:
```
from utils.context import context

naas_cluster = context.get('NAAS_CLUSTER')

```

##### Test Application Context
During development you may want to set test values for the application parameters.\
To do so edit <i>/config/config-test.yaml</i>\
Specify <i>key: value</i> pairs. For example:
```yaml
NAAS_CLUSTER: TEST_CLUSTER
```

Parameter values in <i>config-test.yaml</i> are only used during development. At runtime the values will be overridden by user defined values.

##### Special Context Parameters
At runtime CHIME injects a set of pre-defined parameters for the convenience of the application developer.
For example, a <i>TRACKING_ID</i> parameters is injected, to track each individual execution of the application at runtime.

####  CHIME Client SDK

##### Overview
CHIME client supports the three main CHIME services <b> NaaS, XPaaS</b> and <b>PGW</b>.\
The CHIME python client library is embedded in the CHIME Developer development and runtime environments. 


##### Client Initialization
To initialize the CHIME client set the API configuration in <b>utils/api_init.py</b>\
Configure the API urls (provided by Cellwize support), as well as your application CLIENT_ID and CLIENT_SECRET to enable authentication.
```
# Configure CHIME Services endpoints
NAAS_URL = 'http:/<chime-developer-uri>/naas'
XPAAS_URL = 'https://<chime-developer-uri>/xpaas'
PGW_URL = 'https://<chime-developer-uri>/pgw'
AUTH_URL = 'http://<chime-developer-token-uri>'

# Configure Client_Id and Client_Secret to enable authentication
CLIENT_ID = None
CLIENT_SECRET = None
```
Once configured, <i>api_init.py</i> initializes 3 client objects that are available throughout the application: <i>naas, xpaas, pgw</i>.
All API calls are routed via an API Gateway, that is responsible for securing the CHIME APIs. The initialization code automatically  authenticates the clients,
and configures them with an access token.

##### Making API Calls
To use a CHIME client, simple import it to your code and invoke the API. For example:
```
from utils.api_init import naas

lte_cells_res = naas.api.cells.get_cells(params={'technology': 'LTE', 'fields': '_id,name,mcc,mnc,rsi,pci'})
```
In the example above we are calling the NaaS  <i>cells</i> resource, invoking the <i>get_cells</i> API. 
The response body is available via the <i>body</i> attribute of the response object. It is a dictionary object representing the json response of the REST API call.
```
lte_cells = lte_cells_res.body
```

###### Query parameters
Sending query string parameters is done via the <i>params</i> attribute, which takes a dictionary (json) as value. 
For example:
```
from utils.api_init import naas

lte_cells = naas.api.cells.get_cells(params={'technology': 'LTE', 'fields': '_id,name,mcc,mnc,rsi,pci'})
```
Translates to the a  request : 
```
GET /naas/v1/cells?technology=LTE&fields=_id,name,mcc,mnc,rsi,pci
```
###### Request Body 
Sending a POST request body is dona via the <i>body</i> attribute, which takes a dictionary (json) as value.
For example, sending a workorder request to PGW:
```
# Preparing a Workorder object
work_order = {
        'mode': 'OFFLINE_SIM',
        'method': 'NON_TRANSACTION',
        'priority': '1',
        'trackingId': context.get('TRACKING_ID'),
        'workItems': work_items
    }

# Sending a Workorder request
work_order_res = pgw.api.workorders.send_workorder(body=work_order)
```
Note that we pass the auto populated <i>TRACKING_ID</i> in the workorder request. This allows CHIME Developer to
correlate the execution of the application and the workorder.

######  Path parameters
Some API calls require a Path parameter. Path parameters are send as explicit values in the API call.
For example, retrieving  all cells of a given cluster:
```
cells = naas.api.clusters.get_cluster_cells('TEST_CLUSTER')
```
Translates to a request:
```
GET /v1/naas/clusters/TEST_CLUSTER/cells
```
Which returns all cells belonging to the pre-defined cluster named <i>TEST_CLUSTER</i>

###### Listing available APIs
You can list available resources for each client by running the following:
```
naas.api.get_resource_list()

['cells', 'clusters', 'controllers', 'mos', 'networkmodel', 'neighbors', 'neural_engine', 'x2links']
```
And for each resource, you can list available APIs:
```
naas.api.cells.actions

{
'get_cells': {'method': 'GET', 'url': '/v1/cells'}, 
'get_cells_next_page': {'method': 'GET', 'url': '/v1/cells'}, 
'search_cells': {'method': 'POST', 'url': '/v1/cells'}, 
'get_cell_by_id': {'method': 'GET', 'url': '/v1/cells/{}'}, 
'get_co_sectors': {'method': 'GET', 'url': '/v1/cells/{}/cosectors'}, 
'get_co_sites': {'method': 'GET', 'url': '/v1/cells/{}/cosites'}, 
'get_neighbors': {'method': 'GET', 'url': '/v1/cells/{}/neighbors'}
}

```

#### Installing Dependencies 
If you application requires additional python packages, you can install them into your workspace using the <b>pip install</b> menu command.\
Configure the required libraries in <b>requirements.txt</b>. For example:
```
PyYAML~=5.3.1
oauthlib~=3.1.0
requests-oauthlib~=1.3.0
```
Use  <i>Terminal --> Run Task</i> to run the pre-defined <b>pip install</b> task. The tasks reads your <i>requirements.txt</i> 
and installs it into the development environment. Make sure to select the python container to install the packages into
the embedded CHIME Developer python plugin.\
CHIME Platform reads the same <i>requirements.txt</i> as part of the application build process, and installs all required
 packages into the runtime environment. This ensures that your dev configuration and runtime configurations are always aligned.
