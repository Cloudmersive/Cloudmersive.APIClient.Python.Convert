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


class TextDocumentLine(object):
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
        'line_number': 'int',
        'line_contents': 'str'
    }

    attribute_map = {
        'line_number': 'LineNumber',
        'line_contents': 'LineContents'
    }

    def __init__(self, line_number=None, line_contents=None):  # noqa: E501
        """TextDocumentLine - a model defined in Swagger"""  # noqa: E501

        self._line_number = None
        self._line_contents = None
        self.discriminator = None

        if line_number is not None:
            self.line_number = line_number
        if line_contents is not None:
            self.line_contents = line_contents

    @property
    def line_number(self):
        """Gets the line_number of this TextDocumentLine.  # noqa: E501

        The 1-based line index of the line  # noqa: E501

        :return: The line_number of this TextDocumentLine.  # noqa: E501
        :rtype: int
        """
        return self._line_number

    @line_number.setter
    def line_number(self, line_number):
        """Sets the line_number of this TextDocumentLine.

        The 1-based line index of the line  # noqa: E501

        :param line_number: The line_number of this TextDocumentLine.  # noqa: E501
        :type: int
        """

        self._line_number = line_number

    @property
    def line_contents(self):
        """Gets the line_contents of this TextDocumentLine.  # noqa: E501

        The text contents of a single line of a text file  # noqa: E501

        :return: The line_contents of this TextDocumentLine.  # noqa: E501
        :rtype: str
        """
        return self._line_contents

    @line_contents.setter
    def line_contents(self, line_contents):
        """Sets the line_contents of this TextDocumentLine.

        The text contents of a single line of a text file  # noqa: E501

        :param line_contents: The line_contents of this TextDocumentLine.  # noqa: E501
        :type: str
        """

        self._line_contents = line_contents

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
        if issubclass(TextDocumentLine, dict):
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
        if not isinstance(other, TextDocumentLine):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
