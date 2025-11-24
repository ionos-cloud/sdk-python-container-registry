# ionoscloud_container_registry.NamesApi

All URIs are relative to *https://api.ionos.com/containerregistries*

Method | HTTP request | Description
------------- | ------------- | -------------
[**names_check_usage**](NamesApi.md#names_check_usage) | **HEAD** /names/{name} | Get container registry name availability


# **names_check_usage**
> names_check_usage(name)

Get container registry name availability

Validate that the name is suitable to use for a new registry:
- it uses only the characters "a-z", "0-9", or "-"
- and starts with a letter and ends with a letter or number
- and is between 3 to 63 characters in length
- and is available

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (tokenAuth):

```python
import ionoscloud_container_registry
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
    api_instance = ionoscloud_container_registry.NamesApi(api_client)
    name = 'name_example' # str | The desired registry name

    try:
        # Get container registry name availability
        api_instance.names_check_usage(name)
    except Exception as e:
        print("Exception when calling NamesApi->names_check_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The desired registry name | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. The registry name is valid but already in use |  -  |
**400** | Bad Request |  -  |
**404** | Not found. The registry name is available and valid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

