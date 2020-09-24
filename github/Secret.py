# -*- coding: utf-8 -*-

import github.GithubObject

class Secret(github.GithubObject.CompletableGithubObject):
    """
    This class represents Secrets. The reference can be found here https://docs.github.com/en/rest/reference/actions#list-organization-secrets
    """

    def __repr__(self):
        return self.get__repr__({"name": self._name.value})

    @property
    def name(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._name)
        return self._name.value

    @property
    def created_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._created_at)
        return self._created_at.value

    @property
    def updated_at(self):
        """
        :type: datetime.datetime
        """
        self._completeIfNotSet(self._updated_at)
        return self._updated_at.value

    @property
    def visibility(self):
        """
        :type: bool
        """
        self._completeIfNotSet(self._visibility)
        return self._visibility.value

    @property
    def selected_repositories(self):
        """
        :type: bool
        """
        self._completeIfNotSet(self._selected_repositories)
        return self._selected_repositories.value

    @property
    def url(self):
        """
        :type: string
        """
        self._completeIfNotSet(self._url)
        return self._url.value

    def update(
        self,
        encrypted_value,
        key_id,
        visibility,
        selected_repository_ids=None
    ):
        """
        :calls: `PUT /orgs/{org}/actions/secrets/{secret_name} <https://docs.github.com/en/rest/reference/actions#create-or-update-an-organization-secret>`_
        :encrypted_value: string
        :key_id:
        :visibility: string
        :selected_repositoy_ids: list of ints
        """
        headers, data = self._requester.requestJsonAndCheck("POST", self.url)
