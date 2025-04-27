# cnb_api.StarringApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_stared_repos**](StarringApi.md#get_user_stared_repos) | **GET** /users/{username}/stared-repos | 获取指定用户的 star 仓库列表。Get the list of repositories starred by the specified user.
[**list_star_users**](StarringApi.md#list_star_users) | **GET** /{repo}/-/stars | 获取指定仓库的star用户列表。Get the list of users who starred the specified repository.


# **get_user_stared_repos**
> List[DtoRepos4User] get_user_stared_repos(username, search=search, page=page, page_size=page_size, desc=desc, order_by=order_by)

获取指定用户的 star 仓库列表。Get the list of repositories starred by the specified user.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
account-engage:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_repos4_user import DtoRepos4User
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
    api_instance = cnb_api.StarringApi(api_client)
    username = 'someone' # str | UserName (default to 'someone')
    search = 'search_example' # str | 过滤仓库。Filter by repositories (optional)
    page = 1 # int | Pagination page number (optional) (default to 1)
    page_size = 10 # int | Pagination page size (optional) (default to 10)
    desc = False # bool | Ordering (optional) (default to False)
    order_by = 'order_by_example' # str | Order field，default(last_updated_at) (optional)

    try:
        # 获取指定用户的 star 仓库列表。Get the list of repositories starred by the specified user.
        api_response = api_instance.get_user_stared_repos(username, search=search, page=page, page_size=page_size, desc=desc, order_by=order_by)
        print("The response of StarringApi->get_user_stared_repos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StarringApi->get_user_stared_repos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| UserName | [default to &#39;someone&#39;]
 **search** | **str**| 过滤仓库。Filter by repositories | [optional] 
 **page** | **int**| Pagination page number | [optional] [default to 1]
 **page_size** | **int**| Pagination page size | [optional] [default to 10]
 **desc** | **bool**| Ordering | [optional] [default to False]
 **order_by** | **str**| Order field，default(last_updated_at) | [optional] 

### Return type

[**List[DtoRepos4User]**](DtoRepos4User.md)

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

# **list_star_users**
> DtoRepoStarUsers list_star_users(repo, filter_type, page, page_size)

获取指定仓库的star用户列表。Get the list of users who starred the specified repository.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-basic-info:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_repo_star_users import DtoRepoStarUsers
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
    api_instance = cnb_api.StarringApi(api_client)
    repo = 'repo_example' # str | slug
    filter_type = 'filter_type_example' # str | Filter type
    page = 1 # int | page (default to 1)
    page_size = 10 # int | page (default to 10)

    try:
        # 获取指定仓库的star用户列表。Get the list of users who starred the specified repository.
        api_response = api_instance.list_star_users(repo, filter_type, page, page_size)
        print("The response of StarringApi->list_star_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StarringApi->list_star_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| slug | 
 **filter_type** | **str**| Filter type | 
 **page** | **int**| page | [default to 1]
 **page_size** | **int**| page | [default to 10]

### Return type

[**DtoRepoStarUsers**](DtoRepoStarUsers.md)

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

