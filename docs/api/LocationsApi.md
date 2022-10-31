# LocationsApi

All URIs are relative to *https://api.ionos.com/containerregistries*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**locations_get**](LocationsApi.md#locations_get) | **GET** /locations | Get container registry locations |


# **locations_get**
> LocationsResponse locations_get()

Get container registry locations

### Example

```python
from __future__ import print_function
import time
import ionoscloud_container_registry
from ionoscloud_container_registry.rest import ApiException

# Defining the host is optional and defaults to https://api.ionos.com/containerregistries
configuration = ionoscloud_container_registry.Configuration(
    host = 'https://api.ionos.com/containerregistries',
)

# Example of configuring HTTP Basic Authorization
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

with ionoscloud_container_registry.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_container_registry.LocationsApi(api_client)
    try:
        # Get container registry locations
        api_response = api_instance.locations_get()
        print(api_response)
    except ApiException as e:
        print('Exception when calling LocationsApi.locations_get: %s\n' % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LocationsResponse**](../models/LocationsResponse.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

