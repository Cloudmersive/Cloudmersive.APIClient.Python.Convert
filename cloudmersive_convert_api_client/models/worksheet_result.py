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


class WorksheetResult(object):
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
        'worksheet_number': 'int',
        'worksheet_name': 'str',
        'url': 'str'
    }

    attribute_map = {
        'worksheet_number': 'WorksheetNumber',
        'worksheet_name': 'WorksheetName',
        'url': 'URL'
    }

    def __init__(self, worksheet_number=None, worksheet_name=None, url=None):  # noqa: E501
        """WorksheetResult - a model defined in Swagger"""  # noqa: E501

        self._worksheet_number = None
        self._worksheet_name = None
        self._url = None
        self.discriminator = None

        if worksheet_number is not None:
            self.worksheet_number = worksheet_number
        if worksheet_name is not None:
            self.worksheet_name = worksheet_name
        if url is not None:
            self.url = url

    @property
    def worksheet_number(self):
        """Gets the worksheet_number of this WorksheetResult.  # noqa: E501

        Worksheet number of the converted page, starting with 1 for the left-most worksheet  # noqa: E501

        :return: The worksheet_number of this WorksheetResult.  # noqa: E501
        :rtype: int
        """
        return self._worksheet_number

    @worksheet_number.setter
    def worksheet_number(self, worksheet_number):
        """Sets the worksheet_number of this WorksheetResult.

        Worksheet number of the converted page, starting with 1 for the left-most worksheet  # noqa: E501

        :param worksheet_number: The worksheet_number of this WorksheetResult.  # noqa: E501
        :type: int
        """

        self._worksheet_number = worksheet_number

    @property
    def worksheet_name(self):
        """Gets the worksheet_name of this WorksheetResult.  # noqa: E501

        The name of the worksheet  # noqa: E501

        :return: The worksheet_name of this WorksheetResult.  # noqa: E501
        :rtype: str
        """
        return self._worksheet_name

    @worksheet_name.setter
    def worksheet_name(self, worksheet_name):
        """Sets the worksheet_name of this WorksheetResult.

        The name of the worksheet  # noqa: E501

        :param worksheet_name: The worksheet_name of this WorksheetResult.  # noqa: E501
        :type: str
        """

        self._worksheet_name = worksheet_name

    @property
    def url(self):
        """Gets the url of this WorksheetResult.  # noqa: E501

        URL to the XLSX file of this worksheet; file is stored in an in-memory cache and will be deleted  # noqa: E501

        :return: The url of this WorksheetResult.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this WorksheetResult.

        URL to the XLSX file of this worksheet; file is stored in an in-memory cache and will be deleted  # noqa: E501

        :param url: The url of this WorksheetResult.  # noqa: E501
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
        if issubclass(WorksheetResult, dict):
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
        if not isinstance(other, WorksheetResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other