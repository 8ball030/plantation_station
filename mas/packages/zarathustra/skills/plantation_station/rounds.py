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
from typing import Dict, List, Optional, Set, Tuple

from packages.valory.skills.abstract_round_abci.base import (
    AbciApp,
    AbciAppTransitionFunction,
    AbstractRound,
    AppState,
    BaseSynchronizedData,
    DegenerateRound,
    EventToTimeout,
)

from packages.default_author.skills.plantation_station.payloads import (
    AttestProposalPayload,
    CheckHarvestProposalPayload,
    ControlAdjustmentPayload,
    FederatedLearningPayload,
    ObservationCollectionPayload,
    PrepareAttestationTransactionPayload,
    PrepareObservationTransactionPayload,
    ReadSensorDataPayload,
    RegistrationPayload,
    ResetAndPausePayload,
    TransactionSubmissionPayload,
)


class Event(Enum):
    """PlantationStationAbciApp Events"""

    NO_PROPOSALS = "no_proposals"
    PROPOSALS = "proposals"
    DONE = "done"
    NO_MAJORITY = "no_majority"
    ROUND_TIMEOUT = "round_timeout"
    RESET_TIMEOUT = "reset_timeout"


class SynchronizedData(BaseSynchronizedData):
    """
    Class to represent the synchronized data.

    This data is replicated by the tendermint application.
    """


class AttestProposalRound(AbstractRound):
    """AttestProposalRound"""

    payload_class = AttestProposalPayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    # TODO: replace AbstractRound with one of CollectDifferentUntilAllRound,
    # CollectSameUntilAllRound, CollectSameUntilThresholdRound,
    # CollectDifferentUntilThresholdRound, OnlyKeeperSendsRound, VotingRound,
    # from packages/valory/skills/abstract_round_abci/base.py
    # or implement the methods

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        raise NotImplementedError

    def check_payload(self, payload: AttestProposalPayload) -> None:
        """Check payload."""
        raise NotImplementedError

    def process_payload(self, payload: AttestProposalPayload) -> None:
        """Process payload."""
        raise NotImplementedError


class CheckHarvestProposalRound(AbstractRound):
    """CheckHarvestProposalRound"""

    payload_class = CheckHarvestProposalPayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    # TODO: replace AbstractRound with one of CollectDifferentUntilAllRound,
    # CollectSameUntilAllRound, CollectSameUntilThresholdRound,
    # CollectDifferentUntilThresholdRound, OnlyKeeperSendsRound, VotingRound,
    # from packages/valory/skills/abstract_round_abci/base.py
    # or implement the methods

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        raise NotImplementedError

    def check_payload(self, payload: CheckHarvestProposalPayload) -> None:
        """Check payload."""
        raise NotImplementedError

    def process_payload(self, payload: CheckHarvestProposalPayload) -> None:
        """Process payload."""
        raise NotImplementedError


class ControlAdjustmentRound(AbstractRound):
    """ControlAdjustmentRound"""

    payload_class = ControlAdjustmentPayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    # TODO: replace AbstractRound with one of CollectDifferentUntilAllRound,
    # CollectSameUntilAllRound, CollectSameUntilThresholdRound,
    # CollectDifferentUntilThresholdRound, OnlyKeeperSendsRound, VotingRound,
    # from packages/valory/skills/abstract_round_abci/base.py
    # or implement the methods

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        raise NotImplementedError

    def check_payload(self, payload: ControlAdjustmentPayload) -> None:
        """Check payload."""
        raise NotImplementedError

    def process_payload(self, payload: ControlAdjustmentPayload) -> None:
        """Process payload."""
        raise NotImplementedError


class FederatedLearningRound(AbstractRound):
    """FederatedLearningRound"""

    payload_class = FederatedLearningPayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    # TODO: replace AbstractRound with one of CollectDifferentUntilAllRound,
    # CollectSameUntilAllRound, CollectSameUntilThresholdRound,
    # CollectDifferentUntilThresholdRound, OnlyKeeperSendsRound, VotingRound,
    # from packages/valory/skills/abstract_round_abci/base.py
    # or implement the methods

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        raise NotImplementedError

    def check_payload(self, payload: FederatedLearningPayload) -> None:
        """Check payload."""
        raise NotImplementedError

    def process_payload(self, payload: FederatedLearningPayload) -> None:
        """Process payload."""
        raise NotImplementedError


