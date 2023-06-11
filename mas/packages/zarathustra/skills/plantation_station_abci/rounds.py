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

"""This package contains the rounds of PlantationStationAbciApp."""

from enum import Enum
from typing import Dict, List, Optional, Set, Tuple, Mapping

from packages.valory.skills.abstract_round_abci.base import (
    AbciApp,
    AbciAppTransitionFunction,
    AbstractRound,
    CollectDifferentUntilThresholdRound,
    VotingRound,
    AppState,
    BaseSynchronizedData,
    DegenerateRound,
    EventToTimeout,
    DeserializedCollection,
    CollectSameUntilThresholdRound,
    get_name,
)

from packages.zarathustra.skills.plantation_station_abci.payloads import (
    AttestProposalPayload,
    CheckHarvestProposalPayload,
    ControlAdjustmentPayload,
    FederatedLearningPayload,
    ObservationCollectionPayload,
    PrepareAttestationTransactionPayload,
    PrepareObservationTransactionPayload,
    ReadSensorDataPayload,
)

DUMMY_DATA = dict(
    signature="",
    data_json="",
    most_voted_tx_hash="b0e6add595e00477cf347d09797b156719dc5233283ac76e4efce2a674fe72d9",
)


class Event(Enum):
    """PlantationStationAbciApp Events"""

    NO_PROPOSALS = "no_proposals"
    DONE = "done"
    ROUND_TIMEOUT = "round_timeout"
    PROPOSALS = "proposals"
    NO_MAJORITY = "no_majority"


class SynchronizedData(BaseSynchronizedData):
    """
    Class to represent the synchronized data.

    This data is replicated by the tendermint application.
    """

    @property
    def most_voted_tx_hash(self) -> float:
        """Get the most_voted_tx_hash."""
        return cast(float, self.db.get_strict("most_voted_tx_hash"))

    def _get_deserialized(self, key: str) -> DeserializedCollection:
        """Strictly get a collection and return it deserialized."""
        serialized = self.db.get_strict(key)
        deserialized = CollectionRound.deserialize_collection(serialized)
        return cast(DeserializedCollection, deserialized)

    @property
    def participant_to_observations(self) -> Mapping[str, ObservationCollectionPayload]:
        """Get the participant_to_observations."""
        return cast(
            Mapping[str, ObservationCollectionPayload],
            self._get_deserialized("participant_to_observations"),
        )

    @property
    def participant_to_signatures(self) -> Dict[str, Optional[str]]:
        """Get the `participant_to_signatures`."""
        participant_to_payload = cast(
            Mapping[str, PrepareAttestationTransactionPayload],
            self._get_deserialized("participant_to_signatures"),
        )
        return {
            agent_address: payload.signature
            for agent_address, payload in participant_to_payload.items()
        }

    @property
    def signature(self) -> str:
        """Get the current agent's signature."""
        return str(self.db.get("signature", {}))

    @property
    def data_json(self) -> str:
        """Get the data json."""
        return str(self.db.get("data_json", ""))


class AttestProposalRound(AbstractRound):
    """AttestProposalRound"""

    payload_class = AttestProposalPayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        synchronized_data = self.synchronized_data
        return synchronized_data, Event.DONE

    def check_payload(self, payload: AttestProposalPayload) -> None:
        """Check payload."""

    def process_payload(self, payload: AttestProposalPayload) -> None:
        """Process payload."""


class CheckHarvestProposalRound(AbstractRound):
    """CheckHarvestProposalRound"""

    payload_class = CheckHarvestProposalPayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        synchronized_data = self.synchronized_data
        if True:
            return synchronized_data, Event.PROPOSALS
        return synchronized_data, Event.NO_PROPOSALS

    def check_payload(self, payload: CheckHarvestProposalPayload) -> None:
        """Check payload."""

    def process_payload(self, payload: CheckHarvestProposalPayload) -> None:
        """Process payload."""


class ControlAdjustmentRound(AbstractRound):
    """ControlAdjustmentRound"""

    payload_class = ControlAdjustmentPayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        synchronized_data = self.synchronized_data
        return synchronized_data, Event.DONE

    def check_payload(self, payload: ControlAdjustmentPayload) -> None:
        """Check payload."""

    def process_payload(self, payload: ControlAdjustmentPayload) -> None:
        """Process payload."""


class FederatedLearningRound(AbstractRound):
    """FederatedLearningRound"""

    payload_class = FederatedLearningPayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        synchronized_data = self.synchronized_data
        return synchronized_data, Event.DONE

    def check_payload(self, payload: FederatedLearningPayload) -> None:
        """Check payload."""

    def process_payload(self, payload: FederatedLearningPayload) -> None:
        """Process payload."""


class ObservationCollectionRound(CollectDifferentUntilThresholdRound):
    """ObservationCollectionRound"""

    payload_class = ObservationCollectionPayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData
    collection_key = get_name(SynchronizedData.participant_to_observations)

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        synchronized_data = self.synchronized_data
        return synchronized_data, Event.DONE

    def check_payload(self, payload: ObservationCollectionPayload) -> None:
        """Check payload."""

    def process_payload(self, payload: ObservationCollectionPayload) -> None:
        """Process payload."""


