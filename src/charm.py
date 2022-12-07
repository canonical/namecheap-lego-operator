#!/usr/bin/env python3
# Copyright 2022 Ubuntu
# See LICENSE file for licensing details.

"""Provides Let's Encrypt certificates for namecheap dns provider."""

import logging
from typing import Optional

from charms.acme_client_operator.v0.acme_client import AcmeClient  # type: ignore[import]
from ops.main import main

logger = logging.getLogger(__name__)


class NamecheapAcmeOperatorCharm(AcmeClient):
    """Charm the service."""

    def __init__(self, *args):
        """Uses the Orc8rBase library to manage events."""
        super().__init__(*args)
        self._server = "https://acme-staging-v02.api.letsencrypt.org/directory"

    @property
    def email(self) -> Optional[str]:
        """Returns email from config."""
        return self.model.config.get("email")

    @property
    def namecheap_api_key(self) -> Optional[str]:
        """Returns email from config."""
        return self.model.config.get("namecheap-api-key")

    @property
    def namecheap_api_user(self) -> Optional[str]:
        """Returns email from config."""
        return self.model.config.get("namecheap-api-user")

    @property
    def domain(self) -> Optional[str]:
        """Returns email from config."""
        return self.model.config.get("domain")

    @property
    def namecheap_http_timeout(self) -> Optional[str]:
        """Returns email from config."""
        return self.model.config.get("namecheap-http-timeout")

    @property
    def namecheap_polling_interval(self) -> Optional[str]:
        """Returns email from config."""
        return self.model.config.get("namecheap-polling-interval")

    @property
    def namecheap_propagation_timeout(self) -> Optional[str]:
        """Returns email from config."""
        return self.model.config.get("namecheap-propagation-timeout")

    @property
    def namecheap_sandbox(self) -> Optional[str]:
        """Returns email from config."""
        return self.model.config.get("namecheap-sandbox")

    @property
    def namecheap_ttl(self) -> Optional[str]:
        """Returns email from config."""
        return self.model.config.get("namecheap-ttl")

    @property
    def cmd(self):
        """Command to run to get the certificate."""
        return [
            "lego",
            "--email",
            self.email,
            "--accept-tos",
            "--csr",
            "/tmp/csr.pem",
            "--server",
            self._server,
            "--dns",
            "namecheap",
            "--domains",
            self.domain,
            "run",
        ]

    @property
    def certs_path(self):
        """Path to the certificates."""
        return "/tmp/.lego/certificates/"

    @property
    def plugin_config(self):
        """Plugin specific additional configuration for the command."""
        additional_config = {}
        if self.namecheap_api_user:
            additional_config["NAMECHEAP_API_USER"] = self.namecheap_api_user
        if self.namecheap_api_key:
            additional_config["NAMECHEAP_API_KEY"] = self.namecheap_api_key
        if self.namecheap_ttl:
            additional_config.update({"NAMECHEAP_TTL": self.namecheap_ttl})
        if self.namecheap_sandbox:
            additional_config.update({"NAMECHEAP_SANDBOX": self.namecheap_sandbox})
        if self.namecheap_propagation_timeout:
            additional_config.update(
                {"NAMECHEAP_PROPAGATION_TIMEOUT": self.namecheap_propagation_timeout}
            )
        if self.namecheap_polling_interval:
            additional_config.update(
                {"NAMECHEAP_POLLING_INTERVAL": self.namecheap_polling_interval}
            )
        if self.namecheap_http_timeout:
            additional_config.update({"NAMECHEAP_HTTP_TIMEOUT": self.namecheap_http_timeout})


if __name__ == "__main__":  # pragma: nocover
    main(NamecheapAcmeOperatorCharm)
