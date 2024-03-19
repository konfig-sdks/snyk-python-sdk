# coding: utf-8

"""
    Snyk API

    Snyk helps software-driven businesses develop fast and stay secure. Continuously find and fix vulnerabilities for npm, Maven, NuGet, RubyGems, PyPI and more.

    The version of the OpenAPI document: REST
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel


class ServiceAccountsCreateForOrganizationRequestDataAttributes(BaseModel):
    # Authentication strategy for the service account:   * api_key - Regular Snyk API Key.   * oauth_client_secret - OAuth2 client_credentials grant, which returns a client secret that can be used to retrieve an access token.   * oauth_private_key_jwt - OAuth2 client_credentials grant, using private_key_jwt client_assertion as laid out in OIDC Connect Core 1.0, section 9.
    auth_type: Literal["api_key", "oauth_client_secret", "oauth_private_key_jwt"] = Field(alias='auth_type')

    # A human-friendly name for the service account.
    name: str = Field(alias='name')

    # The ID of the role which the created service account should use. Obtained in the Snyk UI, via \"Group Page\" -> \"Settings\" -> \"Member Roles\" -> \"Create new Role\". Can be shared among multiple accounts.
    role_id: str = Field(alias='role_id')

    # The time, in seconds, that a generated access token will be valid for. Defaults to 1 hour if unset. Only used when auth_type is one of the oauth_* variants.
    access_token_ttl_seconds: typing.Optional[typing.Union[int, float]] = Field(None, alias='access_token_ttl_seconds')

    # A JWKs URL hosting your public keys, used to verify signed JWT requests. Must be https. Required only when auth_type is oauth_private_key_jwt.
    jwks_url: typing.Optional[str] = Field(None, alias='jwks_url')
    class Config:
        arbitrary_types_allowed = True
