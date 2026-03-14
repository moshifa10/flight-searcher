
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    
    def put_testing(self, data:dict) -> dict:
        '''
            This function is responsible for checking each an every data passed in has the iataCode available if not just pass in Testing for that data.
        '''
        code = data["iataCode"]
        if len(code) == 0:
            data["iataCode"] = "Testing"
        return data
    

