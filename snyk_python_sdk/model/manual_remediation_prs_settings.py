# coding: utf-8

"""
    Snyk API

    Missing description placeholder

    The version of the OpenAPI document: REST
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from snyk_python_sdk import schemas  # noqa: F401


class ManualRemediationPRsSettings(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Manually raise pull requests to fix new and existing vulnerabilities. If not specified, settings will be inherited from the Project's integration.
    """


    class MetaOapg:
        
        class properties:
            is_patch_remediation_enabled = schemas.BoolSchema
            __annotations__ = {
                "is_patch_remediation_enabled": is_patch_remediation_enabled,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_patch_remediation_enabled"]) -> MetaOapg.properties.is_patch_remediation_enabled: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["is_patch_remediation_enabled", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_patch_remediation_enabled"]) -> typing.Union[MetaOapg.properties.is_patch_remediation_enabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["is_patch_remediation_enabled", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        is_patch_remediation_enabled: typing.Union[MetaOapg.properties.is_patch_remediation_enabled, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ManualRemediationPRsSettings':
        return super().__new__(
            cls,
            *args,
            is_patch_remediation_enabled=is_patch_remediation_enabled,
            _configuration=_configuration,
            **kwargs,
        )
