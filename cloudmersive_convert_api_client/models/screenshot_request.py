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
        'extra_loading_wait': 'int',
        'screenshot_width': 'int',
        'screenshot_height': 'int'
    }

    attribute_map = {
        'url': 'Url',
        'extra_loading_wait': 'ExtraLoadingWait',
        'screenshot_width': 'ScreenshotWidth',
        'screenshot_height': 'ScreenshotHeight'
    }

    def __init__(self, url=None, extra_loading_wait=None, screenshot_width=None, screenshot_height=None):  # noqa: E501
        """ScreenshotRequest - a model defined in Swagger"""  # noqa: E501

        self._url = None
        self._extra_loading_wait = None
        self._screenshot_width = None
        self._screenshot_height = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if extra_loading_wait is not None:
            self.extra_loading_wait = extra_loading_wait
        if screenshot_width is not None:
            self.screenshot_width = screenshot_width
        if screenshot_height is not None:
            self.screenshot_height = screenshot_height

    @property
    def url(self):
        """Gets the url of this ScreenshotRequest.  # noqa: E501

        URL address of the website to screenshot.  HTTP and HTTPS are both supported, as are custom ports.  # noqa: E501

        :return: The url of this ScreenshotRequest.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ScreenshotRequest.

        URL address of the website to screenshot.  HTTP and HTTPS are both supported, as are custom ports.  # noqa: E501

        :param url: The url of this ScreenshotRequest.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def extra_loading_wait(self):
        """Gets the extra_loading_wait of this ScreenshotRequest.  # noqa: E501

        Optional: Additional number of milliseconds to wait once the web page has finished loading before taking the screenshot.  Can be helpful for highly asynchronous websites.  Provide a value of 0 for the default of 5000 milliseconds (5 seconds). Maximum is 20000 milliseconds (20 seconds).  # noqa: E501

        :return: The extra_loading_wait of this ScreenshotRequest.  # noqa: E501
        :rtype: int
        """
        return self._extra_loading_wait

    @extra_loading_wait.setter
    def extra_loading_wait(self, extra_loading_wait):
        """Sets the extra_loading_wait of this ScreenshotRequest.

        Optional: Additional number of milliseconds to wait once the web page has finished loading before taking the screenshot.  Can be helpful for highly asynchronous websites.  Provide a value of 0 for the default of 5000 milliseconds (5 seconds). Maximum is 20000 milliseconds (20 seconds).  # noqa: E501

        :param extra_loading_wait: The extra_loading_wait of this ScreenshotRequest.  # noqa: E501
        :type: int
        """

        self._extra_loading_wait = extra_loading_wait

    @property
    def screenshot_width(self):
        """Gets the screenshot_width of this ScreenshotRequest.  # noqa: E501

        Optional: Width of the screenshot in pixels; supply 0 to default to 1280 x 1024  # noqa: E501

        :return: The screenshot_width of this ScreenshotRequest.  # noqa: E501
        :rtype: int
        """
        return self._screenshot_width

    @screenshot_width.setter
    def screenshot_width(self, screenshot_width):
        """Sets the screenshot_width of this ScreenshotRequest.

        Optional: Width of the screenshot in pixels; supply 0 to default to 1280 x 1024  # noqa: E501

        :param screenshot_width: The screenshot_width of this ScreenshotRequest.  # noqa: E501
        :type: int
        """

        self._screenshot_width = screenshot_width

    @property
    def screenshot_height(self):
        """Gets the screenshot_height of this ScreenshotRequest.  # noqa: E501

        Optional: Height of the screenshot in pixels; supply 0 to default to 1280 x 1024, supply -1 to measure the full screen height of the page and attempt to take a screen-height screenshot  # noqa: E501

        :return: The screenshot_height of this ScreenshotRequest.  # noqa: E501
        :rtype: int
        """
        return self._screenshot_height

    @screenshot_height.setter
    def screenshot_height(self, screenshot_height):
        """Sets the screenshot_height of this ScreenshotRequest.

        Optional: Height of the screenshot in pixels; supply 0 to default to 1280 x 1024, supply -1 to measure the full screen height of the page and attempt to take a screen-height screenshot  # noqa: E501

        :param screenshot_height: The screenshot_height of this ScreenshotRequest.  # noqa: E501
        :type: int
        """

        self._screenshot_height = screenshot_height

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
        if issubclass(ScreenshotRequest, dict):
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
        if not isinstance(other, ScreenshotRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
