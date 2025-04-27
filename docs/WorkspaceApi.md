# cnb_api.WorkspaceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_workspace**](WorkspaceApi.md#delete_workspace) | **POST** /workspace/delete | 删除我的云原生开发环境。Delete my workspace.
[**get_workspace_detail**](WorkspaceApi.md#get_workspace_detail) | **GET** /{repo}/-/workspace/detail/{sn} | 根据流水线sn查询云原生开发访问地址。Query cloud-native development access address by pipeline SN.
[**list_workspaces**](WorkspaceApi.md#list_workspaces) | **GET** /workspace/list | 获取我的云原生开发环境列表。List my workspaces.


# **delete_workspace**
> DtoWorkspaceDeleteResult delete_workspace(request)

删除我的云原生开发环境。Delete my workspace.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
account-engage:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_workspace_delete_req import DtoWorkspaceDeleteReq
from cnb_api.models.dto_workspace_delete_result import DtoWorkspaceDeleteResult
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
    api_instance = cnb_api.WorkspaceApi(api_client)
    request = cnb_api.DtoWorkspaceDeleteReq() # DtoWorkspaceDeleteReq | params

    try:
        # 删除我的云原生开发环境。Delete my workspace.
        api_response = api_instance.delete_workspace(request)
        print("The response of WorkspaceApi->delete_workspace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceApi->delete_workspace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**DtoWorkspaceDeleteReq**](DtoWorkspaceDeleteReq.md)| params | 

### Return type

[**DtoWorkspaceDeleteResult**](DtoWorkspaceDeleteResult.md)

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

# **get_workspace_detail**
> DtoWorkspaceDetailResult get_workspace_detail(repo, sn)

根据流水线sn查询云原生开发访问地址。Query cloud-native development access address by pipeline SN.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-cnb-detail:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_workspace_detail_result import DtoWorkspaceDetailResult
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
    api_instance = cnb_api.WorkspaceApi(api_client)
    repo = 'repo_example' # str | Repo path
    sn = 'sn_example' # str | SN

    try:
        # 根据流水线sn查询云原生开发访问地址。Query cloud-native development access address by pipeline SN.
        api_response = api_instance.get_workspace_detail(repo, sn)
        print("The response of WorkspaceApi->get_workspace_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceApi->get_workspace_detail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| Repo path | 
 **sn** | **str**| SN | 

### Return type

[**DtoWorkspaceDetailResult**](DtoWorkspaceDetailResult.md)

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

# **list_workspaces**
> DtoWorkspaceListResult list_workspaces(branch=branch, end=end, page=page, page_size=page_size, slug=slug, start=start, status=status)

获取我的云原生开发环境列表。List my workspaces.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
account-engage:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_workspace_list_result import DtoWorkspaceListResult
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
    api_instance = cnb_api.WorkspaceApi(api_client)
    branch = 'branch_example' # str | Git branch name, e.g. \"main\" (optional)
    end = 'end_example' # str | 查询结束时间。Query end time. format YYYY-MM-DD HH:mm:ssZZ, e.g. 2024-12-01 00:00:00+0800 (optional)
    page = 56 # int | Pagination page number, default(1) (optional)
    page_size = 56 # int | Pagination page size, default(20), max(100) (optional)
    slug = 'slug_example' # str | Repository path, e.g. \"groupname/reponame\" (optional)
    start = 'start_example' # str | 查询开始时间。Query start time. format YYYY-MM-DD HH:mm:ssZZ, e.g. 2024-12-01 00:00:00+0800 (optional)
    status = 'status_example' # str | 开发环境状态，running: 开发环境已启动，closed：开发环境已关闭。Workspace status: \"running\" for started, \"closed\" for stopped. (optional)

    try:
        # 获取我的云原生开发环境列表。List my workspaces.
        api_response = api_instance.list_workspaces(branch=branch, end=end, page=page, page_size=page_size, slug=slug, start=start, status=status)
        print("The response of WorkspaceApi->list_workspaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkspaceApi->list_workspaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch** | **str**| Git branch name, e.g. \&quot;main\&quot; | [optional] 
 **end** | **str**| 查询结束时间。Query end time. format YYYY-MM-DD HH:mm:ssZZ, e.g. 2024-12-01 00:00:00+0800 | [optional] 
 **page** | **int**| Pagination page number, default(1) | [optional] 
 **page_size** | **int**| Pagination page size, default(20), max(100) | [optional] 
 **slug** | **str**| Repository path, e.g. \&quot;groupname/reponame\&quot; | [optional] 
 **start** | **str**| 查询开始时间。Query start time. format YYYY-MM-DD HH:mm:ssZZ, e.g. 2024-12-01 00:00:00+0800 | [optional] 
 **status** | **str**| 开发环境状态，running: 开发环境已启动，closed：开发环境已关闭。Workspace status: \&quot;running\&quot; for started, \&quot;closed\&quot; for stopped. | [optional] 

### Return type

[**DtoWorkspaceListResult**](DtoWorkspaceListResult.md)

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

