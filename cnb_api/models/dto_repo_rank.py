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

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cnb_api.models.dto_rank_detail import DtoRankDetail
from typing import Optional, Set
from typing_extensions import Self

class DtoRepoRank(BaseModel):
    """
    DtoRepoRank
    """ # noqa: E501
    rank_type: Optional[StrictStr] = None
    repo_detail: Optional[List[DtoRankDetail]] = None
    top_n: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["rank_type", "repo_detail", "top_n"]

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
        """Create an instance of DtoRepoRank from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in repo_detail (list)
        _items = []
        if self.repo_detail:
            for _item_repo_detail in self.repo_detail:
                if _item_repo_detail:
                    _items.append(_item_repo_detail.to_dict())
            _dict['repo_detail'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DtoRepoRank from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "rank_type": obj.get("rank_type"),
            "repo_detail": [DtoRankDetail.from_dict(_item) for _item in obj["repo_detail"]] if obj.get("repo_detail") is not None else None,
            "top_n": obj.get("top_n")
        })
        return _obj


