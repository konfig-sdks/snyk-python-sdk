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


class CustomBaseImageSnapshot(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            group_id = schemas.UUIDSchema
            include_in_recommendations = schemas.BoolSchema
            org_id = schemas.UUIDSchema
            project_id = schemas.UUIDSchema
            repository = schemas.StrSchema
            tag = schemas.StrSchema
            __annotations__ = {
                "group_id": group_id,
                "include_in_recommendations": include_in_recommendations,
                "org_id": org_id,
                "project_id": project_id,
                "repository": repository,
                "tag": tag,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["group_id"]) -> MetaOapg.properties.group_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["include_in_recommendations"]) -> MetaOapg.properties.include_in_recommendations: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["org_id"]) -> MetaOapg.properties.org_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["project_id"]) -> MetaOapg.properties.project_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["repository"]) -> MetaOapg.properties.repository: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tag"]) -> MetaOapg.properties.tag: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["group_id", "include_in_recommendations", "org_id", "project_id", "repository", "tag", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["group_id"]) -> typing.Union[MetaOapg.properties.group_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["include_in_recommendations"]) -> typing.Union[MetaOapg.properties.include_in_recommendations, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["org_id"]) -> typing.Union[MetaOapg.properties.org_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["project_id"]) -> typing.Union[MetaOapg.properties.project_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["repository"]) -> typing.Union[MetaOapg.properties.repository, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tag"]) -> typing.Union[MetaOapg.properties.tag, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["group_id", "include_in_recommendations", "org_id", "project_id", "repository", "tag", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        group_id: typing.Union[MetaOapg.properties.group_id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        include_in_recommendations: typing.Union[MetaOapg.properties.include_in_recommendations, bool, schemas.Unset] = schemas.unset,
        org_id: typing.Union[MetaOapg.properties.org_id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        project_id: typing.Union[MetaOapg.properties.project_id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        repository: typing.Union[MetaOapg.properties.repository, str, schemas.Unset] = schemas.unset,
        tag: typing.Union[MetaOapg.properties.tag, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CustomBaseImageSnapshot':
        return super().__new__(
            cls,
            *args,
            group_id=group_id,
            include_in_recommendations=include_in_recommendations,
            org_id=org_id,
            project_id=project_id,
            repository=repository,
            tag=tag,
            _configuration=_configuration,
            **kwargs,
        )
