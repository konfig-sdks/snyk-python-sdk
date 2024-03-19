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


class ServiceAccountsUpdateGroupNameByIdResponseDataAttributes(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "auth_type",
            "role_id",
            "name",
        }
        
        class properties:
            
            
            class auth_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "api_key": "API_KEY",
                        "oauth_client_secret": "OAUTH_CLIENT_SECRET",
                        "oauth_private_key_jwt": "OAUTH_PRIVATE_KEY_JWT",
                    }
                
                @schemas.classproperty
                def API_KEY(cls):
                    return cls("api_key")
                
                @schemas.classproperty
                def OAUTH_CLIENT_SECRET(cls):
                    return cls("oauth_client_secret")
                
                @schemas.classproperty
                def OAUTH_PRIVATE_KEY_JWT(cls):
                    return cls("oauth_private_key_jwt")
            name = schemas.StrSchema
            role_id = schemas.UUIDSchema
            access_token_ttl_seconds = schemas.NumberSchema
            api_key = schemas.StrSchema
            client_id = schemas.StrSchema
            client_secret = schemas.StrSchema
            jwks_url = schemas.StrSchema
            
            
            class level(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "Group": "GROUP",
                        "Org": "ORG",
                    }
                
                @schemas.classproperty
                def GROUP(cls):
                    return cls("Group")
                
                @schemas.classproperty
                def ORG(cls):
                    return cls("Org")
            __annotations__ = {
                "auth_type": auth_type,
                "name": name,
                "role_id": role_id,
                "access_token_ttl_seconds": access_token_ttl_seconds,
                "api_key": api_key,
                "client_id": client_id,
                "client_secret": client_secret,
                "jwks_url": jwks_url,
                "level": level,
            }
    
    auth_type: MetaOapg.properties.auth_type
    role_id: MetaOapg.properties.role_id
    name: MetaOapg.properties.name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["auth_type"]) -> MetaOapg.properties.auth_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["role_id"]) -> MetaOapg.properties.role_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["access_token_ttl_seconds"]) -> MetaOapg.properties.access_token_ttl_seconds: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["api_key"]) -> MetaOapg.properties.api_key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client_id"]) -> MetaOapg.properties.client_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client_secret"]) -> MetaOapg.properties.client_secret: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["jwks_url"]) -> MetaOapg.properties.jwks_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["level"]) -> MetaOapg.properties.level: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["auth_type", "name", "role_id", "access_token_ttl_seconds", "api_key", "client_id", "client_secret", "jwks_url", "level", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["auth_type"]) -> MetaOapg.properties.auth_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["role_id"]) -> MetaOapg.properties.role_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["access_token_ttl_seconds"]) -> typing.Union[MetaOapg.properties.access_token_ttl_seconds, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["api_key"]) -> typing.Union[MetaOapg.properties.api_key, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client_id"]) -> typing.Union[MetaOapg.properties.client_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client_secret"]) -> typing.Union[MetaOapg.properties.client_secret, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["jwks_url"]) -> typing.Union[MetaOapg.properties.jwks_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["level"]) -> typing.Union[MetaOapg.properties.level, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["auth_type", "name", "role_id", "access_token_ttl_seconds", "api_key", "client_id", "client_secret", "jwks_url", "level", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        auth_type: typing.Union[MetaOapg.properties.auth_type, str, ],
        role_id: typing.Union[MetaOapg.properties.role_id, str, uuid.UUID, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        access_token_ttl_seconds: typing.Union[MetaOapg.properties.access_token_ttl_seconds, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        api_key: typing.Union[MetaOapg.properties.api_key, str, schemas.Unset] = schemas.unset,
        client_id: typing.Union[MetaOapg.properties.client_id, str, schemas.Unset] = schemas.unset,
        client_secret: typing.Union[MetaOapg.properties.client_secret, str, schemas.Unset] = schemas.unset,
        jwks_url: typing.Union[MetaOapg.properties.jwks_url, str, schemas.Unset] = schemas.unset,
        level: typing.Union[MetaOapg.properties.level, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ServiceAccountsUpdateGroupNameByIdResponseDataAttributes':
        return super().__new__(
            cls,
            *args,
            auth_type=auth_type,
            role_id=role_id,
            name=name,
            access_token_ttl_seconds=access_token_ttl_seconds,
            api_key=api_key,
            client_id=client_id,
            client_secret=client_secret,
            jwks_url=jwks_url,
            level=level,
            _configuration=_configuration,
            **kwargs,
        )
