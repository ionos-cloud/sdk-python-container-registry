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


class RepositoryMetadata(object):
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

        'created_date': 'datetime',

        'created_by': 'str',

        'created_by_user_id': 'str',

        'last_modified_date': 'datetime',

        'last_modified_by': 'str',

        'last_modified_by_user_id': 'str',

        'resource_urn': 'str',

        'artifact_count': 'int',

        'pull_count': 'int',

        'push_count': 'int',

        'last_pulled_at': 'datetime',

        'last_pushed_at': 'datetime',

        'last_severity': 'str',
    }

    attribute_map = {

        'created_date': 'createdDate',

        'created_by': 'createdBy',

        'created_by_user_id': 'createdByUserId',

        'last_modified_date': 'lastModifiedDate',

        'last_modified_by': 'lastModifiedBy',

        'last_modified_by_user_id': 'lastModifiedByUserId',

        'resource_urn': 'resourceURN',

        'artifact_count': 'artifactCount',

        'pull_count': 'pullCount',

        'push_count': 'pushCount',

        'last_pulled_at': 'lastPulledAt',

        'last_pushed_at': 'lastPushedAt',

        'last_severity': 'lastSeverity',
    }

    def __init__(self, created_date=None, created_by=None, created_by_user_id=None, last_modified_date=None, last_modified_by=None, last_modified_by_user_id=None, resource_urn=None, artifact_count=None, pull_count=None, push_count=None, last_pulled_at=None, last_pushed_at=None, last_severity=None, local_vars_configuration=None):  # noqa: E501
        """RepositoryMetadata - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._created_date = None
        self._created_by = None
        self._created_by_user_id = None
        self._last_modified_date = None
        self._last_modified_by = None
        self._last_modified_by_user_id = None
        self._resource_urn = None
        self._artifact_count = None
        self._pull_count = None
        self._push_count = None
        self._last_pulled_at = None
        self._last_pushed_at = None
        self._last_severity = None
        self.discriminator = None

        if created_date is not None:
            self.created_date = created_date
        if created_by is not None:
            self.created_by = created_by
        if created_by_user_id is not None:
            self.created_by_user_id = created_by_user_id
        if last_modified_date is not None:
            self.last_modified_date = last_modified_date
        if last_modified_by is not None:
            self.last_modified_by = last_modified_by
        if last_modified_by_user_id is not None:
            self.last_modified_by_user_id = last_modified_by_user_id
        if resource_urn is not None:
            self.resource_urn = resource_urn
        self.artifact_count = artifact_count
        self.pull_count = pull_count
        self.push_count = push_count
        if last_pulled_at is not None:
            self.last_pulled_at = last_pulled_at
        if last_pushed_at is not None:
            self.last_pushed_at = last_pushed_at
        if last_severity is not None:
            self.last_severity = last_severity


    @property
    def created_date(self):
        """Gets the created_date of this RepositoryMetadata.  # noqa: E501

        The ISO 8601 creation timestamp.  # noqa: E501

        :return: The created_date of this RepositoryMetadata.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this RepositoryMetadata.

        The ISO 8601 creation timestamp.  # noqa: E501

        :param created_date: The created_date of this RepositoryMetadata.  # noqa: E501
        :type created_date: datetime
        """

        self._created_date = created_date

    @property
    def created_by(self):
        """Gets the created_by of this RepositoryMetadata.  # noqa: E501

        Unique name of the identity that created the resource.  # noqa: E501

        :return: The created_by of this RepositoryMetadata.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this RepositoryMetadata.

        Unique name of the identity that created the resource.  # noqa: E501

        :param created_by: The created_by of this RepositoryMetadata.  # noqa: E501
        :type created_by: str
        """

        self._created_by = created_by

    @property
    def created_by_user_id(self):
        """Gets the created_by_user_id of this RepositoryMetadata.  # noqa: E501


        :return: The created_by_user_id of this RepositoryMetadata.  # noqa: E501
        :rtype: str
        """
        return self._created_by_user_id

    @created_by_user_id.setter
    def created_by_user_id(self, created_by_user_id):
        """Sets the created_by_user_id of this RepositoryMetadata.


        :param created_by_user_id: The created_by_user_id of this RepositoryMetadata.  # noqa: E501
        :type created_by_user_id: str
        """

        self._created_by_user_id = created_by_user_id

    @property
    def last_modified_date(self):
        """Gets the last_modified_date of this RepositoryMetadata.  # noqa: E501

        The ISO 8601 modified timestamp.  # noqa: E501

        :return: The last_modified_date of this RepositoryMetadata.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_date

    @last_modified_date.setter
    def last_modified_date(self, last_modified_date):
        """Sets the last_modified_date of this RepositoryMetadata.

        The ISO 8601 modified timestamp.  # noqa: E501

        :param last_modified_date: The last_modified_date of this RepositoryMetadata.  # noqa: E501
        :type last_modified_date: datetime
        """

        self._last_modified_date = last_modified_date

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this RepositoryMetadata.  # noqa: E501

        Unique name of the identity that last modified the resource.  # noqa: E501

        :return: The last_modified_by of this RepositoryMetadata.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this RepositoryMetadata.

        Unique name of the identity that last modified the resource.  # noqa: E501

        :param last_modified_by: The last_modified_by of this RepositoryMetadata.  # noqa: E501
        :type last_modified_by: str
        """

        self._last_modified_by = last_modified_by

    @property
    def last_modified_by_user_id(self):
        """Gets the last_modified_by_user_id of this RepositoryMetadata.  # noqa: E501


        :return: The last_modified_by_user_id of this RepositoryMetadata.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by_user_id

    @last_modified_by_user_id.setter
    def last_modified_by_user_id(self, last_modified_by_user_id):
        """Sets the last_modified_by_user_id of this RepositoryMetadata.


        :param last_modified_by_user_id: The last_modified_by_user_id of this RepositoryMetadata.  # noqa: E501
        :type last_modified_by_user_id: str
        """

        self._last_modified_by_user_id = last_modified_by_user_id

    @property
    def resource_urn(self):
        """Gets the resource_urn of this RepositoryMetadata.  # noqa: E501

        Unique name of the resource.  # noqa: E501

        :return: The resource_urn of this RepositoryMetadata.  # noqa: E501
        :rtype: str
        """
        return self._resource_urn

    @resource_urn.setter
    def resource_urn(self, resource_urn):
        """Sets the resource_urn of this RepositoryMetadata.

        Unique name of the resource.  # noqa: E501

        :param resource_urn: The resource_urn of this RepositoryMetadata.  # noqa: E501
        :type resource_urn: str
        """

        self._resource_urn = resource_urn

    @property
    def artifact_count(self):
        """Gets the artifact_count of this RepositoryMetadata.  # noqa: E501


        :return: The artifact_count of this RepositoryMetadata.  # noqa: E501
        :rtype: int
        """
        return self._artifact_count

    @artifact_count.setter
    def artifact_count(self, artifact_count):
        """Sets the artifact_count of this RepositoryMetadata.


        :param artifact_count: The artifact_count of this RepositoryMetadata.  # noqa: E501
        :type artifact_count: int
        """
        if self.local_vars_configuration.client_side_validation and artifact_count is None:  # noqa: E501
            raise ValueError("Invalid value for `artifact_count`, must not be `None`")  # noqa: E501

        self._artifact_count = artifact_count

    @property
    def pull_count(self):
        """Gets the pull_count of this RepositoryMetadata.  # noqa: E501


        :return: The pull_count of this RepositoryMetadata.  # noqa: E501
        :rtype: int
        """
        return self._pull_count

    @pull_count.setter
    def pull_count(self, pull_count):
        """Sets the pull_count of this RepositoryMetadata.


        :param pull_count: The pull_count of this RepositoryMetadata.  # noqa: E501
        :type pull_count: int
        """
        if self.local_vars_configuration.client_side_validation and pull_count is None:  # noqa: E501
            raise ValueError("Invalid value for `pull_count`, must not be `None`")  # noqa: E501

        self._pull_count = pull_count

    @property
    def push_count(self):
        """Gets the push_count of this RepositoryMetadata.  # noqa: E501


        :return: The push_count of this RepositoryMetadata.  # noqa: E501
        :rtype: int
        """
        return self._push_count

    @push_count.setter
    def push_count(self, push_count):
        """Sets the push_count of this RepositoryMetadata.


        :param push_count: The push_count of this RepositoryMetadata.  # noqa: E501
        :type push_count: int
        """
        if self.local_vars_configuration.client_side_validation and push_count is None:  # noqa: E501
            raise ValueError("Invalid value for `push_count`, must not be `None`")  # noqa: E501

        self._push_count = push_count

    @property
    def last_pulled_at(self):
        """Gets the last_pulled_at of this RepositoryMetadata.  # noqa: E501


        :return: The last_pulled_at of this RepositoryMetadata.  # noqa: E501
        :rtype: datetime
        """
        return self._last_pulled_at

    @last_pulled_at.setter
    def last_pulled_at(self, last_pulled_at):
        """Sets the last_pulled_at of this RepositoryMetadata.


        :param last_pulled_at: The last_pulled_at of this RepositoryMetadata.  # noqa: E501
        :type last_pulled_at: datetime
        """

        self._last_pulled_at = last_pulled_at

    @property
    def last_pushed_at(self):
        """Gets the last_pushed_at of this RepositoryMetadata.  # noqa: E501


        :return: The last_pushed_at of this RepositoryMetadata.  # noqa: E501
        :rtype: datetime
        """
        return self._last_pushed_at

    @last_pushed_at.setter
    def last_pushed_at(self, last_pushed_at):
        """Sets the last_pushed_at of this RepositoryMetadata.


        :param last_pushed_at: The last_pushed_at of this RepositoryMetadata.  # noqa: E501
        :type last_pushed_at: datetime
        """

        self._last_pushed_at = last_pushed_at

    @property
    def last_severity(self):
        """Gets the last_severity of this RepositoryMetadata.  # noqa: E501

        The CVSS vulnerability severity rating  # noqa: E501

        :return: The last_severity of this RepositoryMetadata.  # noqa: E501
        :rtype: str
        """
        return self._last_severity

    @last_severity.setter
    def last_severity(self, last_severity):
        """Sets the last_severity of this RepositoryMetadata.

        The CVSS vulnerability severity rating  # noqa: E501

        :param last_severity: The last_severity of this RepositoryMetadata.  # noqa: E501
        :type last_severity: str
        """

        self._last_severity = last_severity
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
        if not isinstance(other, RepositoryMetadata):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RepositoryMetadata):
            return True

        return self.to_dict() != other.to_dict()
