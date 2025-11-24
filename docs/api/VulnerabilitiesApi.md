# ionoscloud_container_registry.VulnerabilitiesApi

All URIs are relative to *https://api.ionos.com/containerregistries*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vulnerabilities_find_by_id**](VulnerabilitiesApi.md#vulnerabilities_find_by_id) | **GET** /vulnerabilities/{vulnerabilityId} | Retrieve Vulnerability


# **vulnerabilities_find_by_id**
> VulnerabilityRead vulnerabilities_find_by_id(vulnerability_id)

Retrieve Vulnerability

Returns the Vulnerability by ID.

### Example

* Api Key Authentication (tokenAuth):

```python
import ionoscloud_container_registry
from ionoscloud_container_registry.models.vulnerability_read import VulnerabilityRead
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

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ionoscloud_container_registry.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ionoscloud_container_registry.VulnerabilitiesApi(api_client)
    vulnerability_id = 'CVE-2019-1234' # str | The ID of the Vulnerability.

    try:
        # Retrieve Vulnerability
        api_response = api_instance.vulnerabilities_find_by_id(vulnerability_id)
        print("The response of VulnerabilitiesApi->vulnerabilities_find_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VulnerabilitiesApi->vulnerabilities_find_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vulnerability_id** | **str**| The ID of the Vulnerability. | 

### Return type

[**VulnerabilityRead**](VulnerabilityRead.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Getting Vulnerability was successful. |  -  |
**400** | ### Bad Request The request send to the API was malformed.  |  -  |
**401** | ### Unauthorized The request is missing authorization information or the authorization information provided are expired.  |  -  |
**403** | ### Not Allowed The user issuing the request does not have the needed permissions.  |  -  |
**404** | ### Not Found The resource that was requested could not be found.  |  -  |
**429** | ### Too Many Requests The user has sent too many requests in a given amount of time.  |  -  |
**500** | ### Internal Server Error An internal error occurred. We apologize for the inconvenience!  |  -  |
**503** | ### Service Unavailable The server is currently unable to handle the request due to a temporary overloading or maintenance of the server.  |  -  |
**0** | ### Unexpected Internal Server Error An unexpected internal error occurred. We apologize for the inconvenience!  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