class ObservationCollectionRound(AbstractRound):
    """ObservationCollectionRound"""

    payload_class = ObservationCollectionPayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    # TODO: replace AbstractRound with one of CollectDifferentUntilAllRound,
    # CollectSameUntilAllRound, CollectSameUntilThresholdRound,
    # CollectDifferentUntilThresholdRound, OnlyKeeperSendsRound, VotingRound,
    # from packages/valory/skills/abstract_round_abci/base.py
    # or implement the methods

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        raise NotImplementedError

    def check_payload(self, payload: ObservationCollectionPayload) -> None:
        """Check payload."""
        raise NotImplementedError

    def process_payload(self, payload: ObservationCollectionPayload) -> None:
        """Process payload."""
        raise NotImplementedError


class PrepareAttestationTransactionRound(AbstractRound):
    """PrepareAttestationTransactionRound"""

    payload_class = PrepareAttestationTransactionPayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    # TODO: replace AbstractRound with one of CollectDifferentUntilAllRound,
    # CollectSameUntilAllRound, CollectSameUntilThresholdRound,
    # CollectDifferentUntilThresholdRound, OnlyKeeperSendsRound, VotingRound,
    # from packages/valory/skills/abstract_round_abci/base.py
    # or implement the methods

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        raise NotImplementedError

    def check_payload(self, payload: PrepareAttestationTransactionPayload) -> None:
        """Check payload."""
        raise NotImplementedError

    def process_payload(self, payload: PrepareAttestationTransactionPayload) -> None:
        """Process payload."""
        raise NotImplementedError


class PrepareObservationTransactionRound(AbstractRound):
    """PrepareObservationTransactionRound"""

    payload_class = PrepareObservationTransactionPayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    # TODO: replace AbstractRound with one of CollectDifferentUntilAllRound,
    # CollectSameUntilAllRound, CollectSameUntilThresholdRound,
    # CollectDifferentUntilThresholdRound, OnlyKeeperSendsRound, VotingRound,
    # from packages/valory/skills/abstract_round_abci/base.py
    # or implement the methods

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        raise NotImplementedError

    def check_payload(self, payload: PrepareObservationTransactionPayload) -> None:
        """Check payload."""
        raise NotImplementedError

    def process_payload(self, payload: PrepareObservationTransactionPayload) -> None:
        """Process payload."""
        raise NotImplementedError


class ReadSensorDataRound(AbstractRound):
    """ReadSensorDataRound"""

    payload_class = ReadSensorDataPayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    # TODO: replace AbstractRound with one of CollectDifferentUntilAllRound,
    # CollectSameUntilAllRound, CollectSameUntilThresholdRound,
    # CollectDifferentUntilThresholdRound, OnlyKeeperSendsRound, VotingRound,
    # from packages/valory/skills/abstract_round_abci/base.py
    # or implement the methods

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        raise NotImplementedError

    def check_payload(self, payload: ReadSensorDataPayload) -> None:
        """Check payload."""
        raise NotImplementedError

    def process_payload(self, payload: ReadSensorDataPayload) -> None:
        """Process payload."""
        raise NotImplementedError


class RegistrationRound(AbstractRound):
    """RegistrationRound"""

    payload_class = RegistrationPayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    # TODO: replace AbstractRound with one of CollectDifferentUntilAllRound,
    # CollectSameUntilAllRound, CollectSameUntilThresholdRound,
    # CollectDifferentUntilThresholdRound, OnlyKeeperSendsRound, VotingRound,
    # from packages/valory/skills/abstract_round_abci/base.py
    # or implement the methods

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        raise NotImplementedError

    def check_payload(self, payload: RegistrationPayload) -> None:
        """Check payload."""
        raise NotImplementedError

    def process_payload(self, payload: RegistrationPayload) -> None:
        """Process payload."""
        raise NotImplementedError


class ResetAndPauseRound(AbstractRound):
    """ResetAndPauseRound"""

    payload_class = ResetAndPausePayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    # TODO: replace AbstractRound with one of CollectDifferentUntilAllRound,
    # CollectSameUntilAllRound, CollectSameUntilThresholdRound,
    # CollectDifferentUntilThresholdRound, OnlyKeeperSendsRound, VotingRound,
    # from packages/valory/skills/abstract_round_abci/base.py
    # or implement the methods

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        raise NotImplementedError

    def check_payload(self, payload: ResetAndPausePayload) -> None:
        """Check payload."""
        raise NotImplementedError

    def process_payload(self, payload: ResetAndPausePayload) -> None:
        """Process payload."""
        raise NotImplementedError


