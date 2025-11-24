# ionoscloud_container_registry.LocationsApi

All URIs are relative to *https://api.ionos.com/containerregistries*

Method | HTTP request | Description
------------- | ------------- | -------------
[**locations_get**](LocationsApi.md#locations_get) | **GET** /locations | Get container registry locations


# **locations_get**
> LocationsResponse locations_get()

Get container registry locations



### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):

```python
import ionoscloud_container_registry
from ionoscloud_container_registry.models.locations_response import LocationsResponse
from ionoscloud_container_registry.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ionos.com/containerregistries
# See configuration.py for a list of all supported configuration parameters.
configuration = ionoscloud_container_registry.Configuration(
    host = "https://api.ionos.com/containerregistries"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = ionoscloud_container_registry.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ionoscloud_container_registry.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_container_registry.LocationsApi(api_client)

    try:
        # Get container registry locations
        api_response = api_instance.locations_get()
        print("The response of LocationsApi->locations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->locations_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**LocationsResponse**](LocationsResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

