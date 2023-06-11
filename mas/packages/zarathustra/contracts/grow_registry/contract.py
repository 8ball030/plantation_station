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

import logging
from typing import Any

from aea.common import JSONLike
from aea.configurations.base import PublicId
from aea.contracts.base import Contract
from aea_ledger_ethereum import EthereumApi, LedgerApi
from web3.types import TxParams

PUBLIC_ID = PublicId.from_str("zarathustra/grow_registry:0.1.0")

_logger = logging.getLogger(
    f"aea.packages.{PUBLIC_ID.author}.contracts.{PUBLIC_ID.name}.contract"
)

Address = str


class GrowRegistryContract(Contract):
    """GrowRegistryContract"""

    contract_id = PUBLIC_ID

    @classmethod
    def get_raw_transaction(
        cls, ledger_api: LedgerApi, contract_address: str, **kwargs: Any
    ) -> JSONLike:
        """Get raw transaction."""
        raise NotImplementedError

    @classmethod
    def get_raw_message(
        cls, ledger_api: LedgerApi, contract_address: str, **kwargs: Any
    ) -> bytes:
        """Get raw message."""
        raise NotImplementedError

    @classmethod
    def get_state(
        cls, ledger_api: LedgerApi, contract_address: str, **kwargs: Any
    ) -> JSONLike:
        """Get state."""
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
        grow_hash: bytes,
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
    ) -> JSONLike:
        """
        Get the encoded params for `updateHash`.

        :param ledger_api: ledger API object.
        :param contract_address: address of the NFT
        :param grow_id: grow ID
        :param grow_hash: grow hash
        :param sender_address: The address of the tx sender.
        :param gas: Gas
        :param gas_price: Gas Price
        :param max_fee_per_gas: max
        :param max_priority_fee_per_gas: max
        :return: the raw transaction
        """
        eth_api = cast(EthereumApi, ledger_api)
        contract = cls.get_instance(ledger_api, contract_address)
        tx_parameters = TxParams()

        if gas_price is not None:
            tx_parameters["gasPrice"] = Wei(gas_price)  # pragma: nocover

        if max_fee_per_gas is not None:
            tx_parameters["maxFeePerGas"] = Wei(max_fee_per_gas)  # pragma: nocover

        if max_priority_fee_per_gas is not None:
            tx_parameters["maxPriorityFeePerGas"] = Wei(  # pragma: nocover
                max_priority_fee_per_gas
            )

        if (
            gas_price is None
            and max_fee_per_gas is None
            and max_priority_fee_per_gas is None
        ):
            tx_parameters.update(eth_api.try_get_gas_pricing())

        if gas is not None:
            tx_parameters["gas"] = Wei(gas)

        nonce = eth_api._try_get_transaction_count(  # pylint: disable=protected-access
            sender_address
        )
        tx_parameters["nonce"] = Nonce(nonce)

        if nonce is None:
            raise ValueError("No nonce returned.")  # pragma: nocover

        raw_tx = contract.functions.updateHash(grow_id, grow_hash).buildTransaction(
            tx_params
        )

        return raw_tx
