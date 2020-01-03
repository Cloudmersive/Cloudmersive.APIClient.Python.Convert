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


class PdfAnnotation(object):
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
        'title': 'str',
        'annotation_type': 'str',
        'page_number': 'int',
        'annotation_index': 'int',
        'subject': 'str',
        'text_contents': 'str',
        'creation_date': 'datetime',
        'modified_date': 'datetime',
        'left_x': 'float',
        'top_y': 'float',
        'width': 'float',
        'height': 'float'
    }

    attribute_map = {
        'title': 'Title',
        'annotation_type': 'AnnotationType',
        'page_number': 'PageNumber',
        'annotation_index': 'AnnotationIndex',
        'subject': 'Subject',
        'text_contents': 'TextContents',
        'creation_date': 'CreationDate',
        'modified_date': 'ModifiedDate',
        'left_x': 'LeftX',
        'top_y': 'TopY',
        'width': 'Width',
        'height': 'Height'
    }

    def __init__(self, title=None, annotation_type=None, page_number=None, annotation_index=None, subject=None, text_contents=None, creation_date=None, modified_date=None, left_x=None, top_y=None, width=None, height=None):  # noqa: E501
        """PdfAnnotation - a model defined in Swagger"""  # noqa: E501

        self._title = None
        self._annotation_type = None
        self._page_number = None
        self._annotation_index = None
        self._subject = None
        self._text_contents = None
        self._creation_date = None
        self._modified_date = None
        self._left_x = None
        self._top_y = None
        self._width = None
        self._height = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if annotation_type is not None:
            self.annotation_type = annotation_type
        if page_number is not None:
            self.page_number = page_number
        if annotation_index is not None:
            self.annotation_index = annotation_index
        if subject is not None:
            self.subject = subject
        if text_contents is not None:
            self.text_contents = text_contents
        if creation_date is not None:
            self.creation_date = creation_date
        if modified_date is not None:
            self.modified_date = modified_date
        if left_x is not None:
            self.left_x = left_x
        if top_y is not None:
            self.top_y = top_y
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height

    @property
    def title(self):
        """Gets the title of this PdfAnnotation.  # noqa: E501

        Title of the annotation; this is often the author of the annotation in Acrobat-created PDF files  # noqa: E501

        :return: The title of this PdfAnnotation.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this PdfAnnotation.

        Title of the annotation; this is often the author of the annotation in Acrobat-created PDF files  # noqa: E501

        :param title: The title of this PdfAnnotation.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def annotation_type(self):
        """Gets the annotation_type of this PdfAnnotation.  # noqa: E501

        Type of the annotation; possible values are Text  # noqa: E501

        :return: The annotation_type of this PdfAnnotation.  # noqa: E501
        :rtype: str
        """
        return self._annotation_type

    @annotation_type.setter
    def annotation_type(self, annotation_type):
        """Sets the annotation_type of this PdfAnnotation.

        Type of the annotation; possible values are Text  # noqa: E501

        :param annotation_type: The annotation_type of this PdfAnnotation.  # noqa: E501
        :type: str
        """

        self._annotation_type = annotation_type

    @property
    def page_number(self):
        """Gets the page_number of this PdfAnnotation.  # noqa: E501

        The 1-based index of the page containing the annotation  # noqa: E501

        :return: The page_number of this PdfAnnotation.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this PdfAnnotation.

        The 1-based index of the page containing the annotation  # noqa: E501

        :param page_number: The page_number of this PdfAnnotation.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def annotation_index(self):
        """Gets the annotation_index of this PdfAnnotation.  # noqa: E501

        The 0-based index of the annotation in the document  # noqa: E501

        :return: The annotation_index of this PdfAnnotation.  # noqa: E501
        :rtype: int
        """
        return self._annotation_index

    @annotation_index.setter
    def annotation_index(self, annotation_index):
        """Sets the annotation_index of this PdfAnnotation.

        The 0-based index of the annotation in the document  # noqa: E501

        :param annotation_index: The annotation_index of this PdfAnnotation.  # noqa: E501
        :type: int
        """

        self._annotation_index = annotation_index

    @property
    def subject(self):
        """Gets the subject of this PdfAnnotation.  # noqa: E501

        Subject of the annotation  # noqa: E501

        :return: The subject of this PdfAnnotation.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this PdfAnnotation.

        Subject of the annotation  # noqa: E501

        :param subject: The subject of this PdfAnnotation.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def text_contents(self):
        """Gets the text_contents of this PdfAnnotation.  # noqa: E501

        Text contents of the annotation  # noqa: E501

        :return: The text_contents of this PdfAnnotation.  # noqa: E501
        :rtype: str
        """
        return self._text_contents

    @text_contents.setter
    def text_contents(self, text_contents):
        """Sets the text_contents of this PdfAnnotation.

        Text contents of the annotation  # noqa: E501

        :param text_contents: The text_contents of this PdfAnnotation.  # noqa: E501
        :type: str
        """

        self._text_contents = text_contents

    @property
    def creation_date(self):
        """Gets the creation_date of this PdfAnnotation.  # noqa: E501

        Date that the annotation was created  # noqa: E501

        :return: The creation_date of this PdfAnnotation.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this PdfAnnotation.

        Date that the annotation was created  # noqa: E501

        :param creation_date: The creation_date of this PdfAnnotation.  # noqa: E501
        :type: datetime
        """

        self._creation_date = creation_date

    @property
    def modified_date(self):
        """Gets the modified_date of this PdfAnnotation.  # noqa: E501

        Date that the annotation was last modified  # noqa: E501

        :return: The modified_date of this PdfAnnotation.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        """Sets the modified_date of this PdfAnnotation.

        Date that the annotation was last modified  # noqa: E501

        :param modified_date: The modified_date of this PdfAnnotation.  # noqa: E501
        :type: datetime
        """

        self._modified_date = modified_date

    @property
    def left_x(self):
        """Gets the left_x of this PdfAnnotation.  # noqa: E501

        Left X coordinate for the location of the annotation  # noqa: E501

        :return: The left_x of this PdfAnnotation.  # noqa: E501
        :rtype: float
        """
        return self._left_x

    @left_x.setter
    def left_x(self, left_x):
        """Sets the left_x of this PdfAnnotation.

        Left X coordinate for the location of the annotation  # noqa: E501

        :param left_x: The left_x of this PdfAnnotation.  # noqa: E501
        :type: float
        """

        self._left_x = left_x

    @property
    def top_y(self):
        """Gets the top_y of this PdfAnnotation.  # noqa: E501

        Top Y coordination of the location of the annotation  # noqa: E501

        :return: The top_y of this PdfAnnotation.  # noqa: E501
        :rtype: float
        """
        return self._top_y

    @top_y.setter
    def top_y(self, top_y):
        """Sets the top_y of this PdfAnnotation.

        Top Y coordination of the location of the annotation  # noqa: E501

        :param top_y: The top_y of this PdfAnnotation.  # noqa: E501
        :type: float
        """

        self._top_y = top_y

    @property
    def width(self):
        """Gets the width of this PdfAnnotation.  # noqa: E501

        Width of the annotation  # noqa: E501

        :return: The width of this PdfAnnotation.  # noqa: E501
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this PdfAnnotation.

        Width of the annotation  # noqa: E501

        :param width: The width of this PdfAnnotation.  # noqa: E501
        :type: float
        """

        self._width = width

    @property
    def height(self):
        """Gets the height of this PdfAnnotation.  # noqa: E501

        Height of the annotation  # noqa: E501

        :return: The height of this PdfAnnotation.  # noqa: E501
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this PdfAnnotation.

        Height of the annotation  # noqa: E501

        :param height: The height of this PdfAnnotation.  # noqa: E501
        :type: float
        """

        self._height = height

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
        if issubclass(PdfAnnotation, dict):
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
        if not isinstance(other, PdfAnnotation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other