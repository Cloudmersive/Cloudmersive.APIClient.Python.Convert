# GetImageInfoResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**successful** | **bool** |  | [optional] 
**color_space** | **str** | Color space of the image | [optional] 
**color_type** | **str** | Color type of the image | [optional] 
**width** | **int** | Width in pixels of the image | [optional] 
**height** | **int** | Height in pixels of the image | [optional] 
**compression_level** | **int** | Compression level value from 0 (lowest quality) to 100 (highest quality) | [optional] 
**image_hash_signature** | **str** | SHA256 hash signature of the image | [optional] 
**has_transparency** | **bool** | True if the image contains transparency, otherwise false | [optional] 
**mime_type** | **str** | MIME type of the image format | [optional] 
**image_format** | **str** | Image format | [optional] 
**dpi_unit** | **str** | Units of the DPI measurement; can be either in Inches or Centimeters | [optional] 
**dpi** | **float** | DPI (pixels per unit, e.g. pixels per inch) of the image | [optional] 
**color_count** | **int** | Unique colors in the image | [optional] 
**bit_depth** | **int** | Bit depth of the image | [optional] 
**comment** | **str** | Comment string in the image | [optional] 
**exif_profile_name** | **str** | Name of the EXIF profile used | [optional] 
**exif_values** | [**list[ExifValue]**](ExifValue.md) | EXIF tags and values embedded in the image | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


