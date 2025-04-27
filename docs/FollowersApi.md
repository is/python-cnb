# cnb_api.FollowersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_followers_by_user_id**](FollowersApi.md#get_followers_by_user_id) | **GET** /users/{username}/followers | 获取指定用户的粉丝列表。Get the followers list of specified user.
[**get_following_by_user_id**](FollowersApi.md#get_following_by_user_id) | **GET** /users/{username}/following | 获取指定用户的关注人列表。Get the list of users that the specified user is following.


# **get_followers_by_user_id**
> List[DtoUserFollowResult] get_followers_by_user_id(username, page=page, page_size=page_size)

获取指定用户的粉丝列表。Get the followers list of specified user.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
account-engage:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_user_follow_result import DtoUserFollowResult
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
    api_instance = cnb_api.FollowersApi(api_client)
    username = 'someone' # str | User Name (default to 'someone')
    page = 1 # int | Pagination page number (optional) (default to 1)
    page_size = 10 # int | Pagination page size (optional) (default to 10)

    try:
        # 获取指定用户的粉丝列表。Get the followers list of specified user.
        api_response = api_instance.get_followers_by_user_id(username, page=page, page_size=page_size)
        print("The response of FollowersApi->get_followers_by_user_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FollowersApi->get_followers_by_user_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| User Name | [default to &#39;someone&#39;]
 **page** | **int**| Pagination page number | [optional] [default to 1]
 **page_size** | **int**| Pagination page size | [optional] [default to 10]

### Return type

[**List[DtoUserFollowResult]**](DtoUserFollowResult.md)

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

# **get_following_by_user_id**
> List[DtoUserFollowResult] get_following_by_user_id(username, page=page, page_size=page_size)

获取指定用户的关注人列表。Get the list of users that the specified user is following.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
account-engage:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_user_follow_result import DtoUserFollowResult
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
    api_instance = cnb_api.FollowersApi(api_client)
    username = 'someone' # str | User Name (default to 'someone')
    page = 1 # int | Pagination page number (optional) (default to 1)
    page_size = 10 # int | Pagination page size (optional) (default to 10)

    try:
        # 获取指定用户的关注人列表。Get the list of users that the specified user is following.
        api_response = api_instance.get_following_by_user_id(username, page=page, page_size=page_size)
        print("The response of FollowersApi->get_following_by_user_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FollowersApi->get_following_by_user_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| User Name | [default to &#39;someone&#39;]
 **page** | **int**| Pagination page number | [optional] [default to 1]
 **page_size** | **int**| Pagination page size | [optional] [default to 10]

### Return type

[**List[DtoUserFollowResult]**](DtoUserFollowResult.md)

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

