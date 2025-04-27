# cnb_api.BuildApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_build_logs**](BuildApi.md#get_build_logs) | **GET** /{repo}/-/build/logs | 查询流水线构建列表。List pipeline builds.
[**get_build_status**](BuildApi.md#get_build_status) | **GET** /{repo}/-/build/status/{sn} | 查询流水线构建状态。Get pipeline build status.
[**start_build**](BuildApi.md#start_build) | **POST** /{repo}/-/build/start | 开始一个构建。Start a build.
[**stop_build**](BuildApi.md#stop_build) | **POST** /{repo}/-/build/stop/{sn} | 停止一个构建。 Stop a build.


# **get_build_logs**
> DtoBuildLogsResult get_build_logs(repo, create_time=create_time, end_time=end_time, event=event, page=page, pagesize=pagesize, sha=sha, sn=sn, source_ref=source_ref, status=status, target_ref=target_ref, user_id=user_id, user_name=user_name)

查询流水线构建列表。List pipeline builds.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-cnb-trigger:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_build_logs_result import DtoBuildLogsResult
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
    api_instance = cnb_api.BuildApi(api_client)
    repo = 'repo_example' # str | Repo path
    create_time = 'create_time_example' # str | Start date in \"YYYY-MM-DD\" format, e.g. \"2024-12-01\" (optional)
    end_time = 'end_time_example' # str | End date in \"YYYY-MM-DD\" format, e.g. \"2024-12-01\" (optional)
    event = 'event_example' # str | Event name, e.g. \"push\" (optional)
    page = 56 # int | Pagination page number, default(1) (optional)
    pagesize = 56 # int | Pagination page size, default(20), max(100) (optional)
    sha = 'sha_example' # str | Commit ID, e.g. \"2221d4535ec0c921bcd0858627c5025a871dd2b5\" (optional)
    sn = 'sn_example' # str | Build SN, e.g. \"cnb-1qa-1i3f5ecau (optional)
    source_ref = 'source_ref_example' # str | Source branch name, e.g. \"dev\" (optional)
    status = 'status_example' # str | Build status: \"pending\", \"success\", \"error\", \"cancel\" (optional)
    target_ref = 'target_ref_example' # str | Target branch name, e.g. \"main\" (optional)
    user_id = 'user_id_example' # str | User ID (optional)
    user_name = 'user_name_example' # str | Username (optional)

    try:
        # 查询流水线构建列表。List pipeline builds.
        api_response = api_instance.get_build_logs(repo, create_time=create_time, end_time=end_time, event=event, page=page, pagesize=pagesize, sha=sha, sn=sn, source_ref=source_ref, status=status, target_ref=target_ref, user_id=user_id, user_name=user_name)
        print("The response of BuildApi->get_build_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuildApi->get_build_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| Repo path | 
 **create_time** | **str**| Start date in \&quot;YYYY-MM-DD\&quot; format, e.g. \&quot;2024-12-01\&quot; | [optional] 
 **end_time** | **str**| End date in \&quot;YYYY-MM-DD\&quot; format, e.g. \&quot;2024-12-01\&quot; | [optional] 
 **event** | **str**| Event name, e.g. \&quot;push\&quot; | [optional] 
 **page** | **int**| Pagination page number, default(1) | [optional] 
 **pagesize** | **int**| Pagination page size, default(20), max(100) | [optional] 
 **sha** | **str**| Commit ID, e.g. \&quot;2221d4535ec0c921bcd0858627c5025a871dd2b5\&quot; | [optional] 
 **sn** | **str**| Build SN, e.g. \&quot;cnb-1qa-1i3f5ecau | [optional] 
 **source_ref** | **str**| Source branch name, e.g. \&quot;dev\&quot; | [optional] 
 **status** | **str**| Build status: \&quot;pending\&quot;, \&quot;success\&quot;, \&quot;error\&quot;, \&quot;cancel\&quot; | [optional] 
 **target_ref** | **str**| Target branch name, e.g. \&quot;main\&quot; | [optional] 
 **user_id** | **str**| User ID | [optional] 
 **user_name** | **str**| Username | [optional] 

### Return type

[**DtoBuildLogsResult**](DtoBuildLogsResult.md)

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

# **get_build_status**
> DtoBuildStatusResult get_build_status(repo, sn)

查询流水线构建状态。Get pipeline build status.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-cnb-trigger:r

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_build_status_result import DtoBuildStatusResult
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
    api_instance = cnb_api.BuildApi(api_client)
    repo = 'repo_example' # str | Repo path
    sn = 'sn_example' # str | SN

    try:
        # 查询流水线构建状态。Get pipeline build status.
        api_response = api_instance.get_build_status(repo, sn)
        print("The response of BuildApi->get_build_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuildApi->get_build_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| Repo path | 
 **sn** | **str**| SN | 

### Return type

[**DtoBuildStatusResult**](DtoBuildStatusResult.md)

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

# **start_build**
> List[DtoBuildResult] start_build(repo, request)

开始一个构建。Start a build.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-cnb-trigger:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_build_result import DtoBuildResult
from cnb_api.models.dto_start_build_req import DtoStartBuildReq
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
    api_instance = cnb_api.BuildApi(api_client)
    repo = 'repo_example' # str | repo
    request = cnb_api.DtoStartBuildReq() # DtoStartBuildReq | Build params

    try:
        # 开始一个构建。Start a build.
        api_response = api_instance.start_build(repo, request)
        print("The response of BuildApi->start_build:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuildApi->start_build: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **request** | [**DtoStartBuildReq**](DtoStartBuildReq.md)| Build params | 

### Return type

[**List[DtoBuildResult]**](DtoBuildResult.md)

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

# **stop_build**
> List[DtoBuildResult] stop_build(repo, sn)

停止一个构建。 Stop a build.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-cnb-trigger:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_build_result import DtoBuildResult
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
    api_instance = cnb_api.BuildApi(api_client)
    repo = 'repo_example' # str | repo
    sn = 'sn_example' # str | SN

    try:
        # 停止一个构建。 Stop a build.
        api_response = api_instance.stop_build(repo, sn)
        print("The response of BuildApi->stop_build:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuildApi->stop_build: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | 
 **sn** | **str**| SN | 

### Return type

[**List[DtoBuildResult]**](DtoBuildResult.md)

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

