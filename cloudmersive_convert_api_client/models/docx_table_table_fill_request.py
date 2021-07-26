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


class DocxTableTableFillRequest(object):
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
        'table_start_tag': 'str',
        'table_end_tag': 'str',
        'data_to_fill_in': 'list[DocxTableTableFillTableRow]'
    }

    attribute_map = {
        'input_file_url': 'InputFileUrl',
        'input_file_data': 'InputFileData',
        'table_start_tag': 'TableStartTag',
        'table_end_tag': 'TableEndTag',
        'data_to_fill_in': 'DataToFillIn'
    }

    def __init__(self, input_file_url=None, input_file_data=None, table_start_tag=None, table_end_tag=None, data_to_fill_in=None):  # noqa: E501
        """DocxTableTableFillRequest - a model defined in Swagger"""  # noqa: E501

        self._input_file_url = None
        self._input_file_data = None
        self._table_start_tag = None
        self._table_end_tag = None
        self._data_to_fill_in = None
        self.discriminator = None

        if input_file_url is not None:
            self.input_file_url = input_file_url
        if input_file_data is not None:
            self.input_file_data = input_file_data
        if table_start_tag is not None:
            self.table_start_tag = table_start_tag
        if table_end_tag is not None:
            self.table_end_tag = table_end_tag
        if data_to_fill_in is not None:
            self.data_to_fill_in = data_to_fill_in

    @property
    def input_file_url(self):
        """Gets the input_file_url of this DocxTableTableFillRequest.  # noqa: E501

        Optional; Input URL of the document; use BeginEditing to create this  # noqa: E501

        :return: The input_file_url of this DocxTableTableFillRequest.  # noqa: E501
        :rtype: str
        """
        return self._input_file_url

    @input_file_url.setter
    def input_file_url(self, input_file_url):
        """Sets the input_file_url of this DocxTableTableFillRequest.

        Optional; Input URL of the document; use BeginEditing to create this  # noqa: E501

        :param input_file_url: The input_file_url of this DocxTableTableFillRequest.  # noqa: E501
        :type: str
        """

        self._input_file_url = input_file_url

    @property
    def input_file_data(self):
        """Gets the input_file_data of this DocxTableTableFillRequest.  # noqa: E501

        Optional; Input Word Document file content for the operation  # noqa: E501

        :return: The input_file_data of this DocxTableTableFillRequest.  # noqa: E501
        :rtype: str
        """
        return self._input_file_data

    @input_file_data.setter
    def input_file_data(self, input_file_data):
        """Sets the input_file_data of this DocxTableTableFillRequest.

        Optional; Input Word Document file content for the operation  # noqa: E501

        :param input_file_data: The input_file_data of this DocxTableTableFillRequest.  # noqa: E501
        :type: str
        """
        if input_file_data is not None and not re.search(r'^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', input_file_data):  # noqa: E501
            raise ValueError(r"Invalid value for `input_file_data`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._input_file_data = input_file_data

    @property
    def table_start_tag(self):
        """Gets the table_start_tag of this DocxTableTableFillRequest.  # noqa: E501

        Start tag that delineates the beginning of the table  # noqa: E501

        :return: The table_start_tag of this DocxTableTableFillRequest.  # noqa: E501
        :rtype: str
        """
        return self._table_start_tag

    @table_start_tag.setter
    def table_start_tag(self, table_start_tag):
        """Sets the table_start_tag of this DocxTableTableFillRequest.

        Start tag that delineates the beginning of the table  # noqa: E501

        :param table_start_tag: The table_start_tag of this DocxTableTableFillRequest.  # noqa: E501
        :type: str
        """

        self._table_start_tag = table_start_tag

    @property
    def table_end_tag(self):
        """Gets the table_end_tag of this DocxTableTableFillRequest.  # noqa: E501

        End tag that delineates the end of the table  # noqa: E501

        :return: The table_end_tag of this DocxTableTableFillRequest.  # noqa: E501
        :rtype: str
        """
        return self._table_end_tag

    @table_end_tag.setter
    def table_end_tag(self, table_end_tag):
        """Sets the table_end_tag of this DocxTableTableFillRequest.

        End tag that delineates the end of the table  # noqa: E501

        :param table_end_tag: The table_end_tag of this DocxTableTableFillRequest.  # noqa: E501
        :type: str
        """

        self._table_end_tag = table_end_tag

    @property
    def data_to_fill_in(self):
        """Gets the data_to_fill_in of this DocxTableTableFillRequest.  # noqa: E501

        Data set to populate the table with  # noqa: E501

        :return: The data_to_fill_in of this DocxTableTableFillRequest.  # noqa: E501
        :rtype: list[DocxTableTableFillTableRow]
        """
        return self._data_to_fill_in

    @data_to_fill_in.setter
    def data_to_fill_in(self, data_to_fill_in):
        """Sets the data_to_fill_in of this DocxTableTableFillRequest.

        Data set to populate the table with  # noqa: E501

        :param data_to_fill_in: The data_to_fill_in of this DocxTableTableFillRequest.  # noqa: E501
        :type: list[DocxTableTableFillTableRow]
        """

        self._data_to_fill_in = data_to_fill_in

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
        if issubclass(DocxTableTableFillRequest, dict):
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
        if not isinstance(other, DocxTableTableFillRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
