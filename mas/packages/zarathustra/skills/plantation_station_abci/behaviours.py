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
from typing import Generator, Set, Type, cast

from packages.valory.skills.abstract_round_abci.base import AbstractRound
from packages.valory.skills.abstract_round_abci.behaviours import (
    AbstractRoundBehaviour,
    BaseBehaviour,
)
from packages.zarathustra.skills.plantation_station_abci.models import Params
from packages.zarathustra.skills.plantation_station_abci.rounds import (
    AttestProposalPayload,
    AttestProposalRound,
    CheckHarvestProposalPayload,
    CheckHarvestProposalRound,
    ControlAdjustmentPayload,
    ControlAdjustmentRound,
    FederatedLearningPayload,
    FederatedLearningRound,
    ObservationCollectionPayload,
    ObservationCollectionRound,
    PlantationStationAbciApp,
    PrepareAttestationTransactionPayload,
    PrepareAttestationTransactionRound,
    PrepareObservationTransactionPayload,
    PrepareObservationTransactionRound,
    ReadSensorDataPayload,
    ReadSensorDataRound,
    SynchronizedData,
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
            sender = self.context.agent_address
            payload = PrepareAttestationTransactionPayload(sender=sender)

        with self.context.benchmark_tool.measure(self.behaviour_id).consensus():
            yield from self.send_a2a_transaction(payload)
            yield from self.wait_until_round_end()

        self.set_done()


class PrepareObservationTransactionBehaviour(PlantationStationBaseBehaviour):
    """PrepareObservationTransactionBehaviour"""

    matching_round: Type[AbstractRound] = PrepareObservationTransactionRound

    # TODO: implement logic required to set payload content for synchronization
    def async_act(self) -> Generator:
        """Do the act, supporting asynchronous execution."""

        with self.context.benchmark_tool.measure(self.behaviour_id).local():
            sender = self.context.agent_address
            payload = PrepareObservationTransactionPayload(sender=sender)

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
        ReadSensorDataBehaviour,
    ]
