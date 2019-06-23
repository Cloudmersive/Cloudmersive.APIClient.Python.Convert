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

from cloudmersive_convert_api_client.models.docx_style import DocxStyle  # noqa: F401,E501


class GetDocxStylesResponse(object):
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
        'styles': 'list[DocxStyle]'
    }

    attribute_map = {
        'successful': 'Successful',
        'styles': 'Styles'
    }

    def __init__(self, successful=None, styles=None):  # noqa: E501
        """GetDocxStylesResponse - a model defined in Swagger"""  # noqa: E501

        self._successful = None
        self._styles = None
        self.discriminator = None

        if successful is not None:
            self.successful = successful
        if styles is not None:
            self.styles = styles

    @property
    def successful(self):
        """Gets the successful of this GetDocxStylesResponse.  # noqa: E501

        True if successful, false otherwise  # noqa: E501

        :return: The successful of this GetDocxStylesResponse.  # noqa: E501
        :rtype: bool
        """
        return self._successful

    @successful.setter
    def successful(self, successful):
        """Sets the successful of this GetDocxStylesResponse.

        True if successful, false otherwise  # noqa: E501

        :param successful: The successful of this GetDocxStylesResponse.  # noqa: E501
        :type: bool
        """

        self._successful = successful

    @property
    def styles(self):
        """Gets the styles of this GetDocxStylesResponse.  # noqa: E501

        Styles in the DOCX document  # noqa: E501

        :return: The styles of this GetDocxStylesResponse.  # noqa: E501
        :rtype: list[DocxStyle]
        """
        return self._styles

    @styles.setter
    def styles(self, styles):
        """Sets the styles of this GetDocxStylesResponse.

        Styles in the DOCX document  # noqa: E501

        :param styles: The styles of this GetDocxStylesResponse.  # noqa: E501
        :type: list[DocxStyle]
        """

        self._styles = styles

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
        if issubclass(GetDocxStylesResponse, dict):
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
        if not isinstance(other, GetDocxStylesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
