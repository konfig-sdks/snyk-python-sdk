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


class ProjectsUpdateByProjectIdResponseDataRelationshipsOrganization(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "data",
            "links",
        }
        
        class properties:
        
            @staticmethod
            def data() -> typing.Type['ProjectsUpdateByProjectIdResponseDataRelationshipsOrganizationData']:
                return ProjectsUpdateByProjectIdResponseDataRelationshipsOrganizationData
        
            @staticmethod
            def links() -> typing.Type['ProjectsUpdateByProjectIdResponseDataRelationshipsOrganizationLinks']:
                return ProjectsUpdateByProjectIdResponseDataRelationshipsOrganizationLinks
        
            @staticmethod
            def meta() -> typing.Type['ProjectsUpdateByProjectIdResponseDataRelationshipsOrganizationMeta']:
                return ProjectsUpdateByProjectIdResponseDataRelationshipsOrganizationMeta
            __annotations__ = {
                "data": data,
                "links": links,
                "meta": meta,
            }
    
    data: 'ProjectsUpdateByProjectIdResponseDataRelationshipsOrganizationData'
    links: 'ProjectsUpdateByProjectIdResponseDataRelationshipsOrganizationLinks'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> 'ProjectsUpdateByProjectIdResponseDataRelationshipsOrganizationData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["links"]) -> 'ProjectsUpdateByProjectIdResponseDataRelationshipsOrganizationLinks': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["meta"]) -> 'ProjectsUpdateByProjectIdResponseDataRelationshipsOrganizationMeta': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["data", "links", "meta", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> 'ProjectsUpdateByProjectIdResponseDataRelationshipsOrganizationData': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["links"]) -> 'ProjectsUpdateByProjectIdResponseDataRelationshipsOrganizationLinks': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["meta"]) -> typing.Union['ProjectsUpdateByProjectIdResponseDataRelationshipsOrganizationMeta', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["data", "links", "meta", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        data: 'ProjectsUpdateByProjectIdResponseDataRelationshipsOrganizationData',
        links: 'ProjectsUpdateByProjectIdResponseDataRelationshipsOrganizationLinks',
        meta: typing.Union['ProjectsUpdateByProjectIdResponseDataRelationshipsOrganizationMeta', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ProjectsUpdateByProjectIdResponseDataRelationshipsOrganization':
        return super().__new__(
            cls,
            *args,
            data=data,
            links=links,
            meta=meta,
            _configuration=_configuration,
            **kwargs,
        )

from snyk_python_sdk.model.projects_update_by_project_id_response_data_relationships_organization_data import ProjectsUpdateByProjectIdResponseDataRelationshipsOrganizationData
from snyk_python_sdk.model.projects_update_by_project_id_response_data_relationships_organization_links import ProjectsUpdateByProjectIdResponseDataRelationshipsOrganizationLinks
from snyk_python_sdk.model.projects_update_by_project_id_response_data_relationships_organization_meta import ProjectsUpdateByProjectIdResponseDataRelationshipsOrganizationMeta
