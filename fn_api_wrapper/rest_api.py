import requests
import logging
from typing import List, Dict
from json import JSONDecodeError
from fn_api_wrapper.exceptions import FN_API_Exception
from fn_api_wrapper.models import Result

class RestAPI:
    def __init__(self, hostname: str = 'fortniteapi.io', api_key: str = '', ssl_verify: bool = True, logger: logging.Logger = None):
        '''
        Basic body construction for the request
        '''
        self._logger = logger or logging.getLogger(__name__)
        self.url = f"https://{hostname}/"
        self._api_key = api_key
        self._ssl_verify = ssl_verify
        
        if not ssl_verify:
            requests.packages.urllib3.disable_warnings()
        
    def _do(self, http_method: str, endpoint: str, ep_params: Dict = None, data: Dict = None):
        '''
        Construction to join the request with the intended endpoint and capture response
        '''
        full_url = self.url + endpoint
        headers = {'Authorization': self._api_key}
        log_line_pre = f"method={http_method}, url={full_url}, params={ep_params}"
        log_line_post = ','.join((log_line_pre, "success={}, status_code={}, message={}"))
        
        # Capture http params and perform request, catch and raise exceptions as err
        try:
            self._logger.debug(msg=log_line_pre)
            response = requests.request(method=http_method, url=full_url, verify=self._ssl_verify,
                                        headers=headers, params=ep_params, json=data)
        except requests.exceptions.RequestException as err:
            self._logger.error(msg=(str(err)))
        
        try:
            data_out = response.json()
        except (ValueError, JSONDecodeError) as e:
            log_line = f"success=False, status_code={response.status_code}, message={e}"
            self._logger.warning(msg=log_line)
            return Result(False, response.status_code, message=str(e))
        
        is_success = 299 >= response.status_code >= 200
        log_line = f"success={is_success}, status_code={response.status_code}, message={response.reason}"
        self._logger.debug(msg=log_line)
        return Result(is_success, response.status_code, message=response.reason, data=data_out)
        
            
    def get(self, endpoint: str, ep_params: Dict = None) -> Result:
        '''
        Get method
        '''
        return self._do(http_method='GET', endpoint=endpoint, ep_params=ep_params)
        
    def fetch_data(self, url: str) -> bytes:
        #
        http_method = 'GET'
        try:
            log_line = f"method={http_method}, url={url}"
            self._logger.debug(msg=log_line)
            response = requests.request(method=http_method, url=url, verify=self._ssl_verify)
           
        except requests.exceptions.RequestException as err:
            self._logger.error(msg=(str(err)))
            raise FN_API_Exception(str(err)) from err
        
        #This will return byte stream under normal conditions and raise exceptions when needed
        is_success = 299 >= response.status_code >= 200
        log_line = f"success={is_success}, status_code={response.status_code}, message={response.reason}"
        self._logger.debug(msg=log_line)
        
        if not is_success:
            raise FN_API_Exception(response.reason)
        return response.content