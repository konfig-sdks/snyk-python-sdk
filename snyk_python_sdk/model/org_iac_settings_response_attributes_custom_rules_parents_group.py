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


class OrgIacSettingsResponseAttributesCustomRulesParentsGroup(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The Infrastructure as Code settings at the group level.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def custom_rules() -> typing.Type['OrgIacSettingsResponseAttributesCustomRulesParentsGroupCustomRules']:
                return OrgIacSettingsResponseAttributesCustomRulesParentsGroupCustomRules
            updated = schemas.DateTimeSchema
            __annotations__ = {
                "custom_rules": custom_rules,
                "updated": updated,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom_rules"]) -> 'OrgIacSettingsResponseAttributesCustomRulesParentsGroupCustomRules': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated"]) -> MetaOapg.properties.updated: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["custom_rules", "updated", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom_rules"]) -> typing.Union['OrgIacSettingsResponseAttributesCustomRulesParentsGroupCustomRules', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated"]) -> typing.Union[MetaOapg.properties.updated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["custom_rules", "updated", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        custom_rules: typing.Union['OrgIacSettingsResponseAttributesCustomRulesParentsGroupCustomRules', schemas.Unset] = schemas.unset,
        updated: typing.Union[MetaOapg.properties.updated, str, datetime, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OrgIacSettingsResponseAttributesCustomRulesParentsGroup':
        return super().__new__(
            cls,
            *args,
            custom_rules=custom_rules,
            updated=updated,
            _configuration=_configuration,
            **kwargs,
        )

from snyk_python_sdk.model.org_iac_settings_response_attributes_custom_rules_parents_group_custom_rules import OrgIacSettingsResponseAttributesCustomRulesParentsGroupCustomRules