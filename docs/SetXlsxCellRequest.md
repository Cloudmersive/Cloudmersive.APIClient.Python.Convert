# SetXlsxCellRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_file_bytes** | **str** | Optional: Bytes of the input file to operate on | [optional] 
**input_file_url** | **str** | Optional: URL of a file to operate on as input.  This can be a public URL, or you can also use the begin-editing API to upload a document and pass in the secure URL result from that operation as the URL here (this URL is not public). | [optional] 
**worksheet_to_update** | [**XlsxWorksheet**](XlsxWorksheet.md) | Optional; Worksheet (tab) within the spreadsheet to update; leave blank to default to the first worksheet | [optional] 
**row_index** | **int** | 0-based index of the row, 0, 1, 2, ... to set | [optional] 
**cell_index** | **int** | 0-based index of the cell, 0, 1, 2, ... in the row to set | [optional] 
**cell_value** | [**XlsxSpreadsheetCell**](XlsxSpreadsheetCell.md) | New Cell value to update/overwrite into the Excel XLSX spreadsheet | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


