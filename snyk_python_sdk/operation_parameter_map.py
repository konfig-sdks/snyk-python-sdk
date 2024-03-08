operation_parameter_map = {
    '/orgs/{org_id}/apps/installs/{install_id}-DELETE': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'org_id'
            },
            {
                'name': 'install_id'
            },
        ]
    },
    '/groups/{group_id}/apps/installs/{install_id}/secrets-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'version'
            },
            {
                'name': 'group_id'
            },
            {
                'name': 'install_id'
            },
        ]
    },
    '/orgs/{org_id}/apps/creations-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'version'
            },
            {
                'name': 'org_id'
            },
        ]
    },
    '/orgs/{org_id}/apps-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'version'
            },
            {
                'name': 'org_id'
            },
        ]
    },
    '/orgs/{org_id}/apps/{client_id}-DELETE': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'org_id'
            },
            {
                'name': 'client_id'
            },
        ]
    },
    '/orgs/{org_id}/apps/creations/{app_id}-DELETE': {
        'parameters': [
            {
                'name': 'org_id'
            },
            {
                'name': 'app_id'
            },
            {
                'name': 'version'
            },
        ]
    },
    '/self/apps/{app_id}/sessions-GET': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'app_id'
            },
            {
                'name': 'starting_after'
            },
            {
                'name': 'ending_before'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/orgs/{org_id}/apps/creations/{app_id}-GET': {
        'parameters': [
            {
                'name': 'org_id'
            },
            {
                'name': 'app_id'
            },
            {
                'name': 'version'
            },
        ]
    },
    '/orgs/{org_id}/apps/{client_id}-GET': {
        'parameters': [
            {
                'name': 'org_id'
            },
            {
                'name': 'client_id'
            },
            {
                'name': 'version'
            },
        ]
    },
    '/groups/{group_id}/apps/installs-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'relationships'
            },
            {
                'name': 'version'
            },
            {
                'name': 'group_id'
            },
        ]
    },
    '/orgs/{org_id}/apps/installs-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'relationships'
            },
            {
                'name': 'version'
            },
            {
                'name': 'org_id'
            },
        ]
    },
    '/orgs/{org_id}/app_bots-GET': {
        'parameters': [
            {
                'name': 'org_id'
            },
            {
                'name': 'version'
            },
            {
                'name': 'expand'
            },
            {
                'name': 'starting_after'
            },
            {
                'name': 'ending_before'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/self/apps-GET': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'starting_after'
            },
            {
                'name': 'ending_before'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/groups/{group_id}/apps/installs-GET': {
        'parameters': [
            {
                'name': 'group_id'
            },
            {
                'name': 'version'
            },
            {
                'name': 'expand'
            },
            {
                'name': 'starting_after'
            },
            {
                'name': 'ending_before'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/orgs/{org_id}/apps-GET': {
        'parameters': [
            {
                'name': 'org_id'
            },
            {
                'name': 'version'
            },
            {
                'name': 'starting_after'
            },
            {
                'name': 'ending_before'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/orgs/{org_id}/apps/creations-GET': {
        'parameters': [
            {
                'name': 'org_id'
            },
            {
                'name': 'version'
            },
            {
                'name': 'starting_after'
            },
            {
                'name': 'ending_before'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/orgs/{org_id}/apps/installs-GET': {
        'parameters': [
            {
                'name': 'org_id'
            },
            {
                'name': 'version'
            },
            {
                'name': 'expand'
            },
            {
                'name': 'starting_after'
            },
            {
                'name': 'ending_before'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/self/apps/installs-GET': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'expand'
            },
            {
                'name': 'starting_after'
            },
            {
                'name': 'ending_before'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/orgs/{org_id}/apps/creations/{app_id}/secrets-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'version'
            },
            {
                'name': 'org_id'
            },
            {
                'name': 'app_id'
            },
        ]
    },
    '/orgs/{org_id}/apps/installs/{install_id}/secrets-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'version'
            },
            {
                'name': 'org_id'
            },
            {
                'name': 'install_id'
            },
        ]
    },
    '/orgs/{org_id}/apps/{client_id}/secrets-POST': {
        'parameters': [
            {
                'name': 'mode'
            },
            {
                'name': 'version'
            },
            {
                'name': 'org_id'
            },
            {
                'name': 'client_id'
            },
            {
                'name': 'secret'
            },
        ]
    },
    '/self/apps/{app_id}-DELETE': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'app_id'
            },
        ]
    },
    '/orgs/{org_id}/app_bots/{bot_id}-DELETE': {
        'parameters': [
            {
                'name': 'bot_id'
            },
            {
                'name': 'version'
            },
            {
                'name': 'org_id'
            },
        ]
    },
    '/self/apps/installs/{install_id}-DELETE': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'install_id'
            },
        ]
    },
    '/groups/{group_id}/apps/installs/{install_id}-DELETE': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'group_id'
            },
            {
                'name': 'install_id'
            },
        ]
    },
    '/self/apps/{app_id}/sessions/{session_id}-DELETE': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'app_id'
            },
            {
                'name': 'session_id'
            },
        ]
    },
    '/orgs/{org_id}/apps/{client_id}-PATCH': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'version'
            },
            {
                'name': 'org_id'
            },
            {
                'name': 'client_id'
            },
        ]
    },
    '/orgs/{org_id}/apps/creations/{app_id}-PATCH': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'version'
            },
            {
                'name': 'org_id'
            },
            {
                'name': 'app_id'
            },
        ]
    },
    '/groups/{group_id}/audit_logs/search-GET': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'group_id'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
            {
                'name': 'size'
            },
            {
                'name': 'sort_order'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'project_id'
            },
            {
                'name': 'event'
            },
            {
                'name': 'exclude_event'
            },
        ]
    },
    '/orgs/{org_id}/audit_logs/search-GET': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'org_id'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
            {
                'name': 'size'
            },
            {
                'name': 'sort_order'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'project_id'
            },
            {
                'name': 'event'
            },
            {
                'name': 'exclude_event'
            },
        ]
    },
    '/orgs/{org_id}/collections/{collection_id}/relationships/projects-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'version'
            },
            {
                'name': 'org_id'
            },
            {
                'name': 'collection_id'
            },
        ]
    },
    '/orgs/{org_id}/collections-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'version'
            },
            {
                'name': 'org_id'
            },
        ]
    },
    '/orgs/{org_id}/collections/{collection_id}-PATCH': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'version'
            },
            {
                'name': 'org_id'
            },
            {
                'name': 'collection_id'
            },
        ]
    },
    '/orgs/{org_id}/collections/{collection_id}-GET': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'org_id'
            },
            {
                'name': 'collection_id'
            },
        ]
    },
    '/orgs/{org_id}/collections-GET': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'org_id'
            },
            {
                'name': 'starting_after'
            },
            {
                'name': 'ending_before'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'name'
            },
            {
                'name': 'is_generated'
            },
        ]
    },
    '/orgs/{org_id}/collections/{collection_id}/relationships/projects-GET': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'org_id'
            },
            {
                'name': 'collection_id'
            },
            {
                'name': 'starting_after'
            },
            {
                'name': 'ending_before'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'direction'
            },
            {
                'name': 'target_id'
            },
            {
                'name': 'show'
            },
            {
                'name': 'integration'
            },
        ]
    },
    '/orgs/{org_id}/collections/{collection_id}-DELETE': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'org_id'
            },
            {
                'name': 'collection_id'
            },
        ]
    },
    '/orgs/{org_id}/collections/{collection_id}/relationships/projects-DELETE': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'version'
            },
            {
                'name': 'org_id'
            },
            {
                'name': 'collection_id'
            },
        ]
    },
    '/orgs/{org_id}/container_images/{image_id}-GET': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'org_id'
            },
            {
                'name': 'image_id'
            },
        ]
    },
    '/orgs/{org_id}/container_images/{image_id}/relationships/image_target_refs-GET': {
        'parameters': [
            {
                'name': 'org_id'
            },
            {
                'name': 'image_id'
            },
            {
                'name': 'version'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'starting_after'
            },
            {
                'name': 'ending_before'
            },
        ]
    },
    '/orgs/{org_id}/container_images-GET': {
        'parameters': [
            {
                'name': 'org_id'
            },
            {
                'name': 'version'
            },
            {
                'name': 'image_ids'
            },
            {
                'name': 'platform'
            },
            {
                'name': 'names'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'starting_after'
            },
            {
                'name': 'ending_before'
            },
        ]
    },
    '/custom_base_images/{custombaseimage_id}-GET': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'custombaseimage_id'
            },
        ]
    },
    '/custom_base_images-GET': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'starting_after'
            },
            {
                'name': 'ending_before'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'project_id'
            },
            {
                'name': 'org_id'
            },
            {
                'name': 'group_id'
            },
            {
                'name': 'repository'
            },
            {
                'name': 'tag'
            },
            {
                'name': 'include_in_recommendations'
            },
            {
                'name': 'sort_by'
            },
            {
                'name': 'sort_direction'
            },
        ]
    },
    '/custom_base_images-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'version'
            },
        ]
    },
    '/custom_base_images/{custombaseimage_id}-DELETE': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'custombaseimage_id'
            },
        ]
    },
    '/custom_base_images/{custombaseimage_id}-PATCH': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'version'
            },
            {
                'name': 'custombaseimage_id'
            },
        ]
    },
    '/groups/{group_id}/settings/iac-GET': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'group_id'
            },
        ]
    },
    '/orgs/{org_id}/settings/iac-GET': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'org_id'
            },
        ]
    },
    '/groups/{group_id}/settings/iac-PATCH': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'group_id'
            },
            {
                'name': 'data'
            },
        ]
    },
    '/orgs/{org_id}/settings/iac-PATCH': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'org_id'
            },
            {
                'name': 'data'
            },
        ]
    },
    '/orgs/{org_id}/invites/{invite_id}-DELETE': {
        'parameters': [
            {
                'name': 'org_id'
            },
            {
                'name': 'invite_id'
            },
            {
                'name': 'version'
            },
        ]
    },
    '/orgs/{org_id}/invites-GET': {
        'parameters': [
            {
                'name': 'org_id'
            },
            {
                'name': 'version'
            },
            {
                'name': 'starting_after'
            },
            {
                'name': 'ending_before'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/orgs/{org_id}/invites-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'version'
            },
            {
                'name': 'org_id'
            },
        ]
    },
    '/groups/{group_id}/issues-GET': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'group_id'
            },
            {
                'name': 'starting_after'
            },
            {
                'name': 'ending_before'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'scan_item.id'
            },
            {
                'name': 'scan_item.type'
            },
            {
                'name': 'type'
            },
            {
                'name': 'updated_before'
            },
            {
                'name': 'updated_after'
            },
            {
                'name': 'created_before'
            },
            {
                'name': 'created_after'
            },
            {
                'name': 'effective_severity_level'
            },
            {
                'name': 'status'
            },
            {
                'name': 'ignored'
            },
        ]
    },
    '/orgs/{org_id}/issues/{issue_id}-GET': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'org_id'
            },
            {
                'name': 'issue_id'
            },
        ]
    },
    '/groups/{group_id}/issues/{issue_id}-GET': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'group_id'
            },
            {
                'name': 'issue_id'
            },
        ]
    },
    '/orgs/{org_id}/issues-GET': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'org_id'
            },
            {
                'name': 'starting_after'
            },
            {
                'name': 'ending_before'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'scan_item.id'
            },
            {
                'name': 'scan_item.type'
            },
            {
                'name': 'type'
            },
            {
                'name': 'updated_before'
            },
            {
                'name': 'updated_after'
            },
            {
                'name': 'created_before'
            },
            {
                'name': 'created_after'
            },
            {
                'name': 'effective_severity_level'
            },
            {
                'name': 'status'
            },
            {
                'name': 'ignored'
            },
        ]
    },
    '/orgs/{org_id}/packages/{purl}/issues-GET': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'purl'
            },
            {
                'name': 'org_id'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/orgs/{org_id}/packages/issues-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'version'
            },
            {
                'name': 'org_id'
            },
        ]
    },
    '/openapi/{version}-GET': {
        'parameters': [
            {
                'name': 'version'
            },
        ]
    },
    '/openapi-GET': {
        'parameters': [
        ]
    },
    '/orgs/{org_id}-GET': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'org_id'
            },
        ]
    },
    '/orgs-GET': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'starting_after'
            },
            {
                'name': 'ending_before'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'group_id'
            },
            {
                'name': 'is_personal'
            },
            {
                'name': 'slug'
            },
            {
                'name': 'name'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/groups/{group_id}/orgs-GET': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'group_id'
            },
            {
                'name': 'starting_after'
            },
            {
                'name': 'ending_before'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'name'
            },
            {
                'name': 'slug'
            },
        ]
    },
    '/orgs/{org_id}-PATCH': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'version'
            },
            {
                'name': 'org_id'
            },
        ]
    },
    '/orgs/{org_id}/projects/{project_id}-DELETE': {
        'parameters': [
            {
                'name': 'org_id'
            },
            {
                'name': 'project_id'
            },
            {
                'name': 'version'
            },
        ]
    },
    '/orgs/{org_id}/projects/{project_id}-GET': {
        'parameters': [
            {
                'name': 'org_id'
            },
            {
                'name': 'project_id'
            },
            {
                'name': 'version'
            },
            {
                'name': 'expand'
            },
            {
                'name': 'meta.latest_issue_counts'
            },
            {
                'name': 'meta.latest_dependency_total'
            },
        ]
    },
    '/orgs/{org_id}/projects-GET': {
        'parameters': [
            {
                'name': 'org_id'
            },
            {
                'name': 'version'
            },
            {
                'name': 'target_id'
            },
            {
                'name': 'target_reference'
            },
            {
                'name': 'target_file'
            },
            {
                'name': 'target_runtime'
            },
            {
                'name': 'meta_count'
            },
            {
                'name': 'ids'
            },
            {
                'name': 'names'
            },
            {
                'name': 'names_start_with'
            },
            {
                'name': 'origins'
            },
            {
                'name': 'types'
            },
            {
                'name': 'expand'
            },
            {
                'name': 'meta.latest_issue_counts'
            },
            {
                'name': 'meta.latest_dependency_total'
            },
            {
                'name': 'cli_monitored_before'
            },
            {
                'name': 'cli_monitored_after'
            },
            {
                'name': 'importing_user_public_id'
            },
            {
                'name': 'tags'
            },
            {
                'name': 'business_criticality'
            },
            {
                'name': 'environment'
            },
            {
                'name': 'lifecycle'
            },
            {
                'name': 'starting_after'
            },
            {
                'name': 'ending_before'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/orgs/{org_id}/projects/{project_id}-PATCH': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'version'
            },
            {
                'name': 'org_id'
            },
            {
                'name': 'project_id'
            },
            {
                'name': 'expand'
            },
        ]
    },
    '/orgs/{org_id}/projects/{project_id}/sbom-GET': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'org_id'
            },
            {
                'name': 'project_id'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/orgs/{org_id}/settings/sast-GET': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'org_id'
            },
        ]
    },
    '/orgs/{org_id}/settings/sast-PATCH': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'version'
            },
            {
                'name': 'org_id'
            },
        ]
    },
    '/orgs/{org_id}/service_accounts-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'org_id'
            },
            {
                'name': 'version'
            },
        ]
    },
    '/groups/{group_id}/service_accounts-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'group_id'
            },
            {
                'name': 'version'
            },
        ]
    },
    '/groups/{group_id}/service_accounts/{serviceaccount_id}-DELETE': {
        'parameters': [
            {
                'name': 'group_id'
            },
            {
                'name': 'serviceaccount_id'
            },
            {
                'name': 'version'
            },
        ]
    },
    '/orgs/{org_id}/service_accounts/{serviceaccount_id}-DELETE': {
        'parameters': [
            {
                'name': 'org_id'
            },
            {
                'name': 'serviceaccount_id'
            },
            {
                'name': 'version'
            },
        ]
    },
    '/groups/{group_id}/service_accounts/{serviceaccount_id}-GET': {
        'parameters': [
            {
                'name': 'group_id'
            },
            {
                'name': 'serviceaccount_id'
            },
            {
                'name': 'version'
            },
        ]
    },
    '/orgs/{org_id}/service_accounts/{serviceaccount_id}-GET': {
        'parameters': [
            {
                'name': 'org_id'
            },
            {
                'name': 'serviceaccount_id'
            },
            {
                'name': 'version'
            },
        ]
    },
    '/groups/{group_id}/service_accounts-GET': {
        'parameters': [
            {
                'name': 'group_id'
            },
            {
                'name': 'version'
            },
            {
                'name': 'starting_after'
            },
            {
                'name': 'ending_before'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/orgs/{org_id}/service_accounts-GET': {
        'parameters': [
            {
                'name': 'org_id'
            },
            {
                'name': 'version'
            },
            {
                'name': 'starting_after'
            },
            {
                'name': 'ending_before'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/groups/{group_id}/service_accounts/{serviceaccount_id}/secrets-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'group_id'
            },
            {
                'name': 'serviceaccount_id'
            },
            {
                'name': 'version'
            },
        ]
    },
    '/orgs/{org_id}/service_accounts/{serviceaccount_id}/secrets-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'org_id'
            },
            {
                'name': 'serviceaccount_id'
            },
            {
                'name': 'version'
            },
        ]
    },
    '/groups/{group_id}/service_accounts/{serviceaccount_id}-PATCH': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'group_id'
            },
            {
                'name': 'serviceaccount_id'
            },
            {
                'name': 'version'
            },
        ]
    },
    '/orgs/{org_id}/service_accounts/{serviceaccount_id}-PATCH': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'org_id'
            },
            {
                'name': 'serviceaccount_id'
            },
            {
                'name': 'version'
            },
        ]
    },
    '/orgs/{org_id}/slack_app/{tenant_id}/channels/{channel_id}-GET': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'org_id'
            },
            {
                'name': 'channel_id'
            },
            {
                'name': 'tenant_id'
            },
        ]
    },
    '/orgs/{org_id}/slack_app/{tenant_id}/channels-GET': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'org_id'
            },
            {
                'name': 'tenant_id'
            },
            {
                'name': 'starting_after'
            },
            {
                'name': 'ending_before'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/orgs/{org_id}/slack_app/{bot_id}-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'version'
            },
            {
                'name': 'org_id'
            },
            {
                'name': 'bot_id'
            },
        ]
    },
    '/orgs/{org_id}/slack_app/{bot_id}-GET': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'org_id'
            },
            {
                'name': 'bot_id'
            },
        ]
    },
    '/orgs/{org_id}/slack_app/{bot_id}/projects-GET': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'org_id'
            },
            {
                'name': 'bot_id'
            },
            {
                'name': 'starting_after'
            },
            {
                'name': 'ending_before'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/orgs/{org_id}/slack_app/{bot_id}/projects/{project_id}-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'version'
            },
            {
                'name': 'org_id'
            },
            {
                'name': 'project_id'
            },
            {
                'name': 'bot_id'
            },
        ]
    },
    '/orgs/{org_id}/slack_app/{bot_id}-DELETE': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'org_id'
            },
            {
                'name': 'bot_id'
            },
        ]
    },
    '/orgs/{org_id}/slack_app/{bot_id}/projects/{project_id}-DELETE': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'org_id'
            },
            {
                'name': 'project_id'
            },
            {
                'name': 'bot_id'
            },
        ]
    },
    '/orgs/{org_id}/slack_app/{bot_id}/projects/{project_id}-PATCH': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'org_id'
            },
            {
                'name': 'bot_id'
            },
            {
                'name': 'project_id'
            },
            {
                'name': 'data'
            },
        ]
    },
    '/orgs/{org_id}/targets/{target_id}-DELETE': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'org_id'
            },
            {
                'name': 'target_id'
            },
        ]
    },
    '/orgs/{org_id}/targets/{target_id}-GET': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'org_id'
            },
            {
                'name': 'target_id'
            },
        ]
    },
    '/orgs/{org_id}/targets-GET': {
        'parameters': [
            {
                'name': 'version'
            },
            {
                'name': 'org_id'
            },
            {
                'name': 'starting_after'
            },
            {
                'name': 'ending_before'
            },
            {
                'name': 'count'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'is_private'
            },
            {
                'name': 'exclude_empty'
            },
            {
                'name': 'url'
            },
            {
                'name': 'source_types'
            },
            {
                'name': 'display_name'
            },
            {
                'name': 'created_gte'
            },
        ]
    },
};