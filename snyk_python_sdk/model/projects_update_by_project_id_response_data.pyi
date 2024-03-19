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


class ProjectsUpdateByProjectIdResponseData(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "attributes",
            "id",
            "type",
        }
        
        class properties:
        
            @staticmethod
            def attributes() -> typing.Type['ProjectAttributes']:
                return ProjectAttributes
            id = schemas.UUIDSchema
            type = schemas.StrSchema
        
            @staticmethod
            def links() -> typing.Type['Links']:
                return Links
        
            @staticmethod
            def meta() -> typing.Type['ProjectsUpdateByProjectIdResponseDataMeta']:
                return ProjectsUpdateByProjectIdResponseDataMeta
        
            @staticmethod
            def relationships() -> typing.Type['ProjectsUpdateByProjectIdResponseDataRelationships']:
                return ProjectsUpdateByProjectIdResponseDataRelationships
            __annotations__ = {
                "attributes": attributes,
                "id": id,
                "type": type,
                "links": links,
                "meta": meta,
                "relationships": relationships,
            }
    
    attributes: 'ProjectAttributes'
    id: MetaOapg.properties.id
    type: MetaOapg.properties.type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attributes"]) -> 'ProjectAttributes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["links"]) -> 'Links': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["meta"]) -> 'ProjectsUpdateByProjectIdResponseDataMeta': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["relationships"]) -> 'ProjectsUpdateByProjectIdResponseDataRelationships': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["attributes", "id", "type", "links", "meta", "relationships", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attributes"]) -> 'ProjectAttributes': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["links"]) -> typing.Union['Links', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["meta"]) -> typing.Union['ProjectsUpdateByProjectIdResponseDataMeta', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["relationships"]) -> typing.Union['ProjectsUpdateByProjectIdResponseDataRelationships', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["attributes", "id", "type", "links", "meta", "relationships", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        attributes: 'ProjectAttributes',
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        links: typing.Union['Links', schemas.Unset] = schemas.unset,
        meta: typing.Union['ProjectsUpdateByProjectIdResponseDataMeta', schemas.Unset] = schemas.unset,
        relationships: typing.Union['ProjectsUpdateByProjectIdResponseDataRelationships', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ProjectsUpdateByProjectIdResponseData':
        return super().__new__(
            cls,
            *args,
            attributes=attributes,
            id=id,
            type=type,
            links=links,
            meta=meta,
            relationships=relationships,
            _configuration=_configuration,
            **kwargs,
        )

from snyk_python_sdk.model.links import Links
from snyk_python_sdk.model.project_attributes import ProjectAttributes
from snyk_python_sdk.model.projects_update_by_project_id_response_data_meta import ProjectsUpdateByProjectIdResponseDataMeta
from snyk_python_sdk.model.projects_update_by_project_id_response_data_relationships import ProjectsUpdateByProjectIdResponseDataRelationships
