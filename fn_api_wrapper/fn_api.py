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
        You can fetch the user id by passing the username and have the id returned. User id's are used in all player search queries.
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
        
    def all_stats(self, username: str, platform="None"):
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
    
    def all_events(self,region="NAW",lang="en", arena='false'):
        '''
        All events are returned with optional region, lang, and arena args. Defaults are region=NAW lang=en arena=false
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
        This function returns the default rarity value information such as color values. This is useful for correctly coloring loot and weapons.
        '''
        self.lang = lang

        try:
            fetch_rarity = self._rest_api.get(endpoint=f"v2/rarities?lang={lang}")
            rarity = fetch_rarity.data         
        except Exception as err:
            raise FN_API_Exception(msg=err)
        
        return rarity

    def get_shop(self,lang='en', render='false'):
        ''' This function dumps the active shop items. '''
        self.lang = lang
        self.render = render

        try:
            fetch_shop = self._rest_api.get(endpoint=f"v2/shop?lang={lang}&includeRenderData={render}&includeHiddenTabs=false")
            shop = fetch_shop.data         
        except Exception as err:
            raise FN_API_Exception(msg=err)
        
        return shop        

        