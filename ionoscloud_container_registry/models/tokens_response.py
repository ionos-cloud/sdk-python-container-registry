# coding: utf-8

"""
    Container Registry service

    Container Registry service enables IONOS clients to manage docker and OCI compliant registries for use by their managed Kubernetes clusters. Use a Container Registry to ensure you have a privately accessed registry to efficiently support image pulls.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: support@cloud.ionos.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ionoscloud_container_registry.configuration import Configuration


class TokensResponse(object):
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

        'links': 'PaginationLinks',

        'count': 'int',

        'href': 'str',

        'id': 'str',

        'items': 'list[TokenResponse]',

        'limit': 'int',

        'offset': 'int',

        'total': 'int',

        'type': 'str',
    }

    attribute_map = {

        'links': '_links',

        'count': 'count',

        'href': 'href',

        'id': 'id',

        'items': 'items',

        'limit': 'limit',

        'offset': 'offset',

        'total': 'total',

        'type': 'type',
    }

    def __init__(self, links=None, count=None, href=None, id=None, items=None, limit=None, offset=None, total=None, type=None, local_vars_configuration=None):  # noqa: E501
        """TokensResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._links = None
        self._count = None
        self._href = None
        self._id = None
        self._items = None
        self._limit = None
        self._offset = None
        self._total = None
        self._type = None
        self.discriminator = None

        self.links = links
        self.count = count
        if href is not None:
            self.href = href
        if id is not None:
            self.id = id
        self.items = items
        self.limit = limit
        self.offset = offset
        self.total = total
        if type is not None:
            self.type = type


    @property
    def links(self):
        """Gets the links of this TokensResponse.  # noqa: E501


        :return: The links of this TokensResponse.  # noqa: E501
        :rtype: PaginationLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this TokensResponse.


        :param links: The links of this TokensResponse.  # noqa: E501
        :type links: PaginationLinks
        """
        if self.local_vars_configuration.client_side_validation and links is None:  # noqa: E501
            raise ValueError("Invalid value for `links`, must not be `None`")  # noqa: E501

        self._links = links

    @property
    def count(self):
        """Gets the count of this TokensResponse.  # noqa: E501


        :return: The count of this TokensResponse.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this TokensResponse.


        :param count: The count of this TokensResponse.  # noqa: E501
        :type count: int
        """
        if self.local_vars_configuration.client_side_validation and count is None:  # noqa: E501
            raise ValueError("Invalid value for `count`, must not be `None`")  # noqa: E501

        self._count = count

    @property
    def href(self):
        """Gets the href of this TokensResponse.  # noqa: E501


        :return: The href of this TokensResponse.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this TokensResponse.


        :param href: The href of this TokensResponse.  # noqa: E501
        :type href: str
        """

        self._href = href

    @property
    def id(self):
        """Gets the id of this TokensResponse.  # noqa: E501


        :return: The id of this TokensResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TokensResponse.


        :param id: The id of this TokensResponse.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def items(self):
        """Gets the items of this TokensResponse.  # noqa: E501


        :return: The items of this TokensResponse.  # noqa: E501
        :rtype: list[TokenResponse]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this TokensResponse.


        :param items: The items of this TokensResponse.  # noqa: E501
        :type items: list[TokenResponse]
        """

        self._items = items

    @property
    def limit(self):
        """Gets the limit of this TokensResponse.  # noqa: E501


        :return: The limit of this TokensResponse.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this TokensResponse.


        :param limit: The limit of this TokensResponse.  # noqa: E501
        :type limit: int
        """
        if self.local_vars_configuration.client_side_validation and limit is None:  # noqa: E501
            raise ValueError("Invalid value for `limit`, must not be `None`")  # noqa: E501

        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this TokensResponse.  # noqa: E501


        :return: The offset of this TokensResponse.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this TokensResponse.


        :param offset: The offset of this TokensResponse.  # noqa: E501
        :type offset: int
        """
        if self.local_vars_configuration.client_side_validation and offset is None:  # noqa: E501
            raise ValueError("Invalid value for `offset`, must not be `None`")  # noqa: E501

        self._offset = offset

    @property
    def total(self):
        """Gets the total of this TokensResponse.  # noqa: E501


        :return: The total of this TokensResponse.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this TokensResponse.


        :param total: The total of this TokensResponse.  # noqa: E501
        :type total: int
        """
        if self.local_vars_configuration.client_side_validation and total is None:  # noqa: E501
            raise ValueError("Invalid value for `total`, must not be `None`")  # noqa: E501

        self._total = total

    @property
    def type(self):
        """Gets the type of this TokensResponse.  # noqa: E501


        :return: The type of this TokensResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TokensResponse.


        :param type: The type of this TokensResponse.  # noqa: E501
        :type type: str
        """

        self._type = type
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
        if not isinstance(other, TokensResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TokensResponse):
            return True

        return self.to_dict() != other.to_dict()