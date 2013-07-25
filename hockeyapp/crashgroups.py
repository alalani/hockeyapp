"""
Implements an object for calling the CrashGroups API

"""
__author__ = 'Gavin M. Roy'
__email__ = 'gmr@myyearbook.com'
__since__ = '2011-09-13'

import urllib
from . import api

class CrashGroups(api.APIRequest):
    """This API lets you receive the list of crash groups for a given app and optionally a version."""

    def __init__(self, api_key, app_id, version_id=None, sort=None, order=None, page=1):
        """Create the CrashLog request object.

        :param api_key: HockeyApp API key
        :type api_key: str
        :param app_id: The HockeyApp Application Identifier
        :type api_key: str
        :param page: The page offset
        :type page: int

        """
        api.APIRequest.__init__(self, api_key)
        self._key = None
        self._app_id = app_id
        self._page = page
        self._version_id = version_id
        self._sort = sort
        self._order = order

    @property
    def parameters(self):
        """Returns the request parameters

        :returns: dict

        """
        return {'symbolicated': 1,
                'page': self._page,
                'sort': self._sort,
                'order': self._order}

    @property
    def path(self):
        """Returns the request path

        :returns: str

        """
        params = urllib.urlencode(self.parameters)
        if self._version_id != None:
            version_api = "app_versions/%s/" % self._version_id
        else:
            version_api = ""
        
        return api.BASE_URI + 'apps/%s/%scrash_reasons' % (self._app_id, version_api)

class Crashes(api.APIRequest):
    """This API lets you receive the list of crashes in a given CrashGroup"""

    def __init__(self, api_key, app_id, group_id, sort=None, order=None, page=1):
        """Create the CrashLog request object.

        :param api_key: HockeyApp API key
        :type api_key: str
        :param app_id: The HockeyApp Application Identifier
        :type api_key: str
        :param group_id: The identifier for the crash group
        :type group_id: str
        :param page: The page offset
        :type page: int

        """
        api.APIRequest.__init__(self, api_key)
        self._key = None
        self._app_id = app_id
        self._group_id = group_id
        self._sort = sort
        self._order = order
        self._page = page

    @property
    def parameters(self):
        """Returns the request parameters

        :returns: dict

        """
        return {'symbolicated': 1,
                'page': self._page,
                'sort': self._sort,
                'order': self._order}
                

    @property
    def path(self):
        """Returns the request path

        :returns: str

        """
        params = urllib.urlencode(self.parameters)
        
        return api.BASE_URI + 'apps/%s/crash_reasons/%s' % (self._app_id, self._group_id)
