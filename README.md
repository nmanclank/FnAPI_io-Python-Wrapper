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

## Functions with `args`
*Note*: if you import wrapper as listed above in usage example, you would call with:


`fnapi.get_userid("myusername")` 

or
```python
myusername = username 
fnapi.get_userid(myusername)
```
--

---

--
- `get_userid(username, **platform)`

 - *Fetch the user id from the specified username. *
 - *The platform argument is **optional**, but accepts epic, xbl, and psn. Platform defaults to epic accounts.*

- `all_stats(username, **platform)`

 - *Fetch all stats for a specified username. This function passes the username to the id resolver to grab the account id. *
 - *The platform argument is **optional**, but accepts epic, xbl, and psn.  Platform defaults to epic accounts.*

- `all_events(region="NAW",lang="en", arena='false')`

 - *Fetch all in-game events. All arguments are optional, but they will default to the values listed unless specified.*

- `active_events(region="NAW",lang="en", arena='true')`

  - *Functions the same as all_events, but displays only active events.*

- `live_events(region="NAW",lang="en", arena='true')`

  - *See previous function*
 
- `list_augments(season='20',lang="en")`

 - *List all augments for a given season*
 - *also accepts optional lang argument*
 
- `list_drops(search='Active')`

 - *Search twitch drops. The deafault searches active drops, but a search term can be passed.*
 - *You can also pass a blank string to return all drops Ex. search = "" *

- `rarity_values(lang='en')`

 - *return rarity values such as color codes. This is useful for working with items or the shop response.*

- `get_shop(lang='en', render='false')`
 - *Return all items currently shown in the in-game shop.*
 - *Setting (render = true) will return shop items along with the neccesary resources for a visual render of each item. Ex: background color values, item images, etc.*
 
 
####  More actions will be added soon..





















[fnapiio-link]: https://fortniteapi.io/
