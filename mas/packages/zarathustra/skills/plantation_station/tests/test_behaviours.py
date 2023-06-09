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

from pathlib import Path
from typing import Any, Dict, Hashable, Optional, Type
from dataclasses import dataclass, field

import pytest

from packages.valory.skills.abstract_round_abci.base import AbciAppDB
from packages.valory.skills.abstract_round_abci.behaviours import (
    AbstractRoundBehaviour,
    BaseBehaviour,
    make_degenerate_behaviour,
)
from packages.default_author.skills.plantation_station.behaviours import (
    PlantationStationBaseBehaviour,
    PlantationStationRoundBehaviour,
    AttestProposalBehaviour,
    CheckHarvestProposalBehaviour,
    ControlAdjustmentBehaviour,
    FederatedLearningBehaviour,
    ObservationCollectionBehaviour,
    PrepareAttestationTransactionBehaviour,
    PrepareObservationTransactionBehaviour,
    ReadSensorDataBehaviour,
    RegistrationBehaviour,
    ResetAndPauseBehaviour,
    TransactionSubmissionBehaviour,
)
from packages.default_author.skills.plantation_station.rounds import (
    SynchronizedData,
    DegenerateRound,
    Event,
    PlantationStationAbciApp,
    AttestProposalRound,
    CheckHarvestProposalRound,
    ControlAdjustmentRound,
    FederatedLearningRound,
    ObservationCollectionRound,
    PrepareAttestationTransactionRound,
    PrepareObservationTransactionRound,
    ReadSensorDataRound,
    RegistrationRound,
    ResetAndPauseRound,
    TransactionSubmissionRound,
)

from packages.valory.skills.abstract_round_abci.test_tools.base import (
    FSMBehaviourBaseCase,
)


@dataclass
class BehaviourTestCase:
    """BehaviourTestCase"""

    name: str
    initial_data: Dict[str, Hashable]
    event: Event
    kwargs: Dict[str, Any] = field(default_factory=dict)


class BasePlantationStationTest(FSMBehaviourBaseCase):
    """Base test case."""

    path_to_skill = Path(__file__).parent.parent

    behaviour: PlantationStationRoundBehaviour
    behaviour_class: Type[PlantationStationBaseBehaviour]
    next_behaviour_class: Type[PlantationStationBaseBehaviour]
    synchronized_data: SynchronizedData
    done_event = Event.DONE

    @property
    def current_behaviour_id(self) -> str:
        """Current RoundBehaviour's behaviour id"""

        return self.behaviour.current_behaviour.behaviour_id

    def fast_forward(self, data: Optional[Dict[str, Any]] = None) -> None:
        """Fast-forward on initialization"""

        data = data if data is not None else {}
        self.fast_forward_to_behaviour(
            self.behaviour,
            self.behaviour_class.behaviour_id,
            SynchronizedData(AbciAppDB(setup_data=AbciAppDB.data_to_lists(data))),
        )
        assert self.current_behaviour_id == self.behaviour_class.behaviour_id

    def complete(self, event: Event) -> None:
        """Complete test"""

        self.behaviour.act_wrapper()
        self.mock_a2a_transaction()
        self._test_done_flag_set()
        self.end_round(done_event=event)
        assert self.current_behaviour_id == self.next_behaviour_class.behaviour_id


class TestAttestProposalBehaviour(BasePlantationStationTest):
    """Tests AttestProposalBehaviour"""

    # TODO: set next_behaviour_class
    behaviour_class: Type[BaseBehaviour] = AttestProposalBehaviour
    next_behaviour_class: Type[BaseBehaviour] = ...

    # TODO: provide test cases
    @pytest.mark.parametrize("test_case", [])
    def test_run(self, test_case: BehaviourTestCase) -> None:
        """Run tests."""

        self.fast_forward(test_case.initial_data)
        # TODO: mock the necessary calls
        # self.mock_ ...
        self.complete(test_case.event)


class TestCheckHarvestProposalBehaviour(BasePlantationStationTest):
    """Tests CheckHarvestProposalBehaviour"""

    # TODO: set next_behaviour_class
    behaviour_class: Type[BaseBehaviour] = CheckHarvestProposalBehaviour
    next_behaviour_class: Type[BaseBehaviour] = ...

    # TODO: provide test cases
    @pytest.mark.parametrize("test_case", [])
    def test_run(self, test_case: BehaviourTestCase) -> None:
        """Run tests."""

        self.fast_forward(test_case.initial_data)
        # TODO: mock the necessary calls
        # self.mock_ ...
        self.complete(test_case.event)


class TestControlAdjustmentBehaviour(BasePlantationStationTest):
    """Tests ControlAdjustmentBehaviour"""

    # TODO: set next_behaviour_class
    behaviour_class: Type[BaseBehaviour] = ControlAdjustmentBehaviour
    next_behaviour_class: Type[BaseBehaviour] = ...

    # TODO: provide test cases
    @pytest.mark.parametrize("test_case", [])
    def test_run(self, test_case: BehaviourTestCase) -> None:
        """Run tests."""

        self.fast_forward(test_case.initial_data)
        # TODO: mock the necessary calls
        # self.mock_ ...
        self.complete(test_case.event)


