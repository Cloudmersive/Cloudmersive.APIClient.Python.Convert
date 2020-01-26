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


class DetectLineEndingsResponse(object):
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
        'primary_newline_type': 'str',
        'primary_newline_terminator': 'str',
        'input_length': 'int'
    }

    attribute_map = {
        'successful': 'Successful',
        'primary_newline_type': 'PrimaryNewlineType',
        'primary_newline_terminator': 'PrimaryNewlineTerminator',
        'input_length': 'InputLength'
    }

    def __init__(self, successful=None, primary_newline_type=None, primary_newline_terminator=None, input_length=None):  # noqa: E501
        """DetectLineEndingsResponse - a model defined in Swagger"""  # noqa: E501

        self._successful = None
        self._primary_newline_type = None
        self._primary_newline_terminator = None
        self._input_length = None
        self.discriminator = None

        if successful is not None:
            self.successful = successful
        if primary_newline_type is not None:
            self.primary_newline_type = primary_newline_type
        if primary_newline_terminator is not None:
            self.primary_newline_terminator = primary_newline_terminator
        if input_length is not None:
            self.input_length = input_length

    @property
    def successful(self):
        """Gets the successful of this DetectLineEndingsResponse.  # noqa: E501

        True if successful, false otherwise  # noqa: E501

        :return: The successful of this DetectLineEndingsResponse.  # noqa: E501
        :rtype: bool
        """
        return self._successful

    @successful.setter
    def successful(self, successful):
        """Sets the successful of this DetectLineEndingsResponse.

        True if successful, false otherwise  # noqa: E501

        :param successful: The successful of this DetectLineEndingsResponse.  # noqa: E501
        :type: bool
        """

        self._successful = successful

    @property
    def primary_newline_type(self):
        """Gets the primary_newline_type of this DetectLineEndingsResponse.  # noqa: E501

        Type of newline in the file; possible vlaues are \"Mac\" (legacy Mac OS uses carriage return only); \"Unix\" (Unix and Linux OSes, and modern Mac OS); \"Windows\" (Windows operating systems)  # noqa: E501

        :return: The primary_newline_type of this DetectLineEndingsResponse.  # noqa: E501
        :rtype: str
        """
        return self._primary_newline_type

    @primary_newline_type.setter
    def primary_newline_type(self, primary_newline_type):
        """Sets the primary_newline_type of this DetectLineEndingsResponse.

        Type of newline in the file; possible vlaues are \"Mac\" (legacy Mac OS uses carriage return only); \"Unix\" (Unix and Linux OSes, and modern Mac OS); \"Windows\" (Windows operating systems)  # noqa: E501

        :param primary_newline_type: The primary_newline_type of this DetectLineEndingsResponse.  # noqa: E501
        :type: str
        """

        self._primary_newline_type = primary_newline_type

    @property
    def primary_newline_terminator(self):
        """Gets the primary_newline_terminator of this DetectLineEndingsResponse.  # noqa: E501

        Characters used to terminate a newline; can be carriage return, linefeed, or carriage return + linefeed  # noqa: E501

        :return: The primary_newline_terminator of this DetectLineEndingsResponse.  # noqa: E501
        :rtype: str
        """
        return self._primary_newline_terminator

    @primary_newline_terminator.setter
    def primary_newline_terminator(self, primary_newline_terminator):
        """Sets the primary_newline_terminator of this DetectLineEndingsResponse.

        Characters used to terminate a newline; can be carriage return, linefeed, or carriage return + linefeed  # noqa: E501

        :param primary_newline_terminator: The primary_newline_terminator of this DetectLineEndingsResponse.  # noqa: E501
        :type: str
        """

        self._primary_newline_terminator = primary_newline_terminator

    @property
    def input_length(self):
        """Gets the input_length of this DetectLineEndingsResponse.  # noqa: E501

        Length of the input string in characters  # noqa: E501

        :return: The input_length of this DetectLineEndingsResponse.  # noqa: E501
        :rtype: int
        """
        return self._input_length

    @input_length.setter
    def input_length(self, input_length):
        """Sets the input_length of this DetectLineEndingsResponse.

        Length of the input string in characters  # noqa: E501

        :param input_length: The input_length of this DetectLineEndingsResponse.  # noqa: E501
        :type: int
        """

        self._input_length = input_length

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
        if issubclass(DetectLineEndingsResponse, dict):
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
        if not isinstance(other, DetectLineEndingsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
