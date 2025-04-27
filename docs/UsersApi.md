# cnb_api.UsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auto_complete_source**](UsersApi.md#auto_complete_source) | **GET** /user/autocomplete_source | 查询当前用户用户拥有指定权限的所有资源列表。List resources that the current user has specified permissions for.
[**get_user_info**](UsersApi.md#get_user_info) | **GET** /user | 获取指定用户的详情信息。Get detailed information for a specified user.
[**get_user_info_by_name**](UsersApi.md#get_user_info_by_name) | **GET** /users/{username} | 获取指定用户的详情信息。Get detailed information for a specified user.
[**update_user_info**](UsersApi.md#update_user_info) | **POST** /user | 更新指定用户的详情信息。Updates the specified user&#39;s profile information.


# **auto_complete_source**
> List[str] auto_complete_source(source_type=source_type, page=page, page_size=page_size, search=search, access=access)

查询当前用户用户拥有指定权限的所有资源列表。List resources that the current user has specified permissions for.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
account-engage:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cnb_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerAuth
configuration.api_key['BearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with cnb_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cnb_api.UsersApi(api_client)
    source_type = group # str | Source type, default(group) (optional) (default to group)
    page = 1 # int | Pagination page number (optional) (default to 1)
    page_size = 10 # int | Pagination page size (optional) (default to 10)
    search = 'search_example' # str | Filter by resources. (optional)
    access = owner # str | 最小仓库权限，默认owner。Minima repository permissions, default(owner) (optional) (default to owner)

    try:
        # 查询当前用户用户拥有指定权限的所有资源列表。List resources that the current user has specified permissions for.
        api_response = api_instance.auto_complete_source(source_type=source_type, page=page, page_size=page_size, search=search, access=access)
        print("The response of UsersApi->auto_complete_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->auto_complete_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_type** | **str**| Source type, default(group) | [optional] [default to group]
 **page** | **int**| Pagination page number | [optional] [default to 1]
 **page_size** | **int**| Pagination page size | [optional] [default to 10]
 **search** | **str**| Filter by resources. | [optional] 
 **access** | **str**| 最小仓库权限，默认owner。Minima repository permissions, default(owner) | [optional] [default to owner]

### Return type

**List[str]**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.cnb.api+json, application/vnd.cnb.web+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_info**
> DtoUsersResultForSelf get_user_info()

获取指定用户的详情信息。Get detailed information for a specified user.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
account-profile:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_users_result_for_self import DtoUsersResultForSelf
from cnb_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cnb_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerAuth
configuration.api_key['BearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with cnb_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cnb_api.UsersApi(api_client)

    try:
        # 获取指定用户的详情信息。Get detailed information for a specified user.
        api_response = api_instance.get_user_info()
        print("The response of UsersApi->get_user_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_info: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DtoUsersResultForSelf**](DtoUsersResultForSelf.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.cnb.api+json, application/vnd.cnb.web+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_info_by_name**
> DtoUsersResult get_user_info_by_name(username)

获取指定用户的详情信息。Get detailed information for a specified user.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
account-profile:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_users_result import DtoUsersResult
from cnb_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cnb_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerAuth
configuration.api_key['BearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with cnb_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cnb_api.UsersApi(api_client)
    username = 'someone' # str | User Name (default to 'someone')

    try:
        # 获取指定用户的详情信息。Get detailed information for a specified user.
        api_response = api_instance.get_user_info_by_name(username)
        print("The response of UsersApi->get_user_info_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_info_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| User Name | [default to &#39;someone&#39;]

### Return type

[**DtoUsersResult**](DtoUsersResult.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.cnb.api+json, application/vnd.cnb.web+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_info**
> update_user_info(request)

更新指定用户的详情信息。Updates the specified user's profile information.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
account-profile:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.http_update_user_info_payload import HttpUpdateUserInfoPayload
from cnb_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cnb_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerAuth
configuration.api_key['BearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with cnb_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cnb_api.UsersApi(api_client)
    request = cnb_api.HttpUpdateUserInfoPayload() # HttpUpdateUserInfoPayload | user info

    try:
        # 更新指定用户的详情信息。Updates the specified user's profile information.
        api_instance.update_user_info(request)
    except Exception as e:
        print("Exception when calling UsersApi->update_user_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**HttpUpdateUserInfoPayload**](HttpUpdateUserInfoPayload.md)| user info | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

