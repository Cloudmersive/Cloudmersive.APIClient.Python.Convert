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


class DocxStyle(object):
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
        'style_id': 'str',
        'bold': 'bool',
        'italic': 'bool',
        'underline': 'bool',
        'font_size': 'str',
        'font_family': 'str'
    }

    attribute_map = {
        'style_id': 'StyleID',
        'bold': 'Bold',
        'italic': 'Italic',
        'underline': 'Underline',
        'font_size': 'FontSize',
        'font_family': 'FontFamily'
    }

    def __init__(self, style_id=None, bold=None, italic=None, underline=None, font_size=None, font_family=None):  # noqa: E501
        """DocxStyle - a model defined in Swagger"""  # noqa: E501

        self._style_id = None
        self._bold = None
        self._italic = None
        self._underline = None
        self._font_size = None
        self._font_family = None
        self.discriminator = None

        if style_id is not None:
            self.style_id = style_id
        if bold is not None:
            self.bold = bold
        if italic is not None:
            self.italic = italic
        if underline is not None:
            self.underline = underline
        if font_size is not None:
            self.font_size = font_size
        if font_family is not None:
            self.font_family = font_family

    @property
    def style_id(self):
        """Gets the style_id of this DocxStyle.  # noqa: E501

        ID of the style  # noqa: E501

        :return: The style_id of this DocxStyle.  # noqa: E501
        :rtype: str
        """
        return self._style_id

    @style_id.setter
    def style_id(self, style_id):
        """Sets the style_id of this DocxStyle.

        ID of the style  # noqa: E501

        :param style_id: The style_id of this DocxStyle.  # noqa: E501
        :type: str
        """

        self._style_id = style_id

    @property
    def bold(self):
        """Gets the bold of this DocxStyle.  # noqa: E501

        Style applies bold formatting  # noqa: E501

        :return: The bold of this DocxStyle.  # noqa: E501
        :rtype: bool
        """
        return self._bold

    @bold.setter
    def bold(self, bold):
        """Sets the bold of this DocxStyle.

        Style applies bold formatting  # noqa: E501

        :param bold: The bold of this DocxStyle.  # noqa: E501
        :type: bool
        """

        self._bold = bold

    @property
    def italic(self):
        """Gets the italic of this DocxStyle.  # noqa: E501

        Style applies italic formatting  # noqa: E501

        :return: The italic of this DocxStyle.  # noqa: E501
        :rtype: bool
        """
        return self._italic

    @italic.setter
    def italic(self, italic):
        """Sets the italic of this DocxStyle.

        Style applies italic formatting  # noqa: E501

        :param italic: The italic of this DocxStyle.  # noqa: E501
        :type: bool
        """

        self._italic = italic

    @property
    def underline(self):
        """Gets the underline of this DocxStyle.  # noqa: E501

        Style applies underline formatting  # noqa: E501

        :return: The underline of this DocxStyle.  # noqa: E501
        :rtype: bool
        """
        return self._underline

    @underline.setter
    def underline(self, underline):
        """Sets the underline of this DocxStyle.

        Style applies underline formatting  # noqa: E501

        :param underline: The underline of this DocxStyle.  # noqa: E501
        :type: bool
        """

        self._underline = underline

    @property
    def font_size(self):
        """Gets the font_size of this DocxStyle.  # noqa: E501

        Font size  # noqa: E501

        :return: The font_size of this DocxStyle.  # noqa: E501
        :rtype: str
        """
        return self._font_size

    @font_size.setter
    def font_size(self, font_size):
        """Sets the font_size of this DocxStyle.

        Font size  # noqa: E501

        :param font_size: The font_size of this DocxStyle.  # noqa: E501
        :type: str
        """

        self._font_size = font_size

    @property
    def font_family(self):
        """Gets the font_family of this DocxStyle.  # noqa: E501

        Font family  # noqa: E501

        :return: The font_family of this DocxStyle.  # noqa: E501
        :rtype: str
        """
        return self._font_family

    @font_family.setter
    def font_family(self, font_family):
        """Sets the font_family of this DocxStyle.

        Font family  # noqa: E501

        :param font_family: The font_family of this DocxStyle.  # noqa: E501
        :type: str
        """

        self._font_family = font_family

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
        if not isinstance(other, DocxStyle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other