class TestFederatedLearningBehaviour(BasePlantationStationTest):
    """Tests FederatedLearningBehaviour"""

    # TODO: set next_behaviour_class
    behaviour_class: Type[BaseBehaviour] = FederatedLearningBehaviour
    next_behaviour_class: Type[BaseBehaviour] = ...

    # TODO: provide test cases
    @pytest.mark.parametrize("test_case", [])
    def test_run(self, test_case: BehaviourTestCase) -> None:
        """Run tests."""

        self.fast_forward(test_case.initial_data)
        # TODO: mock the necessary calls
        # self.mock_ ...
        self.complete(test_case.event)


class TestObservationCollectionBehaviour(BasePlantationStationTest):
    """Tests ObservationCollectionBehaviour"""

    # TODO: set next_behaviour_class
    behaviour_class: Type[BaseBehaviour] = ObservationCollectionBehaviour
    next_behaviour_class: Type[BaseBehaviour] = ...

    # TODO: provide test cases
    @pytest.mark.parametrize("test_case", [])
    def test_run(self, test_case: BehaviourTestCase) -> None:
        """Run tests."""

        self.fast_forward(test_case.initial_data)
        # TODO: mock the necessary calls
        # self.mock_ ...
        self.complete(test_case.event)


class TestPrepareAttestationTransactionBehaviour(BasePlantationStationTest):
    """Tests PrepareAttestationTransactionBehaviour"""

    # TODO: set next_behaviour_class
    behaviour_class: Type[BaseBehaviour] = PrepareAttestationTransactionBehaviour
    next_behaviour_class: Type[BaseBehaviour] = ...

    # TODO: provide test cases
    @pytest.mark.parametrize("test_case", [])
    def test_run(self, test_case: BehaviourTestCase) -> None:
        """Run tests."""

        self.fast_forward(test_case.initial_data)
        # TODO: mock the necessary calls
        # self.mock_ ...
        self.complete(test_case.event)


class TestPrepareObservationTransactionBehaviour(BasePlantationStationTest):
    """Tests PrepareObservationTransactionBehaviour"""

    # TODO: set next_behaviour_class
    behaviour_class: Type[BaseBehaviour] = PrepareObservationTransactionBehaviour
    next_behaviour_class: Type[BaseBehaviour] = ...

    # TODO: provide test cases
    @pytest.mark.parametrize("test_case", [])
    def test_run(self, test_case: BehaviourTestCase) -> None:
        """Run tests."""

        self.fast_forward(test_case.initial_data)
        # TODO: mock the necessary calls
        # self.mock_ ...
        self.complete(test_case.event)


class TestReadSensorDataBehaviour(BasePlantationStationTest):
    """Tests ReadSensorDataBehaviour"""

    # TODO: set next_behaviour_class
    behaviour_class: Type[BaseBehaviour] = ReadSensorDataBehaviour
    next_behaviour_class: Type[BaseBehaviour] = ...

    # TODO: provide test cases
    @pytest.mark.parametrize("test_case", [])
    def test_run(self, test_case: BehaviourTestCase) -> None:
        """Run tests."""

        self.fast_forward(test_case.initial_data)
        # TODO: mock the necessary calls
        # self.mock_ ...
        self.complete(test_case.event)


class TestRegistrationBehaviour(BasePlantationStationTest):
    """Tests RegistrationBehaviour"""

    # TODO: set next_behaviour_class
    behaviour_class: Type[BaseBehaviour] = RegistrationBehaviour
    next_behaviour_class: Type[BaseBehaviour] = ...

    # TODO: provide test cases
    @pytest.mark.parametrize("test_case", [])
    def test_run(self, test_case: BehaviourTestCase) -> None:
        """Run tests."""

        self.fast_forward(test_case.initial_data)
        # TODO: mock the necessary calls
        # self.mock_ ...
        self.complete(test_case.event)


class TestResetAndPauseBehaviour(BasePlantationStationTest):
    """Tests ResetAndPauseBehaviour"""

    # TODO: set next_behaviour_class
    behaviour_class: Type[BaseBehaviour] = ResetAndPauseBehaviour
    next_behaviour_class: Type[BaseBehaviour] = ...

    # TODO: provide test cases
    @pytest.mark.parametrize("test_case", [])
    def test_run(self, test_case: BehaviourTestCase) -> None:
        """Run tests."""

        self.fast_forward(test_case.initial_data)
        # TODO: mock the necessary calls
        # self.mock_ ...
        self.complete(test_case.event)


class TestTransactionSubmissionBehaviour(BasePlantationStationTest):
    """Tests TransactionSubmissionBehaviour"""

    # TODO: set next_behaviour_class
    behaviour_class: Type[BaseBehaviour] = TransactionSubmissionBehaviour
    next_behaviour_class: Type[BaseBehaviour] = ...

    # TODO: provide test cases
    @pytest.mark.parametrize("test_case", [])
    def test_run(self, test_case: BehaviourTestCase) -> None:
        """Run tests."""

        self.fast_forward(test_case.initial_data)
        # TODO: mock the necessary calls
        # self.mock_ ...
        self.complete(test_case.event)

