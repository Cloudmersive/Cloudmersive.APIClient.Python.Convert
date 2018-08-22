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

from cloudmersive_convert_api_client.models.docx_paragraph import DocxParagraph  # noqa: F401,E501
from cloudmersive_convert_api_client.models.docx_section import DocxSection  # noqa: F401,E501


class DocxHeader(object):
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
        'paragraphs': 'list[DocxParagraph]',
        'sections_with_header': 'list[DocxSection]'
    }

    attribute_map = {
        'paragraphs': 'Paragraphs',
        'sections_with_header': 'SectionsWithHeader'
    }

    def __init__(self, paragraphs=None, sections_with_header=None):  # noqa: E501
        """DocxHeader - a model defined in Swagger"""  # noqa: E501

        self._paragraphs = None
        self._sections_with_header = None
        self.discriminator = None

        if paragraphs is not None:
            self.paragraphs = paragraphs
        if sections_with_header is not None:
            self.sections_with_header = sections_with_header

    @property
    def paragraphs(self):
        """Gets the paragraphs of this DocxHeader.  # noqa: E501

        Paragraphs in this header  # noqa: E501

        :return: The paragraphs of this DocxHeader.  # noqa: E501
        :rtype: list[DocxParagraph]
        """
        return self._paragraphs

    @paragraphs.setter
    def paragraphs(self, paragraphs):
        """Sets the paragraphs of this DocxHeader.

        Paragraphs in this header  # noqa: E501

        :param paragraphs: The paragraphs of this DocxHeader.  # noqa: E501
        :type: list[DocxParagraph]
        """

        self._paragraphs = paragraphs

    @property
    def sections_with_header(self):
        """Gets the sections_with_header of this DocxHeader.  # noqa: E501

        Sections that the header is applied to  # noqa: E501

        :return: The sections_with_header of this DocxHeader.  # noqa: E501
        :rtype: list[DocxSection]
        """
        return self._sections_with_header

    @sections_with_header.setter
    def sections_with_header(self, sections_with_header):
        """Sets the sections_with_header of this DocxHeader.

        Sections that the header is applied to  # noqa: E501

        :param sections_with_header: The sections_with_header of this DocxHeader.  # noqa: E501
        :type: list[DocxSection]
        """

        self._sections_with_header = sections_with_header

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
        if not isinstance(other, DocxHeader):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other