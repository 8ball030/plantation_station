# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2023 Valory AG
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

"""This package contains round behaviours of PlantationStationAbciApp."""

from abc import ABC
from typing import Generator, Set, Type, Dict, Tuple, cast
import copy
import json
import hashlib

from packages.valory.skills.abstract_round_abci.base import AbstractRound
from packages.valory.skills.abstract_round_abci.behaviours import (
    AbstractRoundBehaviour,
    BaseBehaviour,
)

from packages.zarathustra.skills.plantation_station_abci.models import Params
from packages.zarathustra.skills.plantation_station_abci.rounds import (
    SynchronizedData,
    PlantationStationAbciApp,
    AttestProposalRound,
    CheckHarvestProposalRound,
    ControlAdjustmentRound,
    FederatedLearningRound,
    ObservationCollectionRound,
    PrepareAttestationTransactionRound,
    PrepareObservationTransactionRound,
    ReadSensorDataRound,
)
from packages.zarathustra.skills.plantation_station_abci.rounds import (
    AttestProposalPayload,
    CheckHarvestProposalPayload,
    ControlAdjustmentPayload,
    FederatedLearningPayload,
    ObservationCollectionPayload,
    PrepareAttestationTransactionPayload,
    PrepareObservationTransactionPayload,
    ReadSensorDataPayload,
)
# from packages.valory.contracts.gnosis_safe.contract import SafeOperation

DUMMY_DATA = dict(
    signature="",
    data_json="",
    most_voted_tx_hash="b0e6add595e00477cf347d09797b156719dc5233283ac76e4efce2a674fe72d9",
)


class PlantationStationBaseBehaviour(BaseBehaviour, ABC):
    """Base behaviour for the plantation_station_abci skill."""

    @property
    def synchronized_data(self) -> SynchronizedData:
        """Return the synchronized data."""
        return cast(SynchronizedData, super().synchronized_data)

    @property
    def params(self) -> Params:
        """Return the params."""
        return cast(Params, super().params)


class AttestProposalBehaviour(PlantationStationBaseBehaviour):
    """AttestProposalBehaviour"""

    matching_round: Type[AbstractRound] = AttestProposalRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = AttestProposalPayload(sender=sender)

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()


class CheckHarvestProposalBehaviour(PlantationStationBaseBehaviour):
    """CheckHarvestProposalBehaviour"""

    matching_round: Type[AbstractRound] = CheckHarvestProposalRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = CheckHarvestProposalPayload(sender=sender)

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()


class ControlAdjustmentBehaviour(PlantationStationBaseBehaviour):
    """ControlAdjustmentBehaviour"""

    matching_round: Type[AbstractRound] = ControlAdjustmentRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = ControlAdjustmentPayload(sender=sender)

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()


class FederatedLearningBehaviour(PlantationStationBaseBehaviour):
    """FederatedLearningBehaviour"""

    matching_round: Type[AbstractRound] = FederatedLearningRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = FederatedLearningPayload(sender=sender)

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()


class ObservationCollectionBehaviour(PlantationStationBaseBehaviour):
    """ObservationCollectionBehaviour"""

    matching_round: Type[AbstractRound] = ObservationCollectionRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = ObservationCollectionPayload(sender=sender)

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()


class PrepareAttestationTransactionBehaviour(PlantationStationBaseBehaviour):
    """PrepareAttestationTransactionBehaviour"""

    matching_round: Type[AbstractRound] = PrepareAttestationTransactionRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            signature = data_json = None
            payload_string = "0xa2c77193d1b3e9asdaaksdjaskdjalksdjaslkjdaskasdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddsjdalkjsdaslkjdakjsdlkajsdaklsjdakjsdaksjdaksjdaksjdalkjsdalkjsdakjsdakljsdakjsdakjsdakjsdakjsdakjda6db44c0bfef9e3554748be5821b53696135da15a2d061c55c9"
            tx_params = self.prepare_tx_params()
            self.context.logger.error(f"tx_params: {tx_params}")
            if payload_string is not None:
                signature, data_json = yield from self.get_data_signature(tx_params)
            # breakpoint()
            payload = PrepareAttestationTransactionPayload(
                self.context.agent_address, signature, data_json, payload_string
            )
            self.context.logger.error(f"Attestation payload: {payload}")

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()

    def get_data_signature(self, data: Dict) -> Generator[None, None, Tuple[str, str]]:
        """Get signature for the data."""

        data = copy.deepcopy(data)

        data.pop("agent_address", None)  # agent address is unique, need to remove it
        data_json = json.dumps(data, sort_keys=True)
        self.context.logger.error(f"data_json: {data_json}")
        data_bytes = data_json.encode("ascii")
        self.context.logger.error(f"data_bytes: {data_bytes}")
        hash_bytes = hashlib.sha256(data_bytes).digest()
        self.context.logger.error(f"hash_bytes: {hash_bytes}")

        signature_hex = yield from self.get_signature(
            hash_bytes, is_deprecated_mode=True
        )
        # remove the leading '0x'
        signature_hex = signature_hex[2:]
        self.context.logger.info(f"Data signature: {signature_hex}")
        return signature_hex, data_json

    def prepare_tx_params(self, ) -> dict:

        tx_params = dict(
            safe_tx_hash="b0e6add595e00477cf347d09797b156719dc5233283ac76e4efce2a674fe72d9",
            ether_value=0,
            safe_tx_gas=40000000,
            to_address="0x77E9b2EF921253A171Fa0CB9ba80558648Ff7215",
            operation=0,  # == SafeOperation.CALL.value,
            base_gas=0,
            safe_gas_price=0,
            gas_token="0x0000000000000000000000000000000000000000",
            refund_receiver=0x0000000000000000000000000000000000000000,
            use_flashbots=True,
            data="PrepareAttestationTransactionBehaviour",
        )

        return tx_params


class PrepareObservationTransactionBehaviour(PlantationStationBaseBehaviour):
    """PrepareObservationTransactionBehaviour"""

    matching_round: Type[AbstractRound] = PrepareObservationTransactionRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            data = DUMMY_DATA
            payload = PrepareObservationTransactionPayload(sender=sender, **data)

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()


class ReadSensorDataBehaviour(PlantationStationBaseBehaviour):
    """ReadSensorDataBehaviour"""

    matching_round: Type[AbstractRound] = ReadSensorDataRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = ReadSensorDataPayload(sender=sender)

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()


class PlantationStationRoundBehaviour(AbstractRoundBehaviour):
    """PlantationStationRoundBehaviour"""

    initial_behaviour_cls = ObservationCollectionBehaviour
    abci_app_cls = PlantationStationAbciApp  # type: ignore
    behaviours: Set[Type[BaseBehaviour]] = [
        AttestProposalBehaviour,
        CheckHarvestProposalBehaviour,
        ControlAdjustmentBehaviour,
        FederatedLearningBehaviour,
        ObservationCollectionBehaviour,
        PrepareAttestationTransactionBehaviour,
        PrepareObservationTransactionBehaviour,
        ReadSensorDataBehaviour
    ]
