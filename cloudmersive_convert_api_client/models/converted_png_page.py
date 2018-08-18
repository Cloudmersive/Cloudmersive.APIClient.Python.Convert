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


class ConvertedPngPage(object):
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
        'page_number': 'int',
        'url': 'str'
    }

    attribute_map = {
        'page_number': 'PageNumber',
        'url': 'URL'
    }

    def __init__(self, page_number=None, url=None):  # noqa: E501
        """ConvertedPngPage - a model defined in Swagger"""  # noqa: E501

        self._page_number = None
        self._url = None
        self.discriminator = None

        if page_number is not None:
            self.page_number = page_number
        if url is not None:
            self.url = url

    @property
    def page_number(self):
        """Gets the page_number of this ConvertedPngPage.  # noqa: E501

        Page number of the converted page, starting with 1  # noqa: E501

        :return: The page_number of this ConvertedPngPage.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this ConvertedPngPage.

        Page number of the converted page, starting with 1  # noqa: E501

        :param page_number: The page_number of this ConvertedPngPage.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def url(self):
        """Gets the url of this ConvertedPngPage.  # noqa: E501

        URL to the PNG file of this page; file is stored in an in-memory cache and will be deleted  # noqa: E501

        :return: The url of this ConvertedPngPage.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ConvertedPngPage.

        URL to the PNG file of this page; file is stored in an in-memory cache and will be deleted  # noqa: E501

        :param url: The url of this ConvertedPngPage.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if not isinstance(other, ConvertedPngPage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
