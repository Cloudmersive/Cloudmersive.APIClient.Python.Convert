# coding: utf-8

"""
    convertapi

    Convert API lets you effortlessly convert file formats and types.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class XmlFilterWithXPathResult(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'successful': 'bool',
        'xml_nodes': 'list[str]',
        'result_count': 'int'
    }

    attribute_map = {
        'successful': 'Successful',
        'xml_nodes': 'XmlNodes',
        'result_count': 'ResultCount'
    }

    def __init__(self, successful=None, xml_nodes=None, result_count=None):  # noqa: E501
        """XmlFilterWithXPathResult - a model defined in Swagger"""  # noqa: E501

        self._successful = None
        self._xml_nodes = None
        self._result_count = None
        self.discriminator = None

        if successful is not None:
            self.successful = successful
        if xml_nodes is not None:
            self.xml_nodes = xml_nodes
        if result_count is not None:
            self.result_count = result_count

    @property
    def successful(self):
        """Gets the successful of this XmlFilterWithXPathResult.  # noqa: E501

        True if the operation was successful, false otherwise  # noqa: E501

        :return: The successful of this XmlFilterWithXPathResult.  # noqa: E501
        :rtype: bool
        """
        return self._successful

    @successful.setter
    def successful(self, successful):
        """Sets the successful of this XmlFilterWithXPathResult.

        True if the operation was successful, false otherwise  # noqa: E501

        :param successful: The successful of this XmlFilterWithXPathResult.  # noqa: E501
        :type: bool
        """

        self._successful = successful

    @property
    def xml_nodes(self):
        """Gets the xml_nodes of this XmlFilterWithXPathResult.  # noqa: E501

        Matching selected XML nodes as strings  # noqa: E501

        :return: The xml_nodes of this XmlFilterWithXPathResult.  # noqa: E501
        :rtype: list[str]
        """
        return self._xml_nodes

    @xml_nodes.setter
    def xml_nodes(self, xml_nodes):
        """Sets the xml_nodes of this XmlFilterWithXPathResult.

        Matching selected XML nodes as strings  # noqa: E501

        :param xml_nodes: The xml_nodes of this XmlFilterWithXPathResult.  # noqa: E501
        :type: list[str]
        """

        self._xml_nodes = xml_nodes

    @property
    def result_count(self):
        """Gets the result_count of this XmlFilterWithXPathResult.  # noqa: E501

        Count of the matching results  # noqa: E501

        :return: The result_count of this XmlFilterWithXPathResult.  # noqa: E501
        :rtype: int
        """
        return self._result_count

    @result_count.setter
    def result_count(self, result_count):
        """Sets the result_count of this XmlFilterWithXPathResult.

        Count of the matching results  # noqa: E501

        :param result_count: The result_count of this XmlFilterWithXPathResult.  # noqa: E501
        :type: int
        """

        self._result_count = result_count

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(XmlFilterWithXPathResult, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, XmlFilterWithXPathResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
