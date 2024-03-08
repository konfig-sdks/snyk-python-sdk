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


class IssuesListByOrgId403Response(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "jsonapi",
            "errors",
        }
        
        class properties:
        
            @staticmethod
            def errors() -> typing.Type['IssuesListByOrgId403ResponseErrors']:
                return IssuesListByOrgId403ResponseErrors
        
            @staticmethod
            def jsonapi() -> typing.Type['IssuesListByOrgId403ResponseJsonapi']:
                return IssuesListByOrgId403ResponseJsonapi
            __annotations__ = {
                "errors": errors,
                "jsonapi": jsonapi,
            }
    
    jsonapi: 'IssuesListByOrgId403ResponseJsonapi'
    errors: 'IssuesListByOrgId403ResponseErrors'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["errors"]) -> 'IssuesListByOrgId403ResponseErrors': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["jsonapi"]) -> 'IssuesListByOrgId403ResponseJsonapi': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["errors", "jsonapi", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["errors"]) -> 'IssuesListByOrgId403ResponseErrors': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["jsonapi"]) -> 'IssuesListByOrgId403ResponseJsonapi': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["errors", "jsonapi", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        jsonapi: 'IssuesListByOrgId403ResponseJsonapi',
        errors: 'IssuesListByOrgId403ResponseErrors',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'IssuesListByOrgId403Response':
        return super().__new__(
            cls,
            *args,
            jsonapi=jsonapi,
            errors=errors,
            _configuration=_configuration,
            **kwargs,
        )

from snyk_python_sdk.model.issues_list_by_org_id403_response_errors import IssuesListByOrgId403ResponseErrors
from snyk_python_sdk.model.issues_list_by_org_id403_response_jsonapi import IssuesListByOrgId403ResponseJsonapi
