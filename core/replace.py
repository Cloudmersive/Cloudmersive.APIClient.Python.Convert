if response_data.getheader("content-type") == "application/octet-stream":
                return_data = response_data.data
            elif response_type: