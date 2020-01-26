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


class Base64DetectRequest(object):
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
        'base64_content_to_detect': 'str'
    }

    attribute_map = {
        'base64_content_to_detect': 'Base64ContentToDetect'
    }

    def __init__(self, base64_content_to_detect=None):  # noqa: E501
        """Base64DetectRequest - a model defined in Swagger"""  # noqa: E501

        self._base64_content_to_detect = None
        self.discriminator = None

        if base64_content_to_detect is not None:
            self.base64_content_to_detect = base64_content_to_detect

    @property
    def base64_content_to_detect(self):
        """Gets the base64_content_to_detect of this Base64DetectRequest.  # noqa: E501

        Input content text to detect if it is base 64 encoded  # noqa: E501

        :return: The base64_content_to_detect of this Base64DetectRequest.  # noqa: E501
        :rtype: str
        """
        return self._base64_content_to_detect

    @base64_content_to_detect.setter
    def base64_content_to_detect(self, base64_content_to_detect):
        """Sets the base64_content_to_detect of this Base64DetectRequest.

        Input content text to detect if it is base 64 encoded  # noqa: E501

        :param base64_content_to_detect: The base64_content_to_detect of this Base64DetectRequest.  # noqa: E501
        :type: str
        """

        self._base64_content_to_detect = base64_content_to_detect

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
        if issubclass(Base64DetectRequest, dict):
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
        if not isinstance(other, Base64DetectRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
