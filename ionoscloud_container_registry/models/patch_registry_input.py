# coding: utf-8

"""
    Container Registry service

    ## Overview Container Registry service enables IONOS clients to manage docker and OCI compliant registries for use by their managed Kubernetes clusters. Use a Container Registry to ensure you have a privately accessed registry to efficiently support image pulls. ## Changelog ### 1.1.0  - Added new endpoints for Repositories  - Added new endpoints for Artifacts  - Added new endpoints for Vulnerabilities  - Added registry vulnerabilityScanning feature   # noqa: E501

    The version of the OpenAPI document: 1.1.0
    Contact: support@cloud.ionos.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ionoscloud_container_registry.configuration import Configuration


class PatchRegistryInput(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {

        'garbage_collection_schedule': 'WeeklySchedule',

        'features': 'RegistryFeatures',
    }

    attribute_map = {

        'garbage_collection_schedule': 'garbageCollectionSchedule',

        'features': 'features',
    }

    def __init__(self, garbage_collection_schedule=None, features=None, local_vars_configuration=None):  # noqa: E501
        """PatchRegistryInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._garbage_collection_schedule = None
        self._features = None
        self.discriminator = None

        self.garbage_collection_schedule = garbage_collection_schedule
        if features is not None:
            self.features = features


    @property
    def garbage_collection_schedule(self):
        """Gets the garbage_collection_schedule of this PatchRegistryInput.  # noqa: E501


        :return: The garbage_collection_schedule of this PatchRegistryInput.  # noqa: E501
        :rtype: WeeklySchedule
        """
        return self._garbage_collection_schedule

    @garbage_collection_schedule.setter
    def garbage_collection_schedule(self, garbage_collection_schedule):
        """Sets the garbage_collection_schedule of this PatchRegistryInput.


        :param garbage_collection_schedule: The garbage_collection_schedule of this PatchRegistryInput.  # noqa: E501
        :type garbage_collection_schedule: WeeklySchedule
        """

        self._garbage_collection_schedule = garbage_collection_schedule

    @property
    def features(self):
        """Gets the features of this PatchRegistryInput.  # noqa: E501


        :return: The features of this PatchRegistryInput.  # noqa: E501
        :rtype: RegistryFeatures
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this PatchRegistryInput.


        :param features: The features of this PatchRegistryInput.  # noqa: E501
        :type features: RegistryFeatures
        """

        self._features = features
    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PatchRegistryInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PatchRegistryInput):
            return True

        return self.to_dict() != other.to_dict()
