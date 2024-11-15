
from typing import List, Dict, TypeVar
from requests.structures import CaseInsensitiveDict

Model = TypeVar('Model', covariant=True)


from typing import List, Dict, Union


class Result:
    def __init__(self, success: bool, status_code: int, message: str = '', data: List[Dict] = None):
        """

        :param success: True if HTTP Request was successful otherwise is False
        :param status_code: HTTP Status code
        :param message: result in readable format
        :param data: response data
        
        """
        self.success = bool(success)
        self.status_code = int(status_code)
        self.message = str(message)
        self.data = data if data else []

class UserID:

    def __init__(self, result, account_id, *kwargs) -> None:
        self.__dict__.update(kwargs)
        self.result = result
        self.account_id = account_id


