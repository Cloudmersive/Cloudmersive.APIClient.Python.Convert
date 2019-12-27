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


class RemovePptxSlidesRequest(object):
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
        'start_delete_slide_number': 'int',
        'end_delete_slide_number': 'int'
    }

    attribute_map = {
        'input_file_bytes': 'InputFileBytes',
        'input_file_url': 'InputFileUrl',
        'start_delete_slide_number': 'StartDeleteSlideNumber',
        'end_delete_slide_number': 'EndDeleteSlideNumber'
    }

    def __init__(self, input_file_bytes=None, input_file_url=None, start_delete_slide_number=None, end_delete_slide_number=None):  # noqa: E501
        """RemovePptxSlidesRequest - a model defined in Swagger"""  # noqa: E501

        self._input_file_bytes = None
        self._input_file_url = None
        self._start_delete_slide_number = None
        self._end_delete_slide_number = None
        self.discriminator = None

        if input_file_bytes is not None:
            self.input_file_bytes = input_file_bytes
        if input_file_url is not None:
            self.input_file_url = input_file_url
        if start_delete_slide_number is not None:
            self.start_delete_slide_number = start_delete_slide_number
        if end_delete_slide_number is not None:
            self.end_delete_slide_number = end_delete_slide_number

    @property
    def input_file_bytes(self):
        """Gets the input_file_bytes of this RemovePptxSlidesRequest.  # noqa: E501

        Optional: Bytes of the input file to operate on  # noqa: E501

        :return: The input_file_bytes of this RemovePptxSlidesRequest.  # noqa: E501
        :rtype: str
        """
        return self._input_file_bytes

    @input_file_bytes.setter
    def input_file_bytes(self, input_file_bytes):
        """Sets the input_file_bytes of this RemovePptxSlidesRequest.

        Optional: Bytes of the input file to operate on  # noqa: E501

        :param input_file_bytes: The input_file_bytes of this RemovePptxSlidesRequest.  # noqa: E501
        :type: str
        """
        if input_file_bytes is not None and not re.search(r'^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', input_file_bytes):  # noqa: E501
            raise ValueError(r"Invalid value for `input_file_bytes`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._input_file_bytes = input_file_bytes

    @property
    def input_file_url(self):
        """Gets the input_file_url of this RemovePptxSlidesRequest.  # noqa: E501

        Optional: URL of a file to operate on as input.  This can be a public URL, or you can also use the begin-editing API to upload a document and pass in the secure URL result from that operation as the URL here (this URL is not public).  # noqa: E501

        :return: The input_file_url of this RemovePptxSlidesRequest.  # noqa: E501
        :rtype: str
        """
        return self._input_file_url

    @input_file_url.setter
    def input_file_url(self, input_file_url):
        """Sets the input_file_url of this RemovePptxSlidesRequest.

        Optional: URL of a file to operate on as input.  This can be a public URL, or you can also use the begin-editing API to upload a document and pass in the secure URL result from that operation as the URL here (this URL is not public).  # noqa: E501

        :param input_file_url: The input_file_url of this RemovePptxSlidesRequest.  # noqa: E501
        :type: str
        """

        self._input_file_url = input_file_url

    @property
    def start_delete_slide_number(self):
        """Gets the start_delete_slide_number of this RemovePptxSlidesRequest.  # noqa: E501

        Slide number (1-based) to start deleting slides; inclusive  # noqa: E501

        :return: The start_delete_slide_number of this RemovePptxSlidesRequest.  # noqa: E501
        :rtype: int
        """
        return self._start_delete_slide_number

    @start_delete_slide_number.setter
    def start_delete_slide_number(self, start_delete_slide_number):
        """Sets the start_delete_slide_number of this RemovePptxSlidesRequest.

        Slide number (1-based) to start deleting slides; inclusive  # noqa: E501

        :param start_delete_slide_number: The start_delete_slide_number of this RemovePptxSlidesRequest.  # noqa: E501
        :type: int
        """

        self._start_delete_slide_number = start_delete_slide_number

    @property
    def end_delete_slide_number(self):
        """Gets the end_delete_slide_number of this RemovePptxSlidesRequest.  # noqa: E501

        Slide number (1-based) to stop deleting slides; inclusive  # noqa: E501

        :return: The end_delete_slide_number of this RemovePptxSlidesRequest.  # noqa: E501
        :rtype: int
        """
        return self._end_delete_slide_number

    @end_delete_slide_number.setter
    def end_delete_slide_number(self, end_delete_slide_number):
        """Sets the end_delete_slide_number of this RemovePptxSlidesRequest.

        Slide number (1-based) to stop deleting slides; inclusive  # noqa: E501

        :param end_delete_slide_number: The end_delete_slide_number of this RemovePptxSlidesRequest.  # noqa: E501
        :type: int
        """

        self._end_delete_slide_number = end_delete_slide_number

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
        if issubclass(RemovePptxSlidesRequest, dict):
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
        if not isinstance(other, RemovePptxSlidesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
