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


class RequiredServiceAccountAttributes(TypedDict):
    # The authentication strategy for the service account:   * api_key - Regular Snyk API Key.   * oauth_client_secret - OAuth2 client_credentials grant, which returns a client secret that can be used to retrieve an access token.   * oauth_private_key_jwt - OAuth2 client_credentials grant, using private_key_jwt client_assertion as laid out OIDC Connect Core 1.0, section 9.
    auth_type: str

    # A human-friendly name of the service account.
    name: str

    # The ID of the role which the Service Account is associated with.
    role_id: str

class OptionalServiceAccountAttributes(TypedDict, total=False):
    # The time, in seconds, that a generated access token will be valid for. Defaults to 1hr if unset. Only provided when auth_type is oauth_private_key_jwt.
    access_token_ttl_seconds: typing.Union[int, float]

    # The Snyk API Key for this service account. Only returned on creation, and only when auth_type is api_key.
    api_key: str

    # The service account's attached client-id. Used to request an access-token. Only provided when auth_type is oauth_private_key_jwt.
    client_id: str

    # The client secret used for obtaining access tokens. Only sent on creation of new service accounts and cannot be retrieved thereafter. Only provided when auth_type is oauth_client_secret.
    client_secret: str

    # A JWKs URL used to verify signed JWT requests against. Must be https. Only provided when auth_type is oauth_private_key_jwt.
    jwks_url: str

    # The level of access for the service account:   * Group - the service account was created at the Group level.   * Org - the service account was created at the Org level.
    level: str

class ServiceAccountAttributes(RequiredServiceAccountAttributes, OptionalServiceAccountAttributes):
    pass
