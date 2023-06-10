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

"""This package contains the tests for rounds of Plantation."""

from typing import Any, Type, Dict, List, Callable, Hashable, Mapping
from dataclasses import dataclass, field

import pytest

from packages.zarathustra.skills.plantation_abci.payloads import (
    AttestProposalPayload,
    CheckHarvestProposalPayload,
    CheckLateTxHashesPayload,
    CheckTransactionHistoryPayload,
    CollectSignaturePayload,
    ControlAdjustmentPayload,
    FederatedLearningPayload,
    FinalizationPayload,
    ObservationCollectionPayload,
    PrepareAttestationTransactionPayload,
    PrepareObservationTransactionPayload,
    RandomnessTransactionSubmissionPayload,
    ReadSensorDataPayload,
    RegistrationPayload,
    RegistrationStartupPayload,
    ResetAndPausePayload,
    ResetPayload,
    SelectKeeperTransactionSubmissionAPayload,
    SelectKeeperTransactionSubmissionBAfterTimeoutPayload,
    SelectKeeperTransactionSubmissionBPayload,
    SynchronizeLateMessagesPayload,
    ValidateTransactionPayload,
)
from packages.zarathustra.skills.plantation_abci.rounds import (
    AbstractRound,
    Event,
    SynchronizedData,
    AttestProposalRound,
    CheckHarvestProposalRound,
    CheckLateTxHashesRound,
    CheckTransactionHistoryRound,
    CollectSignatureRound,
    ControlAdjustmentRound,
    FederatedLearningRound,
    FinalizationRound,
    ObservationCollectionRound,
    PrepareAttestationTransactionRound,
    PrepareObservationTransactionRound,
    RandomnessTransactionSubmissionRound,
    ReadSensorDataRound,
    RegistrationRound,
    RegistrationStartupRound,
    ResetAndPauseRound,
    ResetRound,
    SelectKeeperTransactionSubmissionARound,
    SelectKeeperTransactionSubmissionBAfterTimeoutRound,
    SelectKeeperTransactionSubmissionBRound,
    SynchronizeLateMessagesRound,
    ValidateTransactionRound,
)
from packages.valory.skills.abstract_round_abci.base import (
    BaseTxPayload,
)
from packages.valory.skills.abstract_round_abci.test_tools.rounds import (
    BaseRoundTestClass,
    BaseOnlyKeeperSendsRoundTest,
    BaseCollectDifferentUntilThresholdRoundTest,
    BaseCollectSameUntilThresholdRoundTest,
 )


@dataclass
class RoundTestCase:
    """RoundTestCase"""

    name: str
    initial_data: Dict[str, Hashable]
    payloads: Mapping[str, BaseTxPayload]
    final_data: Dict[str, Hashable]
    event: Event
    synchronized_data_attr_checks: List[Callable] = field(default_factory=list)
    kwargs: Dict[str, Any] = field(default_factory=dict)


MAX_PARTICIPANTS: int = 4


class BasePlantationRoundTest(BaseRoundTestClass):
    """Base test class for Plantation rounds."""

    round_cls: Type[AbstractRound]
    synchronized_data: SynchronizedData
    _synchronized_data_class = SynchronizedData
    _event_class = Event

    def run_test(self, test_case: RoundTestCase) -> None:
        """Run the test"""

        self.synchronized_data.update(**test_case.initial_data)

        test_round = self.round_cls(
            synchronized_data=self.synchronized_data,
        )

        self._complete_run(
            self._test_round(
                test_round=test_round,
                round_payloads=test_case.payloads,
                synchronized_data_update_fn=lambda sync_data, _: sync_data.update(**test_case.final_data),
                synchronized_data_attr_checks=test_case.synchronized_data_attr_checks,
                exit_event=test_case.event,
                **test_case.kwargs,  # varies per BaseRoundTestClass child
            )
        )


