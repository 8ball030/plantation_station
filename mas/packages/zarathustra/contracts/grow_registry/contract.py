# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2023 zarathustra
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

"""This module contains the GrowRegistry contract interface."""

from typing import Any

from aea.common import JSONLike
from aea.configurations.base import PublicId
from aea.contracts.base import Contract
from aea.crypto.base import LedgerApi

PUBLIC_ID = PublicId.from_str("zarathustra/grow_registry:0.1.0")

Address = str


class GrowRegistryContract(Contract):
    """GrowRegistryContract"""

    contract_id = PUBLIC_ID

    @classmethod
    def get_raw_transaction(
        cls, ledger_api: LedgerApi, contract_address: str, **kwargs: Any
    ) -> JSONLike:
        """
        Handler method for the 'GET_RAW_TRANSACTION' requests.

        Implement this method in the sub class if you want
        to handle the contract requests manually.

        :param ledger_api: the ledger apis.
        :param contract_address: the contract address.
        :param kwargs: the keyword arguments.
        :return: the tx  # noqa: DAR202
        """
        raise NotImplementedError

    @classmethod
    def get_raw_message(
        cls, ledger_api: LedgerApi, contract_address: str, **kwargs: Any
    ) -> bytes:
        """
        Handler method for the 'GET_RAW_MESSAGE' requests.

        Implement this method in the sub class if you want
        to handle the contract requests manually.

        :param ledger_api: the ledger apis.
        :param contract_address: the contract address.
        :param kwargs: the keyword arguments.
        :return: the tx  # noqa: DAR202
        """
        raise NotImplementedError

    @classmethod
    def get_state(
        cls, ledger_api: LedgerApi, contract_address: str, **kwargs: Any
    ) -> JSONLike:
        """
        Handler method for the 'GET_STATE' requests.

        Implement this method in the sub class if you want
        to handle the contract requests manually.

        :param ledger_api: the ledger apis.
        :param contract_address: the contract address.
        :param kwargs: the keyword arguments.
        :return: the tx  # noqa: DAR202
        """
        raise NotImplementedError

    @classmethod
    def approve(
        cls,
        ledger_api: LedgerApi,
        contract_address: Address,
        spender: Address,
        id: int,
    ) -> None:

        contract_interface = cls.get_instance(
            ledger_api=ledger_api,
            contract_address=contract_address,
        )

        contract_interface.functions.approve(spender, id).call()

    @classmethod
    def create(
        cls,
        ledger_api: LedgerApi,
        contract_address: Address,
        grow_owner: Address,
        grower: Address,
        grow_hash: byts,
    ) -> int:

        contract_interface = cls.get_instance(
            ledger_api=ledger_api,
            contract_address=contract_address,
        )

        grow_id = contract_interface.functions.create(
            grow_owner, grower, grow_hash
        ).call()

        return grow_id

    @classmethod
    def propose_to_harvest(
        cls,
        ledger_api: LedgerApi,
        contract_address: Address,
        grow_id: int,
    ) -> None:

        contract_interface = cls.get_instance(
            ledger_api=ledger_api,
            contract_address=contract_address,
        )

        contract_interface.functions.proposeToHarvest(grow_id).call()

    @classmethod
    def harvest(
        cls,
        ledger_api: LedgerApi,
        contract_address: Address,
        grow_id: int,
    ) -> None:

        contract_interface = cls.get_instance(
            ledger_api=ledger_api,
            contract_address=contract_address,
        )

        contract_interface.functions.harvest(grow_id).call()

    @classmethod
    def redeem(
        cls,
        ledger_api: LedgerApi,
        contract_address: Address,
        grow_id: int,
    ) -> None:

        contract_interface = cls.get_instance(
            ledger_api=ledger_api,
            contract_address=contract_address,
        )

        contract_interface.functions.redeem(grow_id).call()

    @classmethod
    def update_hash(
        cls,
        ledger_api: LedgerApi,
        contract_address: Address,
        grow_id: int,
        grow_hash: bytes,
    ) -> None:

        contract_interface = cls.get_instance(
            ledger_api=ledger_api,
            contract_address=contract_address,
        )

        contract_interface.functions.updateHash(grow_id, grow_hash).call()
