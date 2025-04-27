# cnb_api.CollaboratorsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_members_of_group**](CollaboratorsApi.md#add_members_of_group) | **POST** /{group}/-/members/{username} | 添加成员。Add members.
[**add_members_of_mission**](CollaboratorsApi.md#add_members_of_mission) | **POST** /{mission}/-/members/{username} | 添加成员。Add members.
[**add_members_of_registry**](CollaboratorsApi.md#add_members_of_registry) | **POST** /{registry}/-/members/{username} | 添加成员。Add members.
[**add_members_of_repo**](CollaboratorsApi.md#add_members_of_repo) | **POST** /{repo}/-/members/{username} | 添加成员。Add members.
[**delete_members_of_group**](CollaboratorsApi.md#delete_members_of_group) | **DELETE** /{group}/-/members/{username} | 删除指定组织或仓库的直接成员。Remove direct members from specified organization/repository.
[**delete_members_of_repo**](CollaboratorsApi.md#delete_members_of_repo) | **DELETE** /{repo}/-/members/{username} | 删除指定组织或仓库的直接成员。Remove direct members from specified organization/repository.
[**delete_outside_collaborators**](CollaboratorsApi.md#delete_outside_collaborators) | **DELETE** /{repo}/-/outside-collaborators/{username} | 删除指定仓库的外部贡献者。Removes external contributors from specified repository.
[**list_all_members**](CollaboratorsApi.md#list_all_members) | **GET** /{repo}/-/list-members | 获取指定仓库内的有效成员列表，包含继承成员。List active members in specified repository including inherited members.
[**list_inherit_members_of_group**](CollaboratorsApi.md#list_inherit_members_of_group) | **GET** /{group}/-/inherit-members | 获取指定组织或仓库内的继承成员。List inherited members within specified organization or repository。
[**list_inherit_members_of_repo**](CollaboratorsApi.md#list_inherit_members_of_repo) | **GET** /{repo}/-/inherit-members | 获取指定组织或仓库内的继承成员。List inherited members within specified organization or repository。
[**list_members_of_group**](CollaboratorsApi.md#list_members_of_group) | **GET** /{group}/-/members | 获取指定组织或仓库内的所有直接成员。List all direct members within specified organization or repository.
[**list_members_of_repo**](CollaboratorsApi.md#list_members_of_repo) | **GET** /{repo}/-/members | 获取指定组织或仓库内的所有直接成员。List all direct members within specified organization or repository.
[**list_outside_collaborators**](CollaboratorsApi.md#list_outside_collaborators) | **GET** /{repo}/-/outside-collaborators | 获取指定仓库内的外部贡献者。List external contributors in specified repository.
[**top_contributors**](CollaboratorsApi.md#top_contributors) | **GET** /{repo}/-/top-activity-users | 获取 top 贡献用户。List the top contributing users
[**update_members_of_group**](CollaboratorsApi.md#update_members_of_group) | **PUT** /{group}/-/members/{username} | 更新指定组织或仓库内的直接成员权限信息。Update permission information for direct members in specified organization/repository.
[**update_members_of_repo**](CollaboratorsApi.md#update_members_of_repo) | **PUT** /{repo}/-/members/{username} | 更新指定组织或仓库内的直接成员权限信息。Update permission information for direct members in specified organization/repository.
[**update_outside_collaborators**](CollaboratorsApi.md#update_outside_collaborators) | **PUT** /{repo}/-/outside-collaborators/{username} | 更新指定仓库的外部贡献者权限信息。 Update permission information for external contributors in specified repository.


# **add_members_of_group**
> add_members_of_group(group, username, request)

添加成员。Add members.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
group-manage:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_update_members_request import DtoUpdateMembersRequest
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
    api_instance = cnb_api.CollaboratorsApi(api_client)
    group = 'group_example' # str | slug
    username = 'username_example' # str | username
    request = cnb_api.DtoUpdateMembersRequest() # DtoUpdateMembersRequest | member information

    try:
        # 添加成员。Add members.
        api_instance.add_members_of_group(group, username, request)
    except Exception as e:
        print("Exception when calling CollaboratorsApi->add_members_of_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| slug | 
 **username** | **str**| username | 
 **request** | [**DtoUpdateMembersRequest**](DtoUpdateMembersRequest.md)| member information | 

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

# **add_members_of_mission**
> add_members_of_mission(mission, username, request)

添加成员。Add members.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
mission-manage:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_update_members_request import DtoUpdateMembersRequest
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
    api_instance = cnb_api.CollaboratorsApi(api_client)
    mission = 'mission_example' # str | slug
    username = 'username_example' # str | username
    request = cnb_api.DtoUpdateMembersRequest() # DtoUpdateMembersRequest | member information

    try:
        # 添加成员。Add members.
        api_instance.add_members_of_mission(mission, username, request)
    except Exception as e:
        print("Exception when calling CollaboratorsApi->add_members_of_mission: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mission** | **str**| slug | 
 **username** | **str**| username | 
 **request** | [**DtoUpdateMembersRequest**](DtoUpdateMembersRequest.md)| member information | 

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

# **add_members_of_registry**
> add_members_of_registry(registry, username, request)

添加成员。Add members.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
registry-manage:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_update_members_request import DtoUpdateMembersRequest
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
    api_instance = cnb_api.CollaboratorsApi(api_client)
    registry = 'registry_example' # str | slug
    username = 'username_example' # str | username
    request = cnb_api.DtoUpdateMembersRequest() # DtoUpdateMembersRequest | member information

    try:
        # 添加成员。Add members.
        api_instance.add_members_of_registry(registry, username, request)
    except Exception as e:
        print("Exception when calling CollaboratorsApi->add_members_of_registry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry** | **str**| slug | 
 **username** | **str**| username | 
 **request** | [**DtoUpdateMembersRequest**](DtoUpdateMembersRequest.md)| member information | 

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

# **add_members_of_repo**
> add_members_of_repo(repo, username, request)

添加成员。Add members.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-manage:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_update_members_request import DtoUpdateMembersRequest
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
    api_instance = cnb_api.CollaboratorsApi(api_client)
    repo = 'repo_example' # str | slug
    username = 'username_example' # str | username
    request = cnb_api.DtoUpdateMembersRequest() # DtoUpdateMembersRequest | member information

    try:
        # 添加成员。Add members.
        api_instance.add_members_of_repo(repo, username, request)
    except Exception as e:
        print("Exception when calling CollaboratorsApi->add_members_of_repo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| slug | 
 **username** | **str**| username | 
 **request** | [**DtoUpdateMembersRequest**](DtoUpdateMembersRequest.md)| member information | 

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

# **delete_members_of_group**
> delete_members_of_group(group, username)

删除指定组织或仓库的直接成员。Remove direct members from specified organization/repository.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
group-manage:rw

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
    api_instance = cnb_api.CollaboratorsApi(api_client)
    group = 'group_example' # str | slug
    username = 'username_example' # str | username

    try:
        # 删除指定组织或仓库的直接成员。Remove direct members from specified organization/repository.
        api_instance.delete_members_of_group(group, username)
    except Exception as e:
        print("Exception when calling CollaboratorsApi->delete_members_of_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| slug | 
 **username** | **str**| username | 

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

# **delete_members_of_repo**
> delete_members_of_repo(repo, username)

删除指定组织或仓库的直接成员。Remove direct members from specified organization/repository.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-manage:rw

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
    api_instance = cnb_api.CollaboratorsApi(api_client)
    repo = 'repo_example' # str | slug
    username = 'username_example' # str | username

    try:
        # 删除指定组织或仓库的直接成员。Remove direct members from specified organization/repository.
        api_instance.delete_members_of_repo(repo, username)
    except Exception as e:
        print("Exception when calling CollaboratorsApi->delete_members_of_repo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| slug | 
 **username** | **str**| username | 

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

# **delete_outside_collaborators**
> delete_outside_collaborators(repo, username)

删除指定仓库的外部贡献者。Removes external contributors from specified repository.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-manage:rw

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
    api_instance = cnb_api.CollaboratorsApi(api_client)
    repo = 'repo_example' # str | slug
    username = 'username_example' # str | username

    try:
        # 删除指定仓库的外部贡献者。Removes external contributors from specified repository.
        api_instance.delete_outside_collaborators(repo, username)
    except Exception as e:
        print("Exception when calling CollaboratorsApi->delete_outside_collaborators: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| slug | 
 **username** | **str**| username | 

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

# **list_all_members**
> List[DtoUsersWithAccessLevelInSlug] list_all_members(repo, page=page, page_size=page_size, role=role, search=search, names=names, order_by=order_by, desc=desc)

获取指定仓库内的有效成员列表，包含继承成员。List active members in specified repository including inherited members.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-manage:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_users_with_access_level_in_slug import DtoUsersWithAccessLevelInSlug
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
    api_instance = cnb_api.CollaboratorsApi(api_client)
    repo = 'repo_example' # str | slug
    page = 1 # int | Pagination page number (optional) (default to 1)
    page_size = 10 # int | Pagination page size (optional) (default to 10)
    role = 'role_example' # str | Role (optional)
    search = 'search_example' # str | 过滤成员。Filter by member (optional)
    names = 'names_example' # str | 精准匹配用户名,多个用户名用逗号间隔。Exact username matching, multiple usernames separated by commas. (optional)
    order_by = 'order_by_example' # str | Order field，default(created_at) (optional)
    desc = False # bool | Ordering (optional) (default to False)

    try:
        # 获取指定仓库内的有效成员列表，包含继承成员。List active members in specified repository including inherited members.
        api_response = api_instance.list_all_members(repo, page=page, page_size=page_size, role=role, search=search, names=names, order_by=order_by, desc=desc)
        print("The response of CollaboratorsApi->list_all_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollaboratorsApi->list_all_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| slug | 
 **page** | **int**| Pagination page number | [optional] [default to 1]
 **page_size** | **int**| Pagination page size | [optional] [default to 10]
 **role** | **str**| Role | [optional] 
 **search** | **str**| 过滤成员。Filter by member | [optional] 
 **names** | **str**| 精准匹配用户名,多个用户名用逗号间隔。Exact username matching, multiple usernames separated by commas. | [optional] 
 **order_by** | **str**| Order field，default(created_at) | [optional] 
 **desc** | **bool**| Ordering | [optional] [default to False]

### Return type

[**List[DtoUsersWithAccessLevelInSlug]**](DtoUsersWithAccessLevelInSlug.md)

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

# **list_inherit_members_of_group**
> List[DtoListInheritMembers] list_inherit_members_of_group(group, search=search, role=role, page=page, page_size=page_size)

获取指定组织或仓库内的继承成员。List inherited members within specified organization or repository。

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
group-manage:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_list_inherit_members import DtoListInheritMembers
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
    api_instance = cnb_api.CollaboratorsApi(api_client)
    group = 'group_example' # str | slug
    search = 'search_example' # str | 过滤成员。Filter by member (optional)
    role = 'role_example' # str | Role (optional)
    page = 1 # int | Pagination page number (optional) (default to 1)
    page_size = 10 # int | Pagination page size (optional) (default to 10)

    try:
        # 获取指定组织或仓库内的继承成员。List inherited members within specified organization or repository。
        api_response = api_instance.list_inherit_members_of_group(group, search=search, role=role, page=page, page_size=page_size)
        print("The response of CollaboratorsApi->list_inherit_members_of_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollaboratorsApi->list_inherit_members_of_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| slug | 
 **search** | **str**| 过滤成员。Filter by member | [optional] 
 **role** | **str**| Role | [optional] 
 **page** | **int**| Pagination page number | [optional] [default to 1]
 **page_size** | **int**| Pagination page size | [optional] [default to 10]

### Return type

[**List[DtoListInheritMembers]**](DtoListInheritMembers.md)

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

# **list_inherit_members_of_repo**
> List[DtoListInheritMembers] list_inherit_members_of_repo(repo, search=search, role=role, page=page, page_size=page_size)

获取指定组织或仓库内的继承成员。List inherited members within specified organization or repository。

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-manage:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_list_inherit_members import DtoListInheritMembers
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
    api_instance = cnb_api.CollaboratorsApi(api_client)
    repo = 'repo_example' # str | slug
    search = 'search_example' # str | 过滤成员。Filter by member (optional)
    role = 'role_example' # str | Role (optional)
    page = 1 # int | Pagination page number (optional) (default to 1)
    page_size = 10 # int | Pagination page size (optional) (default to 10)

    try:
        # 获取指定组织或仓库内的继承成员。List inherited members within specified organization or repository。
        api_response = api_instance.list_inherit_members_of_repo(repo, search=search, role=role, page=page, page_size=page_size)
        print("The response of CollaboratorsApi->list_inherit_members_of_repo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollaboratorsApi->list_inherit_members_of_repo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| slug | 
 **search** | **str**| 过滤成员。Filter by member | [optional] 
 **role** | **str**| Role | [optional] 
 **page** | **int**| Pagination page number | [optional] [default to 1]
 **page_size** | **int**| Pagination page size | [optional] [default to 10]

### Return type

[**List[DtoListInheritMembers]**](DtoListInheritMembers.md)

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

# **list_members_of_group**
> List[DtoUsersWithAccessLevelInSlug] list_members_of_group(group, page=page, page_size=page_size, role=role, search=search)

获取指定组织或仓库内的所有直接成员。List all direct members within specified organization or repository.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
group-manage:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_users_with_access_level_in_slug import DtoUsersWithAccessLevelInSlug
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
    api_instance = cnb_api.CollaboratorsApi(api_client)
    group = 'group_example' # str | slug
    page = 1 # int | Pagination page numbe (optional) (default to 1)
    page_size = 10 # int | Pagination page size (optional) (default to 10)
    role = 'role_example' # str | Role (optional)
    search = 'search_example' # str | 过滤成员。Filter by member. (optional)

    try:
        # 获取指定组织或仓库内的所有直接成员。List all direct members within specified organization or repository.
        api_response = api_instance.list_members_of_group(group, page=page, page_size=page_size, role=role, search=search)
        print("The response of CollaboratorsApi->list_members_of_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollaboratorsApi->list_members_of_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| slug | 
 **page** | **int**| Pagination page numbe | [optional] [default to 1]
 **page_size** | **int**| Pagination page size | [optional] [default to 10]
 **role** | **str**| Role | [optional] 
 **search** | **str**| 过滤成员。Filter by member. | [optional] 

### Return type

[**List[DtoUsersWithAccessLevelInSlug]**](DtoUsersWithAccessLevelInSlug.md)

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

# **list_members_of_repo**
> List[DtoUsersWithAccessLevelInSlug] list_members_of_repo(repo, page=page, page_size=page_size, role=role, search=search)

获取指定组织或仓库内的所有直接成员。List all direct members within specified organization or repository.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-manage:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_users_with_access_level_in_slug import DtoUsersWithAccessLevelInSlug
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
    api_instance = cnb_api.CollaboratorsApi(api_client)
    repo = 'repo_example' # str | slug
    page = 1 # int | Pagination page numbe (optional) (default to 1)
    page_size = 10 # int | Pagination page size (optional) (default to 10)
    role = 'role_example' # str | Role (optional)
    search = 'search_example' # str | 过滤成员。Filter by member. (optional)

    try:
        # 获取指定组织或仓库内的所有直接成员。List all direct members within specified organization or repository.
        api_response = api_instance.list_members_of_repo(repo, page=page, page_size=page_size, role=role, search=search)
        print("The response of CollaboratorsApi->list_members_of_repo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollaboratorsApi->list_members_of_repo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| slug | 
 **page** | **int**| Pagination page numbe | [optional] [default to 1]
 **page_size** | **int**| Pagination page size | [optional] [default to 10]
 **role** | **str**| Role | [optional] 
 **search** | **str**| 过滤成员。Filter by member. | [optional] 

### Return type

[**List[DtoUsersWithAccessLevelInSlug]**](DtoUsersWithAccessLevelInSlug.md)

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

# **list_outside_collaborators**
> List[DtoOutsideCollaboratorInRepo] list_outside_collaborators(repo, page=page, page_size=page_size, role=role, search=search)

获取指定仓库内的外部贡献者。List external contributors in specified repository.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-manage:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_outside_collaborator_in_repo import DtoOutsideCollaboratorInRepo
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
    api_instance = cnb_api.CollaboratorsApi(api_client)
    repo = 'repo_example' # str | slug
    page = 1 # int | Pagination page number (optional) (default to 1)
    page_size = 10 # int | Pagination page size (optional) (default to 10)
    role = 'role_example' # str | Role (optional)
    search = 'search_example' # str | 过滤成员。Filter by member. (optional)

    try:
        # 获取指定仓库内的外部贡献者。List external contributors in specified repository.
        api_response = api_instance.list_outside_collaborators(repo, page=page, page_size=page_size, role=role, search=search)
        print("The response of CollaboratorsApi->list_outside_collaborators:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollaboratorsApi->list_outside_collaborators: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| slug | 
 **page** | **int**| Pagination page number | [optional] [default to 1]
 **page_size** | **int**| Pagination page size | [optional] [default to 10]
 **role** | **str**| Role | [optional] 
 **search** | **str**| 过滤成员。Filter by member. | [optional] 

### Return type

[**List[DtoOutsideCollaboratorInRepo]**](DtoOutsideCollaboratorInRepo.md)

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

# **top_contributors**
> List[DtoUsersResult] top_contributors(repo, top=top)

获取 top 贡献用户。List the top contributing users

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-base-info:r

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
    api_instance = cnb_api.CollaboratorsApi(api_client)
    repo = 'repo_example' # str | slug
    top = 5 # int | limit, max(10) (optional) (default to 5)

    try:
        # 获取 top 贡献用户。List the top contributing users
        api_response = api_instance.top_contributors(repo, top=top)
        print("The response of CollaboratorsApi->top_contributors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollaboratorsApi->top_contributors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| slug | 
 **top** | **int**| limit, max(10) | [optional] [default to 5]

### Return type

[**List[DtoUsersResult]**](DtoUsersResult.md)

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

# **update_members_of_group**
> update_members_of_group(group, username, request)

更新指定组织或仓库内的直接成员权限信息。Update permission information for direct members in specified organization/repository.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
group-manage:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_update_members_request import DtoUpdateMembersRequest
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
    api_instance = cnb_api.CollaboratorsApi(api_client)
    group = 'group_example' # str | slug
    username = 'username_example' # str | username
    request = cnb_api.DtoUpdateMembersRequest() # DtoUpdateMembersRequest | member information

    try:
        # 更新指定组织或仓库内的直接成员权限信息。Update permission information for direct members in specified organization/repository.
        api_instance.update_members_of_group(group, username, request)
    except Exception as e:
        print("Exception when calling CollaboratorsApi->update_members_of_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| slug | 
 **username** | **str**| username | 
 **request** | [**DtoUpdateMembersRequest**](DtoUpdateMembersRequest.md)| member information | 

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

# **update_members_of_repo**
> update_members_of_repo(repo, username, request)

更新指定组织或仓库内的直接成员权限信息。Update permission information for direct members in specified organization/repository.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-manage:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_update_members_request import DtoUpdateMembersRequest
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
    api_instance = cnb_api.CollaboratorsApi(api_client)
    repo = 'repo_example' # str | slug
    username = 'username_example' # str | username
    request = cnb_api.DtoUpdateMembersRequest() # DtoUpdateMembersRequest | member information

    try:
        # 更新指定组织或仓库内的直接成员权限信息。Update permission information for direct members in specified organization/repository.
        api_instance.update_members_of_repo(repo, username, request)
    except Exception as e:
        print("Exception when calling CollaboratorsApi->update_members_of_repo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| slug | 
 **username** | **str**| username | 
 **request** | [**DtoUpdateMembersRequest**](DtoUpdateMembersRequest.md)| member information | 

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

# **update_outside_collaborators**
> update_outside_collaborators(repo, username, role)

更新指定仓库的外部贡献者权限信息。 Update permission information for external contributors in specified repository.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-manage:rw

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
    api_instance = cnb_api.CollaboratorsApi(api_client)
    repo = 'repo_example' # str | slug
    username = 'username_example' # str | username
    role = 'role_example' # str | Role

    try:
        # 更新指定仓库的外部贡献者权限信息。 Update permission information for external contributors in specified repository.
        api_instance.update_outside_collaborators(repo, username, role)
    except Exception as e:
        print("Exception when calling CollaboratorsApi->update_outside_collaborators: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| slug | 
 **username** | **str**| username | 
 **role** | **str**| Role | 

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

