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


class DocxCellStyle(object):
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
        'path': 'str',
        'name': 'str',
        'format_id': 'int',
        'built_in_id': 'int'
    }

    attribute_map = {
        'path': 'Path',
        'name': 'Name',
        'format_id': 'FormatID',
        'built_in_id': 'BuiltInID'
    }

    def __init__(self, path=None, name=None, format_id=None, built_in_id=None):  # noqa: E501
        """DocxCellStyle - a model defined in Swagger"""  # noqa: E501

        self._path = None
        self._name = None
        self._format_id = None
        self._built_in_id = None
        self.discriminator = None

        if path is not None:
            self.path = path
        if name is not None:
            self.name = name
        if format_id is not None:
            self.format_id = format_id
        if built_in_id is not None:
            self.built_in_id = built_in_id

    @property
    def path(self):
        """Gets the path of this DocxCellStyle.  # noqa: E501

        The Path of the location of this object; leave blank for new rows  # noqa: E501

        :return: The path of this DocxCellStyle.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this DocxCellStyle.

        The Path of the location of this object; leave blank for new rows  # noqa: E501

        :param path: The path of this DocxCellStyle.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def name(self):
        """Gets the name of this DocxCellStyle.  # noqa: E501

        Name of the style  # noqa: E501

        :return: The name of this DocxCellStyle.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DocxCellStyle.

        Name of the style  # noqa: E501

        :param name: The name of this DocxCellStyle.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def format_id(self):
        """Gets the format_id of this DocxCellStyle.  # noqa: E501

        Format ID of the cell style  # noqa: E501

        :return: The format_id of this DocxCellStyle.  # noqa: E501
        :rtype: int
        """
        return self._format_id

    @format_id.setter
    def format_id(self, format_id):
        """Sets the format_id of this DocxCellStyle.

        Format ID of the cell style  # noqa: E501

        :param format_id: The format_id of this DocxCellStyle.  # noqa: E501
        :type: int
        """

        self._format_id = format_id

    @property
    def built_in_id(self):
        """Gets the built_in_id of this DocxCellStyle.  # noqa: E501

        Built=in ID of the cell style  # noqa: E501

        :return: The built_in_id of this DocxCellStyle.  # noqa: E501
        :rtype: int
        """
        return self._built_in_id

    @built_in_id.setter
    def built_in_id(self, built_in_id):
        """Sets the built_in_id of this DocxCellStyle.

        Built=in ID of the cell style  # noqa: E501

        :param built_in_id: The built_in_id of this DocxCellStyle.  # noqa: E501
        :type: int
        """

        self._built_in_id = built_in_id

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
        if issubclass(DocxCellStyle, dict):
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
        if not isinstance(other, DocxCellStyle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other