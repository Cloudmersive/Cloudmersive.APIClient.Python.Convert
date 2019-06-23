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


class HtmlTemplateOperation(object):
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
        'action': 'int',
        'match_agsint': 'str',
        'replace_with': 'str'
    }

    attribute_map = {
        'action': 'Action',
        'match_agsint': 'MatchAgsint',
        'replace_with': 'ReplaceWith'
    }

    def __init__(self, action=None, match_agsint=None, replace_with=None):  # noqa: E501
        """HtmlTemplateOperation - a model defined in Swagger"""  # noqa: E501

        self._action = None
        self._match_agsint = None
        self._replace_with = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if match_agsint is not None:
            self.match_agsint = match_agsint
        if replace_with is not None:
            self.replace_with = replace_with

    @property
    def action(self):
        """Gets the action of this HtmlTemplateOperation.  # noqa: E501


        :return: The action of this HtmlTemplateOperation.  # noqa: E501
        :rtype: int
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this HtmlTemplateOperation.


        :param action: The action of this HtmlTemplateOperation.  # noqa: E501
        :type: int
        """
        allowed_values = [1]  # noqa: E501
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def match_agsint(self):
        """Gets the match_agsint of this HtmlTemplateOperation.  # noqa: E501


        :return: The match_agsint of this HtmlTemplateOperation.  # noqa: E501
        :rtype: str
        """
        return self._match_agsint

    @match_agsint.setter
    def match_agsint(self, match_agsint):
        """Sets the match_agsint of this HtmlTemplateOperation.


        :param match_agsint: The match_agsint of this HtmlTemplateOperation.  # noqa: E501
        :type: str
        """

        self._match_agsint = match_agsint

    @property
    def replace_with(self):
        """Gets the replace_with of this HtmlTemplateOperation.  # noqa: E501


        :return: The replace_with of this HtmlTemplateOperation.  # noqa: E501
        :rtype: str
        """
        return self._replace_with

    @replace_with.setter
    def replace_with(self, replace_with):
        """Sets the replace_with of this HtmlTemplateOperation.


        :param replace_with: The replace_with of this HtmlTemplateOperation.  # noqa: E501
        :type: str
        """

        self._replace_with = replace_with

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
        if issubclass(HtmlTemplateOperation, dict):
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
        if not isinstance(other, HtmlTemplateOperation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
