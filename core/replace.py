            if response_data.getheader("content-type") == "application/octet-stream":
                return_data = response_data.data
            elif response_type:
                return_data = self.deserialize(response_data, response_type)