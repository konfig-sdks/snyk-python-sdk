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


class RequiredServiceAccountsCreateGroupRequestDataAttributes(TypedDict):
    # Authentication strategy for the service account:   * api_key - Regular Snyk API Key.   * oauth_client_secret - OAuth2 client_credentials grant, which returns a client secret that can be used to retrieve an access token.   * oauth_private_key_jwt - OAuth2 client_credentials grant, using private_key_jwt client_assertion as laid out in OIDC Connect Core 1.0, section 9.
    auth_type: str

    # A human-friendly name for the service account.
    name: str

    # The ID of the role which the created service account should use.
    role_id: str

class OptionalServiceAccountsCreateGroupRequestDataAttributes(TypedDict, total=False):
    # The time, in seconds, that a generated access token will be valid for. Defaults to 1 hour if unset. Only used when auth_type is one of the oauth_* variants.
    access_token_ttl_seconds: typing.Union[int, float]

    # A JWKs URL hosting your public keys, used to verify signed JWT requests. Must be https. Required only when auth_type is oauth_private_key_jwt.
    jwks_url: str

class ServiceAccountsCreateGroupRequestDataAttributes(RequiredServiceAccountsCreateGroupRequestDataAttributes, OptionalServiceAccountsCreateGroupRequestDataAttributes):
    pass