class PrepareAttestationTransactionRound(CollectSameUntilThresholdRound):
    """PrepareAttestationTransactionRound"""

    payload_class = PrepareAttestationTransactionPayload
    synchronized_data_class = SynchronizedData
    done_event = Event.DONE
    no_majority_event = Event.NO_MAJORITY

    collection_key = get_name(SynchronizedData.participant_to_signatures)
    selection_key = (
        get_name(SynchronizedData.signature),
        get_name(SynchronizedData.data_json),
        get_name(SynchronizedData.most_voted_tx_hash),
    )


class PrepareObservationTransactionRound(AbstractRound):
    """PrepareObservationTransactionRound"""

    payload_class = PrepareObservationTransactionPayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""

        most_voted_tx_hash = self.context.synchronized_data.most_voted_tx_hash
        payload = self.payload_class(
            sender=self.context.agent_address, 
            **DUMMY_DATA,
            )
        self.send_a2a_transaction(payload)

        synchronized_data = self.synchronized_data
        return synchronized_data, Event.DONE        

    # def check_payload(self, payload: PrepareObservationTransactionPayload) -> None:
    #     """Check payload."""

    # def process_payload(self, payload: PrepareObservationTransactionPayload) -> None:
    #     """Process payload."""


class ReadSensorDataRound(AbstractRound):
    """ReadSensorDataRound"""

    payload_class = ReadSensorDataPayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        synchronized_data = self.synchronized_data
        return synchronized_data, Event.DONE

    def check_payload(self, payload: ReadSensorDataPayload) -> None:
        """Check payload."""

    def process_payload(self, payload: ReadSensorDataPayload) -> None:
        """Process payload."""


class ResetPlantationStationRound(DegenerateRound):
    """ResetPlantationStationRound"""


class TransactionSubmissionRound(DegenerateRound):
    """TransactionSubmissionRound"""


class PlantationStationAbciApp(AbciApp[Event]):
    """PlantationStationAbciApp"""

    initial_round_cls: AppState = ObservationCollectionRound
    initial_states: Set[AppState] = {ObservationCollectionRound}
    transition_function: AbciAppTransitionFunction = {
        ObservationCollectionRound: {
            Event.DONE: FederatedLearningRound,
            Event.ROUND_TIMEOUT: ResetPlantationStationRound,
            Event.NO_MAJORITY: ResetPlantationStationRound
        },
        FederatedLearningRound: {
            Event.DONE: CheckHarvestProposalRound,
            Event.ROUND_TIMEOUT: ResetPlantationStationRound,
            Event.NO_MAJORITY: ResetPlantationStationRound
        },
        CheckHarvestProposalRound: {
            Event.NO_PROPOSALS: ReadSensorDataRound,
            Event.PROPOSALS: AttestProposalRound,
            Event.ROUND_TIMEOUT: ResetPlantationStationRound,
            Event.NO_MAJORITY: ResetPlantationStationRound
        },
        AttestProposalRound: {
            Event.DONE: PrepareAttestationTransactionRound,
            Event.ROUND_TIMEOUT: ResetPlantationStationRound,
            Event.NO_MAJORITY: ResetPlantationStationRound
        },
        PrepareAttestationTransactionRound: {
            Event.DONE: TransactionSubmissionRound,
            Event.ROUND_TIMEOUT: ResetPlantationStationRound,
            Event.NO_MAJORITY: ResetPlantationStationRound
        },
        ReadSensorDataRound: {
            Event.DONE: ControlAdjustmentRound,
            Event.ROUND_TIMEOUT: ResetPlantationStationRound,
            Event.NO_MAJORITY: ResetPlantationStationRound
        },
        ControlAdjustmentRound: {
            Event.DONE: PrepareObservationTransactionRound,
            Event.ROUND_TIMEOUT: ResetPlantationStationRound,
            Event.NO_MAJORITY: ResetPlantationStationRound
        },
        PrepareObservationTransactionRound: {
            Event.DONE: TransactionSubmissionRound,
            Event.ROUND_TIMEOUT: ResetPlantationStationRound,
            Event.NO_MAJORITY: ResetPlantationStationRound
        },
        TransactionSubmissionRound: {},
        ResetPlantationStationRound: {}
    }
    final_states: Set[AppState] = {ResetPlantationStationRound, TransactionSubmissionRound}
    event_to_timeout: EventToTimeout = {}
    cross_period_persisted_keys: Set[str] = set()
    db_pre_conditions: Dict[AppState, Set[str]] = {
        ObservationCollectionRound: {
            get_name(SynchronizedData.participants),
        },
    }
    db_post_conditions: Dict[AppState, Set[str]] = {
        ResetPlantationStationRound: set(),
        TransactionSubmissionRound: {get_name(SynchronizedData.most_voted_tx_hash)},
    }
