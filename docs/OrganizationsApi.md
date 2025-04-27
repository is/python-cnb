# cnb_api.OrganizationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_organization**](OrganizationsApi.md#create_organization) | **POST** /groups | 创建新组织。Create new organization.
[**delete_organization**](OrganizationsApi.md#delete_organization) | **DELETE** /{group} | 删除指定组织。Delete the specified organization.
[**get_group**](OrganizationsApi.md#get_group) | **GET** /{group} | 获取指定组织信息。Get information for the specified organization.
[**get_group_setting**](OrganizationsApi.md#get_group_setting) | **GET** /{group}/-/settings | 获取指定组织的配置详情。Get the configuration details for the specified organization.
[**get_groups_by_user_id**](OrganizationsApi.md#get_groups_by_user_id) | **GET** /users/{username}/groups | 获取指定用户拥有权限的顶层组织列表。 Get a list of top-level organizations that the specified user has permissions to access.
[**list_groups**](OrganizationsApi.md#list_groups) | **GET** /user/groups/{group} | 查询当前用户在指定组织下拥有指定权限的子组织列表。Get the list of sub-organizations that the current user has access to in the specified organization.
[**list_subgroups**](OrganizationsApi.md#list_subgroups) | **GET** /{group}/-/sub-groups | 获取指定组织下的子组织列表。Get the list of sub-organizations under the specified organization.
[**list_top_groups**](OrganizationsApi.md#list_top_groups) | **GET** /user/groups | 获取当前用户拥有权限的顶层组织列表。Get top-level organizations list that the current user has access to.
[**update_group_avatar**](OrganizationsApi.md#update_group_avatar) | **PUT** /{group}/-/avatar | 更新组织头像 URL 地址。Updates the organization avatar URL.
[**update_group_setting**](OrganizationsApi.md#update_group_setting) | **PUT** /{group}/-/settings | 更新指定组织的配置。Updates the configuration for the specified organization.
[**update_organization**](OrganizationsApi.md#update_organization) | **PUT** /{group} | 更新组织信息, 可更新的内容为: 组织描述, 组织展示名称, 组织网站, 组织联系邮箱。Updates organization information including: description, display name, website URL and contact email.


# **create_organization**
> create_organization(request)

创建新组织。Create new organization.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
group-manage:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_create_group_req import DtoCreateGroupReq
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
    api_instance = cnb_api.OrganizationsApi(api_client)
    request = cnb_api.DtoCreateGroupReq() # DtoCreateGroupReq | group information

    try:
        # 创建新组织。Create new organization.
        api_instance.create_organization(request)
    except Exception as e:
        print("Exception when calling OrganizationsApi->create_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**DtoCreateGroupReq**](DtoCreateGroupReq.md)| group information | 

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

# **delete_organization**
> delete_organization(group, x_cnb_identity_ticket=x_cnb_identity_ticket)

删除指定组织。Delete the specified organization.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
group-delete:rw

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
    api_instance = cnb_api.OrganizationsApi(api_client)
    group = 'group_example' # str | group path
    x_cnb_identity_ticket = 'x_cnb_identity_ticket_example' # str | 微信身份验证票据，首次请求不传会返回新票据。WeChat auth ticket, will return new ticket if not provided in first request. (optional)

    try:
        # 删除指定组织。Delete the specified organization.
        api_instance.delete_organization(group, x_cnb_identity_ticket=x_cnb_identity_ticket)
    except Exception as e:
        print("Exception when calling OrganizationsApi->delete_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| group path | 
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

# **get_group**
> DtoOrganizationAccess get_group(group)

获取指定组织信息。Get information for the specified organization.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
group-resource:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_organization_access import DtoOrganizationAccess
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
    api_instance = cnb_api.OrganizationsApi(api_client)
    group = 'group_example' # str | group path

    try:
        # 获取指定组织信息。Get information for the specified organization.
        api_response = api_instance.get_group(group)
        print("The response of OrganizationsApi->get_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->get_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| group path | 

### Return type

[**DtoOrganizationAccess**](DtoOrganizationAccess.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.cnb.api+json, application/vnd.cnb.web+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | group |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_setting**
> DtoOrganizationSettingWithParent get_group_setting(group)

获取指定组织的配置详情。Get the configuration details for the specified organization.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
group-manage:r

### Example


```python
import cnb_api
from cnb_api.models.dto_organization_setting_with_parent import DtoOrganizationSettingWithParent
from cnb_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cnb_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cnb_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cnb_api.OrganizationsApi(api_client)
    group = 'group_example' # str | group path

    try:
        # 获取指定组织的配置详情。Get the configuration details for the specified organization.
        api_response = api_instance.get_group_setting(group)
        print("The response of OrganizationsApi->get_group_setting:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->get_group_setting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| group path | 

### Return type

[**DtoOrganizationSettingWithParent**](DtoOrganizationSettingWithParent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.cnb.api+json, application/vnd.cnb.web+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_groups_by_user_id**
> DtoOrganizationUnion get_groups_by_user_id(username, search=search, page=page, page_size=page_size, desc=desc, order_by=order_by)

获取指定用户拥有权限的顶层组织列表。 Get a list of top-level organizations that the specified user has permissions to access.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
account-engage:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_organization_union import DtoOrganizationUnion
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
    api_instance = cnb_api.OrganizationsApi(api_client)
    username = 'someone' # str | UserName (default to 'someone')
    search = 'search_example' # str | Filter organizations. (optional)
    page = 1 # int | Pagination page number (optional) (default to 1)
    page_size = 10 # int | Pagination page size (optional) (default to 10)
    desc = False # bool | Sort order. (optional) (default to False)
    order_by = 'order_by_example' # str | Sort type, defaults to created_at (optional)

    try:
        # 获取指定用户拥有权限的顶层组织列表。 Get a list of top-level organizations that the specified user has permissions to access.
        api_response = api_instance.get_groups_by_user_id(username, search=search, page=page, page_size=page_size, desc=desc, order_by=order_by)
        print("The response of OrganizationsApi->get_groups_by_user_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->get_groups_by_user_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| UserName | [default to &#39;someone&#39;]
 **search** | **str**| Filter organizations. | [optional] 
 **page** | **int**| Pagination page number | [optional] [default to 1]
 **page_size** | **int**| Pagination page size | [optional] [default to 10]
 **desc** | **bool**| Sort order. | [optional] [default to False]
 **order_by** | **str**| Sort type, defaults to created_at | [optional] 

### Return type

[**DtoOrganizationUnion**](DtoOrganizationUnion.md)

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

# **list_groups**
> List[DtoOrganizationAccess] list_groups(group, page=page, page_size=page_size, access=access)

查询当前用户在指定组织下拥有指定权限的子组织列表。Get the list of sub-organizations that the current user has access to in the specified organization.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
account-engage:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_organization_access import DtoOrganizationAccess
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
    api_instance = cnb_api.OrganizationsApi(api_client)
    group = 'hello' # str | Group slug (default to 'hello')
    page = 1 # int | Pagination page number (optional) (default to 1)
    page_size = 10 # int | Pagination page size (optional) (default to 10)
    access = 56 # int | access level (optional)

    try:
        # 查询当前用户在指定组织下拥有指定权限的子组织列表。Get the list of sub-organizations that the current user has access to in the specified organization.
        api_response = api_instance.list_groups(group, page=page, page_size=page_size, access=access)
        print("The response of OrganizationsApi->list_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->list_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| Group slug | [default to &#39;hello&#39;]
 **page** | **int**| Pagination page number | [optional] [default to 1]
 **page_size** | **int**| Pagination page size | [optional] [default to 10]
 **access** | **int**| access level | [optional] 

### Return type

[**List[DtoOrganizationAccess]**](DtoOrganizationAccess.md)

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

# **list_subgroups**
> List[DtoOrganizationUnion] list_subgroups(group, page, page_size, search=search)

获取指定组织下的子组织列表。Get the list of sub-organizations under the specified organization.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
group-resource:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_organization_union import DtoOrganizationUnion
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
    api_instance = cnb_api.OrganizationsApi(api_client)
    group = 'group_example' # str | Slug
    page = 1 # int | Pagination page number (default to 1)
    page_size = 10 # int | Pagination page size (default to 10)
    search = 'search_example' # str | Filter organization (optional)

    try:
        # 获取指定组织下的子组织列表。Get the list of sub-organizations under the specified organization.
        api_response = api_instance.list_subgroups(group, page, page_size, search=search)
        print("The response of OrganizationsApi->list_subgroups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->list_subgroups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| Slug | 
 **page** | **int**| Pagination page number | [default to 1]
 **page_size** | **int**| Pagination page size | [default to 10]
 **search** | **str**| Filter organization | [optional] 

### Return type

[**List[DtoOrganizationUnion]**](DtoOrganizationUnion.md)

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

# **list_top_groups**
> List[DtoOrganizationAccess] list_top_groups(page=page, page_size=page_size, search=search, role=role)

获取当前用户拥有权限的顶层组织列表。Get top-level organizations list that the current user has access to.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
account-engage:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_organization_access import DtoOrganizationAccess
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
    api_instance = cnb_api.OrganizationsApi(api_client)
    page = 1 # int | Pagination page number (optional) (default to 1)
    page_size = 10 # int | Pagination page size (optional) (default to 10)
    search = 'search_example' # str | Filter by organizations. (optional)
    role = 'role_example' # str | Filter by role. (optional)

    try:
        # 获取当前用户拥有权限的顶层组织列表。Get top-level organizations list that the current user has access to.
        api_response = api_instance.list_top_groups(page=page, page_size=page_size, search=search, role=role)
        print("The response of OrganizationsApi->list_top_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->list_top_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Pagination page number | [optional] [default to 1]
 **page_size** | **int**| Pagination page size | [optional] [default to 10]
 **search** | **str**| Filter by organizations. | [optional] 
 **role** | **str**| Filter by role. | [optional] 

### Return type

[**List[DtoOrganizationAccess]**](DtoOrganizationAccess.md)

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

# **update_group_avatar**
> update_group_avatar(group, request)

更新组织头像 URL 地址。Updates the organization avatar URL.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
group-manage:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_update_group_avatar_req import DtoUpdateGroupAvatarReq
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
    api_instance = cnb_api.OrganizationsApi(api_client)
    group = 'group_example' # str | slug
    request = cnb_api.DtoUpdateGroupAvatarReq() # DtoUpdateGroupAvatarReq | group avatar url to update

    try:
        # 更新组织头像 URL 地址。Updates the organization avatar URL.
        api_instance.update_group_avatar(group, request)
    except Exception as e:
        print("Exception when calling OrganizationsApi->update_group_avatar: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| slug | 
 **request** | [**DtoUpdateGroupAvatarReq**](DtoUpdateGroupAvatarReq.md)| group avatar url to update | 

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

# **update_group_setting**
> update_group_setting(group, request)

更新指定组织的配置。Updates the configuration for the specified organization.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
group-manage:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_group_setting_req import DtoGroupSettingReq
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
    api_instance = cnb_api.OrganizationsApi(api_client)
    group = 'group_example' # str | slug
    request = cnb_api.DtoGroupSettingReq() # DtoGroupSettingReq | group information to update

    try:
        # 更新指定组织的配置。Updates the configuration for the specified organization.
        api_instance.update_group_setting(group, request)
    except Exception as e:
        print("Exception when calling OrganizationsApi->update_group_setting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| slug | 
 **request** | [**DtoGroupSettingReq**](DtoGroupSettingReq.md)| group information to update | 

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

# **update_organization**
> update_organization(group, request)

更新组织信息, 可更新的内容为: 组织描述, 组织展示名称, 组织网站, 组织联系邮箱。Updates organization information including: description, display name, website URL and contact email.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
group-manage:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_update_group_req import DtoUpdateGroupReq
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
    api_instance = cnb_api.OrganizationsApi(api_client)
    group = 'group_example' # str | slug
    request = cnb_api.DtoUpdateGroupReq() # DtoUpdateGroupReq | group information to update

    try:
        # 更新组织信息, 可更新的内容为: 组织描述, 组织展示名称, 组织网站, 组织联系邮箱。Updates organization information including: description, display name, website URL and contact email.
        api_instance.update_organization(group, request)
    except Exception as e:
        print("Exception when calling OrganizationsApi->update_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| slug | 
 **request** | [**DtoUpdateGroupReq**](DtoUpdateGroupReq.md)| group information to update | 

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

