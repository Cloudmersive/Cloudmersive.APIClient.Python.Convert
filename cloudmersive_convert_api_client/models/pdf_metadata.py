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


class PdfMetadata(object):
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
        'title': 'str',
        'keywords': 'str',
        'subject': 'str',
        'author': 'str',
        'creator': 'str',
        'date_modified': 'datetime',
        'date_created': 'datetime'
    }

    attribute_map = {
        'successful': 'Successful',
        'title': 'Title',
        'keywords': 'Keywords',
        'subject': 'Subject',
        'author': 'Author',
        'creator': 'Creator',
        'date_modified': 'DateModified',
        'date_created': 'DateCreated'
    }

    def __init__(self, successful=None, title=None, keywords=None, subject=None, author=None, creator=None, date_modified=None, date_created=None):  # noqa: E501
        """PdfMetadata - a model defined in Swagger"""  # noqa: E501

        self._successful = None
        self._title = None
        self._keywords = None
        self._subject = None
        self._author = None
        self._creator = None
        self._date_modified = None
        self._date_created = None
        self.discriminator = None

        if successful is not None:
            self.successful = successful
        if title is not None:
            self.title = title
        if keywords is not None:
            self.keywords = keywords
        if subject is not None:
            self.subject = subject
        if author is not None:
            self.author = author
        if creator is not None:
            self.creator = creator
        if date_modified is not None:
            self.date_modified = date_modified
        if date_created is not None:
            self.date_created = date_created

    @property
    def successful(self):
        """Gets the successful of this PdfMetadata.  # noqa: E501

        True if the operation was successful, false otherwise  # noqa: E501

        :return: The successful of this PdfMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._successful

    @successful.setter
    def successful(self, successful):
        """Sets the successful of this PdfMetadata.

        True if the operation was successful, false otherwise  # noqa: E501

        :param successful: The successful of this PdfMetadata.  # noqa: E501
        :type: bool
        """

        self._successful = successful

    @property
    def title(self):
        """Gets the title of this PdfMetadata.  # noqa: E501

        Title of the document  # noqa: E501

        :return: The title of this PdfMetadata.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this PdfMetadata.

        Title of the document  # noqa: E501

        :param title: The title of this PdfMetadata.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def keywords(self):
        """Gets the keywords of this PdfMetadata.  # noqa: E501

        Keywords of the document  # noqa: E501

        :return: The keywords of this PdfMetadata.  # noqa: E501
        :rtype: str
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this PdfMetadata.

        Keywords of the document  # noqa: E501

        :param keywords: The keywords of this PdfMetadata.  # noqa: E501
        :type: str
        """

        self._keywords = keywords

    @property
    def subject(self):
        """Gets the subject of this PdfMetadata.  # noqa: E501

        Subject of the document  # noqa: E501

        :return: The subject of this PdfMetadata.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this PdfMetadata.

        Subject of the document  # noqa: E501

        :param subject: The subject of this PdfMetadata.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def author(self):
        """Gets the author of this PdfMetadata.  # noqa: E501

        User name of the creator/author of the document, if available, null if not available  # noqa: E501

        :return: The author of this PdfMetadata.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this PdfMetadata.

        User name of the creator/author of the document, if available, null if not available  # noqa: E501

        :param author: The author of this PdfMetadata.  # noqa: E501
        :type: str
        """

        self._author = author

    @property
    def creator(self):
        """Gets the creator of this PdfMetadata.  # noqa: E501

        Creator of the document  # noqa: E501

        :return: The creator of this PdfMetadata.  # noqa: E501
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this PdfMetadata.

        Creator of the document  # noqa: E501

        :param creator: The creator of this PdfMetadata.  # noqa: E501
        :type: str
        """

        self._creator = creator

    @property
    def date_modified(self):
        """Gets the date_modified of this PdfMetadata.  # noqa: E501

        The timestamp that the document was last modified, if available, null if not available  # noqa: E501

        :return: The date_modified of this PdfMetadata.  # noqa: E501
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this PdfMetadata.

        The timestamp that the document was last modified, if available, null if not available  # noqa: E501

        :param date_modified: The date_modified of this PdfMetadata.  # noqa: E501
        :type: datetime
        """

        self._date_modified = date_modified

    @property
    def date_created(self):
        """Gets the date_created of this PdfMetadata.  # noqa: E501

        The timestamp that the document was created, if available, null if not available  # noqa: E501

        :return: The date_created of this PdfMetadata.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this PdfMetadata.

        The timestamp that the document was created, if available, null if not available  # noqa: E501

        :param date_created: The date_created of this PdfMetadata.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

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
        if issubclass(PdfMetadata, dict):
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
        if not isinstance(other, PdfMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
