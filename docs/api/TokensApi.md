# TokensApi

All URIs are relative to *https://api.ionos.com/containerregistries*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**registries_tokens_delete**](TokensApi.md#registries_tokens_delete) | **DELETE** /registries/{registryId}/tokens/{tokenId} | Delete token |
| [**registries_tokens_find_by_id**](TokensApi.md#registries_tokens_find_by_id) | **GET** /registries/{registryId}/tokens/{tokenId} | Get token information |
| [**registries_tokens_get**](TokensApi.md#registries_tokens_get) | **GET** /registries/{registryId}/tokens | List all tokens for the container registry |
| [**registries_tokens_patch**](TokensApi.md#registries_tokens_patch) | **PATCH** /registries/{registryId}/tokens/{tokenId} | Update token |
| [**registries_tokens_post**](TokensApi.md#registries_tokens_post) | **POST** /registries/{registryId}/tokens | Create token |
| [**registries_tokens_put**](TokensApi.md#registries_tokens_put) | **PUT** /registries/{registryId}/tokens/{tokenId} | Create or replace token |


# **registries_tokens_delete**
> registries_tokens_delete(registry_id, token_id)

Delete token

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
    api_instance = ionoscloud_container_registry.TokensApi(api_client)
    registry_id = 'registry_id_example' # str | The unique ID of the registry
    token_id = 'token_id_example' # str | The unique ID of the token
    try:
        # Delete token
        api_instance.registries_tokens_delete(registry_id, token_id)
    except ApiException as e:
        print('Exception when calling TokensApi.registries_tokens_delete: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **registry_id** | [**str**](.md)| The unique ID of the registry |  |
| **token_id** | [**str**](.md)| The unique ID of the token |  |

### Return type

void (empty response body)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **registries_tokens_find_by_id**
> TokenResponse registries_tokens_find_by_id(registry_id, token_id)

Get token information

Gets all information for a specific token used to access a container registry

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
    api_instance = ionoscloud_container_registry.TokensApi(api_client)
    registry_id = 'registry_id_example' # str | The unique ID of the registry
    token_id = 'token_id_example' # str | The unique ID of the token
    try:
        # Get token information
        api_response = api_instance.registries_tokens_find_by_id(registry_id, token_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling TokensApi.registries_tokens_find_by_id: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **registry_id** | [**str**](.md)| The unique ID of the registry |  |
| **token_id** | [**str**](.md)| The unique ID of the token |  |

### Return type

[**TokenResponse**](../models/TokenResponse.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **registries_tokens_get**
> TokensResponse registries_tokens_get(registry_id, offset=offset, limit=limit)

List all tokens for the container registry

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
    api_instance = ionoscloud_container_registry.TokensApi(api_client)
    registry_id = 'registry_id_example' # str | The unique ID of the registry
    try:
        # List all tokens for the container registry
        api_response = api_instance.registries_tokens_get(registry_id)
        print(api_response)
    except ApiException as e:
        print('Exception when calling TokensApi.registries_tokens_get: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **registry_id** | [**str**](.md)| The unique ID of the registry |  |
| **offset** | **str**| The first element (from the complete list of the elements) to include in the response (used together with limit for pagination) | [optional] [default to &#39;0&#39;] |
| **limit** | **str**| The maximum number of elements to return (used together with offset for pagination) | [optional] [default to &#39;100&#39;] |

### Return type

[**TokensResponse**](../models/TokensResponse.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

# **registries_tokens_patch**
> TokenResponse registries_tokens_patch(registry_id, token_id, patch_token_input)

Update token

Update token properties, for example: - change status to 'enabled' or 'disabled' - change expiry date

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
    api_instance = ionoscloud_container_registry.TokensApi(api_client)
    registry_id = 'registry_id_example' # str | The unique ID of the registry
    token_id = 'token_id_example' # str | The unique ID of the token
    patch_token_input = ionoscloud_container_registry.PatchTokenInput() # PatchTokenInput | 
    try:
        # Update token
        api_response = api_instance.registries_tokens_patch(registry_id, token_id, patch_token_input)
        print(api_response)
    except ApiException as e:
        print('Exception when calling TokensApi.registries_tokens_patch: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **registry_id** | [**str**](.md)| The unique ID of the registry |  |
| **token_id** | [**str**](.md)| The unique ID of the token |  |
| **patch_token_input** | [**PatchTokenInput**](PatchTokenInput.md)|  |  |

### Return type

[**TokenResponse**](../models/TokenResponse.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **registries_tokens_post**
> PostTokenOutput registries_tokens_post(registry_id, post_token_input)

Create token

Create a token - password is only available once in the POST response

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
    api_instance = ionoscloud_container_registry.TokensApi(api_client)
    registry_id = 'registry_id_example' # str | The unique ID of the registry
    post_token_input = ionoscloud_container_registry.PostTokenInput() # PostTokenInput | 
    try:
        # Create token
        api_response = api_instance.registries_tokens_post(registry_id, post_token_input)
        print(api_response)
    except ApiException as e:
        print('Exception when calling TokensApi.registries_tokens_post: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **registry_id** | [**str**](.md)| The unique ID of the registry |  |
| **post_token_input** | [**PostTokenInput**](PostTokenInput.md)|  |  |

### Return type

[**PostTokenOutput**](../models/PostTokenOutput.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

# **registries_tokens_put**
> PutTokenOutput registries_tokens_put(registry_id, token_id, put_token_input)

Create or replace token

Create/replace a token - password is only available once in the create response - \"name\" cannot be changed

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
    api_instance = ionoscloud_container_registry.TokensApi(api_client)
    registry_id = 'registry_id_example' # str | The unique ID of the registry
    token_id = 'token_id_example' # str | The unique ID of the token
    put_token_input = ionoscloud_container_registry.PutTokenInput() # PutTokenInput | 
    try:
        # Create or replace token
        api_response = api_instance.registries_tokens_put(registry_id, token_id, put_token_input)
        print(api_response)
    except ApiException as e:
        print('Exception when calling TokensApi.registries_tokens_put: %s\n' % e)
```

### Parameters

| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **registry_id** | [**str**](.md)| The unique ID of the registry |  |
| **token_id** | **str**| The unique ID of the token |  |
| **put_token_input** | [**PutTokenInput**](PutTokenInput.md)|  |  |

### Return type

[**PutTokenOutput**](../models/PutTokenOutput.md)

### Authorization

basicAuth, tokenAuth

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

