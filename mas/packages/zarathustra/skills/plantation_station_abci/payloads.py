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

"""This module contains the transaction payloads of the PlantationStationAbciApp."""

from dataclasses import dataclass

from packages.valory.skills.abstract_round_abci.base import BaseTxPayload


@dataclass(frozen=True)
class AttestProposalPayload(BaseTxPayload):
    """Represent a transaction payload for the AttestProposalRound."""

    # TODO: define your attributes


@dataclass(frozen=True)
class CheckHarvestProposalPayload(BaseTxPayload):
    """Represent a transaction payload for the CheckHarvestProposalRound."""

    # TODO: define your attributes


@dataclass(frozen=True)
class ControlAdjustmentPayload(BaseTxPayload):
    """Represent a transaction payload for the ControlAdjustmentRound."""

    # TODO: define your attributes


@dataclass(frozen=True)
class FederatedLearningPayload(BaseTxPayload):
    """Represent a transaction payload for the FederatedLearningRound."""

    # TODO: define your attributes


@dataclass(frozen=True)
class ObservationCollectionPayload(BaseTxPayload):
    """Represent a transaction payload for the ObservationCollectionRound."""

    # TODO: define your attributes


@dataclass(frozen=True)
class PrepareAttestationTransactionPayload(BaseTxPayload):
    """Represent a transaction payload for the PrepareAttestationTransactionRound."""

    # TODO: define your attributes


@dataclass(frozen=True)
class PrepareObservationTransactionPayload(BaseTxPayload):
    """Represent a transaction payload for the PrepareObservationTransactionRound."""

    # TODO: define your attributes


@dataclass(frozen=True)
class ReadSensorDataPayload(BaseTxPayload):
    """Represent a transaction payload for the ReadSensorDataRound."""

    ipfs_hash: str

