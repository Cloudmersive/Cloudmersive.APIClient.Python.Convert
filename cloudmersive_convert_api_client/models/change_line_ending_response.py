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


class ChangeLineEndingResponse(object):
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
        'text_content_result': 'str'
    }

    attribute_map = {
        'successful': 'Successful',
        'text_content_result': 'TextContentResult'
    }

    def __init__(self, successful=None, text_content_result=None):  # noqa: E501
        """ChangeLineEndingResponse - a model defined in Swagger"""  # noqa: E501

        self._successful = None
        self._text_content_result = None
        self.discriminator = None

        if successful is not None:
            self.successful = successful
        if text_content_result is not None:
            self.text_content_result = text_content_result

    @property
    def successful(self):
        """Gets the successful of this ChangeLineEndingResponse.  # noqa: E501

        True if successful, false otherwise  # noqa: E501

        :return: The successful of this ChangeLineEndingResponse.  # noqa: E501
        :rtype: bool
        """
        return self._successful

    @successful.setter
    def successful(self, successful):
        """Sets the successful of this ChangeLineEndingResponse.

        True if successful, false otherwise  # noqa: E501

        :param successful: The successful of this ChangeLineEndingResponse.  # noqa: E501
        :type: bool
        """

        self._successful = successful

    @property
    def text_content_result(self):
        """Gets the text_content_result of this ChangeLineEndingResponse.  # noqa: E501

        Text content result  # noqa: E501

        :return: The text_content_result of this ChangeLineEndingResponse.  # noqa: E501
        :rtype: str
        """
        return self._text_content_result

    @text_content_result.setter
    def text_content_result(self, text_content_result):
        """Sets the text_content_result of this ChangeLineEndingResponse.

        Text content result  # noqa: E501

        :param text_content_result: The text_content_result of this ChangeLineEndingResponse.  # noqa: E501
        :type: str
        """

        self._text_content_result = text_content_result

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
        if issubclass(ChangeLineEndingResponse, dict):
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
        if not isinstance(other, ChangeLineEndingResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
