# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CloningInfo(Model):
    """Information needed for cloning operation.

    All required parameters must be populated in order to send to Azure.

    :param correlation_id: Correlation ID of cloning operation. This ID ties
     multiple cloning operations
     together to use the same snapshot.
    :type correlation_id: str
    :param overwrite: <code>true</code> to overwrite destination app;
     otherwise, <code>false</code>.
    :type overwrite: bool
    :param clone_custom_host_names: <code>true</code> to clone custom
     hostnames from source app; otherwise, <code>false</code>.
    :type clone_custom_host_names: bool
    :param clone_source_control: <code>true</code> to clone source control
     from source app; otherwise, <code>false</code>.
    :type clone_source_control: bool
    :param source_web_app_id: Required. ARM resource ID of the source app. App
     resource ID is of the form
     /subscriptions/{subId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}
     for production slots and
     /subscriptions/{subId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/slots/{slotName}
     for other slots.
    :type source_web_app_id: str
    :param source_web_app_location: Location of source app ex: West US or
     North Europe
    :type source_web_app_location: str
    :param hosting_environment: App Service Environment.
    :type hosting_environment: str
    :param app_settings_overrides: Application setting overrides for cloned
     app. If specified, these settings override the settings cloned
     from source app. Otherwise, application settings from source app are
     retained.
    :type app_settings_overrides: dict[str, str]
    :param configure_load_balancing: <code>true</code> to configure load
     balancing for source and destination app.
    :type configure_load_balancing: bool
    :param traffic_manager_profile_id: ARM resource ID of the Traffic Manager
     profile to use, if it exists. Traffic Manager resource ID is of the form
     /subscriptions/{subId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/trafficManagerProfiles/{profileName}.
    :type traffic_manager_profile_id: str
    :param traffic_manager_profile_name: Name of Traffic Manager profile to
     create. This is only needed if Traffic Manager profile does not already
     exist.
    :type traffic_manager_profile_name: str
    """

    _validation = {
        'source_web_app_id': {'required': True},
    }

    _attribute_map = {
        'correlation_id': {'key': 'correlationId', 'type': 'str'},
        'overwrite': {'key': 'overwrite', 'type': 'bool'},
        'clone_custom_host_names': {'key': 'cloneCustomHostNames', 'type': 'bool'},
        'clone_source_control': {'key': 'cloneSourceControl', 'type': 'bool'},
        'source_web_app_id': {'key': 'sourceWebAppId', 'type': 'str'},
        'source_web_app_location': {'key': 'sourceWebAppLocation', 'type': 'str'},
        'hosting_environment': {'key': 'hostingEnvironment', 'type': 'str'},
        'app_settings_overrides': {'key': 'appSettingsOverrides', 'type': '{str}'},
        'configure_load_balancing': {'key': 'configureLoadBalancing', 'type': 'bool'},
        'traffic_manager_profile_id': {'key': 'trafficManagerProfileId', 'type': 'str'},
        'traffic_manager_profile_name': {'key': 'trafficManagerProfileName', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(CloningInfo, self).__init__(**kwargs)
        self.correlation_id = kwargs.get('correlation_id', None)
        self.overwrite = kwargs.get('overwrite', None)
        self.clone_custom_host_names = kwargs.get('clone_custom_host_names', None)
        self.clone_source_control = kwargs.get('clone_source_control', None)
        self.source_web_app_id = kwargs.get('source_web_app_id', None)
        self.source_web_app_location = kwargs.get('source_web_app_location', None)
        self.hosting_environment = kwargs.get('hosting_environment', None)
        self.app_settings_overrides = kwargs.get('app_settings_overrides', None)
        self.configure_load_balancing = kwargs.get('configure_load_balancing', None)
        self.traffic_manager_profile_id = kwargs.get('traffic_manager_profile_id', None)
        self.traffic_manager_profile_name = kwargs.get('traffic_manager_profile_name', None)