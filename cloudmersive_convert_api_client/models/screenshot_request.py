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


class ScreenshotRequest(object):
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
        'url': 'str',
        'extra_loading_wait': 'int'
    }

    attribute_map = {
        'url': 'Url',
        'extra_loading_wait': 'ExtraLoadingWait'
    }

    def __init__(self, url=None, extra_loading_wait=None):  # noqa: E501
        """ScreenshotRequest - a model defined in Swagger"""  # noqa: E501

        self._url = None
        self._extra_loading_wait = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if extra_loading_wait is not None:
            self.extra_loading_wait = extra_loading_wait

    @property
    def url(self):
        """Gets the url of this ScreenshotRequest.  # noqa: E501


        :return: The url of this ScreenshotRequest.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ScreenshotRequest.


        :param url: The url of this ScreenshotRequest.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def extra_loading_wait(self):
        """Gets the extra_loading_wait of this ScreenshotRequest.  # noqa: E501


        :return: The extra_loading_wait of this ScreenshotRequest.  # noqa: E501
        :rtype: int
        """
        return self._extra_loading_wait

    @extra_loading_wait.setter
    def extra_loading_wait(self, extra_loading_wait):
        """Sets the extra_loading_wait of this ScreenshotRequest.


        :param extra_loading_wait: The extra_loading_wait of this ScreenshotRequest.  # noqa: E501
        :type: int
        """

        self._extra_loading_wait = extra_loading_wait

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ScreenshotRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
