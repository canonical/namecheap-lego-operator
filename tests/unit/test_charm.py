# Copyright 2022 Canonical Ltd.
# See LICENSE file for licensing details.
#
# Learn more about testing at: https://juju.is/docs/sdk/testing

import unittest

from ops import testing
from ops.model import ActiveStatus, BlockedStatus
from ops.testing import Harness

from charm import NamecheapAcmeOperatorCharm

testing.SIMULATE_CAN_CONNECT = True


class TestCharm(unittest.TestCase):
    def setUp(self):
        self.harness = Harness(NamecheapAcmeOperatorCharm)
        self.harness.set_leader(True)
        self.harness.set_can_connect("lego", True)
        self.addCleanup(self.harness.cleanup)
        self.harness.begin()
        self.r_id = self.harness.add_relation("certificates", "remote")
        self.harness.add_relation_unit(self.r_id, "remote/0")

    def test_given_config_changed_when_email_is_valid_then_status_is_active(self):
        self.harness.update_config(
            {
                "email": "example@email.com",
                "namecheap-api-user": "example",
                "namecheap-api-key": "example",
            }
        )
        self.assertEqual(self.harness.model.unit.status, ActiveStatus())

    def test_given_config_changed_when_email_is_invalid_then_status_is_blocked(self):
        self.harness.update_config(
            {
                "email": "invalid-email",
                "namecheap-api-user": "example",
                "namecheap-api-key": "example",
            }
        )
        self.assertEqual(self.harness.model.unit.status, BlockedStatus("Invalid email address"))

    def test_given_config_changed_when_api_user_is_not_provided_then_status_is_blocked(self):
        self.harness.update_config(
            {
                "email": "invalid-email",
            }
        )
        self.assertEqual(
            self.harness.model.unit.status,
            BlockedStatus("namecheap-api-key and namecheap-api-user must be set"),
        )
