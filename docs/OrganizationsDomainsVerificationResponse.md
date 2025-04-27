# OrganizationsDomainsVerificationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domains** | **List[str]** |  | [optional] 
**domains_by** | **List[str]** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | **bool** |  | [optional] 
**txt_match** | **bool** |  | [optional] 
**txt_value** | **str** |  | [optional] 
**valid** | **bool** |  | [optional] 

## Example

```python
from cnb_api.models.organizations_domains_verification_response import OrganizationsDomainsVerificationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationsDomainsVerificationResponse from a JSON string
organizations_domains_verification_response_instance = OrganizationsDomainsVerificationResponse.from_json(json)
# print the JSON string representation of the object
print(OrganizationsDomainsVerificationResponse.to_json())

# convert the object into a dict
organizations_domains_verification_response_dict = organizations_domains_verification_response_instance.to_dict()
# create an instance of OrganizationsDomainsVerificationResponse from a dict
organizations_domains_verification_response_from_dict = OrganizationsDomainsVerificationResponse.from_dict(organizations_domains_verification_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


