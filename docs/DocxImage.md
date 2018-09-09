# DocxImage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | The Path of the location of this object; leave blank for new tables | [optional] 
**image_name** | **str** | The Name of the image | [optional] 
**image_id** | **int** | The Id of the image | [optional] 
**image_description** | **str** | The Description of the image | [optional] 
**image_width** | **int** | Width of the image in EMUs (English Metric Units); set to 0 to default to page width and aspect-ratio based height | [optional] 
**image_height** | **int** | Height of the image in EMUs (English Metric Units); set to 0 to default to page width and aspect-ratio based height | [optional] 
**x_offset** | **int** | X (horizontal) offset of the image | [optional] 
**y_offset** | **int** | Y (vertical) offset of the image | [optional] 
**image_data_embed_id** | **str** | Read-only; internal ID for the image contents | [optional] 
**image_data_content_type** | **str** | Read-only; image data MIME content-type | [optional] 
**image_internal_file_name** | **str** | Read-only; internal file name/path for the image | [optional] 
**image_contents_url** | **str** | URL to the image contents; file is stored in an in-memory cache and will be deleted.  Call Finish-Editing to get the contents. | [optional] 
**inline_with_text** | **bool** | True if the image is inline with the text; false if it is floating | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


