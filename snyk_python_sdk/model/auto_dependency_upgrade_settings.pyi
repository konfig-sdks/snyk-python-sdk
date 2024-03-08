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


class AutoDependencyUpgradeSettings(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Automatically create pull requests on recurring tests for dependencies as upgrades become available. If not specified, settings will be inherited from the Project's integration.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def ignored_dependencies() -> typing.Type['AutoDependencyUpgradeSettingsIgnoredDependencies']:
                return AutoDependencyUpgradeSettingsIgnoredDependencies
            is_enabled = schemas.BoolSchema
            is_inherited = schemas.BoolSchema
            is_major_upgrade_enabled = schemas.BoolSchema
            
            
            class limit(
                schemas.NumberSchema
            ):
                pass
            minimum_age = schemas.NumberSchema
            __annotations__ = {
                "ignored_dependencies": ignored_dependencies,
                "is_enabled": is_enabled,
                "is_inherited": is_inherited,
                "is_major_upgrade_enabled": is_major_upgrade_enabled,
                "limit": limit,
                "minimum_age": minimum_age,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ignored_dependencies"]) -> 'AutoDependencyUpgradeSettingsIgnoredDependencies': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_enabled"]) -> MetaOapg.properties.is_enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_inherited"]) -> MetaOapg.properties.is_inherited: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_major_upgrade_enabled"]) -> MetaOapg.properties.is_major_upgrade_enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["limit"]) -> MetaOapg.properties.limit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["minimum_age"]) -> MetaOapg.properties.minimum_age: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["ignored_dependencies", "is_enabled", "is_inherited", "is_major_upgrade_enabled", "limit", "minimum_age", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ignored_dependencies"]) -> typing.Union['AutoDependencyUpgradeSettingsIgnoredDependencies', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_enabled"]) -> typing.Union[MetaOapg.properties.is_enabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_inherited"]) -> typing.Union[MetaOapg.properties.is_inherited, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_major_upgrade_enabled"]) -> typing.Union[MetaOapg.properties.is_major_upgrade_enabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["limit"]) -> typing.Union[MetaOapg.properties.limit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["minimum_age"]) -> typing.Union[MetaOapg.properties.minimum_age, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["ignored_dependencies", "is_enabled", "is_inherited", "is_major_upgrade_enabled", "limit", "minimum_age", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        ignored_dependencies: typing.Union['AutoDependencyUpgradeSettingsIgnoredDependencies', schemas.Unset] = schemas.unset,
        is_enabled: typing.Union[MetaOapg.properties.is_enabled, bool, schemas.Unset] = schemas.unset,
        is_inherited: typing.Union[MetaOapg.properties.is_inherited, bool, schemas.Unset] = schemas.unset,
        is_major_upgrade_enabled: typing.Union[MetaOapg.properties.is_major_upgrade_enabled, bool, schemas.Unset] = schemas.unset,
        limit: typing.Union[MetaOapg.properties.limit, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        minimum_age: typing.Union[MetaOapg.properties.minimum_age, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AutoDependencyUpgradeSettings':
        return super().__new__(
            cls,
            *args,
            ignored_dependencies=ignored_dependencies,
            is_enabled=is_enabled,
            is_inherited=is_inherited,
            is_major_upgrade_enabled=is_major_upgrade_enabled,
            limit=limit,
            minimum_age=minimum_age,
            _configuration=_configuration,
            **kwargs,
        )

from snyk_python_sdk.model.auto_dependency_upgrade_settings_ignored_dependencies import AutoDependencyUpgradeSettingsIgnoredDependencies