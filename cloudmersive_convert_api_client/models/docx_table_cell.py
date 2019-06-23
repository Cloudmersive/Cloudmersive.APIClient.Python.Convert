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


class DocxTableCell(object):
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
        'cell_index': 'int',
        'path': 'str',
        'paragraphs': 'list[DocxParagraph]',
        'cell_shading_color': 'str',
        'cell_shading_fill': 'str',
        'cell_shading_pattern': 'str',
        'cell_width_mode': 'str',
        'cell_width': 'str'
    }

    attribute_map = {
        'cell_index': 'CellIndex',
        'path': 'Path',
        'paragraphs': 'Paragraphs',
        'cell_shading_color': 'CellShadingColor',
        'cell_shading_fill': 'CellShadingFill',
        'cell_shading_pattern': 'CellShadingPattern',
        'cell_width_mode': 'CellWidthMode',
        'cell_width': 'CellWidth'
    }

    def __init__(self, cell_index=None, path=None, paragraphs=None, cell_shading_color=None, cell_shading_fill=None, cell_shading_pattern=None, cell_width_mode=None, cell_width=None):  # noqa: E501
        """DocxTableCell - a model defined in Swagger"""  # noqa: E501

        self._cell_index = None
        self._path = None
        self._paragraphs = None
        self._cell_shading_color = None
        self._cell_shading_fill = None
        self._cell_shading_pattern = None
        self._cell_width_mode = None
        self._cell_width = None
        self.discriminator = None

        if cell_index is not None:
            self.cell_index = cell_index
        if path is not None:
            self.path = path
        if paragraphs is not None:
            self.paragraphs = paragraphs
        if cell_shading_color is not None:
            self.cell_shading_color = cell_shading_color
        if cell_shading_fill is not None:
            self.cell_shading_fill = cell_shading_fill
        if cell_shading_pattern is not None:
            self.cell_shading_pattern = cell_shading_pattern
        if cell_width_mode is not None:
            self.cell_width_mode = cell_width_mode
        if cell_width is not None:
            self.cell_width = cell_width

    @property
    def cell_index(self):
        """Gets the cell_index of this DocxTableCell.  # noqa: E501

        The index of the cell, 0-based  # noqa: E501

        :return: The cell_index of this DocxTableCell.  # noqa: E501
        :rtype: int
        """
        return self._cell_index

    @cell_index.setter
    def cell_index(self, cell_index):
        """Sets the cell_index of this DocxTableCell.

        The index of the cell, 0-based  # noqa: E501

        :param cell_index: The cell_index of this DocxTableCell.  # noqa: E501
        :type: int
        """

        self._cell_index = cell_index

    @property
    def path(self):
        """Gets the path of this DocxTableCell.  # noqa: E501

        The Path of the location of this object; leave blank for new tables  # noqa: E501

        :return: The path of this DocxTableCell.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this DocxTableCell.

        The Path of the location of this object; leave blank for new tables  # noqa: E501

        :param path: The path of this DocxTableCell.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def paragraphs(self):
        """Gets the paragraphs of this DocxTableCell.  # noqa: E501

        Paragraphs inside the cell; this is where the contents of the cell are stored  # noqa: E501

        :return: The paragraphs of this DocxTableCell.  # noqa: E501
        :rtype: list[DocxParagraph]
        """
        return self._paragraphs

    @paragraphs.setter
    def paragraphs(self, paragraphs):
        """Sets the paragraphs of this DocxTableCell.

        Paragraphs inside the cell; this is where the contents of the cell are stored  # noqa: E501

        :param paragraphs: The paragraphs of this DocxTableCell.  # noqa: E501
        :type: list[DocxParagraph]
        """

        self._paragraphs = paragraphs

    @property
    def cell_shading_color(self):
        """Gets the cell_shading_color of this DocxTableCell.  # noqa: E501

        Color of the cell shading  # noqa: E501

        :return: The cell_shading_color of this DocxTableCell.  # noqa: E501
        :rtype: str
        """
        return self._cell_shading_color

    @cell_shading_color.setter
    def cell_shading_color(self, cell_shading_color):
        """Sets the cell_shading_color of this DocxTableCell.

        Color of the cell shading  # noqa: E501

        :param cell_shading_color: The cell_shading_color of this DocxTableCell.  # noqa: E501
        :type: str
        """

        self._cell_shading_color = cell_shading_color

    @property
    def cell_shading_fill(self):
        """Gets the cell_shading_fill of this DocxTableCell.  # noqa: E501

        Fill of the cell shading  # noqa: E501

        :return: The cell_shading_fill of this DocxTableCell.  # noqa: E501
        :rtype: str
        """
        return self._cell_shading_fill

    @cell_shading_fill.setter
    def cell_shading_fill(self, cell_shading_fill):
        """Sets the cell_shading_fill of this DocxTableCell.

        Fill of the cell shading  # noqa: E501

        :param cell_shading_fill: The cell_shading_fill of this DocxTableCell.  # noqa: E501
        :type: str
        """

        self._cell_shading_fill = cell_shading_fill

    @property
    def cell_shading_pattern(self):
        """Gets the cell_shading_pattern of this DocxTableCell.  # noqa: E501

        Pattern of the cell shading  # noqa: E501

        :return: The cell_shading_pattern of this DocxTableCell.  # noqa: E501
        :rtype: str
        """
        return self._cell_shading_pattern

    @cell_shading_pattern.setter
    def cell_shading_pattern(self, cell_shading_pattern):
        """Sets the cell_shading_pattern of this DocxTableCell.

        Pattern of the cell shading  # noqa: E501

        :param cell_shading_pattern: The cell_shading_pattern of this DocxTableCell.  # noqa: E501
        :type: str
        """

        self._cell_shading_pattern = cell_shading_pattern

    @property
    def cell_width_mode(self):
        """Gets the cell_width_mode of this DocxTableCell.  # noqa: E501

        Width mode of the cell; can be auto (for automatic) or manual  # noqa: E501

        :return: The cell_width_mode of this DocxTableCell.  # noqa: E501
        :rtype: str
        """
        return self._cell_width_mode

    @cell_width_mode.setter
    def cell_width_mode(self, cell_width_mode):
        """Sets the cell_width_mode of this DocxTableCell.

        Width mode of the cell; can be auto (for automatic) or manual  # noqa: E501

        :param cell_width_mode: The cell_width_mode of this DocxTableCell.  # noqa: E501
        :type: str
        """

        self._cell_width_mode = cell_width_mode

    @property
    def cell_width(self):
        """Gets the cell_width of this DocxTableCell.  # noqa: E501

        Width of the cell  # noqa: E501

        :return: The cell_width of this DocxTableCell.  # noqa: E501
        :rtype: str
        """
        return self._cell_width

    @cell_width.setter
    def cell_width(self, cell_width):
        """Sets the cell_width of this DocxTableCell.

        Width of the cell  # noqa: E501

        :param cell_width: The cell_width of this DocxTableCell.  # noqa: E501
        :type: str
        """

        self._cell_width = cell_width

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
        if issubclass(DocxTableCell, dict):
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
        if not isinstance(other, DocxTableCell):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
