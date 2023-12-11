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


class DocxTableTableFillMultiRequest(object):
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
        'input_file_url': 'str',
        'input_file_data': 'str',
        'tables_to_fill': 'list[DocxTableSingleTableFill]'
    }

    attribute_map = {
        'input_file_url': 'InputFileUrl',
        'input_file_data': 'InputFileData',
        'tables_to_fill': 'TablesToFill'
    }

    def __init__(self, input_file_url=None, input_file_data=None, tables_to_fill=None):  # noqa: E501
        """DocxTableTableFillMultiRequest - a model defined in Swagger"""  # noqa: E501

        self._input_file_url = None
        self._input_file_data = None
        self._tables_to_fill = None
        self.discriminator = None

        if input_file_url is not None:
            self.input_file_url = input_file_url
        if input_file_data is not None:
            self.input_file_data = input_file_data
        if tables_to_fill is not None:
            self.tables_to_fill = tables_to_fill

    @property
    def input_file_url(self):
        """Gets the input_file_url of this DocxTableTableFillMultiRequest.  # noqa: E501

        Optional; Input URL of the document; use BeginEditing to create this  # noqa: E501

        :return: The input_file_url of this DocxTableTableFillMultiRequest.  # noqa: E501
        :rtype: str
        """
        return self._input_file_url

    @input_file_url.setter
    def input_file_url(self, input_file_url):
        """Sets the input_file_url of this DocxTableTableFillMultiRequest.

        Optional; Input URL of the document; use BeginEditing to create this  # noqa: E501

        :param input_file_url: The input_file_url of this DocxTableTableFillMultiRequest.  # noqa: E501
        :type: str
        """

        self._input_file_url = input_file_url

    @property
    def input_file_data(self):
        """Gets the input_file_data of this DocxTableTableFillMultiRequest.  # noqa: E501

        Optional; Input Word Document file content for the operation  # noqa: E501

        :return: The input_file_data of this DocxTableTableFillMultiRequest.  # noqa: E501
        :rtype: str
        """
        return self._input_file_data

    @input_file_data.setter
    def input_file_data(self, input_file_data):
        """Sets the input_file_data of this DocxTableTableFillMultiRequest.

        Optional; Input Word Document file content for the operation  # noqa: E501

        :param input_file_data: The input_file_data of this DocxTableTableFillMultiRequest.  # noqa: E501
        :type: str
        """
        if input_file_data is not None and not re.search(r'^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', input_file_data):  # noqa: E501
            raise ValueError(r"Invalid value for `input_file_data`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._input_file_data = input_file_data

    @property
    def tables_to_fill(self):
        """Gets the tables_to_fill of this DocxTableTableFillMultiRequest.  # noqa: E501

        Tables and datasets to fill into the document  # noqa: E501

        :return: The tables_to_fill of this DocxTableTableFillMultiRequest.  # noqa: E501
        :rtype: list[DocxTableSingleTableFill]
        """
        return self._tables_to_fill

    @tables_to_fill.setter
    def tables_to_fill(self, tables_to_fill):
        """Sets the tables_to_fill of this DocxTableTableFillMultiRequest.

        Tables and datasets to fill into the document  # noqa: E501

        :param tables_to_fill: The tables_to_fill of this DocxTableTableFillMultiRequest.  # noqa: E501
        :type: list[DocxTableSingleTableFill]
        """

        self._tables_to_fill = tables_to_fill

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
        if issubclass(DocxTableTableFillMultiRequest, dict):
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
        if not isinstance(other, DocxTableTableFillMultiRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other