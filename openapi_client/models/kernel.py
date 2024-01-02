# coding: utf-8

"""
    Jupyter Server API

    Server API

    The version of the OpenAPI document: 5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Kernel(BaseModel):
    """
    Kernel information
    """ # noqa: E501
    id: StrictStr = Field(description="uuid of kernel")
    name: StrictStr = Field(description="kernel spec name")
    last_activity: Optional[StrictStr] = Field(default=None, description="ISO 8601 timestamp for the last-seen activity on this kernel. Use this in combination with execution_state == 'idle' to identify which kernels have been idle since a given time. Timestamps will be UTC, indicated 'Z' suffix. Added in notebook server 5.0. ")
    connections: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The number of active connections to this kernel. ")
    execution_state: Optional[StrictStr] = Field(default=None, description="Current execution state of the kernel (typically 'idle' or 'busy', but may be other values, such as 'starting'). Added in notebook server 5.0. ")
    __properties: ClassVar[List[str]] = ["id", "name", "last_activity", "connections", "execution_state"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Kernel from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Kernel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "last_activity": obj.get("last_activity"),
            "connections": obj.get("connections"),
            "execution_state": obj.get("execution_state")
        })
        return _obj

