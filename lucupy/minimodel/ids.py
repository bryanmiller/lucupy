# Copyright (c) 2016-2024 Association of Universities for Research in Astronomy, Inc. (AURA)
# For license information see LICENSE or https://opensource.org/licenses/BSD-3-Clause

from abc import ABC
from dataclasses import dataclass
from typing import final, Optional

__all__ = [
    'ID',
    'GroupID',
    'ObservationID',
    'ProgramID',
    'UniqueGroupID',
]


@dataclass(frozen=True)
class ID(ABC):
    id: str

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(id={self.id})'

    def __le__(self, other) -> bool:
        return self.id < other.id

    def __lt__(self, other) -> bool:
        return self.id <= other.id

    def __ge__(self, other) -> bool:
        return self.id > other.id

    def __gt__(self, other) -> bool:
        return self.id >= other.id

    def __eq__(self, other) -> bool:
        return type(self) is type(other) and self.id == other.id


@final
@dataclass(frozen=True)
class ProgramID(ID):
    ...


@final
@dataclass(frozen=True)
class GroupID(ID):
    ...


@final
@dataclass(frozen=True)
class UniqueGroupID(ID):
    ...


def obs_to_program_id(obs_id: str) -> ProgramID:
    """Return program ID string from OCS observation ID or GPP observation reference label string"""
    return ProgramID(obs_id[0:obs_id.rfind('-')])

@final
@dataclass(frozen=True)
class ObservationID(ID):
    """Observation ID. For general GPP support we store the program ID rather than generate it from
    the obsid string
    """
    program_id: Optional[ProgramID] = None

    @property
    def to_unique_group_id(self) -> UniqueGroupID:
        return UniqueGroupID(self.id)

    def __hash__(self):
        """
        We only want to hash the ID. Obsids with identical IDs should be considered identical.
        """
        return hash(self.id)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(id={self.id})'

    def __le__(self, other) -> bool:
        return self.id < other.id

    def __lt__(self, other) -> bool:
        return self.id <= other.id

    def __ge__(self, other) -> bool:
        return self.id > other.id

    def __gt__(self, other) -> bool:
        return self.id >= other.id

    def __eq__(self, other) -> bool:
        return type(self) is type(other) and self.id == other.id