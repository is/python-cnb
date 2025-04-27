# cnb_api.AssetsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_commit_assets**](AssetsApi.md#get_commit_assets) | **GET** /{repo}/-/commit-assets/download/{fileName} | 发起一个获取 commits 附件的请求，返回内容或者 302 到某个地址。Get a request to fetch a commit assets and returns the content directly or a 302 redirect to the assets URL.
[**get_files**](AssetsApi.md#get_files) | **GET** /{repo}/-/files/{userIdKey}/{randomUUID}/{fileName} | 发起一个获取 files 的请求，返回内容或者 302 到某个地址。Initiate a request to retrieve files, returns content or 302 redirect.
[**get_imgs**](AssetsApi.md#get_imgs) | **GET** /{repo}/-/imgs/{userIdKey}/{fileName} | 发起一个获取 imgs 的请求，返回内容或者 302 到某个地址。Initiate a request to get images, returns content or 302 redirect.
[**get_latest_releases_asset**](AssetsApi.md#get_latest_releases_asset) | **GET** /{repo}/-/releases/latest/download/{fileName} | 发起一个获取 latest release 附件的请求，返回内容或者 302 到某个地址。Initiate a request to get latest release attachments, returns content or 302 redirect.
[**get_logos**](AssetsApi.md#get_logos) | **GET** /{group}/-/logos/{size} | 发起一个获取 logo 的请求，返回内容或者 302 到某个地址。Post a request to fetch a logo and returns the content directly or a 302 redirect to the logo URL.
[**get_releases_asset**](AssetsApi.md#get_releases_asset) | **GET** /{repo}/-/releases/download/{fileName} | 发起一个获取 release 附件的请求，返回内容或者 302 到某个地址。Initiate a request to get release attachments, returns content or 302 redirect.
[**get_user_avatar**](AssetsApi.md#get_user_avatar) | **GET** /users/{username}/avatar/{size} | 获取指定用户的用户头像。Get the user&#39;s avatar.
[**put_files**](AssetsApi.md#put_files) | **PUT** /{repo}/-/files/{userIdKey}/{randomUUID}/{fileName} | 发起一个确认 files 的请求，上传的图片要调用此接口才能生效。Initiate a request to confirm files, uploaded images need to call this API to take effect.
[**put_imgs**](AssetsApi.md#put_imgs) | **PUT** /{repo}/-/imgs/{userIdKey}/{fileName} | 发起一个确认 imgs 的请求，上传的图片要调用此接口才能生效。Initiate a request to confirm images, uploaded images need to call this API to take effect.
[**put_logos**](AssetsApi.md#put_logos) | **PUT** /{group}/-/logos | 确认上传的logo。Confirms the uploaded logo.
[**upload_files**](AssetsApi.md#upload_files) | **POST** /{repo}/-/upload/files | 发起一个上传 files 的请求，返回上传 cos 的 url 和 form 内容。Initiate a request to upload files,returns COS upload URL and form data.
[**upload_imgs**](AssetsApi.md#upload_imgs) | **POST** /{repo}/-/upload/imgs | 发起一个上传 imgs 的请求，返回上传 cos 的 url 和 form 内容。发起一个上传 imgs 的请求，返回上传 cos 的 url 和 form 内容.
[**upload_logos**](AssetsApi.md#upload_logos) | **POST** /{group}/-/upload/logos | 发起一个上传 logo 的请求，返回上传 cos 的 url 和 form 内容。Post a request to upload a logo.
[**upload_releases**](AssetsApi.md#upload_releases) | **POST** /{repo}/-/upload/releases/{tagName} | 发起一个上传 release 附件的请求，返回上传 cos 的 url 和 form 内容。Initiate a request to upload release attachments, returns COS upload URL and form data.


# **get_commit_assets**
> get_commit_assets(repo, file_name)

发起一个获取 commits 附件的请求，返回内容或者 302 到某个地址。Get a request to fetch a commit assets and returns the content directly or a 302 redirect to the assets URL.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-contents:r

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
    api_instance = cnb_api.AssetsApi(api_client)
    repo = 'test-group/test-repo' # str | Repo (default to 'test-group/test-repo')
    file_name = 'file_name_example' # str | File path that contain commit hash，eg: 3bba1ce6a8c35ee1264c7449f4f0b512bd751eac/test.png

    try:
        # 发起一个获取 commits 附件的请求，返回内容或者 302 到某个地址。Get a request to fetch a commit assets and returns the content directly or a 302 redirect to the assets URL.
        api_instance.get_commit_assets(repo, file_name)
    except Exception as e:
        print("Exception when calling AssetsApi->get_commit_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| Repo | [default to &#39;test-group/test-repo&#39;]
 **file_name** | **str**| File path that contain commit hash，eg: 3bba1ce6a8c35ee1264c7449f4f0b512bd751eac/test.png | 

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
**302** | Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_files**
> get_files(repo, user_id_key, random_uuid, file_name)

发起一个获取 files 的请求，返回内容或者 302 到某个地址。Initiate a request to retrieve files, returns content or 302 redirect.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-contents:r

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
    api_instance = cnb_api.AssetsApi(api_client)
    repo = 'test-group/test-repo' # str | repo (default to 'test-group/test-repo')
    user_id_key = 'user_id_key_example' # str | user_id_key
    random_uuid = 'random_uuid_example' # str | random_uuid
    file_name = 'file_name_example' # str | file_name

    try:
        # 发起一个获取 files 的请求，返回内容或者 302 到某个地址。Initiate a request to retrieve files, returns content or 302 redirect.
        api_instance.get_files(repo, user_id_key, random_uuid, file_name)
    except Exception as e:
        print("Exception when calling AssetsApi->get_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | [default to &#39;test-group/test-repo&#39;]
 **user_id_key** | **str**| user_id_key | 
 **random_uuid** | **str**| random_uuid | 
 **file_name** | **str**| file_name | 

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
**302** | Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_imgs**
> get_imgs(repo, user_id_key, file_name)

发起一个获取 imgs 的请求，返回内容或者 302 到某个地址。Initiate a request to get images, returns content or 302 redirect.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-contents:r

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
    api_instance = cnb_api.AssetsApi(api_client)
    repo = 'test-group/test-repo' # str | repo (default to 'test-group/test-repo')
    user_id_key = 'user_id_key_example' # str | user_id_key
    file_name = 'file_name_example' # str | file_name

    try:
        # 发起一个获取 imgs 的请求，返回内容或者 302 到某个地址。Initiate a request to get images, returns content or 302 redirect.
        api_instance.get_imgs(repo, user_id_key, file_name)
    except Exception as e:
        print("Exception when calling AssetsApi->get_imgs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | [default to &#39;test-group/test-repo&#39;]
 **user_id_key** | **str**| user_id_key | 
 **file_name** | **str**| file_name | 

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
**302** | Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_releases_asset**
> get_latest_releases_asset(repo, file_name)

发起一个获取 latest release 附件的请求，返回内容或者 302 到某个地址。Initiate a request to get latest release attachments, returns content or 302 redirect.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-contents:r

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
    api_instance = cnb_api.AssetsApi(api_client)
    repo = 'test-group/test-repo' # str | Repo (default to 'test-group/test-repo')
    file_name = 'file_name_example' # str | File name, eg: test.png

    try:
        # 发起一个获取 latest release 附件的请求，返回内容或者 302 到某个地址。Initiate a request to get latest release attachments, returns content or 302 redirect.
        api_instance.get_latest_releases_asset(repo, file_name)
    except Exception as e:
        print("Exception when calling AssetsApi->get_latest_releases_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| Repo | [default to &#39;test-group/test-repo&#39;]
 **file_name** | **str**| File name, eg: test.png | 

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
**302** | Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logos**
> get_logos(group, size)

发起一个获取 logo 的请求，返回内容或者 302 到某个地址。Post a request to fetch a logo and returns the content directly or a 302 redirect to the logo URL.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
group-resource:r

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
    api_instance = cnb_api.AssetsApi(api_client)
    group = 'test-group' # str | group (default to 'test-group')
    size = 'size_example' # str | size

    try:
        # 发起一个获取 logo 的请求，返回内容或者 302 到某个地址。Post a request to fetch a logo and returns the content directly or a 302 redirect to the logo URL.
        api_instance.get_logos(group, size)
    except Exception as e:
        print("Exception when calling AssetsApi->get_logos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| group | [default to &#39;test-group&#39;]
 **size** | **str**| size | 

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
**302** | Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_releases_asset**
> get_releases_asset(repo, file_name)

发起一个获取 release 附件的请求，返回内容或者 302 到某个地址。Initiate a request to get release attachments, returns content or 302 redirect.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-contents:r

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
    api_instance = cnb_api.AssetsApi(api_client)
    repo = 'test-group/test-repo' # str | Repo (default to 'test-group/test-repo')
    file_name = 'file_name_example' # str | Including tag name and filename (e.g. v1.0/test.png)

    try:
        # 发起一个获取 release 附件的请求，返回内容或者 302 到某个地址。Initiate a request to get release attachments, returns content or 302 redirect.
        api_instance.get_releases_asset(repo, file_name)
    except Exception as e:
        print("Exception when calling AssetsApi->get_releases_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| Repo | [default to &#39;test-group/test-repo&#39;]
 **file_name** | **str**| Including tag name and filename (e.g. v1.0/test.png) | 

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
**302** | Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_avatar**
> get_user_avatar(username, size)

获取指定用户的用户头像。Get the user's avatar.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
account-profile:r

### Example


```python
import cnb_api
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
    api_instance = cnb_api.AssetsApi(api_client)
    username = 'someone' # str | User Name (default to 'someone')
    size = 'size_example' # str | Size of the avatar. s or l

    try:
        # 获取指定用户的用户头像。Get the user's avatar.
        api_instance.get_user_avatar(username, size)
    except Exception as e:
        print("Exception when calling AssetsApi->get_user_avatar: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| User Name | [default to &#39;someone&#39;]
 **size** | **str**| Size of the avatar. s or l | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_files**
> put_files(repo, user_id_key, random_uuid, file_name, token)

发起一个确认 files 的请求，上传的图片要调用此接口才能生效。Initiate a request to confirm files, uploaded images need to call this API to take effect.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-contents:rw

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
    api_instance = cnb_api.AssetsApi(api_client)
    repo = 'test-group/test-repo' # str | Repo (default to 'test-group/test-repo')
    user_id_key = 'user_id_key_example' # str | user_id_key
    random_uuid = 'random_uuid_example' # str | random_uuid
    file_name = 'file_name_example' # str | file_name
    token = 'token_example' # str | 获取 uploadurl 时返回的token。Token returned when getting upload URL.

    try:
        # 发起一个确认 files 的请求，上传的图片要调用此接口才能生效。Initiate a request to confirm files, uploaded images need to call this API to take effect.
        api_instance.put_files(repo, user_id_key, random_uuid, file_name, token)
    except Exception as e:
        print("Exception when calling AssetsApi->put_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| Repo | [default to &#39;test-group/test-repo&#39;]
 **user_id_key** | **str**| user_id_key | 
 **random_uuid** | **str**| random_uuid | 
 **file_name** | **str**| file_name | 
 **token** | **str**| 获取 uploadurl 时返回的token。Token returned when getting upload URL. | 

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

# **put_imgs**
> put_imgs(repo, user_id_key, file_name, token)

发起一个确认 imgs 的请求，上传的图片要调用此接口才能生效。Initiate a request to confirm images, uploaded images need to call this API to take effect.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-contents:rw

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
    api_instance = cnb_api.AssetsApi(api_client)
    repo = 'test-group/test-repo' # str | Repo (default to 'test-group/test-repo')
    user_id_key = 'user_id_key_example' # str | user_id_key
    file_name = 'file_name_example' # str | file_name
    token = 'token_example' # str | 获取 uploadurl 时返回的token。Token returned when getting upload URL.

    try:
        # 发起一个确认 imgs 的请求，上传的图片要调用此接口才能生效。Initiate a request to confirm images, uploaded images need to call this API to take effect.
        api_instance.put_imgs(repo, user_id_key, file_name, token)
    except Exception as e:
        print("Exception when calling AssetsApi->put_imgs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| Repo | [default to &#39;test-group/test-repo&#39;]
 **user_id_key** | **str**| user_id_key | 
 **file_name** | **str**| file_name | 
 **token** | **str**| 获取 uploadurl 时返回的token。Token returned when getting upload URL. | 

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

# **put_logos**
> put_logos(group, token)

确认上传的logo。Confirms the uploaded logo.

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
    api_instance = cnb_api.AssetsApi(api_client)
    group = 'test-group/test-repo' # str | group (default to 'test-group/test-repo')
    token = 'token_example' # str | 获取 uploadurl 时返回的token。The token returned when getting the uploadurl.

    try:
        # 确认上传的logo。Confirms the uploaded logo.
        api_instance.put_logos(group, token)
    except Exception as e:
        print("Exception when calling AssetsApi->put_logos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| group | [default to &#39;test-group/test-repo&#39;]
 **token** | **str**| 获取 uploadurl 时返回的token。The token returned when getting the uploadurl. | 

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

# **upload_files**
> DtoUploadAssetsResponse upload_files(repo, request)

发起一个上传 files 的请求，返回上传 cos 的 url 和 form 内容。Initiate a request to upload files,returns COS upload URL and form data.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-contents:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_upload_assets_response import DtoUploadAssetsResponse
from cnb_api.models.dto_upload_request_params import DtoUploadRequestParams
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
    api_instance = cnb_api.AssetsApi(api_client)
    repo = 'test-group/test-repo' # str | repo (default to 'test-group/test-repo')
    request = cnb_api.DtoUploadRequestParams() # DtoUploadRequestParams | UploadRequestParams

    try:
        # 发起一个上传 files 的请求，返回上传 cos 的 url 和 form 内容。Initiate a request to upload files,returns COS upload URL and form data.
        api_response = api_instance.upload_files(repo, request)
        print("The response of AssetsApi->upload_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->upload_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | [default to &#39;test-group/test-repo&#39;]
 **request** | [**DtoUploadRequestParams**](DtoUploadRequestParams.md)| UploadRequestParams | 

### Return type

[**DtoUploadAssetsResponse**](DtoUploadAssetsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/vnd.cnb.web+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_imgs**
> DtoUploadAssetsResponse upload_imgs(repo, request)

发起一个上传 imgs 的请求，返回上传 cos 的 url 和 form 内容。发起一个上传 imgs 的请求，返回上传 cos 的 url 和 form 内容.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-contents:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_upload_assets_response import DtoUploadAssetsResponse
from cnb_api.models.dto_upload_request_params import DtoUploadRequestParams
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
    api_instance = cnb_api.AssetsApi(api_client)
    repo = 'test-group/test-repo' # str | repo (default to 'test-group/test-repo')
    request = cnb_api.DtoUploadRequestParams() # DtoUploadRequestParams | UploadRequestParams

    try:
        # 发起一个上传 imgs 的请求，返回上传 cos 的 url 和 form 内容。发起一个上传 imgs 的请求，返回上传 cos 的 url 和 form 内容.
        api_response = api_instance.upload_imgs(repo, request)
        print("The response of AssetsApi->upload_imgs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->upload_imgs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | [default to &#39;test-group/test-repo&#39;]
 **request** | [**DtoUploadRequestParams**](DtoUploadRequestParams.md)| UploadRequestParams | 

### Return type

[**DtoUploadAssetsResponse**](DtoUploadAssetsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/vnd.cnb.web+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_logos**
> DtoUploadAssetsResponse upload_logos(group, request)

发起一个上传 logo 的请求，返回上传 cos 的 url 和 form 内容。Post a request to upload a logo.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
group-manage:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_upload_assets_response import DtoUploadAssetsResponse
from cnb_api.models.dto_upload_request_params import DtoUploadRequestParams
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
    api_instance = cnb_api.AssetsApi(api_client)
    group = 'test-group' # str | group (default to 'test-group')
    request = cnb_api.DtoUploadRequestParams() # DtoUploadRequestParams | UploadRequestParams

    try:
        # 发起一个上传 logo 的请求，返回上传 cos 的 url 和 form 内容。Post a request to upload a logo.
        api_response = api_instance.upload_logos(group, request)
        print("The response of AssetsApi->upload_logos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->upload_logos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| group | [default to &#39;test-group&#39;]
 **request** | [**DtoUploadRequestParams**](DtoUploadRequestParams.md)| UploadRequestParams | 

### Return type

[**DtoUploadAssetsResponse**](DtoUploadAssetsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/vnd.cnb.web+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_releases**
> DtoUploadAssetsResponse upload_releases(repo, tag_name, request)

发起一个上传 release 附件的请求，返回上传 cos 的 url 和 form 内容。Initiate a request to upload release attachments, returns COS upload URL and form data.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
repo-contents:rw

### Example

* Api Key Authentication (BearerAuth):

```python
import cnb_api
from cnb_api.models.dto_upload_assets_response import DtoUploadAssetsResponse
from cnb_api.models.dto_upload_request_params import DtoUploadRequestParams
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
    api_instance = cnb_api.AssetsApi(api_client)
    repo = 'test-group/test-repo' # str | repo (default to 'test-group/test-repo')
    tag_name = 'tag_name_example' # str | tag_name
    request = cnb_api.DtoUploadRequestParams() # DtoUploadRequestParams | UploadRequestParams

    try:
        # 发起一个上传 release 附件的请求，返回上传 cos 的 url 和 form 内容。Initiate a request to upload release attachments, returns COS upload URL and form data.
        api_response = api_instance.upload_releases(repo, tag_name, request)
        print("The response of AssetsApi->upload_releases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->upload_releases: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| repo | [default to &#39;test-group/test-repo&#39;]
 **tag_name** | **str**| tag_name | 
 **request** | [**DtoUploadRequestParams**](DtoUploadRequestParams.md)| UploadRequestParams | 

### Return type

[**DtoUploadAssetsResponse**](DtoUploadAssetsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/vnd.cnb.web+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

