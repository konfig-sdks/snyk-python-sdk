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


class ProjectsListForOrgResponseDataItemRelationshipsImporter(
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
            def data() -> typing.Type['ProjectsListForOrgResponseDataItemRelationshipsImporterData']:
                return ProjectsListForOrgResponseDataItemRelationshipsImporterData
        
            @staticmethod
            def links() -> typing.Type['ProjectsListForOrgResponseDataItemRelationshipsImporterLinks']:
                return ProjectsListForOrgResponseDataItemRelationshipsImporterLinks
        
            @staticmethod
            def meta() -> typing.Type['ProjectsListForOrgResponseDataItemRelationshipsImporterMeta']:
                return ProjectsListForOrgResponseDataItemRelationshipsImporterMeta
            __annotations__ = {
                "data": data,
                "links": links,
                "meta": meta,
            }
    
    data: 'ProjectsListForOrgResponseDataItemRelationshipsImporterData'
    links: 'ProjectsListForOrgResponseDataItemRelationshipsImporterLinks'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> 'ProjectsListForOrgResponseDataItemRelationshipsImporterData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["links"]) -> 'ProjectsListForOrgResponseDataItemRelationshipsImporterLinks': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["meta"]) -> 'ProjectsListForOrgResponseDataItemRelationshipsImporterMeta': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["data", "links", "meta", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> 'ProjectsListForOrgResponseDataItemRelationshipsImporterData': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["links"]) -> 'ProjectsListForOrgResponseDataItemRelationshipsImporterLinks': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["meta"]) -> typing.Union['ProjectsListForOrgResponseDataItemRelationshipsImporterMeta', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["data", "links", "meta", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        data: 'ProjectsListForOrgResponseDataItemRelationshipsImporterData',
        links: 'ProjectsListForOrgResponseDataItemRelationshipsImporterLinks',
        meta: typing.Union['ProjectsListForOrgResponseDataItemRelationshipsImporterMeta', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ProjectsListForOrgResponseDataItemRelationshipsImporter':
        return super().__new__(
            cls,
            *args,
            data=data,
            links=links,
            meta=meta,
            _configuration=_configuration,
            **kwargs,
        )

from snyk_python_sdk.model.projects_list_for_org_response_data_item_relationships_importer_data import ProjectsListForOrgResponseDataItemRelationshipsImporterData
from snyk_python_sdk.model.projects_list_for_org_response_data_item_relationships_importer_links import ProjectsListForOrgResponseDataItemRelationshipsImporterLinks
from snyk_python_sdk.model.projects_list_for_org_response_data_item_relationships_importer_meta import ProjectsListForOrgResponseDataItemRelationshipsImporterMeta