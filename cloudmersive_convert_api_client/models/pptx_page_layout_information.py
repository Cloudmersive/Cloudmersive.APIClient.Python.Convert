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


class PptxPageLayoutInformation(object):
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
        'orientation': 'str',
        'width': 'int',
        'height': 'int'
    }

    attribute_map = {
        'successful': 'Successful',
        'orientation': 'Orientation',
        'width': 'Width',
        'height': 'Height'
    }

    def __init__(self, successful=None, orientation=None, width=None, height=None):  # noqa: E501
        """PptxPageLayoutInformation - a model defined in Swagger"""  # noqa: E501

        self._successful = None
        self._orientation = None
        self._width = None
        self._height = None
        self.discriminator = None

        if successful is not None:
            self.successful = successful
        if orientation is not None:
            self.orientation = orientation
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height

    @property
    def successful(self):
        """Gets the successful of this PptxPageLayoutInformation.  # noqa: E501

        True if successful, false otherwise  # noqa: E501

        :return: The successful of this PptxPageLayoutInformation.  # noqa: E501
        :rtype: bool
        """
        return self._successful

    @successful.setter
    def successful(self, successful):
        """Sets the successful of this PptxPageLayoutInformation.

        True if successful, false otherwise  # noqa: E501

        :param successful: The successful of this PptxPageLayoutInformation.  # noqa: E501
        :type: bool
        """

        self._successful = successful

    @property
    def orientation(self):
        """Gets the orientation of this PptxPageLayoutInformation.  # noqa: E501

        Orientation of the presentation, either portrait or landscape  # noqa: E501

        :return: The orientation of this PptxPageLayoutInformation.  # noqa: E501
        :rtype: str
        """
        return self._orientation

    @orientation.setter
    def orientation(self, orientation):
        """Sets the orientation of this PptxPageLayoutInformation.

        Orientation of the presentation, either portrait or landscape  # noqa: E501

        :param orientation: The orientation of this PptxPageLayoutInformation.  # noqa: E501
        :type: str
        """

        self._orientation = orientation

    @property
    def width(self):
        """Gets the width of this PptxPageLayoutInformation.  # noqa: E501

        Width of the presentation in Emu, where 1 inch equals 914400 emu.  # noqa: E501

        :return: The width of this PptxPageLayoutInformation.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this PptxPageLayoutInformation.

        Width of the presentation in Emu, where 1 inch equals 914400 emu.  # noqa: E501

        :param width: The width of this PptxPageLayoutInformation.  # noqa: E501
        :type: int
        """

        self._width = width

    @property
    def height(self):
        """Gets the height of this PptxPageLayoutInformation.  # noqa: E501

        Height of the presentation in Emu, where 1 inch equals 914400 emu.  # noqa: E501

        :return: The height of this PptxPageLayoutInformation.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this PptxPageLayoutInformation.

        Height of the presentation in Emu, where 1 inch equals 914400 emu.  # noqa: E501

        :param height: The height of this PptxPageLayoutInformation.  # noqa: E501
        :type: int
        """

        self._height = height

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
        if issubclass(PptxPageLayoutInformation, dict):
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
        if not isinstance(other, PptxPageLayoutInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other