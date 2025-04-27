# cnb_api.MissionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_mission**](MissionsApi.md#delete_mission) | **DELETE** /{mission} | 删除指定任务集。Delete the specified mission.


# **delete_mission**
> delete_mission(mission, x_cnb_identity_ticket=x_cnb_identity_ticket)

删除指定任务集。Delete the specified mission.

访问令牌调用此接口需包含以下权限。Required permissions for access token. 
mission-delete:rw

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
    api_instance = cnb_api.MissionsApi(api_client)
    mission = 'mission_example' # str | mission path
    x_cnb_identity_ticket = 'x_cnb_identity_ticket_example' # str | 微信身份验证票据，首次请求不传会返回新票据。WeChat auth ticket, will return new ticket if not provided in first request. (optional)

    try:
        # 删除指定任务集。Delete the specified mission.
        api_instance.delete_mission(mission, x_cnb_identity_ticket=x_cnb_identity_ticket)
    except Exception as e:
        print("Exception when calling MissionsApi->delete_mission: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mission** | **str**| mission path | 
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

