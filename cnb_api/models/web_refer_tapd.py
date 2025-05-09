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

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class WebReferTapd(BaseModel):
    """
    WebReferTapd
    """ # noqa: E501
    created: Optional[StrictStr] = None
    due: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    owner: Optional[StrictStr] = None
    priority: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    view_link: Optional[StrictStr] = None
    workspace_id: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["created", "due", "id", "name", "owner", "priority", "status", "type", "view_link", "workspace_id"]

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
        """Create an instance of WebReferTapd from a JSON string"""
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
        """Create an instance of WebReferTapd from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created": obj.get("created"),
            "due": obj.get("due"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "owner": obj.get("owner"),
            "priority": obj.get("priority"),
            "status": obj.get("status"),
            "type": obj.get("type"),
            "view_link": obj.get("view_link"),
            "workspace_id": obj.get("workspace_id")
        })
        return _obj


