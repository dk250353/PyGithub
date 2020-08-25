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

