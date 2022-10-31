# NamesApi

All URIs are relative to *https://api.ionos.com/containerregistries*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**names_check_usage**](NamesApi.md#names_check_usage) | **HEAD** /names/{name} | Get container registry name availability |


# **names_check_usage**
> names_check_usage(name)

Get container registry name availability

Validate that the name is suitable to use for a new registry: - it uses only the characters \"a-z\", \"0-9\", or \"-\" - and starts with a letter and ends with a letter or number - and is between 3 to 63 characters in length - and is available

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
    api_instance = ionoscloud_container_registry.NamesApi(api_client)
    name = 'name_example' # str | The desired registry name
    try:
        # Get container registry name availability
        api_instance.names_check_usage(name)
    except ApiException as e:
        print('Exception when calling NamesApi.names_check_usage: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **name** | **str**| The desired registry name |  |

### Return type

void (empty response body)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

