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


class XmlAddChildWithXPathResult(object):
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
        'resulting_xml_document': 'str',
        'nodes_edited_count': 'int'
    }

    attribute_map = {
        'successful': 'Successful',
        'resulting_xml_document': 'ResultingXmlDocument',
        'nodes_edited_count': 'NodesEditedCount'
    }

    def __init__(self, successful=None, resulting_xml_document=None, nodes_edited_count=None):  # noqa: E501
        """XmlAddChildWithXPathResult - a model defined in Swagger"""  # noqa: E501

        self._successful = None
        self._resulting_xml_document = None
        self._nodes_edited_count = None
        self.discriminator = None

        if successful is not None:
            self.successful = successful
        if resulting_xml_document is not None:
            self.resulting_xml_document = resulting_xml_document
        if nodes_edited_count is not None:
            self.nodes_edited_count = nodes_edited_count

    @property
    def successful(self):
        """Gets the successful of this XmlAddChildWithXPathResult.  # noqa: E501

        True if the operation was successful, false otherwise  # noqa: E501

        :return: The successful of this XmlAddChildWithXPathResult.  # noqa: E501
        :rtype: bool
        """
        return self._successful

    @successful.setter
    def successful(self, successful):
        """Sets the successful of this XmlAddChildWithXPathResult.

        True if the operation was successful, false otherwise  # noqa: E501

        :param successful: The successful of this XmlAddChildWithXPathResult.  # noqa: E501
        :type: bool
        """

        self._successful = successful

    @property
    def resulting_xml_document(self):
        """Gets the resulting_xml_document of this XmlAddChildWithXPathResult.  # noqa: E501

        Resulting, modified XML document  # noqa: E501

        :return: The resulting_xml_document of this XmlAddChildWithXPathResult.  # noqa: E501
        :rtype: str
        """
        return self._resulting_xml_document

    @resulting_xml_document.setter
    def resulting_xml_document(self, resulting_xml_document):
        """Sets the resulting_xml_document of this XmlAddChildWithXPathResult.

        Resulting, modified XML document  # noqa: E501

        :param resulting_xml_document: The resulting_xml_document of this XmlAddChildWithXPathResult.  # noqa: E501
        :type: str
        """

        self._resulting_xml_document = resulting_xml_document

    @property
    def nodes_edited_count(self):
        """Gets the nodes_edited_count of this XmlAddChildWithXPathResult.  # noqa: E501

        Count of the matching results  # noqa: E501

        :return: The nodes_edited_count of this XmlAddChildWithXPathResult.  # noqa: E501
        :rtype: int
        """
        return self._nodes_edited_count

    @nodes_edited_count.setter
    def nodes_edited_count(self, nodes_edited_count):
        """Sets the nodes_edited_count of this XmlAddChildWithXPathResult.

        Count of the matching results  # noqa: E501

        :param nodes_edited_count: The nodes_edited_count of this XmlAddChildWithXPathResult.  # noqa: E501
        :type: int
        """

        self._nodes_edited_count = nodes_edited_count

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
        if issubclass(XmlAddChildWithXPathResult, dict):
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
        if not isinstance(other, XmlAddChildWithXPathResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
