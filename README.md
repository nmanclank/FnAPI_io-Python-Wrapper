# FortniteAPI.io Python-Wrapper

A python-wrapper to easily integrate api responses from [FortniteAPI.io][fnapiio-link]

### How to install:

Installation is simple, just place fn_api_wrapper in the root directory of your project. Afterwards, you can import the wrapper wherever.

***Note:** An API Key is needed to utilize this wrapper. You can obtain one for free at 
https://fortniteapi.io/ 

Consider purchasing a premium key to support the author of the API and to unlock premium features. 

### Usage:

```python
from fn_api_wrapper.fn_api import FN_API
from fn_api_wrapper.models import *

fnapi = FN_API('API_KEY_HERE')



fnapi.get_userid('username_here')
# Returns id of user
```



























[fnapiio-link]: https://fortniteapi.io/
