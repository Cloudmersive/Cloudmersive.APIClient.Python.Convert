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


class AutodetectGetInfoResult(object):
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
        'detected_file_extension': 'str',
        'detected_mime_type': 'str',
        'page_count': 'int',
        'author': 'str',
        'date_modified': 'datetime',
        'alternate_file_type_candidates': 'list[AlternateFileFormatCandidate]'
    }

    attribute_map = {
        'successful': 'Successful',
        'detected_file_extension': 'DetectedFileExtension',
        'detected_mime_type': 'DetectedMimeType',
        'page_count': 'PageCount',
        'author': 'Author',
        'date_modified': 'DateModified',
        'alternate_file_type_candidates': 'AlternateFileTypeCandidates'
    }

    def __init__(self, successful=None, detected_file_extension=None, detected_mime_type=None, page_count=None, author=None, date_modified=None, alternate_file_type_candidates=None):  # noqa: E501
        """AutodetectGetInfoResult - a model defined in Swagger"""  # noqa: E501

        self._successful = None
        self._detected_file_extension = None
        self._detected_mime_type = None
        self._page_count = None
        self._author = None
        self._date_modified = None
        self._alternate_file_type_candidates = None
        self.discriminator = None

        if successful is not None:
            self.successful = successful
        if detected_file_extension is not None:
            self.detected_file_extension = detected_file_extension
        if detected_mime_type is not None:
            self.detected_mime_type = detected_mime_type
        if page_count is not None:
            self.page_count = page_count
        if author is not None:
            self.author = author
        if date_modified is not None:
            self.date_modified = date_modified
        if alternate_file_type_candidates is not None:
            self.alternate_file_type_candidates = alternate_file_type_candidates

    @property
    def successful(self):
        """Gets the successful of this AutodetectGetInfoResult.  # noqa: E501

        True if the operation was successful, false otherwise  # noqa: E501

        :return: The successful of this AutodetectGetInfoResult.  # noqa: E501
        :rtype: bool
        """
        return self._successful

    @successful.setter
    def successful(self, successful):
        """Sets the successful of this AutodetectGetInfoResult.

        True if the operation was successful, false otherwise  # noqa: E501

        :param successful: The successful of this AutodetectGetInfoResult.  # noqa: E501
        :type: bool
        """

        self._successful = successful

    @property
    def detected_file_extension(self):
        """Gets the detected_file_extension of this AutodetectGetInfoResult.  # noqa: E501

        Detected file extension of the file format, with a leading period  # noqa: E501

        :return: The detected_file_extension of this AutodetectGetInfoResult.  # noqa: E501
        :rtype: str
        """
        return self._detected_file_extension

    @detected_file_extension.setter
    def detected_file_extension(self, detected_file_extension):
        """Sets the detected_file_extension of this AutodetectGetInfoResult.

        Detected file extension of the file format, with a leading period  # noqa: E501

        :param detected_file_extension: The detected_file_extension of this AutodetectGetInfoResult.  # noqa: E501
        :type: str
        """

        self._detected_file_extension = detected_file_extension

    @property
    def detected_mime_type(self):
        """Gets the detected_mime_type of this AutodetectGetInfoResult.  # noqa: E501

        MIME type of this file extension  # noqa: E501

        :return: The detected_mime_type of this AutodetectGetInfoResult.  # noqa: E501
        :rtype: str
        """
        return self._detected_mime_type

    @detected_mime_type.setter
    def detected_mime_type(self, detected_mime_type):
        """Sets the detected_mime_type of this AutodetectGetInfoResult.

        MIME type of this file extension  # noqa: E501

        :param detected_mime_type: The detected_mime_type of this AutodetectGetInfoResult.  # noqa: E501
        :type: str
        """

        self._detected_mime_type = detected_mime_type

    @property
    def page_count(self):
        """Gets the page_count of this AutodetectGetInfoResult.  # noqa: E501

        Number of pages in a page-based document; for presentations, this is the number of slides and for a spreadsheet this is the number of worksheets.  Contains 0 when the page count cannot be determined, or if the concept of page count does not apply (e.g. for an image)  # noqa: E501

        :return: The page_count of this AutodetectGetInfoResult.  # noqa: E501
        :rtype: int
        """
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        """Sets the page_count of this AutodetectGetInfoResult.

        Number of pages in a page-based document; for presentations, this is the number of slides and for a spreadsheet this is the number of worksheets.  Contains 0 when the page count cannot be determined, or if the concept of page count does not apply (e.g. for an image)  # noqa: E501

        :param page_count: The page_count of this AutodetectGetInfoResult.  # noqa: E501
        :type: int
        """

        self._page_count = page_count

    @property
    def author(self):
        """Gets the author of this AutodetectGetInfoResult.  # noqa: E501

        User name of the creator/author of the document, if available, null if not available  # noqa: E501

        :return: The author of this AutodetectGetInfoResult.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this AutodetectGetInfoResult.

        User name of the creator/author of the document, if available, null if not available  # noqa: E501

        :param author: The author of this AutodetectGetInfoResult.  # noqa: E501
        :type: str
        """

        self._author = author

    @property
    def date_modified(self):
        """Gets the date_modified of this AutodetectGetInfoResult.  # noqa: E501

        The timestamp that the document was last modified, if available, null if not available  # noqa: E501

        :return: The date_modified of this AutodetectGetInfoResult.  # noqa: E501
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this AutodetectGetInfoResult.

        The timestamp that the document was last modified, if available, null if not available  # noqa: E501

        :param date_modified: The date_modified of this AutodetectGetInfoResult.  # noqa: E501
        :type: datetime
        """

        self._date_modified = date_modified

    @property
    def alternate_file_type_candidates(self):
        """Gets the alternate_file_type_candidates of this AutodetectGetInfoResult.  # noqa: E501

        Alternate file type options and their probability  # noqa: E501

        :return: The alternate_file_type_candidates of this AutodetectGetInfoResult.  # noqa: E501
        :rtype: list[AlternateFileFormatCandidate]
        """
        return self._alternate_file_type_candidates

    @alternate_file_type_candidates.setter
    def alternate_file_type_candidates(self, alternate_file_type_candidates):
        """Sets the alternate_file_type_candidates of this AutodetectGetInfoResult.

        Alternate file type options and their probability  # noqa: E501

        :param alternate_file_type_candidates: The alternate_file_type_candidates of this AutodetectGetInfoResult.  # noqa: E501
        :type: list[AlternateFileFormatCandidate]
        """

        self._alternate_file_type_candidates = alternate_file_type_candidates

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
        if issubclass(AutodetectGetInfoResult, dict):
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
        if not isinstance(other, AutodetectGetInfoResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
