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


class GetImageInfoResult(object):
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
        'color_space': 'str',
        'color_type': 'str',
        'width': 'int',
        'height': 'int',
        'compression_level': 'int',
        'image_hash_signature': 'str',
        'has_transparency': 'bool',
        'mime_type': 'str',
        'image_format': 'str',
        'dpi_unit': 'str',
        'dpi': 'float',
        'color_count': 'int',
        'bit_depth': 'int',
        'comment': 'str',
        'exif_profile_name': 'str',
        'exif_values': 'list[ExifValue]'
    }

    attribute_map = {
        'successful': 'Successful',
        'color_space': 'ColorSpace',
        'color_type': 'ColorType',
        'width': 'Width',
        'height': 'Height',
        'compression_level': 'CompressionLevel',
        'image_hash_signature': 'ImageHashSignature',
        'has_transparency': 'HasTransparency',
        'mime_type': 'MimeType',
        'image_format': 'ImageFormat',
        'dpi_unit': 'DPIUnit',
        'dpi': 'DPI',
        'color_count': 'ColorCount',
        'bit_depth': 'BitDepth',
        'comment': 'Comment',
        'exif_profile_name': 'ExifProfileName',
        'exif_values': 'ExifValues'
    }

    def __init__(self, successful=None, color_space=None, color_type=None, width=None, height=None, compression_level=None, image_hash_signature=None, has_transparency=None, mime_type=None, image_format=None, dpi_unit=None, dpi=None, color_count=None, bit_depth=None, comment=None, exif_profile_name=None, exif_values=None):  # noqa: E501
        """GetImageInfoResult - a model defined in Swagger"""  # noqa: E501

        self._successful = None
        self._color_space = None
        self._color_type = None
        self._width = None
        self._height = None
        self._compression_level = None
        self._image_hash_signature = None
        self._has_transparency = None
        self._mime_type = None
        self._image_format = None
        self._dpi_unit = None
        self._dpi = None
        self._color_count = None
        self._bit_depth = None
        self._comment = None
        self._exif_profile_name = None
        self._exif_values = None
        self.discriminator = None

        if successful is not None:
            self.successful = successful
        if color_space is not None:
            self.color_space = color_space
        if color_type is not None:
            self.color_type = color_type
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if compression_level is not None:
            self.compression_level = compression_level
        if image_hash_signature is not None:
            self.image_hash_signature = image_hash_signature
        if has_transparency is not None:
            self.has_transparency = has_transparency
        if mime_type is not None:
            self.mime_type = mime_type
        if image_format is not None:
            self.image_format = image_format
        if dpi_unit is not None:
            self.dpi_unit = dpi_unit
        if dpi is not None:
            self.dpi = dpi
        if color_count is not None:
            self.color_count = color_count
        if bit_depth is not None:
            self.bit_depth = bit_depth
        if comment is not None:
            self.comment = comment
        if exif_profile_name is not None:
            self.exif_profile_name = exif_profile_name
        if exif_values is not None:
            self.exif_values = exif_values

    @property
    def successful(self):
        """Gets the successful of this GetImageInfoResult.  # noqa: E501


        :return: The successful of this GetImageInfoResult.  # noqa: E501
        :rtype: bool
        """
        return self._successful

    @successful.setter
    def successful(self, successful):
        """Sets the successful of this GetImageInfoResult.


        :param successful: The successful of this GetImageInfoResult.  # noqa: E501
        :type: bool
        """

        self._successful = successful

    @property
    def color_space(self):
        """Gets the color_space of this GetImageInfoResult.  # noqa: E501

        Color space of the image  # noqa: E501

        :return: The color_space of this GetImageInfoResult.  # noqa: E501
        :rtype: str
        """
        return self._color_space

    @color_space.setter
    def color_space(self, color_space):
        """Sets the color_space of this GetImageInfoResult.

        Color space of the image  # noqa: E501

        :param color_space: The color_space of this GetImageInfoResult.  # noqa: E501
        :type: str
        """

        self._color_space = color_space

    @property
    def color_type(self):
        """Gets the color_type of this GetImageInfoResult.  # noqa: E501

        Color type of the image  # noqa: E501

        :return: The color_type of this GetImageInfoResult.  # noqa: E501
        :rtype: str
        """
        return self._color_type

    @color_type.setter
    def color_type(self, color_type):
        """Sets the color_type of this GetImageInfoResult.

        Color type of the image  # noqa: E501

        :param color_type: The color_type of this GetImageInfoResult.  # noqa: E501
        :type: str
        """

        self._color_type = color_type

    @property
    def width(self):
        """Gets the width of this GetImageInfoResult.  # noqa: E501

        Width in pixels of the image  # noqa: E501

        :return: The width of this GetImageInfoResult.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this GetImageInfoResult.

        Width in pixels of the image  # noqa: E501

        :param width: The width of this GetImageInfoResult.  # noqa: E501
        :type: int
        """

        self._width = width

    @property
    def height(self):
        """Gets the height of this GetImageInfoResult.  # noqa: E501

        Height in pixels of the image  # noqa: E501

        :return: The height of this GetImageInfoResult.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this GetImageInfoResult.

        Height in pixels of the image  # noqa: E501

        :param height: The height of this GetImageInfoResult.  # noqa: E501
        :type: int
        """

        self._height = height

    @property
    def compression_level(self):
        """Gets the compression_level of this GetImageInfoResult.  # noqa: E501

        Compression level value from 0 (lowest quality) to 100 (highest quality)  # noqa: E501

        :return: The compression_level of this GetImageInfoResult.  # noqa: E501
        :rtype: int
        """
        return self._compression_level

    @compression_level.setter
    def compression_level(self, compression_level):
        """Sets the compression_level of this GetImageInfoResult.

        Compression level value from 0 (lowest quality) to 100 (highest quality)  # noqa: E501

        :param compression_level: The compression_level of this GetImageInfoResult.  # noqa: E501
        :type: int
        """

        self._compression_level = compression_level

    @property
    def image_hash_signature(self):
        """Gets the image_hash_signature of this GetImageInfoResult.  # noqa: E501

        SHA256 hash signature of the image  # noqa: E501

        :return: The image_hash_signature of this GetImageInfoResult.  # noqa: E501
        :rtype: str
        """
        return self._image_hash_signature

    @image_hash_signature.setter
    def image_hash_signature(self, image_hash_signature):
        """Sets the image_hash_signature of this GetImageInfoResult.

        SHA256 hash signature of the image  # noqa: E501

        :param image_hash_signature: The image_hash_signature of this GetImageInfoResult.  # noqa: E501
        :type: str
        """

        self._image_hash_signature = image_hash_signature

    @property
    def has_transparency(self):
        """Gets the has_transparency of this GetImageInfoResult.  # noqa: E501

        True if the image contains transparency, otherwise false  # noqa: E501

        :return: The has_transparency of this GetImageInfoResult.  # noqa: E501
        :rtype: bool
        """
        return self._has_transparency

    @has_transparency.setter
    def has_transparency(self, has_transparency):
        """Sets the has_transparency of this GetImageInfoResult.

        True if the image contains transparency, otherwise false  # noqa: E501

        :param has_transparency: The has_transparency of this GetImageInfoResult.  # noqa: E501
        :type: bool
        """

        self._has_transparency = has_transparency

    @property
    def mime_type(self):
        """Gets the mime_type of this GetImageInfoResult.  # noqa: E501

        MIME type of the image format  # noqa: E501

        :return: The mime_type of this GetImageInfoResult.  # noqa: E501
        :rtype: str
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        """Sets the mime_type of this GetImageInfoResult.

        MIME type of the image format  # noqa: E501

        :param mime_type: The mime_type of this GetImageInfoResult.  # noqa: E501
        :type: str
        """

        self._mime_type = mime_type

    @property
    def image_format(self):
        """Gets the image_format of this GetImageInfoResult.  # noqa: E501

        Image format  # noqa: E501

        :return: The image_format of this GetImageInfoResult.  # noqa: E501
        :rtype: str
        """
        return self._image_format

    @image_format.setter
    def image_format(self, image_format):
        """Sets the image_format of this GetImageInfoResult.

        Image format  # noqa: E501

        :param image_format: The image_format of this GetImageInfoResult.  # noqa: E501
        :type: str
        """

        self._image_format = image_format

    @property
    def dpi_unit(self):
        """Gets the dpi_unit of this GetImageInfoResult.  # noqa: E501

        Units of the DPI measurement; can be either in Inches or Centimeters  # noqa: E501

        :return: The dpi_unit of this GetImageInfoResult.  # noqa: E501
        :rtype: str
        """
        return self._dpi_unit

    @dpi_unit.setter
    def dpi_unit(self, dpi_unit):
        """Sets the dpi_unit of this GetImageInfoResult.

        Units of the DPI measurement; can be either in Inches or Centimeters  # noqa: E501

        :param dpi_unit: The dpi_unit of this GetImageInfoResult.  # noqa: E501
        :type: str
        """

        self._dpi_unit = dpi_unit

    @property
    def dpi(self):
        """Gets the dpi of this GetImageInfoResult.  # noqa: E501

        DPI (pixels per unit, e.g. pixels per inch) of the image  # noqa: E501

        :return: The dpi of this GetImageInfoResult.  # noqa: E501
        :rtype: float
        """
        return self._dpi

    @dpi.setter
    def dpi(self, dpi):
        """Sets the dpi of this GetImageInfoResult.

        DPI (pixels per unit, e.g. pixels per inch) of the image  # noqa: E501

        :param dpi: The dpi of this GetImageInfoResult.  # noqa: E501
        :type: float
        """

        self._dpi = dpi

    @property
    def color_count(self):
        """Gets the color_count of this GetImageInfoResult.  # noqa: E501

        Unique colors in the image  # noqa: E501

        :return: The color_count of this GetImageInfoResult.  # noqa: E501
        :rtype: int
        """
        return self._color_count

    @color_count.setter
    def color_count(self, color_count):
        """Sets the color_count of this GetImageInfoResult.

        Unique colors in the image  # noqa: E501

        :param color_count: The color_count of this GetImageInfoResult.  # noqa: E501
        :type: int
        """

        self._color_count = color_count

    @property
    def bit_depth(self):
        """Gets the bit_depth of this GetImageInfoResult.  # noqa: E501

        Bit depth of the image  # noqa: E501

        :return: The bit_depth of this GetImageInfoResult.  # noqa: E501
        :rtype: int
        """
        return self._bit_depth

    @bit_depth.setter
    def bit_depth(self, bit_depth):
        """Sets the bit_depth of this GetImageInfoResult.

        Bit depth of the image  # noqa: E501

        :param bit_depth: The bit_depth of this GetImageInfoResult.  # noqa: E501
        :type: int
        """

        self._bit_depth = bit_depth

    @property
    def comment(self):
        """Gets the comment of this GetImageInfoResult.  # noqa: E501

        Comment string in the image  # noqa: E501

        :return: The comment of this GetImageInfoResult.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this GetImageInfoResult.

        Comment string in the image  # noqa: E501

        :param comment: The comment of this GetImageInfoResult.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def exif_profile_name(self):
        """Gets the exif_profile_name of this GetImageInfoResult.  # noqa: E501

        Name of the EXIF profile used  # noqa: E501

        :return: The exif_profile_name of this GetImageInfoResult.  # noqa: E501
        :rtype: str
        """
        return self._exif_profile_name

    @exif_profile_name.setter
    def exif_profile_name(self, exif_profile_name):
        """Sets the exif_profile_name of this GetImageInfoResult.

        Name of the EXIF profile used  # noqa: E501

        :param exif_profile_name: The exif_profile_name of this GetImageInfoResult.  # noqa: E501
        :type: str
        """

        self._exif_profile_name = exif_profile_name

    @property
    def exif_values(self):
        """Gets the exif_values of this GetImageInfoResult.  # noqa: E501

        EXIF tags and values embedded in the image  # noqa: E501

        :return: The exif_values of this GetImageInfoResult.  # noqa: E501
        :rtype: list[ExifValue]
        """
        return self._exif_values

    @exif_values.setter
    def exif_values(self, exif_values):
        """Sets the exif_values of this GetImageInfoResult.

        EXIF tags and values embedded in the image  # noqa: E501

        :param exif_values: The exif_values of this GetImageInfoResult.  # noqa: E501
        :type: list[ExifValue]
        """

        self._exif_values = exif_values

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
        if issubclass(GetImageInfoResult, dict):
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
        if not isinstance(other, GetImageInfoResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
