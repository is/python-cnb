# cnb_api.ContributorsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_member_access_level_of_group**](ContributorsApi.md#get_member_access_level_of_group) | **GET** /{group}/-/members/access-level | 获取指定组织或仓库内, 访问成员在当前层级内的权限信息。Get permission information for accessing members at current level.
[**get_member_access_level_of_repo**](ContributorsApi.md#get_member_access_level_of_repo) | **GET** /{repo}/-/members/access-level | 获取指定组织或仓库内, 访问成员在当前层级内的权限信息。Get permission information for accessing members at current level.
[**list_member_access_level_of_group**](ContributorsApi.md#list_member_access_level_of_group) | **GET** /{group}/-/members/{username}/access-level | 获取指定组织或仓库内指定成员的权限信息, 结果按组织层级来展示, 包含上层组织的权限继承信息。Get specified member&#39;s permissions with organizational hierarchy.
[**list_member_access_level_of_repo**](ContributorsApi.md#list_member_access_level_of_repo) | **GET** /{repo}/-/members/{username}/access-level | 获取指定组织或仓库内指定成员的权限信息, 结果按组织层级来展示, 包含上层组织的权限继承信息。Get specified member&#39;s permissions with organizational hierarchy.


# **get_member_access_level_of_group**
> DtoMemberAccessLevelInSlugUnion get_member_access_level_of_group(group, include_inherit=include_inherit)

获取指定组织或仓库内, 访问成员在当前层级内的权限信息。Get permission information for accessing members at current level.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
group-manage:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_member_access_level_in_slug_union import DtoMemberAccessLevelInSlugUnion
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
    api_instance = cnb_api.ContributorsApi(api_client)
    group = 'group_example' # str | slug
    include_inherit = True # bool | 是否包含继承的权限。If inherited permissions are included. (optional) (default to True)

    try:
        # 获取指定组织或仓库内, 访问成员在当前层级内的权限信息。Get permission information for accessing members at current level.
        api_response = api_instance.get_member_access_level_of_group(group, include_inherit=include_inherit)
        print("The response of ContributorsApi->get_member_access_level_of_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContributorsApi->get_member_access_level_of_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| slug | 
 **include_inherit** | **bool**| 是否包含继承的权限。If inherited permissions are included. | [optional] [default to True]

### Return type

[**DtoMemberAccessLevelInSlugUnion**](DtoMemberAccessLevelInSlugUnion.md)

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

# **get_member_access_level_of_repo**
> DtoMemberAccessLevelInSlugUnion get_member_access_level_of_repo(repo, include_inherit=include_inherit)

获取指定组织或仓库内, 访问成员在当前层级内的权限信息。Get permission information for accessing members at current level.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-manage:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_member_access_level_in_slug_union import DtoMemberAccessLevelInSlugUnion
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
    api_instance = cnb_api.ContributorsApi(api_client)
    repo = 'repo_example' # str | slug
    include_inherit = True # bool | 是否包含继承的权限。If inherited permissions are included. (optional) (default to True)

    try:
        # 获取指定组织或仓库内, 访问成员在当前层级内的权限信息。Get permission information for accessing members at current level.
        api_response = api_instance.get_member_access_level_of_repo(repo, include_inherit=include_inherit)
        print("The response of ContributorsApi->get_member_access_level_of_repo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContributorsApi->get_member_access_level_of_repo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| slug | 
 **include_inherit** | **bool**| 是否包含继承的权限。If inherited permissions are included. | [optional] [default to True]

### Return type

[**DtoMemberAccessLevelInSlugUnion**](DtoMemberAccessLevelInSlugUnion.md)

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

# **list_member_access_level_of_group**
> List[DtoMemberAccessLevel] list_member_access_level_of_group(group, username)

获取指定组织或仓库内指定成员的权限信息, 结果按组织层级来展示, 包含上层组织的权限继承信息。Get specified member's permissions with organizational hierarchy.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
group-manage:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_member_access_level import DtoMemberAccessLevel
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
    api_instance = cnb_api.ContributorsApi(api_client)
    group = 'group_example' # str | slug
    username = 'username_example' # str | username

    try:
        # 获取指定组织或仓库内指定成员的权限信息, 结果按组织层级来展示, 包含上层组织的权限继承信息。Get specified member's permissions with organizational hierarchy.
        api_response = api_instance.list_member_access_level_of_group(group, username)
        print("The response of ContributorsApi->list_member_access_level_of_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContributorsApi->list_member_access_level_of_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| slug | 
 **username** | **str**| username | 

### Return type

[**List[DtoMemberAccessLevel]**](DtoMemberAccessLevel.md)

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

# **list_member_access_level_of_repo**
> List[DtoMemberAccessLevel] list_member_access_level_of_repo(repo, username)

获取指定组织或仓库内指定成员的权限信息, 结果按组织层级来展示, 包含上层组织的权限继承信息。Get specified member's permissions with organizational hierarchy.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-manage:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_member_access_level import DtoMemberAccessLevel
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
    api_instance = cnb_api.ContributorsApi(api_client)
    repo = 'repo_example' # str | slug
    username = 'username_example' # str | username

    try:
        # 获取指定组织或仓库内指定成员的权限信息, 结果按组织层级来展示, 包含上层组织的权限继承信息。Get specified member's permissions with organizational hierarchy.
        api_response = api_instance.list_member_access_level_of_repo(repo, username)
        print("The response of ContributorsApi->list_member_access_level_of_repo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContributorsApi->list_member_access_level_of_repo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| slug | 
 **username** | **str**| username | 

### Return type

[**List[DtoMemberAccessLevel]**](DtoMemberAccessLevel.md)

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

