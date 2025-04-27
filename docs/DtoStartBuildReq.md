# DtoStartBuildReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch** | **str** | 触发分支，默认为主分支 | [optional] 
**config** | **str** | 指定配置文件内容，yaml 格式 | [optional] 
**env** | **Dict[str, str]** | 环境变量，对象格式 | [optional] 
**event** | **str** | 事件名，必须是 api_trigger 或以 api_trigger_ 开头，默认为 &#x60;api_trigger&#x60; | [optional] 
**sha** | **str** | commit id ，优先级比 tag 高，默认为分支最新提交记录 | [optional] 
**sync** | **str** | 是否等待构建正式触发，为false时会立刻返回 sn 和 buildLogUrl | [optional] 
**tag** | **str** | 触发 tag，优先级比 branch 高 | [optional] 

## Example

```python
from cnb_api.models.dto_start_build_req import DtoStartBuildReq

# TODO update the JSON string below
json = "{}"
# create an instance of DtoStartBuildReq from a JSON string
dto_start_build_req_instance = DtoStartBuildReq.from_json(json)
# print the JSON string representation of the object
print(DtoStartBuildReq.to_json())

# convert the object into a dict
dto_start_build_req_dict = dto_start_build_req_instance.to_dict()
# create an instance of DtoStartBuildReq from a dict
dto_start_build_req_from_dict = DtoStartBuildReq.from_dict(dto_start_build_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


