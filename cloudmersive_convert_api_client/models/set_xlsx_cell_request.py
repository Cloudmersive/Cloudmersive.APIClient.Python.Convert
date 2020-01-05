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

from cloudmersive_convert_api_client.models.xlsx_spreadsheet_cell import XlsxSpreadsheetCell  # noqa: F401,E501
from cloudmersive_convert_api_client.models.xlsx_worksheet import XlsxWorksheet  # noqa: F401,E501


class SetXlsxCellRequest(object):
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
        'input_file_bytes': 'str',
        'input_file_url': 'str',
        'worksheet_to_update': 'XlsxWorksheet',
        'row_index': 'int',
        'cell_index': 'int',
        'cell_value': 'XlsxSpreadsheetCell'
    }

    attribute_map = {
        'input_file_bytes': 'InputFileBytes',
        'input_file_url': 'InputFileUrl',
        'worksheet_to_update': 'WorksheetToUpdate',
        'row_index': 'RowIndex',
        'cell_index': 'CellIndex',
        'cell_value': 'CellValue'
    }

    def __init__(self, input_file_bytes=None, input_file_url=None, worksheet_to_update=None, row_index=None, cell_index=None, cell_value=None):  # noqa: E501
        """SetXlsxCellRequest - a model defined in Swagger"""  # noqa: E501

        self._input_file_bytes = None
        self._input_file_url = None
        self._worksheet_to_update = None
        self._row_index = None
        self._cell_index = None
        self._cell_value = None
        self.discriminator = None

        if input_file_bytes is not None:
            self.input_file_bytes = input_file_bytes
        if input_file_url is not None:
            self.input_file_url = input_file_url
        if worksheet_to_update is not None:
            self.worksheet_to_update = worksheet_to_update
        if row_index is not None:
            self.row_index = row_index
        if cell_index is not None:
            self.cell_index = cell_index
        if cell_value is not None:
            self.cell_value = cell_value

    @property
    def input_file_bytes(self):
        """Gets the input_file_bytes of this SetXlsxCellRequest.  # noqa: E501

        Optional: Bytes of the input file to operate on  # noqa: E501

        :return: The input_file_bytes of this SetXlsxCellRequest.  # noqa: E501
        :rtype: str
        """
        return self._input_file_bytes

    @input_file_bytes.setter
    def input_file_bytes(self, input_file_bytes):
        """Sets the input_file_bytes of this SetXlsxCellRequest.

        Optional: Bytes of the input file to operate on  # noqa: E501

        :param input_file_bytes: The input_file_bytes of this SetXlsxCellRequest.  # noqa: E501
        :type: str
        """
        if input_file_bytes is not None and not re.search(r'^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', input_file_bytes):  # noqa: E501
            raise ValueError(r"Invalid value for `input_file_bytes`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._input_file_bytes = input_file_bytes

    @property
    def input_file_url(self):
        """Gets the input_file_url of this SetXlsxCellRequest.  # noqa: E501

        Optional: URL of a file to operate on as input.  This can be a public URL, or you can also use the begin-editing API to upload a document and pass in the secure URL result from that operation as the URL here (this URL is not public).  # noqa: E501

        :return: The input_file_url of this SetXlsxCellRequest.  # noqa: E501
        :rtype: str
        """
        return self._input_file_url

    @input_file_url.setter
    def input_file_url(self, input_file_url):
        """Sets the input_file_url of this SetXlsxCellRequest.

        Optional: URL of a file to operate on as input.  This can be a public URL, or you can also use the begin-editing API to upload a document and pass in the secure URL result from that operation as the URL here (this URL is not public).  # noqa: E501

        :param input_file_url: The input_file_url of this SetXlsxCellRequest.  # noqa: E501
        :type: str
        """

        self._input_file_url = input_file_url

    @property
    def worksheet_to_update(self):
        """Gets the worksheet_to_update of this SetXlsxCellRequest.  # noqa: E501

        Optional; Worksheet (tab) within the spreadsheet to update; leave blank to default to the first worksheet  # noqa: E501

        :return: The worksheet_to_update of this SetXlsxCellRequest.  # noqa: E501
        :rtype: XlsxWorksheet
        """
        return self._worksheet_to_update

    @worksheet_to_update.setter
    def worksheet_to_update(self, worksheet_to_update):
        """Sets the worksheet_to_update of this SetXlsxCellRequest.

        Optional; Worksheet (tab) within the spreadsheet to update; leave blank to default to the first worksheet  # noqa: E501

        :param worksheet_to_update: The worksheet_to_update of this SetXlsxCellRequest.  # noqa: E501
        :type: XlsxWorksheet
        """

        self._worksheet_to_update = worksheet_to_update

    @property
    def row_index(self):
        """Gets the row_index of this SetXlsxCellRequest.  # noqa: E501

        0-based index of the row, 0, 1, 2, ... to set  # noqa: E501

        :return: The row_index of this SetXlsxCellRequest.  # noqa: E501
        :rtype: int
        """
        return self._row_index

    @row_index.setter
    def row_index(self, row_index):
        """Sets the row_index of this SetXlsxCellRequest.

        0-based index of the row, 0, 1, 2, ... to set  # noqa: E501

        :param row_index: The row_index of this SetXlsxCellRequest.  # noqa: E501
        :type: int
        """

        self._row_index = row_index

    @property
    def cell_index(self):
        """Gets the cell_index of this SetXlsxCellRequest.  # noqa: E501

        0-based index of the cell, 0, 1, 2, ... in the row to set  # noqa: E501

        :return: The cell_index of this SetXlsxCellRequest.  # noqa: E501
        :rtype: int
        """
        return self._cell_index

    @cell_index.setter
    def cell_index(self, cell_index):
        """Sets the cell_index of this SetXlsxCellRequest.

        0-based index of the cell, 0, 1, 2, ... in the row to set  # noqa: E501

        :param cell_index: The cell_index of this SetXlsxCellRequest.  # noqa: E501
        :type: int
        """

        self._cell_index = cell_index

    @property
    def cell_value(self):
        """Gets the cell_value of this SetXlsxCellRequest.  # noqa: E501

        New Cell value to update/overwrite into the Excel XLSX spreadsheet  # noqa: E501

        :return: The cell_value of this SetXlsxCellRequest.  # noqa: E501
        :rtype: XlsxSpreadsheetCell
        """
        return self._cell_value

    @cell_value.setter
    def cell_value(self, cell_value):
        """Sets the cell_value of this SetXlsxCellRequest.

        New Cell value to update/overwrite into the Excel XLSX spreadsheet  # noqa: E501

        :param cell_value: The cell_value of this SetXlsxCellRequest.  # noqa: E501
        :type: XlsxSpreadsheetCell
        """

        self._cell_value = cell_value

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
        if issubclass(SetXlsxCellRequest, dict):
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
        if not isinstance(other, SetXlsxCellRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
