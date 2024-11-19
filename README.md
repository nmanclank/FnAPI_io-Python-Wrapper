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






---

- `get_userid(username, **platform)`  
  *Fetch the user ID from the specified username.*  
  *The platform argument is **optional**, but accepts epic, xbl, and psn. Platform defaults to epic accounts.*

---

- `all_stats_by_username(username, **platform)`  
  *Fetch all stats for a specified username. This function passes the username to the ID resolver to grab the account ID.*  
  *The platform argument is **optional**, but accepts epic, xbl, and psn. Platform defaults to epic accounts.*

---

- `all_stats_by_id(id)`  
  *Fetch all stats for a specified player ID.*  
  *The player ID is passed directly to the API to retrieve stats.*

---

- `all_tournaments(region="NAW", lang="en", arena='false')`  
  *Fetch all tournament events with optional region, language, and arena filters.*  
  *Defaults are region=NAW, lang=en, arena=false.*

---

- `tournament_scores(tourney_id)`  
  *Fetch scores for a given tournament ID.*  
  *Defaults to the provided tournament ID if none is specified.*

---

- `tournament_data(session_id)`  
  *Fetch tournament replay data (Meta Data and Replay chunks) for a given session ID.*  
  *Defaults to the provided session ID if none is specified.*

---

- `active_events(region="NAW", lang="en", arena='true')`  
  *Fetch all active events with optional region, language, and arena filters.*  
  *Defaults are region=NAW, lang=en, arena=true.*

---

- `live_events(region="NAW", lang="en", arena='true')`  
  *Fetch all live events with optional region, language, and arena filters.*  
  *Defaults are region=NAW, lang=en, arena=true.*

---

- `list_augments(season='20', lang="en")`  
  *Fetch augments for a specified season. The season must have augments available to return.*  
  *Defaults to season=20 and lang=en.*

---

- `list_drops(search='Active')`  
  *Fetch active Twitch drops. An empty string can be passed to return all drops.*

---

- `rarity_values(lang='en')`  
  *Fetch the default rarity value information, such as color values, useful for correctly coloring loot and weapons.*  

---

- `get_shop(lang='en', render='false')`  
  *Fetch the active shop items.*  
  *Defaults to lang=en and render=false.*

---

- `upcoming_items(lang='en')`  
  *Fetch items coming soon to the game.*  
  *Defaults to lang=en.*

---

- `item_details(item, lang='en')`  
  *Fetch details for a specific item by ID.*  
  *Item ID can be found in the full list of items.*

---

- `item_sets(lang='en')`  
  *Fetch a list of all the sets used by cosmetics.*

---

- `get_news(lang='en')`  
  *Fetch current news in Fortnite Battle Royale and Save the World.*  
  *Defaults to lang=en.*

---

- `get_rewards(season='current', lang='en')`  
  *Fetch battle pass rewards for the given season. Defaults to the current season.*  
  *Defaults to lang=en.*

---

- `get_achievements(lang='en')`  
  *Fetch a list of all achievements.*  
  *Defaults to lang=en.*

---

- `get_map()`  
  *Fetch the current map image (2048x2048 px).*

---

- `get_poi_map()`  
  *Fetch the current map image (2048x2048 px) with POI names.*

---

- `get_all_maps()`  
  *Fetch a list of links for all maps.*

---

- `get_all_season_info(lang='en')`  
  *Fetch a list of all season dates and associated patch versions.*  
  *Defaults to lang=en.*

---

- `get_bundles(lang='en')`  
  *Fetch a list of recent bundles.*  
  *Defaults to lang=en.*

---

- `get_loot(lang='en')`  
  *Fetch a list of all loot and weapons in the game, along with basic stats.*  
  *Defaults to lang=en.*

---

- `loot_stats(loot='WID_Assault_AutoHigh_Athena_SR_Ore_T03', lang='en')`  
  *Fetch stats for a specific weapon or loot item.*  
  *Defaults to lang=en.*

---

- `get_modes(lang='en')`  
  *Fetch a list of all the game modes in the game files.*  
  *Defaults to lang=en.*

---

- `get_featured_islands()`  
  *Fetch a list of all current featured islands in Creative mode.*

---

- `search_islands(island='1787-6243-5207')`  
  *Fetch details for a specified island by its code.*  
  *Defaults to the provided island code if none is specified.*

---

- `creator_code(creator)`  
  *Fetch details for a specified creator code.*  
  *Defaults to 'ninja' if no creator is specified.*

---

- `all_fish(lang='en')`  
  *Fetch a list of all fish and their details.*  
  *Defaults to lang=en.*

---

- `current_crew_info(lang='en')`  
  *Fetch current Fortnite Crew information and pricing.*  
  *Defaults to lang=en.*

---

- `crew_history(lang='en')`  
  *Fetch the history of Fortnite Crew information for each month.*  
  *Defaults to lang=en.*

---

- `discovery_islands()`  
  *Fetch a list of creative islands in the discovery tab.*

---

- `get_vehicles(lang='en')`  
  *Fetch a list of all vehicles with stats, names, gear, and icons.*  
  *Defaults to lang=en.*

---















[fnapiio-link]: https://fortniteapi.io/
