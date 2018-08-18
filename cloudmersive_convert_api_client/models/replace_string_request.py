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


class ReplaceStringRequest(object):
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
        'match_string': 'str',
        'replace_string': 'str',
        'match_case': 'bool'
    }

    attribute_map = {
        'input_file_bytes': 'InputFileBytes',
        'input_file_url': 'InputFileUrl',
        'match_string': 'MatchString',
        'replace_string': 'ReplaceString',
        'match_case': 'MatchCase'
    }

    def __init__(self, input_file_bytes=None, input_file_url=None, match_string=None, replace_string=None, match_case=None):  # noqa: E501
        """ReplaceStringRequest - a model defined in Swagger"""  # noqa: E501

        self._input_file_bytes = None
        self._input_file_url = None
        self._match_string = None
        self._replace_string = None
        self._match_case = None
        self.discriminator = None

        if input_file_bytes is not None:
            self.input_file_bytes = input_file_bytes
        if input_file_url is not None:
            self.input_file_url = input_file_url
        if match_string is not None:
            self.match_string = match_string
        if replace_string is not None:
            self.replace_string = replace_string
        if match_case is not None:
            self.match_case = match_case

    @property
    def input_file_bytes(self):
        """Gets the input_file_bytes of this ReplaceStringRequest.  # noqa: E501

        Optional: Bytes of the input file to operate on  # noqa: E501

        :return: The input_file_bytes of this ReplaceStringRequest.  # noqa: E501
        :rtype: str
        """
        return self._input_file_bytes

    @input_file_bytes.setter
    def input_file_bytes(self, input_file_bytes):
        """Sets the input_file_bytes of this ReplaceStringRequest.

        Optional: Bytes of the input file to operate on  # noqa: E501

        :param input_file_bytes: The input_file_bytes of this ReplaceStringRequest.  # noqa: E501
        :type: str
        """
        if input_file_bytes is not None and not re.search('^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', input_file_bytes):  # noqa: E501
            raise ValueError("Invalid value for `input_file_bytes`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._input_file_bytes = input_file_bytes

    @property
    def input_file_url(self):
        """Gets the input_file_url of this ReplaceStringRequest.  # noqa: E501

        Optional: URL of a file to operate on as input.  This can be a public URL, or you can also use the begin-editing API to upload a document and pass in the secure URL result from that operation as the URL here (this URL is not public).  # noqa: E501

        :return: The input_file_url of this ReplaceStringRequest.  # noqa: E501
        :rtype: str
        """
        return self._input_file_url

    @input_file_url.setter
    def input_file_url(self, input_file_url):
        """Sets the input_file_url of this ReplaceStringRequest.

        Optional: URL of a file to operate on as input.  This can be a public URL, or you can also use the begin-editing API to upload a document and pass in the secure URL result from that operation as the URL here (this URL is not public).  # noqa: E501

        :param input_file_url: The input_file_url of this ReplaceStringRequest.  # noqa: E501
        :type: str
        """

        self._input_file_url = input_file_url

    @property
    def match_string(self):
        """Gets the match_string of this ReplaceStringRequest.  # noqa: E501

        String to search for and match against, to be replaced  # noqa: E501

        :return: The match_string of this ReplaceStringRequest.  # noqa: E501
        :rtype: str
        """
        return self._match_string

    @match_string.setter
    def match_string(self, match_string):
        """Sets the match_string of this ReplaceStringRequest.

        String to search for and match against, to be replaced  # noqa: E501

        :param match_string: The match_string of this ReplaceStringRequest.  # noqa: E501
        :type: str
        """

        self._match_string = match_string

    @property
    def replace_string(self):
        """Gets the replace_string of this ReplaceStringRequest.  # noqa: E501

        String to replace the matched values with  # noqa: E501

        :return: The replace_string of this ReplaceStringRequest.  # noqa: E501
        :rtype: str
        """
        return self._replace_string

    @replace_string.setter
    def replace_string(self, replace_string):
        """Sets the replace_string of this ReplaceStringRequest.

        String to replace the matched values with  # noqa: E501

        :param replace_string: The replace_string of this ReplaceStringRequest.  # noqa: E501
        :type: str
        """

        self._replace_string = replace_string

    @property
    def match_case(self):
        """Gets the match_case of this ReplaceStringRequest.  # noqa: E501

        True if the case should be matched, false for case insensitive match  # noqa: E501

        :return: The match_case of this ReplaceStringRequest.  # noqa: E501
        :rtype: bool
        """
        return self._match_case

    @match_case.setter
    def match_case(self, match_case):
        """Sets the match_case of this ReplaceStringRequest.

        True if the case should be matched, false for case insensitive match  # noqa: E501

        :param match_case: The match_case of this ReplaceStringRequest.  # noqa: E501
        :type: bool
        """

        self._match_case = match_case

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
        if not isinstance(other, ReplaceStringRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
