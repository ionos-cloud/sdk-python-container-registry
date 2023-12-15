from __future__ import absolute_import

import re  # noqa: F401
import six

from ionoscloud_container_registry.api_client import ApiClient
from ionoscloud_container_registry.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class VulnerabilitiesApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def vulnerabilities_find_by_id(self, vulnerability_id, **kwargs):  # noqa: E501
        """Retrieve Vulnerability  # noqa: E501

        Returns the Vulnerability by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.vulnerabilities_find_by_id(vulnerability_id, async_req=True)
        >>> result = thread.get()

        :param vulnerability_id: The ID of the Vulnerability that should be retrieved. (required)
        :type vulnerability_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: VulnerabilityRead
        """
        kwargs['_return_http_data_only'] = True
        return self.vulnerabilities_find_by_id_with_http_info(vulnerability_id, **kwargs)  # noqa: E501

    def vulnerabilities_find_by_id_with_http_info(self, vulnerability_id, **kwargs):  # noqa: E501
        """Retrieve Vulnerability  # noqa: E501

        Returns the Vulnerability by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.vulnerabilities_find_by_id_with_http_info(vulnerability_id, async_req=True)
        >>> result = thread.get()

        :param vulnerability_id: The ID of the Vulnerability that should be retrieved. (required)
        :type vulnerability_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(VulnerabilityRead, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'vulnerability_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                'response_type',
                'query_params'
            ]
        )

        for local_var_params_key, local_var_params_val in six.iteritems(local_var_params['kwargs']):
            if local_var_params_key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method vulnerabilities_find_by_id" % local_var_params_key
                )
            local_var_params[local_var_params_key] = local_var_params_val
        del local_var_params['kwargs']
        # verify the required parameter 'vulnerability_id' is set
        if self.api_client.client_side_validation and ('vulnerability_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['vulnerability_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `vulnerability_id` when calling `vulnerabilities_find_by_id`")  # noqa: E501

        if self.api_client.client_side_validation and ('vulnerability_id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['vulnerability_id']) > 64):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `vulnerability_id` when calling `vulnerabilities_find_by_id`, length must be less than or equal to `64`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'vulnerability_id' in local_var_params:
            path_params['vulnerabilityId'] = local_var_params['vulnerability_id']  # noqa: E501

        query_params = list(local_var_params.get('query_params', {}).items())

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['tokenAuth']  # noqa: E501

        response_type = 'VulnerabilityRead'
        if 'response_type' in kwargs:
            response_type = kwargs['response_type']

        return self.api_client.call_api(
            '/vulnerabilities/{vulnerabilityId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=response_type,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
