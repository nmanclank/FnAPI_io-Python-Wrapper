import os
from typing import Iterator, Callable
from fn_api_wrapper.rest_api import RestAPI
from fn_api_wrapper.exceptions import FN_API_Exception
from fn_api_wrapper.models import *
import logging

class FN_API:
    def __init__(self, api_key: str = '', ssl_verify: bool = True,
                 logger: logging.Logger = None):
        hostname = 'fortniteapi.io'
        self._rest_api = RestAPI(hostname, api_key, ssl_verify, logger)
    
    def get_userid(self, username: str, platform="None") -> UserID:
        '''
        You can fetch the user id by passing the username and have the id returned. 
        User id's are used in all player search queries.
        '''
        self.username = username
        try:
            if platform != "None": # If a platform was specified we attempt to search for the id on this platform.
                resultss = self._rest_api.get(endpoint=f'v2/lookup?username={username}&platform={platform}')        
                imgs = UserID(**resultss.data)
            else: # Else we default to epic
                resultss = self._rest_api.get(endpoint=f'v2/lookup?username={username}')        
                imgs = UserID(**resultss.data)
            return imgs.account_id
        
        except Exception as err:
            self._logger.error(msg=(str(err)))
            raise FN_API_Exception(str(err)) from err
        
    def all_stats_by_username(self, username: str, platform="None"):
        '''
        All player stats are returned by this function. For your convience, you can pass the username with optional platform arg
        and the username will be resolved to an id. 
        '''
        self.username = username
        catch_id = self.get_userid(username, platform)
        try:
            fetch_stats = self._rest_api.get(endpoint=f"v1/stats?account={catch_id}")
            player_stats = fetch_stats.data            
        except Exception as err:
            raise FN_API_Exception(msg=err)
        
        return player_stats

    def ranked_stats_by_username(self, username: str, platform="None"):
        '''
        Ranked player stats are returned by this function. For your convience, you can pass the username with optional platform arg
        and the username will be resolved to an id. 
        '''
        self.username = username
        catch_id = self.get_userid(username, platform)
        try:
            fetch_stats = self._rest_api.get(endpoint=f"v2/ranked/user?account={catch_id}")
            player_stats = fetch_stats.data            
        except Exception as err:
            raise FN_API_Exception(msg=err)
        
        return player_stats
    
    def all_stats_by_id(self, id):
        '''
        All player stats are returned by this function with given player id.
        '''
        
        try:
            fetch_stats = self._rest_api.get(endpoint=f"v1/stats?account={id}")
            player_stats = fetch_stats.data            
        except Exception as err:
            raise FN_API_Exception(msg=err)
        
        return player_stats

    def ranked_stats_by_id(self, id):
        '''
        Ranked player stats are returned by this function with given player id.
        '''
        
        try:
            fetch_stats = self._rest_api.get(endpoint=f"v2/ranked/user?account={id}")
            player_stats = fetch_stats.data            
        except Exception as err:
            raise FN_API_Exception(msg=err)
        
        return player_stats
    
    def all_tournaments(self,region="NAW",lang="en", arena='false'):
        '''
        All tournament events are returned with optional region, lang, and arena args. Defaults are region=NAW lang=en arena=false
        '''
        self.arena = arena
        self.region = region
        self.lang = lang

        try:
            fetch_events = self._rest_api.get(endpoint=f"v1/events/list?lang={lang}&region={region}&showArena={arena}")
            events = fetch_events.data         
        except Exception as err:
            raise FN_API_Exception(msg=err)
        
        return events

    def tournament_scores(self, tourney_id="epicgames_S14_FNCS_Qualifier1_EU_PC"):
        '''
        Return the scores for given tournament id
        
        Ex. https://fortniteapi.io/v1/events/cumulative?eventId=epicgames_S14_FNCS_Qualifier1_EU_PC
        '''
        try:
            fetch_events = self._rest_api.get(endpoint=f"v1/events/cumulative?eventId={tourney_id}")
            events = fetch_events.data         
        except Exception as err:
            raise FN_API_Exception(msg=err)
        
        return events
    
    def tournament_data(self, session_id="fbb092f4356349209e08c06d96eb8f26"):
        '''
        Return the replay data for given tournament id - Meta Data and Replay chunks
        
        Ex. https://fortniteapi.io/v1/events/replay?session=fbb092f4356349209e08c06d96eb8f26
        '''
        try:
            fetch_events = self._rest_api.get(endpoint=f"v1/events/replay?session={session_id}")
            events = fetch_events.data         
        except Exception as err:
            raise FN_API_Exception(msg=err)
        
        return events
        
    def active_events(self,region="NAW",lang="en", arena='true'):
        '''
        All active events are returned with the same optional arguments as all_events
        '''
        self.arena = arena
        self.region = region
        self.lang = lang

        try:
            fetch_events = self._rest_api.get(endpoint=f"v1/events/list/active?lang={lang}&region={region}&showArena={arena}")
            events = fetch_events.data         
        except Exception as err:
            raise FN_API_Exception(msg=err)
        
        return events
     
    def live_events(self,region="NAW",lang="en", arena='true'):
        '''
        All live events are returned with the optional arguments region, lang, and arena.
        '''
        self.arena = arena
        self.region = region
        self.lang = lang

        try:
            fetch_events = self._rest_api.get(endpoint=f"v1/events/list/live?lang={lang}&region={region}&showArena={arena}")
            events = fetch_events.data         
        except Exception as err:
            raise FN_API_Exception(msg=err)
        
        return events
    
    def list_augments(self,season='20',lang="en"):
        '''
        This function returns augments for a specified season. The season must have augments to return. Optional
        arg default lang=en
        '''
        self.season = season
        self.lang = lang

        try:
            fetch_events = self._rest_api.get(endpoint=f"v1/augments?lang={lang}&season={season}")
            augments = fetch_events.data         
        except Exception as err:
            raise FN_API_Exception(msg=err)
        
        return augments
    
    def list_drops(self,search='Active'):
        ''' This function returns active twitch drops. Pass empty string with "" to return all drops'''
        self.search = search

        try:
            fetch_events = self._rest_api.get(endpoint=f"v1/twitch/drops?status={search}")
            drops = fetch_events.data         
        except Exception as err:
            raise FN_API_Exception(msg=err)
        
        return drops
    
    def rarity_values(self,lang='en'):
        ''' 
        This function returns the default rarity value information such as color values. 
        This is useful for correctly coloring loot and weapons.
        '''

        try:
            fetch_rarity = self._rest_api.get(endpoint=f"v2/rarities?lang={lang}")
            rarity = fetch_rarity.data         
        except Exception as err:
            raise FN_API_Exception(msg=err)
        
        return rarity

    def get_shop(self,lang='en', render='false'):
        ''' 
        This function dumps the active shop items.
        '''
        try:
            fetch_shop = self._rest_api.get(endpoint=f"v2/shop?lang={lang}&includeRenderData={render}&includeHiddenTabs=false")
            shop = fetch_shop.data         
        except Exception as err:
            raise FN_API_Exception(msg=err)
        
        return shop
    
    def upcoming_items(self,lang='en'):
        ''' 
        This function dumps items coming soon to the game.
        '''

        try:
            fetch_items = self._rest_api.get(endpoint=f"v2/items/upcoming?lang={lang}")
            items = fetch_items.data         
        except Exception as err:
            raise FN_API_Exception(msg=err)
        
        return items 

    def item_details(self, item, lang='en'):
        ''' 
        Search item details by providing the correct item id.
        
        Ex.  https://fortniteapi.io/v2/items/get?id=CID_242_Athena_Commando_F_Bullseye&lang=en
        
        Item id can be found in the full list of items
        '''
        try:
            fetch_items = self._rest_api.get(endpoint=f"v2/items/get?id={item}&lang={lang}")
            items = fetch_items.data         
        except Exception as err:
            raise FN_API_Exception(msg=err)
        
        return items
    
    def item_sets(self, lang='en'):
        ''' 
        Returns list of all the sets used by cosmetics
        '''
        try:
            fetch_sets = self._rest_api.get(endpoint=f"/v2/items/sets?lang={lang}")
            items = fetch_sets.data         
        except Exception as err:
            raise FN_API_Exception(msg=err)
        
        return items

    def get_news(self, lang='en'):
        ''' 
        Returns current news in Fortnite br and Save the World
        '''
        try:
            fetch_news = self._rest_api.get(endpoint=f"v1/news?lang={lang}&type=br")
            news = fetch_news.data         
        except Exception as err:
            raise FN_API_Exception(msg=err)
        
        return news
    
    def get_rewards(self, season='current', lang='en'):
        ''' 
        Returns battlepass rewards for given season. This defaults to the current season, but can be specified
        '''
        try:
            fetch_rewards = self._rest_api.get(endpoint=f"v2/battlepass?lang={lang}&season={season}")
            rewards = fetch_rewards.data         
        except Exception as err:
            raise FN_API_Exception(msg=err)
        
        return rewards

    def get_achievements(self, lang='en'):
        ''' 
        Returns a list of all achievements
        '''
        try:
            fetch_achv = self._rest_api.get(endpoint=f"v1/achievements?lang={lang}")
            achievements = fetch_achv.data         
        except Exception as err:
            raise FN_API_Exception(msg=err)
        
        return achievements

    def get_map():
        ''' 
        Returns image of the current map as 2048x2048 px
        '''
        map = "https://media.fortniteapi.io/images/map.png"
        
        return map
    
    def get_poi_map():
        ''' 
        Returns image of the current map as 2048x2048 px with poi names
        '''
        map = "https://media.fortniteapi.io/images/map.png?showPOI=true"
        
        return map

    def get_all_maps(self):
        ''' 
        Returns a list links for all maps
        '''
        try:
            fetch_maps = self._rest_api.get(endpoint=f"v1/maps/list")
            maps = fetch_maps.data         
        except Exception as err:
            raise FN_API_Exception(msg=err)
        
        return maps
    
    def get_all_season_info(self, lang='en'):
        ''' 
        Returns list of all season dates and patch versions associated
        '''
        try:
            season_details = self._rest_api.get(endpoint=f"v1/seasons/list?lang={lang}")
            details = season_details.data         
        except Exception as err:
            raise FN_API_Exception(msg=err)
        
        return details
    
    def get_bundles(self, lang='en'):
        ''' 
        Returns list of recent bundles
        '''
        try:
            fetch = self._rest_api.get(endpoint=f"v2/bundles?lang={lang}")
            details = fetch.data         
        except Exception as err:
            raise FN_API_Exception(msg=err)
        
        return details

    def get_loot(self, lang='en'):
        ''' 
        Returns list of all loot and weapons in the game along with basic stats
        '''
        try:
            fetch = self._rest_api.get(endpoint=f"v1/loot/list?lang={lang}")
            details = fetch.data         
        except Exception as err:
            raise FN_API_Exception(msg=err)
        
        return details

    def loot_stats(self, loot='WID_Assault_AutoHigh_Athena_SR_Ore_T03', lang='en'):
        ''' 
        Returns all weapon/loot stats for specific item
        
        Ex. https://fortniteapi.io/v1/loot/get?id=WID_Assault_AutoHigh_Athena_SR_Ore_T03&lang=en

        '''
        try:
            fetch = self._rest_api.get(endpoint=f"v1/loot/get?id={loot}&lang={lang}")
            details = fetch.data         
        except Exception as err:
            raise FN_API_Exception(msg=err)
        
        return details
    
    def get_loot_spawns(self, mode='Playlist_DefaultSolo'):
        ''' 
        Returns the spawn chances for each loot type for a given game mode
        
        Ex. https://fortniteapi.io/v1/loot/chances?mode=Playlist_DefaultSolo

        '''
        try:
            fetch = self._rest_api.get(endpoint=f"v1/loot/chances?mode={mode}")
            details = fetch.data         
        except Exception as err:
            raise FN_API_Exception(msg=err)
        
        return details

    def get_modes(self, lang='en'):
        ''' 
        Returns all the game modes in game files
        '''
        try:
            fetch = self._rest_api.get(endpoint=f"v1/game/modes?lang={lang}")
            details = fetch.data         
        except Exception as err:
            raise FN_API_Exception(msg=err)
        
        return details        

    def get_featured_islands(self):
        ''' 
        Returns all current featured islands in creative mode
        '''
        try:
            fetch = self._rest_api.get(endpoint=f"v1/creative/featured")
            details = fetch.data         
        except Exception as err:
            raise FN_API_Exception(msg=err)
        
        return details
    
    def search_islands(self, island='1787-6243-5207'):
        ''' 
        Returns all details for given item id
        '''
        try:
            fetch = self._rest_api.get(endpoint=f"v1/creative/island?code={island}")
            details = fetch.data         
        except Exception as err:
            raise FN_API_Exception(msg=err)
        
        return details
    
    def creator_code(self, creator='ninja'):
        ''' 
        Returns all details for given creator code
        '''
        try:
            fetch = self._rest_api.get(endpoint=f"v1/creator?code={creator}")
            details = fetch.data         
        except Exception as err:
            raise FN_API_Exception(msg=err)
        
        return details

    def all_fish(self, lang='en'):
        ''' 
        Returns list of all fish and details
        '''
        try:
            fetch = self._rest_api.get(endpoint=f"v1/loot/fish?lang={lang}")
            details = fetch.data         
        except Exception as err:
            raise FN_API_Exception(msg=err)
        
        return details

    def current_crew_info(self, lang='en'):
        ''' 
        Returns current fortnite crew info and pricing
        '''
        try:
            fetch = self._rest_api.get(endpoint=f"v2/crew?lang={lang}")
            details = fetch.data         
        except Exception as err:
            raise FN_API_Exception(msg=err)
        
        return details

    def crew_history(self, lang='en'):
        ''' 
        Returns history of crew info for each month
        '''
        try:
            fetch = self._rest_api.get(endpoint=f"v2/crew/history?lang={lang}")
            details = fetch.data         
        except Exception as err:
            raise FN_API_Exception(msg=err)
        
        return details 

    def discovery_islands(self):
        ''' 
        Returns list if creative islands in discovery tab
        '''
        try:
            fetch = self._rest_api.get(endpoint=f"v3/creative/discovery")
            details = fetch.data         
        except Exception as err:
            raise FN_API_Exception(msg=err)
        
        return details 

    def get_vehicles(self, lang='en'):
        ''' 
        Returns list of vehicles with stats, name, gear, and icons.
        '''
        try:
            fetch = self._rest_api.get(endpoint=f"v2/game/vehicles")
            details = fetch.data         
        except Exception as err:
            raise FN_API_Exception(msg=err)
        
        return details    