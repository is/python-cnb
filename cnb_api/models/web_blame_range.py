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

from pydantic import BaseModel, ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from cnb_api.models.web_commit import WebCommit
from typing import Optional, Set
from typing_extensions import Self

class WebBlameRange(BaseModel):
    """
    WebBlameRange
    """ # noqa: E501
    age: Optional[StrictInt] = None
    commit: Optional[WebCommit] = None
    ending_line: Optional[StrictInt] = None
    starting_line: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["age", "commit", "ending_line", "starting_line"]

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
        """Create an instance of WebBlameRange from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of commit
        if self.commit:
            _dict['commit'] = self.commit.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WebBlameRange from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "age": obj.get("age"),
            "commit": WebCommit.from_dict(obj["commit"]) if obj.get("commit") is not None else None,
            "ending_line": obj.get("ending_line"),
            "starting_line": obj.get("starting_line")
        })
        return _obj


