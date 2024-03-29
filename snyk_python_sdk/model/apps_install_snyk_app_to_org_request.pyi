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


class AppsInstallSnykAppToOrgRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "relationships",
            "data",
        }
        
        class properties:
        
            @staticmethod
            def data() -> typing.Type['AppsInstallSnykAppToOrgRequestData']:
                return AppsInstallSnykAppToOrgRequestData
        
            @staticmethod
            def relationships() -> typing.Type['AppsInstallSnykAppToOrgRequestRelationships']:
                return AppsInstallSnykAppToOrgRequestRelationships
            __annotations__ = {
                "data": data,
                "relationships": relationships,
            }
    
    relationships: 'AppsInstallSnykAppToOrgRequestRelationships'
    data: 'AppsInstallSnykAppToOrgRequestData'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> 'AppsInstallSnykAppToOrgRequestData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["relationships"]) -> 'AppsInstallSnykAppToOrgRequestRelationships': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["data", "relationships", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> 'AppsInstallSnykAppToOrgRequestData': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["relationships"]) -> 'AppsInstallSnykAppToOrgRequestRelationships': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["data", "relationships", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        relationships: 'AppsInstallSnykAppToOrgRequestRelationships',
        data: 'AppsInstallSnykAppToOrgRequestData',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AppsInstallSnykAppToOrgRequest':
        return super().__new__(
            cls,
            *args,
            relationships=relationships,
            data=data,
            _configuration=_configuration,
            **kwargs,
        )

from snyk_python_sdk.model.apps_install_snyk_app_to_org_request_data import AppsInstallSnykAppToOrgRequestData
from snyk_python_sdk.model.apps_install_snyk_app_to_org_request_relationships import AppsInstallSnykAppToOrgRequestRelationships