class TransactionSubmissionRound(AbstractRound):
    """TransactionSubmissionRound"""

    payload_class = TransactionSubmissionPayload
    payload_attribute = ""  # TODO: update
    synchronized_data_class = SynchronizedData

    # TODO: replace AbstractRound with one of CollectDifferentUntilAllRound,
    # CollectSameUntilAllRound, CollectSameUntilThresholdRound,
    # CollectDifferentUntilThresholdRound, OnlyKeeperSendsRound, VotingRound,
    # from packages/valory/skills/abstract_round_abci/base.py
    # or implement the methods

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Enum]]:
        """Process the end of the block."""
        raise NotImplementedError

    def check_payload(self, payload: TransactionSubmissionPayload) -> None:
        """Check payload."""
        raise NotImplementedError

    def process_payload(self, payload: TransactionSubmissionPayload) -> None:
        """Process payload."""
        raise NotImplementedError


class PlantationStationAbciApp(AbciApp[Event]):
    """PlantationStationAbciApp"""

    initial_round_cls: AppState = RegistrationRound
    initial_states: Set[AppState] = {RegistrationRound}
    transition_function: AbciAppTransitionFunction = {
        RegistrationRound: {
            Event.DONE: ObservationCollectionRound
        },
        ObservationCollectionRound: {
            Event.DONE: FederatedLearningRound,
            Event.ROUND_TIMEOUT: ResetAndPauseRound,
            Event.NO_MAJORITY: ResetAndPauseRound
        },
        FederatedLearningRound: {
            Event.DONE: CheckHarvestProposalRound,
            Event.ROUND_TIMEOUT: ResetAndPauseRound,
            Event.NO_MAJORITY: ResetAndPauseRound
        },
        CheckHarvestProposalRound: {
            Event.NO_PROPOSALS: ReadSensorDataRound,
            Event.PROPOSALS: AttestProposalRound,
            Event.ROUND_TIMEOUT: ResetAndPauseRound,
            Event.NO_MAJORITY: ResetAndPauseRound
        },
        AttestProposalRound: {
            Event.DONE: PrepareAttestationTransactionRound,
            Event.ROUND_TIMEOUT: ResetAndPauseRound,
            Event.NO_MAJORITY: ResetAndPauseRound
        },
        PrepareAttestationTransactionRound: {
            Event.DONE: TransactionSubmissionRound,
            Event.ROUND_TIMEOUT: ResetAndPauseRound,
            Event.NO_MAJORITY: ResetAndPauseRound
        },
        ReadSensorDataRound: {
            Event.DONE: ControlAdjustmentRound,
            Event.ROUND_TIMEOUT: ResetAndPauseRound,
            Event.NO_MAJORITY: ResetAndPauseRound
        },
        ControlAdjustmentRound: {
            Event.DONE: PrepareObservationTransactionRound,
            Event.ROUND_TIMEOUT: ResetAndPauseRound,
            Event.NO_MAJORITY: ResetAndPauseRound
        },
        PrepareObservationTransactionRound: {
            Event.DONE: TransactionSubmissionRound,
            Event.ROUND_TIMEOUT: ResetAndPauseRound,
            Event.NO_MAJORITY: ResetAndPauseRound
        },
        TransactionSubmissionRound: {
            Event.DONE: ResetAndPauseRound,
            Event.ROUND_TIMEOUT: ResetAndPauseRound,
            Event.NO_MAJORITY: ResetAndPauseRound
        },
        ResetAndPauseRound: {
            Event.DONE: ObservationCollectionRound,
            Event.NO_MAJORITY: ResetAndPauseRound,
            Event.RESET_TIMEOUT: ResetAndPauseRound
        }
    }
    final_states: Set[AppState] = set()
    event_to_timeout: EventToTimeout = {}
    cross_period_persisted_keys: Set[str] = []
    db_pre_conditions: Dict[AppState, Set[str]] = {
        RegistrationRound: [],
    }
    db_post_conditions: Dict[AppState, Set[str]] = {

    }
