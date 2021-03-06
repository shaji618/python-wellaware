from __future__ import unicode_literals

from wellaware.constants import Config, make_headers
from wellaware.base.base_resource import RestClient
from wellaware.exceptions import InvalidInputException
from token import Token


class Tokens(object):

    ENDPOINT = '/tokens'
    REST_CLIENT = RestClient()

    @classmethod
    def get_base_uri(cls, endpoint, **id_dict):
        if id_dict:
            return endpoint.format(**id_dict)
        return endpoint

    @classmethod
    def login(cls, username, password, expires=True, parameters=None):
        form_data = {'username': username, 'password': password, 'expires': expires}
        response = cls.REST_CLIENT.post(
            cls.get_base_uri(cls.ENDPOINT), data=form_data, headers=Config.auth_headers, params=parameters
        )

        response = cls.REST_CLIENT.handle_response(response)
        return Token(jwt=response.json()['token'])

    @classmethod
    def impersonate(cls, token, tenant_id=None, subject_id=None, role=None, expires=True, parameters=None):
        data = {'expires': expires}
        if tenant_id is not None and role is not None:
            data['tenantId'] = tenant_id
            data['role'] = role
        elif subject_id is not None:
            data['subjectId'] = subject_id
        else:
            raise InvalidInputException(422, "Must provide either tenant_id and role OR subject_id")

        response = cls.REST_CLIENT.post(
            cls.get_base_uri(cls.ENDPOINT), data=data, headers=make_headers(token), params=parameters
        )

        response = cls.REST_CLIENT.handle_response(response)
        return Token(jwt=response.json()['token'])
