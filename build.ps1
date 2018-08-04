#Remove-Item –path ./ –recurse
& java -jar swagger-codegen-cli.jar generate -i https://api.cloudmersive.com/swagger/api/convert -l python -c packageconfig.json
(Get-Content ./cloudmersive_convert_api_client/api_client.py).replace((Get-Content ./core/orig.py), (Get-Content ./core/replace.py)) | Set-Content ./cloudmersive_convert_api_client/api_client.py