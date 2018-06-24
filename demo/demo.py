from __future__ import print_function
import time
import cloudmersive_convert_api_client
from cloudmersive_convert_api_client.rest import ApiException
from pprint import pprint




# create an instance of the API class
api_instance = cloudmersive_convert_api_client.ConvertDataApi()
input_file = 'C:\\temp\\input.csv' # file | Input file to perform the operation on.

api_instance.api_client.configuration.api_key = {}
api_instance.api_client.configuration.api_key['Apikey'] = '04d1a7be-c9d1-4d93-8ec4-e7545c2a570a'

try:
    # CSV to JSON conversion
    api_response = api_instance.convert_data_csv_to_json(input_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConvertDataApi->convert_data_csv_to_json: %s\n" % e)