class TestAttestProposalRound(BasePlantationRoundTest):
    """Tests for AttestProposalRound."""

    round_class = AttestProposalRound

    # TODO: provide test cases
    @pytest.mark.parametrize("test_case", [])
    def test_run(self, test_case: RoundTestCase) -> None:
        """Run tests."""

        self.run_test(test_case)


class TestCheckHarvestProposalRound(BasePlantationRoundTest):
    """Tests for CheckHarvestProposalRound."""

    round_class = CheckHarvestProposalRound

    # TODO: provide test cases
    @pytest.mark.parametrize("test_case", [])
    def test_run(self, test_case: RoundTestCase) -> None:
        """Run tests."""

        self.run_test(test_case)


class TestCheckLateTxHashesRound(BasePlantationRoundTest):
    """Tests for CheckLateTxHashesRound."""

    round_class = CheckLateTxHashesRound

    # TODO: provide test cases
    @pytest.mark.parametrize("test_case", [])
    def test_run(self, test_case: RoundTestCase) -> None:
        """Run tests."""

        self.run_test(test_case)


class TestCheckTransactionHistoryRound(BasePlantationRoundTest):
    """Tests for CheckTransactionHistoryRound."""

    round_class = CheckTransactionHistoryRound

    # TODO: provide test cases
    @pytest.mark.parametrize("test_case", [])
    def test_run(self, test_case: RoundTestCase) -> None:
        """Run tests."""

        self.run_test(test_case)


class TestCollectSignatureRound(BasePlantationRoundTest):
    """Tests for CollectSignatureRound."""

    round_class = CollectSignatureRound

    # TODO: provide test cases
    @pytest.mark.parametrize("test_case", [])
    def test_run(self, test_case: RoundTestCase) -> None:
        """Run tests."""

        self.run_test(test_case)


class TestControlAdjustmentRound(BasePlantationRoundTest):
    """Tests for ControlAdjustmentRound."""

    round_class = ControlAdjustmentRound

    # TODO: provide test cases
    @pytest.mark.parametrize("test_case", [])
    def test_run(self, test_case: RoundTestCase) -> None:
        """Run tests."""

        self.run_test(test_case)


class TestFederatedLearningRound(BasePlantationRoundTest):
    """Tests for FederatedLearningRound."""

    round_class = FederatedLearningRound

    # TODO: provide test cases
    @pytest.mark.parametrize("test_case", [])
    def test_run(self, test_case: RoundTestCase) -> None:
        """Run tests."""

        self.run_test(test_case)


class TestFinalizationRound(BasePlantationRoundTest):
    """Tests for FinalizationRound."""

    round_class = FinalizationRound

    # TODO: provide test cases
    @pytest.mark.parametrize("test_case", [])
    def test_run(self, test_case: RoundTestCase) -> None:
        """Run tests."""

        self.run_test(test_case)


class TestObservationCollectionRound(BasePlantationRoundTest):
    """Tests for ObservationCollectionRound."""

    round_class = ObservationCollectionRound

    # TODO: provide test cases
    @pytest.mark.parametrize("test_case", [])
    def test_run(self, test_case: RoundTestCase) -> None:
        """Run tests."""

        self.run_test(test_case)


class TestPrepareAttestationTransactionRound(BasePlantationRoundTest):
    """Tests for PrepareAttestationTransactionRound."""

    round_class = PrepareAttestationTransactionRound

    # TODO: provide test cases
    @pytest.mark.parametrize("test_case", [])
    def test_run(self, test_case: RoundTestCase) -> None:
        """Run tests."""

        self.run_test(test_case)


class TestPrepareObservationTransactionRound(BasePlantationRoundTest):
    """Tests for PrepareObservationTransactionRound."""

    round_class = PrepareObservationTransactionRound

    # TODO: provide test cases
    @pytest.mark.parametrize("test_case", [])
    def test_run(self, test_case: RoundTestCase) -> None:
        """Run tests."""

        self.run_test(test_case)


