# coding: utf-8

"""
    Snyk API

    Missing description placeholder

    The version of the OpenAPI document: REST
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel


class ServiceAccountsManageClientSecretResponseDataAttributes(BaseModel):
    # The authentication strategy for the service account:   * api_key - Regular Snyk API Key.   * oauth_client_secret - OAuth2 client_credentials grant, which returns a client secret that can be used to retrieve an access token.   * oauth_private_key_jwt - OAuth2 client_credentials grant, using private_key_jwt client_assertion as laid out OIDC Connect Core 1.0, section 9.
    auth_type: Literal["api_key", "oauth_client_secret", "oauth_private_key_jwt"] = Field(alias='auth_type')

    # A human-friendly name of the service account.
    name: str = Field(alias='name')

    # The ID of the role which the Service Account is associated with.
    role_id: str = Field(alias='role_id')

    # The time, in seconds, that a generated access token will be valid for. Defaults to 1hr if unset. Only provided when auth_type is oauth_private_key_jwt.
    access_token_ttl_seconds: typing.Optional[typing.Union[int, float]] = Field(None, alias='access_token_ttl_seconds')

    # The Snyk API Key for this service account. Only returned on creation, and only when auth_type is api_key.
    api_key: typing.Optional[str] = Field(None, alias='api_key')

    # The service account's attached client-id. Used to request an access-token. Only provided when auth_type is oauth_private_key_jwt.
    client_id: typing.Optional[str] = Field(None, alias='client_id')

    # The client secret used for obtaining access tokens. Only sent on creation of new service accounts and cannot be retrieved thereafter. Only provided when auth_type is oauth_client_secret.
    client_secret: typing.Optional[str] = Field(None, alias='client_secret')

    # A JWKs URL used to verify signed JWT requests against. Must be https. Only provided when auth_type is oauth_private_key_jwt.
    jwks_url: typing.Optional[str] = Field(None, alias='jwks_url')

    # The level of access for the service account:   * Group - the service account was created at the Group level.   * Org - the service account was created at the Org level.
    level: typing.Optional[Literal["Group", "Org"]] = Field(None, alias='level')
    class Config:
        arbitrary_types_allowed = True
