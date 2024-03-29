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


class OSConditionRiskFactor(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "updated_at",
            "name",
            "value",
        }
        
        class properties:
            name = schemas.StrSchema
            updated_at = schemas.DateTimeSchema
            value = schemas.BoolSchema
            included_in_score = schemas.BoolSchema
        
            @staticmethod
            def links() -> typing.Type['RiskFactorLinks']:
                return RiskFactorLinks
            __annotations__ = {
                "name": name,
                "updated_at": updated_at,
                "value": value,
                "included_in_score": included_in_score,
                "links": links,
            }
    
    updated_at: MetaOapg.properties.updated_at
    name: MetaOapg.properties.name
    value: MetaOapg.properties.value
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["included_in_score"]) -> MetaOapg.properties.included_in_score: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["links"]) -> 'RiskFactorLinks': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "updated_at", "value", "included_in_score", "links", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["included_in_score"]) -> typing.Union[MetaOapg.properties.included_in_score, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["links"]) -> typing.Union['RiskFactorLinks', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "updated_at", "value", "included_in_score", "links", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        updated_at: typing.Union[MetaOapg.properties.updated_at, str, datetime, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        value: typing.Union[MetaOapg.properties.value, bool, ],
        included_in_score: typing.Union[MetaOapg.properties.included_in_score, bool, schemas.Unset] = schemas.unset,
        links: typing.Union['RiskFactorLinks', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OSConditionRiskFactor':
        return super().__new__(
            cls,
            *args,
            updated_at=updated_at,
            name=name,
            value=value,
            included_in_score=included_in_score,
            links=links,
            _configuration=_configuration,
            **kwargs,
        )

from snyk_python_sdk.model.risk_factor_links import RiskFactorLinks