class TestRandomnessTransactionSubmissionRound(BasePlantationRoundTest):
    """Tests for RandomnessTransactionSubmissionRound."""

    round_class = RandomnessTransactionSubmissionRound

    # TODO: provide test cases
    @pytest.mark.parametrize("test_case", [])
    def test_run(self, test_case: RoundTestCase) -> None:
        """Run tests."""

        self.run_test(test_case)


class TestReadSensorDataRound(BasePlantationRoundTest):
    """Tests for ReadSensorDataRound."""

    round_class = ReadSensorDataRound

    # TODO: provide test cases
    @pytest.mark.parametrize("test_case", [])
    def test_run(self, test_case: RoundTestCase) -> None:
        """Run tests."""

        self.run_test(test_case)


class TestRegistrationRound(BasePlantationRoundTest):
    """Tests for RegistrationRound."""

    round_class = RegistrationRound

    # TODO: provide test cases
    @pytest.mark.parametrize("test_case", [])
    def test_run(self, test_case: RoundTestCase) -> None:
        """Run tests."""

        self.run_test(test_case)


class TestRegistrationStartupRound(BasePlantationRoundTest):
    """Tests for RegistrationStartupRound."""

    round_class = RegistrationStartupRound

    # TODO: provide test cases
    @pytest.mark.parametrize("test_case", [])
    def test_run(self, test_case: RoundTestCase) -> None:
        """Run tests."""

        self.run_test(test_case)


class TestResetAndPauseRound(BasePlantationRoundTest):
    """Tests for ResetAndPauseRound."""

    round_class = ResetAndPauseRound

    # TODO: provide test cases
    @pytest.mark.parametrize("test_case", [])
    def test_run(self, test_case: RoundTestCase) -> None:
        """Run tests."""

        self.run_test(test_case)


class TestResetRound(BasePlantationRoundTest):
    """Tests for ResetRound."""

    round_class = ResetRound

    # TODO: provide test cases
    @pytest.mark.parametrize("test_case", [])
    def test_run(self, test_case: RoundTestCase) -> None:
        """Run tests."""

        self.run_test(test_case)


class TestSelectKeeperTransactionSubmissionARound(BasePlantationRoundTest):
    """Tests for SelectKeeperTransactionSubmissionARound."""

    round_class = SelectKeeperTransactionSubmissionARound

    # TODO: provide test cases
    @pytest.mark.parametrize("test_case", [])
    def test_run(self, test_case: RoundTestCase) -> None:
        """Run tests."""

        self.run_test(test_case)


class TestSelectKeeperTransactionSubmissionBAfterTimeoutRound(BasePlantationRoundTest):
    """Tests for SelectKeeperTransactionSubmissionBAfterTimeoutRound."""

    round_class = SelectKeeperTransactionSubmissionBAfterTimeoutRound

    # TODO: provide test cases
    @pytest.mark.parametrize("test_case", [])
    def test_run(self, test_case: RoundTestCase) -> None:
        """Run tests."""

        self.run_test(test_case)


class TestSelectKeeperTransactionSubmissionBRound(BasePlantationRoundTest):
    """Tests for SelectKeeperTransactionSubmissionBRound."""

    round_class = SelectKeeperTransactionSubmissionBRound

    # TODO: provide test cases
    @pytest.mark.parametrize("test_case", [])
    def test_run(self, test_case: RoundTestCase) -> None:
        """Run tests."""

        self.run_test(test_case)


class TestSynchronizeLateMessagesRound(BasePlantationRoundTest):
    """Tests for SynchronizeLateMessagesRound."""

    round_class = SynchronizeLateMessagesRound

    # TODO: provide test cases
    @pytest.mark.parametrize("test_case", [])
    def test_run(self, test_case: RoundTestCase) -> None:
        """Run tests."""

        self.run_test(test_case)


class TestValidateTransactionRound(BasePlantationRoundTest):
    """Tests for ValidateTransactionRound."""

    round_class = ValidateTransactionRound

    # TODO: provide test cases
    @pytest.mark.parametrize("test_case", [])
    def test_run(self, test_case: RoundTestCase) -> None:
        """Run tests."""

        self.run_test(test_case)

