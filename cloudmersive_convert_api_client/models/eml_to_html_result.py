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

from cloudmersive_convert_api_client.models.eml_attachment import EmlAttachment  # noqa: F401,E501


class EmlToHtmlResult(object):
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
        'content': 'str',
        'body': 'str',
        '_from': 'str',
        'to': 'str',
        'cc': 'str',
        'bcc': 'str',
        'received_time': 'str',
        'subject': 'str',
        'organization': 'str',
        'attachments': 'list[EmlAttachment]'
    }

    attribute_map = {
        'successful': 'Successful',
        'content': 'Content',
        'body': 'Body',
        '_from': 'From',
        'to': 'To',
        'cc': 'Cc',
        'bcc': 'Bcc',
        'received_time': 'ReceivedTime',
        'subject': 'Subject',
        'organization': 'Organization',
        'attachments': 'Attachments'
    }

    def __init__(self, successful=None, content=None, body=None, _from=None, to=None, cc=None, bcc=None, received_time=None, subject=None, organization=None, attachments=None):  # noqa: E501
        """EmlToHtmlResult - a model defined in Swagger"""  # noqa: E501

        self._successful = None
        self._content = None
        self._body = None
        self.__from = None
        self._to = None
        self._cc = None
        self._bcc = None
        self._received_time = None
        self._subject = None
        self._organization = None
        self._attachments = None
        self.discriminator = None

        if successful is not None:
            self.successful = successful
        if content is not None:
            self.content = content
        if body is not None:
            self.body = body
        if _from is not None:
            self._from = _from
        if to is not None:
            self.to = to
        if cc is not None:
            self.cc = cc
        if bcc is not None:
            self.bcc = bcc
        if received_time is not None:
            self.received_time = received_time
        if subject is not None:
            self.subject = subject
        if organization is not None:
            self.organization = organization
        if attachments is not None:
            self.attachments = attachments

    @property
    def successful(self):
        """Gets the successful of this EmlToHtmlResult.  # noqa: E501

        True if the operation was successful, false otherwise  # noqa: E501

        :return: The successful of this EmlToHtmlResult.  # noqa: E501
        :rtype: bool
        """
        return self._successful

    @successful.setter
    def successful(self, successful):
        """Sets the successful of this EmlToHtmlResult.

        True if the operation was successful, false otherwise  # noqa: E501

        :param successful: The successful of this EmlToHtmlResult.  # noqa: E501
        :type: bool
        """

        self._successful = successful

    @property
    def content(self):
        """Gets the content of this EmlToHtmlResult.  # noqa: E501

        An HTML string version of the EML file  # noqa: E501

        :return: The content of this EmlToHtmlResult.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this EmlToHtmlResult.

        An HTML string version of the EML file  # noqa: E501

        :param content: The content of this EmlToHtmlResult.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def body(self):
        """Gets the body of this EmlToHtmlResult.  # noqa: E501

        The main body of the EML file's email as an HTML string  # noqa: E501

        :return: The body of this EmlToHtmlResult.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this EmlToHtmlResult.

        The main body of the EML file's email as an HTML string  # noqa: E501

        :param body: The body of this EmlToHtmlResult.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def _from(self):
        """Gets the _from of this EmlToHtmlResult.  # noqa: E501

        The From sender of the EML file's email  # noqa: E501

        :return: The _from of this EmlToHtmlResult.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this EmlToHtmlResult.

        The From sender of the EML file's email  # noqa: E501

        :param _from: The _from of this EmlToHtmlResult.  # noqa: E501
        :type: str
        """

        self.__from = _from

    @property
    def to(self):
        """Gets the to of this EmlToHtmlResult.  # noqa: E501

        The To recipients of the EML file's email  # noqa: E501

        :return: The to of this EmlToHtmlResult.  # noqa: E501
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this EmlToHtmlResult.

        The To recipients of the EML file's email  # noqa: E501

        :param to: The to of this EmlToHtmlResult.  # noqa: E501
        :type: str
        """

        self._to = to

    @property
    def cc(self):
        """Gets the cc of this EmlToHtmlResult.  # noqa: E501

        The CC recipients of the EML file's email  # noqa: E501

        :return: The cc of this EmlToHtmlResult.  # noqa: E501
        :rtype: str
        """
        return self._cc

    @cc.setter
    def cc(self, cc):
        """Sets the cc of this EmlToHtmlResult.

        The CC recipients of the EML file's email  # noqa: E501

        :param cc: The cc of this EmlToHtmlResult.  # noqa: E501
        :type: str
        """

        self._cc = cc

    @property
    def bcc(self):
        """Gets the bcc of this EmlToHtmlResult.  # noqa: E501

        The BCC recipients of the EML file's email  # noqa: E501

        :return: The bcc of this EmlToHtmlResult.  # noqa: E501
        :rtype: str
        """
        return self._bcc

    @bcc.setter
    def bcc(self, bcc):
        """Sets the bcc of this EmlToHtmlResult.

        The BCC recipients of the EML file's email  # noqa: E501

        :param bcc: The bcc of this EmlToHtmlResult.  # noqa: E501
        :type: str
        """

        self._bcc = bcc

    @property
    def received_time(self):
        """Gets the received_time of this EmlToHtmlResult.  # noqa: E501

        The time that the EML file's email was received  # noqa: E501

        :return: The received_time of this EmlToHtmlResult.  # noqa: E501
        :rtype: str
        """
        return self._received_time

    @received_time.setter
    def received_time(self, received_time):
        """Sets the received_time of this EmlToHtmlResult.

        The time that the EML file's email was received  # noqa: E501

        :param received_time: The received_time of this EmlToHtmlResult.  # noqa: E501
        :type: str
        """

        self._received_time = received_time

    @property
    def subject(self):
        """Gets the subject of this EmlToHtmlResult.  # noqa: E501

        The subject of the EML file's email  # noqa: E501

        :return: The subject of this EmlToHtmlResult.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this EmlToHtmlResult.

        The subject of the EML file's email  # noqa: E501

        :param subject: The subject of this EmlToHtmlResult.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def organization(self):
        """Gets the organization of this EmlToHtmlResult.  # noqa: E501

        The Organization of the EML file's email  # noqa: E501

        :return: The organization of this EmlToHtmlResult.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this EmlToHtmlResult.

        The Organization of the EML file's email  # noqa: E501

        :param organization: The organization of this EmlToHtmlResult.  # noqa: E501
        :type: str
        """

        self._organization = organization

    @property
    def attachments(self):
        """Gets the attachments of this EmlToHtmlResult.  # noqa: E501

        List of all attachments for the EML file  # noqa: E501

        :return: The attachments of this EmlToHtmlResult.  # noqa: E501
        :rtype: list[EmlAttachment]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this EmlToHtmlResult.

        List of all attachments for the EML file  # noqa: E501

        :param attachments: The attachments of this EmlToHtmlResult.  # noqa: E501
        :type: list[EmlAttachment]
        """

        self._attachments = attachments

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
        if issubclass(EmlToHtmlResult, dict):
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
        if not isinstance(other, EmlToHtmlResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
