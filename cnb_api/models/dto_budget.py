# coding: utf-8

"""
    CNB OPENAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Contact: cnb@tencent.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from cnb_api.models.constant_budget_sts import ConstantBudgetSts
from typing import Optional, Set
from typing_extensions import Self

class DtoBudget(BaseModel):
    """
    DtoBudget
    """ # noqa: E501
    charge_type_ci: Optional[StrictInt] = Field(default=None, description="单位：核时")
    charge_type_ci_policy: Optional[Union[StrictFloat, StrictInt]] = None
    charge_type_ci_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="ci价格，单位：分")
    charge_type_dev: Optional[StrictInt] = None
    charge_type_dev_policy: Optional[Union[StrictFloat, StrictInt]] = None
    charge_type_dev_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="开发价格，单位：分")
    charge_type_git: Optional[StrictInt] = Field(default=None, description="单位：Gib")
    charge_type_git_policy: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="折扣，没折扣是100")
    charge_type_git_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="git存储价格，单位：分")
    charge_type_object: Optional[StrictInt] = None
    charge_type_object_policy: Optional[Union[StrictFloat, StrictInt]] = None
    charge_type_object_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="对象存储价格，单位：分")
    name: Optional[StrictStr] = Field(default=None, description="预算单名称")
    status: Optional[ConstantBudgetSts] = Field(default=None, description="预算单状态，1-正常，2-隔离，3-销毁")
    uin: Optional[StrictStr] = Field(default=None, description="云账号id")
    __properties: ClassVar[List[str]] = ["charge_type_ci", "charge_type_ci_policy", "charge_type_ci_price", "charge_type_dev", "charge_type_dev_policy", "charge_type_dev_price", "charge_type_git", "charge_type_git_policy", "charge_type_git_price", "charge_type_object", "charge_type_object_policy", "charge_type_object_price", "name", "status", "uin"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of DtoBudget from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DtoBudget from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "charge_type_ci": obj.get("charge_type_ci"),
            "charge_type_ci_policy": obj.get("charge_type_ci_policy"),
            "charge_type_ci_price": obj.get("charge_type_ci_price"),
            "charge_type_dev": obj.get("charge_type_dev"),
            "charge_type_dev_policy": obj.get("charge_type_dev_policy"),
            "charge_type_dev_price": obj.get("charge_type_dev_price"),
            "charge_type_git": obj.get("charge_type_git"),
            "charge_type_git_policy": obj.get("charge_type_git_policy"),
            "charge_type_git_price": obj.get("charge_type_git_price"),
            "charge_type_object": obj.get("charge_type_object"),
            "charge_type_object_policy": obj.get("charge_type_object_policy"),
            "charge_type_object_price": obj.get("charge_type_object_price"),
            "name": obj.get("name"),
            "status": obj.get("status"),
            "uin": obj.get("uin")
        })
        return _obj


