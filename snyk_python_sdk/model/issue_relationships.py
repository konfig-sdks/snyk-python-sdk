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


class IssueRelationships(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    issue relationships
    """


    class MetaOapg:
        required = {
            "organization",
            "scan_item",
        }
        
        class properties:
        
            @staticmethod
            def organization() -> typing.Type['IssueRelationshipsOrganization']:
                return IssueRelationshipsOrganization
        
            @staticmethod
            def scan_item() -> typing.Type['IssueRelationshipsScanItem']:
                return IssueRelationshipsScanItem
        
            @staticmethod
            def ignore() -> typing.Type['IssueRelationshipsIgnore']:
                return IssueRelationshipsIgnore
        
            @staticmethod
            def test_executions() -> typing.Type['IssueRelationshipsTestExecutions']:
                return IssueRelationshipsTestExecutions
            __annotations__ = {
                "organization": organization,
                "scan_item": scan_item,
                "ignore": ignore,
                "test_executions": test_executions,
            }
    
    organization: 'IssueRelationshipsOrganization'
    scan_item: 'IssueRelationshipsScanItem'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["organization"]) -> 'IssueRelationshipsOrganization': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scan_item"]) -> 'IssueRelationshipsScanItem': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ignore"]) -> 'IssueRelationshipsIgnore': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["test_executions"]) -> 'IssueRelationshipsTestExecutions': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["organization", "scan_item", "ignore", "test_executions", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["organization"]) -> 'IssueRelationshipsOrganization': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scan_item"]) -> 'IssueRelationshipsScanItem': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ignore"]) -> typing.Union['IssueRelationshipsIgnore', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["test_executions"]) -> typing.Union['IssueRelationshipsTestExecutions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["organization", "scan_item", "ignore", "test_executions", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        organization: 'IssueRelationshipsOrganization',
        scan_item: 'IssueRelationshipsScanItem',
        ignore: typing.Union['IssueRelationshipsIgnore', schemas.Unset] = schemas.unset,
        test_executions: typing.Union['IssueRelationshipsTestExecutions', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'IssueRelationships':
        return super().__new__(
            cls,
            *args,
            organization=organization,
            scan_item=scan_item,
            ignore=ignore,
            test_executions=test_executions,
            _configuration=_configuration,
            **kwargs,
        )

from snyk_python_sdk.model.issue_relationships_ignore import IssueRelationshipsIgnore
from snyk_python_sdk.model.issue_relationships_organization import IssueRelationshipsOrganization
from snyk_python_sdk.model.issue_relationships_scan_item import IssueRelationshipsScanItem
from snyk_python_sdk.model.issue_relationships_test_executions import IssueRelationshipsTestExecutions
