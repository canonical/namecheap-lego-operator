#!/usr/bin/env python3
# Copyright 2022 Canonical Ltd.
# See LICENSE file for licensing details.

"""Retrieves certificates from an ACME server using the namecheap dns provider."""

import logging
from typing import Dict, Optional

from charms.acme_client_operator.v0.acme_client import AcmeClient  # type: ignore[import]
from ops.main import main

logger = logging.getLogger(__name__)


class NamecheapAcmeOperatorCharm(AcmeClient):
    """Main class that is instantiated every time an event occurs."""

    def __init__(self, *args):
        """Uses the acme_client library to manage events."""
        super().__init__(*args)

    @property
    def _namecheap_api_key(self) -> Optional[str]:
        """Returns email from config."""
        return self.model.config.get("namecheap-api-key")

    @property
    def _namecheap_api_user(self) -> Optional[str]:
        """Returns email from config."""
        return self.model.config.get("namecheap-api-user")

    @property
    def _namecheap_http_timeout(self) -> Optional[str]:
        """Returns email from config."""
        return str(self.model.config.get("namecheap-http-timeout"))

    @property
    def _namecheap_polling_interval(self) -> Optional[str]:
        """Returns email from config."""
        return str(self.model.config.get("namecheap-polling-interval"))

    @property
    def _namecheap_propagation_timeout(self) -> Optional[str]:
        """Returns email from config."""
        return str(self.model.config.get("namecheap-propagation-timeout"))

    @property
    def _namecheap_ttl(self) -> Optional[str]:
        """Returns email from config."""
        return str(self.model.config.get("namecheap-ttl"))

    @property
    def _namecheap_sandbox(self) -> Optional[str]:
        """Returns email from config."""
        return self.model.config.get("namecheap-sandbox")

    @property
    def _plugin_config(self) -> Dict[str, str]:
        """Plugin specific additional configuration for the command."""
        additional_config = {}
        if self._namecheap_api_user:
            additional_config.update({"NAMECHEAP_API_KEY": self._namecheap_api_user})
        if self._namecheap_api_key:
            additional_config.update({"NAMECHEAP_API_KEY": self._namecheap_api_key})
        if self._namecheap_ttl:
            additional_config.update({"NAMECHEAP_TTL": self._namecheap_ttl})
        if self._namecheap_sandbox:
            additional_config.update({"NAMECHEAP_SANDBOX": self._namecheap_sandbox})
        if self._namecheap_propagation_timeout:
            additional_config.update(
                {"NAMECHEAP_PROPAGATION_TIMEOUT": self._namecheap_propagation_timeout}
            )
        if self._namecheap_polling_interval:
            additional_config.update(
                {"NAMECHEAP_POLLING_INTERVAL": self._namecheap_polling_interval}
            )
        if self._namecheap_http_timeout:
            additional_config.update({"NAMECHEAP_HTTP_TIMEOUT": self._namecheap_http_timeout})
        return additional_config

    @property
    def _email(self) -> Optional[str]:
        """Returns email from config."""
        return self.model.config.get("email")

    @property
    def _plugin(self) -> str:
        """Returns plugin."""
        return "namecheap"


if __name__ == "__main__":  # pragma: nocover
    main(NamecheapAcmeOperatorCharm)
