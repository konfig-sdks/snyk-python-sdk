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


class CoordinateRepresentations(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    A list of precise locations that surface an issue. A coordinate may have multiple representations.

    """


    class MetaOapg:
        
        
        class items(
            schemas.ComposedSchema,
        ):
        
        
            class MetaOapg:
                
                
                class one_of_0(
                    schemas.DictSchema
                ):
                
                
                    class MetaOapg:
                        required = {
                            "resourcePath",
                        }
                        
                        class properties:
                            
                            
                            class resourcePath(
                                schemas.StrSchema
                            ):
                                pass
                            __annotations__ = {
                                "resourcePath": resourcePath,
                            }
                    
                    resourcePath: MetaOapg.properties.resourcePath
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["resourcePath"]) -> MetaOapg.properties.resourcePath: ...
                    
                    @typing.overload
                    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                    
                    def __getitem__(self, name: typing.Union[typing_extensions.Literal["resourcePath", ], str]):
                        # dict_instance[name] accessor
                        return super().__getitem__(name)
                    
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["resourcePath"]) -> MetaOapg.properties.resourcePath: ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                    
                    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["resourcePath", ], str]):
                        return super().get_item_oapg(name)
                    
                
                    def __new__(
                        cls,
                        *args: typing.Union[dict, frozendict.frozendict, ],
                        resourcePath: typing.Union[MetaOapg.properties.resourcePath, str, ],
                        _configuration: typing.Optional[schemas.Configuration] = None,
                        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                    ) -> 'one_of_0':
                        return super().__new__(
                            cls,
                            *args,
                            resourcePath=resourcePath,
                            _configuration=_configuration,
                            **kwargs,
                        )
                
                
                class one_of_1(
                    schemas.DictSchema
                ):
                
                
                    class MetaOapg:
                        required = {
                            "dependency",
                        }
                        
                        class properties:
                        
                            @staticmethod
                            def dependency() -> typing.Type['Dependency']:
                                return Dependency
                            __annotations__ = {
                                "dependency": dependency,
                            }
                    
                    dependency: 'Dependency'
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["dependency"]) -> 'Dependency': ...
                    
                    @typing.overload
                    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                    
                    def __getitem__(self, name: typing.Union[typing_extensions.Literal["dependency", ], str]):
                        # dict_instance[name] accessor
                        return super().__getitem__(name)
                    
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["dependency"]) -> 'Dependency': ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                    
                    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["dependency", ], str]):
                        return super().get_item_oapg(name)
                    
                
                    def __new__(
                        cls,
                        *args: typing.Union[dict, frozendict.frozendict, ],
                        dependency: 'Dependency',
                        _configuration: typing.Optional[schemas.Configuration] = None,
                        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                    ) -> 'one_of_1':
                        return super().__new__(
                            cls,
                            *args,
                            dependency=dependency,
                            _configuration=_configuration,
                            **kwargs,
                        )
                
                
                class one_of_2(
                    schemas.DictSchema
                ):
                
                
                    class MetaOapg:
                        required = {
                            "cloud_resource",
                        }
                        
                        class properties:
                        
                            @staticmethod
                            def cloud_resource() -> typing.Type['CloudResource']:
                                return CloudResource
                            __annotations__ = {
                                "cloud_resource": cloud_resource,
                            }
                    
                    cloud_resource: 'CloudResource'
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["cloud_resource"]) -> 'CloudResource': ...
                    
                    @typing.overload
                    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                    
                    def __getitem__(self, name: typing.Union[typing_extensions.Literal["cloud_resource", ], str]):
                        # dict_instance[name] accessor
                        return super().__getitem__(name)
                    
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["cloud_resource"]) -> 'CloudResource': ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                    
                    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["cloud_resource", ], str]):
                        return super().get_item_oapg(name)
                    
                
                    def __new__(
                        cls,
                        *args: typing.Union[dict, frozendict.frozendict, ],
                        cloud_resource: 'CloudResource',
                        _configuration: typing.Optional[schemas.Configuration] = None,
                        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                    ) -> 'one_of_2':
                        return super().__new__(
                            cls,
                            *args,
                            cloud_resource=cloud_resource,
                            _configuration=_configuration,
                            **kwargs,
                        )
                
                
                class one_of_3(
                    schemas.DictSchema
                ):
                
                
                    class MetaOapg:
                        required = {
                            "sourceLocation",
                        }
                        
                        class properties:
                        
                            @staticmethod
                            def sourceLocation() -> typing.Type['SourceLocation']:
                                return SourceLocation
                            __annotations__ = {
                                "sourceLocation": sourceLocation,
                            }
                    
                    sourceLocation: 'SourceLocation'
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["sourceLocation"]) -> 'SourceLocation': ...
                    
                    @typing.overload
                    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                    
                    def __getitem__(self, name: typing.Union[typing_extensions.Literal["sourceLocation", ], str]):
                        # dict_instance[name] accessor
                        return super().__getitem__(name)
                    
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["sourceLocation"]) -> 'SourceLocation': ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                    
                    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["sourceLocation", ], str]):
                        return super().get_item_oapg(name)
                    
                
                    def __new__(
                        cls,
                        *args: typing.Union[dict, frozendict.frozendict, ],
                        sourceLocation: 'SourceLocation',
                        _configuration: typing.Optional[schemas.Configuration] = None,
                        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                    ) -> 'one_of_3':
                        return super().__new__(
                            cls,
                            *args,
                            sourceLocation=sourceLocation,
                            _configuration=_configuration,
                            **kwargs,
                        )
                
                @classmethod
                @functools.lru_cache()
                def one_of(cls):
                    # we need this here to make our import statements work
                    # we must store _composed_schemas in here so the code is only run
                    # when we invoke this method. If we kept this at the class
                    # level we would get an error because the class level
                    # code would be run when this module is imported, and these composed
                    # classes don't exist yet because their module has not finished
                    # loading
                    return [
                        cls.one_of_0,
                        cls.one_of_1,
                        cls.one_of_2,
                        cls.one_of_3,
                    ]
        
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'items':
                return super().__new__(
                    cls,
                    *args,
                    _configuration=_configuration,
                    **kwargs,
                )

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'CoordinateRepresentations':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)

from snyk_python_sdk.model.cloud_resource import CloudResource
from snyk_python_sdk.model.dependency import Dependency
from snyk_python_sdk.model.source_location import SourceLocation
