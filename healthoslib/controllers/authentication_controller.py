# -*- coding: utf-8 -*-

"""
    healthoslib.controllers.authentication_controller

    This file was automatically generated by APIMATIC BETA v2.0 on 02/18/2017
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.o_auth_2 import OAuth2
from ..exceptions.api_exception import APIException

class AuthenticationController(BaseController):

    """A Controller to access Endpoints in the healthoslib API."""
    

    def create_request_access_token(self,
                                    body):
        """Does a POST request to /oauth/token.json.

        TODO: Add Description

        Args:
            body (RequestAccessTokenRequest): TODO: type description here.
                Example: 

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri.format(Configuration.host)
        _query_builder += '/oauth/token.json'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        _context = self.execute_request(_request)        

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 401:
            raise APIException('Unauthorized', _context)
        self.validate_response(_context)    

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)
