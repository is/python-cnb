# cnb_api.RepositoriesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_a_fork**](RepositoriesApi.md#create_a_fork) | **POST** /{repo}/-/forks | fork 仓库。Fork a repository.
[**create_repo**](RepositoriesApi.md#create_repo) | **POST** /{group}/-/repos | 创建仓库。Create repositories.
[**delete_repo**](RepositoriesApi.md#delete_repo) | **DELETE** /{repo} | 删除指定仓库。Delete the specified repository.
[**get_group_sub_repos**](RepositoriesApi.md#get_group_sub_repos) | **GET** /{group}/-/repos | 查询组织下访问用户有权限查看到仓库。List the repositories that the user has access to.
[**get_pinned_repo_by_group**](RepositoriesApi.md#get_pinned_repo_by_group) | **GET** /{group}/-/pinned-repos | 获取指定组织的仓库墙列表。List the pinned repositories of a group.
[**get_pinned_repo_by_id**](RepositoriesApi.md#get_pinned_repo_by_id) | **GET** /users/{username}/pinned-repos | 获取指定用户的用户仓库墙。 Get a list of repositories that the specified user has pinned.
[**get_repo**](RepositoriesApi.md#get_repo) | **GET** /{repo} | 获取指定仓库信息。Get information for the specified repository.
[**get_repos**](RepositoriesApi.md#get_repos) | **GET** /user/repos | 获取当前用户拥有指定权限及其以上权限的仓库。List repositories owned by the current user with the specified permissions or higher.
[**get_repos_by_user_name**](RepositoriesApi.md#get_repos_by_user_name) | **GET** /users/{username}/repos | 获取指定用户有指定以上权限并且客人态可见的仓库。List repositories where the specified user has the specified permission level or higher and are visible to guests.
[**get_user_all_stared_repos**](RepositoriesApi.md#get_user_all_stared_repos) | **GET** /user/stared-repos | 获取当前用户 star 的仓库列表。List all stared repositories.
[**list_forks_repos**](RepositoriesApi.md#list_forks_repos) | **GET** /{repo}/-/forks | 获取指定仓库的 fork 列表。Get fork list for specified repository.
[**set_pinned_repo_by_group**](RepositoriesApi.md#set_pinned_repo_by_group) | **PUT** /{group}/-/pinned-repos | 更新指定组织仓库墙。Update the pinned repositories of a group.
[**update_repo**](RepositoriesApi.md#update_repo) | **PATCH** /{repo} | 更新仓库信息, 可更新的内容为: 仓库简介, 仓库站点, 仓库主题, 开源许可证。updates repository details including description, website URL,topics and license type.


# **create_a_fork**
> create_a_fork(repo, request)

fork 仓库。Fork a repository.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
group-resource:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_fork_req import DtoForkReq
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
    api_instance = cnb_api.RepositoriesApi(api_client)
    repo = 'repo_example' # str | slug
    request = cnb_api.DtoForkReq() # DtoForkReq | target

    try:
        # fork 仓库。Fork a repository.
        api_instance.create_a_fork(repo, request)
    except Exception as e:
        print("Exception when calling RepositoriesApi->create_a_fork: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| slug | 
 **request** | [**DtoForkReq**](DtoForkReq.md)| target | 

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
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repo**
> create_repo(group, request)

创建仓库。Create repositories.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
group-resource:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_create_repo_req import DtoCreateRepoReq
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
    api_instance = cnb_api.RepositoriesApi(api_client)
    group = 'hello' # str | Group slug (default to 'hello')
    request = cnb_api.DtoCreateRepoReq() # DtoCreateRepoReq | repo information

    try:
        # 创建仓库。Create repositories.
        api_instance.create_repo(group, request)
    except Exception as e:
        print("Exception when calling RepositoriesApi->create_repo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| Group slug | [default to &#39;hello&#39;]
 **request** | [**DtoCreateRepoReq**](DtoCreateRepoReq.md)| repo information | 

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
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_repo**
> delete_repo(repo, x_cnb_identity_ticket=x_cnb_identity_ticket)

删除指定仓库。Delete the specified repository.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-delete:rw

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
    api_instance = cnb_api.RepositoriesApi(api_client)
    repo = 'repo_example' # str | repo path
    x_cnb_identity_ticket = 'x_cnb_identity_ticket_example' # str | 微信身份验证票据，首次请求不传会返回新票据。WeChat auth ticket, will return new ticket if not provided in first request. (optional)

    try:
        # 删除指定仓库。Delete the specified repository.
        api_instance.delete_repo(repo, x_cnb_identity_ticket=x_cnb_identity_ticket)
    except Exception as e:
        print("Exception when calling RepositoriesApi->delete_repo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo path | 
 **x_cnb_identity_ticket** | **str**| 微信身份验证票据，首次请求不传会返回新票据。WeChat auth ticket, will return new ticket if not provided in first request. | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_sub_repos**
> List[DtoRepos4UserBase] get_group_sub_repos(group, page=page, page_size=page_size, filter_type=filter_type, order_by=order_by, desc=desc, descendant=descendant, search=search)

查询组织下访问用户有权限查看到仓库。List the repositories that the user has access to.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
group-resource:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_repos4_user_base import DtoRepos4UserBase
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
    api_instance = cnb_api.RepositoriesApi(api_client)
    group = 'group_example' # str | slug
    page = 1 # int | Pagination page number (optional) (default to 1)
    page_size = 10 # int | Pagination page size (optional) (default to 10)
    filter_type = 'filter_type_example' # str | Repositories type (optional)
    order_by = 'order_by_example' # str | Order field，default(last_updated_at) (optional)
    desc = False # bool | Ordering (optional) (default to False)
    descendant = 'descendant_example' # str | 查全部/查询直接属于当前组织的仓库/查询子组织的仓库。Get all/Get repos belong to current org or sub-orgs (optional)
    search = 'search_example' # str | Key word (optional)

    try:
        # 查询组织下访问用户有权限查看到仓库。List the repositories that the user has access to.
        api_response = api_instance.get_group_sub_repos(group, page=page, page_size=page_size, filter_type=filter_type, order_by=order_by, desc=desc, descendant=descendant, search=search)
        print("The response of RepositoriesApi->get_group_sub_repos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoriesApi->get_group_sub_repos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| slug | 
 **page** | **int**| Pagination page number | [optional] [default to 1]
 **page_size** | **int**| Pagination page size | [optional] [default to 10]
 **filter_type** | **str**| Repositories type | [optional] 
 **order_by** | **str**| Order field，default(last_updated_at) | [optional] 
 **desc** | **bool**| Ordering | [optional] [default to False]
 **descendant** | **str**| 查全部/查询直接属于当前组织的仓库/查询子组织的仓库。Get all/Get repos belong to current org or sub-orgs | [optional] 
 **search** | **str**| Key word | [optional] 

### Return type

[**List[DtoRepos4UserBase]**](DtoRepos4UserBase.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.cnb.api+json, application/vnd.cnb.web+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pinned_repo_by_group**
> List[DtoRepos4UserBase] get_pinned_repo_by_group(group)

获取指定组织的仓库墙列表。List the pinned repositories of a group.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
group-manage:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_repos4_user_base import DtoRepos4UserBase
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
    api_instance = cnb_api.RepositoriesApi(api_client)
    group = 'group_example' # str | slug

    try:
        # 获取指定组织的仓库墙列表。List the pinned repositories of a group.
        api_response = api_instance.get_pinned_repo_by_group(group)
        print("The response of RepositoriesApi->get_pinned_repo_by_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoriesApi->get_pinned_repo_by_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| slug | 

### Return type

[**List[DtoRepos4UserBase]**](DtoRepos4UserBase.md)

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

# **get_pinned_repo_by_id**
> List[DtoRepos4User] get_pinned_repo_by_id(username)

获取指定用户的用户仓库墙。 Get a list of repositories that the specified user has pinned.

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
    api_instance = cnb_api.RepositoriesApi(api_client)
    username = 'someone' # str | User Name (default to 'someone')

    try:
        # 获取指定用户的用户仓库墙。 Get a list of repositories that the specified user has pinned.
        api_response = api_instance.get_pinned_repo_by_id(username)
        print("The response of RepositoriesApi->get_pinned_repo_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoriesApi->get_pinned_repo_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| User Name | [default to &#39;someone&#39;]

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

# **get_repo**
> DtoRepos4User get_repo(repo)

获取指定仓库信息。Get information for the specified repository.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-basic-info:r

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
    api_instance = cnb_api.RepositoriesApi(api_client)
    repo = 'repo_example' # str | repo path

    try:
        # 获取指定仓库信息。Get information for the specified repository.
        api_response = api_instance.get_repo(repo)
        print("The response of RepositoriesApi->get_repo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoriesApi->get_repo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo path | 

### Return type

[**DtoRepos4User**](DtoRepos4User.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.cnb.api+json, application/vnd.cnb.web+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | repo |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repos**
> List[DtoRepos4User] get_repos(page=page, page_size=page_size, search=search, filter_type=filter_type, role=role, order_by=order_by, desc=desc)

获取当前用户拥有指定权限及其以上权限的仓库。List repositories owned by the current user with the specified permissions or higher.

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
    api_instance = cnb_api.RepositoriesApi(api_client)
    page = 1 # int | Pagination page number (optional) (default to 1)
    page_size = 10 # int | Pagination page size (optional) (default to 10)
    search = 'search_example' # str | Filter by repositories (optional)
    filter_type = 'filter_type_example' # str | Type (optional)
    role = owner # str | 最小仓库权限，默认owner。Minima repository permissions, default(owner) (optional) (default to owner)
    order_by = 'order_by_example' # str | Order field，default(last_updated_at) (optional)
    desc = False # bool | 排序顺序。Ordering. (optional) (default to False)

    try:
        # 获取当前用户拥有指定权限及其以上权限的仓库。List repositories owned by the current user with the specified permissions or higher.
        api_response = api_instance.get_repos(page=page, page_size=page_size, search=search, filter_type=filter_type, role=role, order_by=order_by, desc=desc)
        print("The response of RepositoriesApi->get_repos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoriesApi->get_repos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Pagination page number | [optional] [default to 1]
 **page_size** | **int**| Pagination page size | [optional] [default to 10]
 **search** | **str**| Filter by repositories | [optional] 
 **filter_type** | **str**| Type | [optional] 
 **role** | **str**| 最小仓库权限，默认owner。Minima repository permissions, default(owner) | [optional] [default to owner]
 **order_by** | **str**| Order field，default(last_updated_at) | [optional] 
 **desc** | **bool**| 排序顺序。Ordering. | [optional] [default to False]

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

# **get_repos_by_user_name**
> List[DtoRepos4User] get_repos_by_user_name(username, search=search, role=role, page=page, page_size=page_size, desc=desc, order_by=order_by)

获取指定用户有指定以上权限并且客人态可见的仓库。List repositories where the specified user has the specified permission level or higher and are visible to guests.

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
    api_instance = cnb_api.RepositoriesApi(api_client)
    username = 'someone' # str | UserName (default to 'someone')
    search = 'search_example' # str | Filter by repositories (optional)
    role = owner # str | 最小仓库权限，默认owner。Minima repository permissions, default(owner). (optional) (default to owner)
    page = 1 # int | Pagination page number (optional) (default to 1)
    page_size = 10 # int | Pagination page size (optional) (default to 10)
    desc = False # bool | 排序顺序。Ordering. (optional) (default to False)
    order_by = 'order_by_example' # str | Order field，default(last_updated_at) (optional)

    try:
        # 获取指定用户有指定以上权限并且客人态可见的仓库。List repositories where the specified user has the specified permission level or higher and are visible to guests.
        api_response = api_instance.get_repos_by_user_name(username, search=search, role=role, page=page, page_size=page_size, desc=desc, order_by=order_by)
        print("The response of RepositoriesApi->get_repos_by_user_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoriesApi->get_repos_by_user_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| UserName | [default to &#39;someone&#39;]
 **search** | **str**| Filter by repositories | [optional] 
 **role** | **str**| 最小仓库权限，默认owner。Minima repository permissions, default(owner). | [optional] [default to owner]
 **page** | **int**| Pagination page number | [optional] [default to 1]
 **page_size** | **int**| Pagination page size | [optional] [default to 10]
 **desc** | **bool**| 排序顺序。Ordering. | [optional] [default to False]
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

# **get_user_all_stared_repos**
> List[DtoRepos4UserBase] get_user_all_stared_repos(page=page, page_size=page_size, search=search, desc=desc, order_by=order_by)

获取当前用户 star 的仓库列表。List all stared repositories.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
account-engage:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_repos4_user_base import DtoRepos4UserBase
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
    api_instance = cnb_api.RepositoriesApi(api_client)
    page = 1 # int | Pagination page number (optional) (default to 1)
    page_size = 10 # int | Pagination page size (optional) (default to 10)
    search = 'search_example' # str | Filter by repositories (optional)
    desc = False # bool | 排序顺序。Ordering. (optional) (default to False)
    order_by = 'order_by_example' # str | Order field，default(last_updated_at) (optional)

    try:
        # 获取当前用户 star 的仓库列表。List all stared repositories.
        api_response = api_instance.get_user_all_stared_repos(page=page, page_size=page_size, search=search, desc=desc, order_by=order_by)
        print("The response of RepositoriesApi->get_user_all_stared_repos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoriesApi->get_user_all_stared_repos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Pagination page number | [optional] [default to 1]
 **page_size** | **int**| Pagination page size | [optional] [default to 10]
 **search** | **str**| Filter by repositories | [optional] 
 **desc** | **bool**| 排序顺序。Ordering. | [optional] [default to False]
 **order_by** | **str**| Order field，default(last_updated_at) | [optional] 

### Return type

[**List[DtoRepos4UserBase]**](DtoRepos4UserBase.md)

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

# **list_forks_repos**
> List[DtoForks] list_forks_repos(repo, page, page_size)

获取指定仓库的 fork 列表。Get fork list for specified repository.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-base-info:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_forks import DtoForks
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
    api_instance = cnb_api.RepositoriesApi(api_client)
    repo = 'repo_example' # str | slug
    page = 1 # int | Pagination page numbe (default to 1)
    page_size = 10 # int | Pagination page size (default to 10)

    try:
        # 获取指定仓库的 fork 列表。Get fork list for specified repository.
        api_response = api_instance.list_forks_repos(repo, page, page_size)
        print("The response of RepositoriesApi->list_forks_repos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoriesApi->list_forks_repos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| slug | 
 **page** | **int**| Pagination page numbe | [default to 1]
 **page_size** | **int**| Pagination page size | [default to 10]

### Return type

[**List[DtoForks]**](DtoForks.md)

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

# **set_pinned_repo_by_group**
> List[DtoRepos4UserBase] set_pinned_repo_by_group(group, request)

更新指定组织仓库墙。Update the pinned repositories of a group.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
group-manage:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_repos4_user_base import DtoRepos4UserBase
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
    api_instance = cnb_api.RepositoriesApi(api_client)
    group = 'group_example' # str | slug
    request = ['request_example'] # List[str] | repo path

    try:
        # 更新指定组织仓库墙。Update the pinned repositories of a group.
        api_response = api_instance.set_pinned_repo_by_group(group, request)
        print("The response of RepositoriesApi->set_pinned_repo_by_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoriesApi->set_pinned_repo_by_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| slug | 
 **request** | [**List[str]**](str.md)| repo path | 

### Return type

[**List[DtoRepos4UserBase]**](DtoRepos4UserBase.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/vnd.cnb.api+json, application/vnd.cnb.web+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repo**
> update_repo(repo, request)

更新仓库信息, 可更新的内容为: 仓库简介, 仓库站点, 仓库主题, 开源许可证。updates repository details including description, website URL,topics and license type.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-manage:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_repo_patch import DtoRepoPatch
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
    api_instance = cnb_api.RepositoriesApi(api_client)
    repo = 'repo_example' # str | repo path
    request = cnb_api.DtoRepoPatch() # DtoRepoPatch | request body

    try:
        # 更新仓库信息, 可更新的内容为: 仓库简介, 仓库站点, 仓库主题, 开源许可证。updates repository details including description, website URL,topics and license type.
        api_instance.update_repo(repo, request)
    except Exception as e:
        print("Exception when calling RepositoriesApi->update_repo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo path | 
 **request** | [**DtoRepoPatch**](DtoRepoPatch.md)| request body | 

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

