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


class CreateBlankDocxRequest(object):
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
        'initial_text': 'str'
    }

    attribute_map = {
        'initial_text': 'InitialText'
    }

    def __init__(self, initial_text=None):  # noqa: E501
        """CreateBlankDocxRequest - a model defined in Swagger"""  # noqa: E501

        self._initial_text = None
        self.discriminator = None

        if initial_text is not None:
            self.initial_text = initial_text

    @property
    def initial_text(self):
        """Gets the initial_text of this CreateBlankDocxRequest.  # noqa: E501

        Optional; initial text to include in the document  # noqa: E501

        :return: The initial_text of this CreateBlankDocxRequest.  # noqa: E501
        :rtype: str
        """
        return self._initial_text

    @initial_text.setter
    def initial_text(self, initial_text):
        """Sets the initial_text of this CreateBlankDocxRequest.

        Optional; initial text to include in the document  # noqa: E501

        :param initial_text: The initial_text of this CreateBlankDocxRequest.  # noqa: E501
        :type: str
        """

        self._initial_text = initial_text

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
        if issubclass(CreateBlankDocxRequest, dict):
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
        if not isinstance(other, CreateBlankDocxRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other