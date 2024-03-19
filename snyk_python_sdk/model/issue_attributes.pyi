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


class IssueAttributes(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    issue attributes
    """


    class MetaOapg:
        required = {
            "ignored",
            "updated_at",
            "created_at",
            "title",
            "type",
            "key",
            "effective_severity_level",
            "status",
        }
        
        class properties:
            
            
            class title(
                schemas.StrSchema
            ):
                pass
            created_at = schemas.DateTimeSchema
            
            
            class effective_severity_level(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def INFO(cls):
                    return cls("info")
                
                @schemas.classproperty
                def LOW(cls):
                    return cls("low")
                
                @schemas.classproperty
                def MEDIUM(cls):
                    return cls("medium")
                
                @schemas.classproperty
                def HIGH(cls):
                    return cls("high")
                
                @schemas.classproperty
                def CRITICAL(cls):
                    return cls("critical")
            ignored = schemas.BoolSchema
            
            
            class key(
                schemas.StrSchema
            ):
                pass
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def OPEN(cls):
                    return cls("open")
                
                @schemas.classproperty
                def RESOLVED(cls):
                    return cls("resolved")
        
            @staticmethod
            def type() -> typing.Type['TypeDef']:
                return TypeDef
            updated_at = schemas.DateTimeSchema
            
            
            class description(
                schemas.StrSchema
            ):
                pass
            
            
            class classes(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ModelClass']:
                        return ModelClass
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ModelClass'], typing.List['ModelClass']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'classes':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ModelClass':
                    return super().__getitem__(i)
            
            
            class coordinates(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Coordinate']:
                        return Coordinate
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['Coordinate'], typing.List['Coordinate']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'coordinates':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Coordinate':
                    return super().__getitem__(i)
            
            
            class problems(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Problem']:
                        return Problem
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['Problem'], typing.List['Problem']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'problems':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Problem':
                    return super().__getitem__(i)
        
            @staticmethod
            def resolution() -> typing.Type['Resolution']:
                return Resolution
        
            @staticmethod
            def risk() -> typing.Type['Risk']:
                return Risk
            
            
            class tool(
                schemas.StrSchema
            ):
                pass
            __annotations__ = {
                "title": title,
                "created_at": created_at,
                "effective_severity_level": effective_severity_level,
                "ignored": ignored,
                "key": key,
                "status": status,
                "type": type,
                "updated_at": updated_at,
                "description": description,
                "classes": classes,
                "coordinates": coordinates,
                "problems": problems,
                "resolution": resolution,
                "risk": risk,
                "tool": tool,
            }
    
    ignored: MetaOapg.properties.ignored
    updated_at: MetaOapg.properties.updated_at
    created_at: MetaOapg.properties.created_at
    title: MetaOapg.properties.title
    type: 'TypeDef'
    key: MetaOapg.properties.key
    effective_severity_level: MetaOapg.properties.effective_severity_level
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["effective_severity_level"]) -> MetaOapg.properties.effective_severity_level: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ignored"]) -> MetaOapg.properties.ignored: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["key"]) -> MetaOapg.properties.key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> 'TypeDef': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["classes"]) -> MetaOapg.properties.classes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["coordinates"]) -> MetaOapg.properties.coordinates: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["problems"]) -> MetaOapg.properties.problems: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resolution"]) -> 'Resolution': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["risk"]) -> 'Risk': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tool"]) -> MetaOapg.properties.tool: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "created_at", "effective_severity_level", "ignored", "key", "status", "type", "updated_at", "description", "classes", "coordinates", "problems", "resolution", "risk", "tool", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["effective_severity_level"]) -> MetaOapg.properties.effective_severity_level: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ignored"]) -> MetaOapg.properties.ignored: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["key"]) -> MetaOapg.properties.key: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> 'TypeDef': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["classes"]) -> typing.Union[MetaOapg.properties.classes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["coordinates"]) -> typing.Union[MetaOapg.properties.coordinates, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["problems"]) -> typing.Union[MetaOapg.properties.problems, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resolution"]) -> typing.Union['Resolution', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["risk"]) -> typing.Union['Risk', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tool"]) -> typing.Union[MetaOapg.properties.tool, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "created_at", "effective_severity_level", "ignored", "key", "status", "type", "updated_at", "description", "classes", "coordinates", "problems", "resolution", "risk", "tool", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        ignored: typing.Union[MetaOapg.properties.ignored, bool, ],
        updated_at: typing.Union[MetaOapg.properties.updated_at, str, datetime, ],
        created_at: typing.Union[MetaOapg.properties.created_at, str, datetime, ],
        title: typing.Union[MetaOapg.properties.title, str, ],
        type: 'TypeDef',
        key: typing.Union[MetaOapg.properties.key, str, ],
        effective_severity_level: typing.Union[MetaOapg.properties.effective_severity_level, str, ],
        status: typing.Union[MetaOapg.properties.status, str, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        classes: typing.Union[MetaOapg.properties.classes, list, tuple, schemas.Unset] = schemas.unset,
        coordinates: typing.Union[MetaOapg.properties.coordinates, list, tuple, schemas.Unset] = schemas.unset,
        problems: typing.Union[MetaOapg.properties.problems, list, tuple, schemas.Unset] = schemas.unset,
        resolution: typing.Union['Resolution', schemas.Unset] = schemas.unset,
        risk: typing.Union['Risk', schemas.Unset] = schemas.unset,
        tool: typing.Union[MetaOapg.properties.tool, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'IssueAttributes':
        return super().__new__(
            cls,
            *args,
            ignored=ignored,
            updated_at=updated_at,
            created_at=created_at,
            title=title,
            type=type,
            key=key,
            effective_severity_level=effective_severity_level,
            status=status,
            description=description,
            classes=classes,
            coordinates=coordinates,
            problems=problems,
            resolution=resolution,
            risk=risk,
            tool=tool,
            _configuration=_configuration,
            **kwargs,
        )

from snyk_python_sdk.model.coordinate import Coordinate
from snyk_python_sdk.model.model_class import ModelClass
from snyk_python_sdk.model.problem import Problem
from snyk_python_sdk.model.resolution import Resolution
from snyk_python_sdk.model.risk import Risk
from snyk_python_sdk.model.type_def import TypeDef
