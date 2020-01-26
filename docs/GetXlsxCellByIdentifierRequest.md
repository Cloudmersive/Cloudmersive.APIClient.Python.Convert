# GetXlsxCellByIdentifierRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_file_bytes** | **str** | Optional: Bytes of the input file to operate on | [optional] 
**input_file_url** | **str** | Optional: URL of a file to operate on as input.  This can be a public URL, or you can also use the begin-editing API to upload a document and pass in the secure URL result from that operation as the URL here (this URL is not public). | [optional] 
**worksheet_to_query** | [**XlsxWorksheet**](XlsxWorksheet.md) | Optional; Worksheet (tab) within the spreadsheet to get the rows and cells of; leave blank to default to the first worksheet | [optional] 
**cell_identifier** | **str** | Required; Excel cell identifier, e.g. A1, B22, C33, etc. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

