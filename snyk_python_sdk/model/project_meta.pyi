# coding: utf-8

"""
    Snyk API

    Snyk helps software-driven businesses develop fast and stay secure. Continuously find and fix vulnerabilities for npm, Maven, NuGet, RubyGems, PyPI and more.

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


class ProjectMeta(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "issues_critical_count",
            "issues_medium_count",
            "last_tested_at",
            "imported",
            "issues_low_count",
            "issues_high_count",
        }
        
        class properties:
            imported = schemas.DateTimeSchema
            issues_critical_count = schemas.NumberSchema
            issues_high_count = schemas.NumberSchema
            issues_low_count = schemas.NumberSchema
            issues_medium_count = schemas.NumberSchema
            last_tested_at = schemas.DateTimeSchema
            __annotations__ = {
                "imported": imported,
                "issues_critical_count": issues_critical_count,
                "issues_high_count": issues_high_count,
                "issues_low_count": issues_low_count,
                "issues_medium_count": issues_medium_count,
                "last_tested_at": last_tested_at,
            }
    
    issues_critical_count: MetaOapg.properties.issues_critical_count
    issues_medium_count: MetaOapg.properties.issues_medium_count
    last_tested_at: MetaOapg.properties.last_tested_at
    imported: MetaOapg.properties.imported
    issues_low_count: MetaOapg.properties.issues_low_count
    issues_high_count: MetaOapg.properties.issues_high_count
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["imported"]) -> MetaOapg.properties.imported: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["issues_critical_count"]) -> MetaOapg.properties.issues_critical_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["issues_high_count"]) -> MetaOapg.properties.issues_high_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["issues_low_count"]) -> MetaOapg.properties.issues_low_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["issues_medium_count"]) -> MetaOapg.properties.issues_medium_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_tested_at"]) -> MetaOapg.properties.last_tested_at: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["imported", "issues_critical_count", "issues_high_count", "issues_low_count", "issues_medium_count", "last_tested_at", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["imported"]) -> MetaOapg.properties.imported: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["issues_critical_count"]) -> MetaOapg.properties.issues_critical_count: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["issues_high_count"]) -> MetaOapg.properties.issues_high_count: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["issues_low_count"]) -> MetaOapg.properties.issues_low_count: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["issues_medium_count"]) -> MetaOapg.properties.issues_medium_count: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_tested_at"]) -> MetaOapg.properties.last_tested_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["imported", "issues_critical_count", "issues_high_count", "issues_low_count", "issues_medium_count", "last_tested_at", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        issues_critical_count: typing.Union[MetaOapg.properties.issues_critical_count, decimal.Decimal, int, float, ],
        issues_medium_count: typing.Union[MetaOapg.properties.issues_medium_count, decimal.Decimal, int, float, ],
        last_tested_at: typing.Union[MetaOapg.properties.last_tested_at, str, datetime, ],
        imported: typing.Union[MetaOapg.properties.imported, str, datetime, ],
        issues_low_count: typing.Union[MetaOapg.properties.issues_low_count, decimal.Decimal, int, float, ],
        issues_high_count: typing.Union[MetaOapg.properties.issues_high_count, decimal.Decimal, int, float, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ProjectMeta':
        return super().__new__(
            cls,
            *args,
            issues_critical_count=issues_critical_count,
            issues_medium_count=issues_medium_count,
            last_tested_at=last_tested_at,
            imported=imported,
            issues_low_count=issues_low_count,
            issues_high_count=issues_high_count,
            _configuration=_configuration,
            **kwargs,
        )
