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


class PostTokenProperties(object):
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

        'expiry_date': 'datetime',

        'name': 'str',

        'scopes': 'list[Scope]',

        'status': 'str',
    }

    attribute_map = {

        'expiry_date': 'expiryDate',

        'name': 'name',

        'scopes': 'scopes',

        'status': 'status',
    }

    def __init__(self, expiry_date=None, name=None, scopes=None, status=None, local_vars_configuration=None):  # noqa: E501
        """PostTokenProperties - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._expiry_date = None
        self._name = None
        self._scopes = None
        self._status = None
        self.discriminator = None

        self.expiry_date = expiry_date
        self.name = name
        self.scopes = scopes
        if status is not None:
            self.status = status


    @property
    def expiry_date(self):
        """Gets the expiry_date of this PostTokenProperties.  # noqa: E501


        :return: The expiry_date of this PostTokenProperties.  # noqa: E501
        :rtype: datetime
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        """Sets the expiry_date of this PostTokenProperties.


        :param expiry_date: The expiry_date of this PostTokenProperties.  # noqa: E501
        :type expiry_date: datetime
        """

        self._expiry_date = expiry_date

    @property
    def name(self):
        """Gets the name of this PostTokenProperties.  # noqa: E501


        :return: The name of this PostTokenProperties.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PostTokenProperties.


        :param name: The name of this PostTokenProperties.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and not re.search(r'^[A-Za-z][-A-Za-z0-9]{0,61}[A-Za-z0-9]$', name)):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[A-Za-z][-A-Za-z0-9]{0,61}[A-Za-z0-9]$/`")  # noqa: E501

        self._name = name

    @property
    def scopes(self):
        """Gets the scopes of this PostTokenProperties.  # noqa: E501


        :return: The scopes of this PostTokenProperties.  # noqa: E501
        :rtype: list[Scope]
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """Sets the scopes of this PostTokenProperties.


        :param scopes: The scopes of this PostTokenProperties.  # noqa: E501
        :type scopes: list[Scope]
        """

        self._scopes = scopes

    @property
    def status(self):
        """Gets the status of this PostTokenProperties.  # noqa: E501


        :return: The status of this PostTokenProperties.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PostTokenProperties.


        :param status: The status of this PostTokenProperties.  # noqa: E501
        :type status: str
        """
        allowed_values = ["enabled", "disabled"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status
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
        if not isinstance(other, PostTokenProperties):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PostTokenProperties):
            return True

        return self.to_dict() != other.to_dict()
