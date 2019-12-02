# backend/tancho/pets/models.py

from enum import Enum
from pydantic import BaseModel
from typing import List, Optional


class PetState(str, Enum):
    """[summary]
        Used to manage supported pet states.
    [description]
        Simple enumeration to link the pets state.
    """
    injured = "Injured"
    underfed = "Underfed"
    critical = "Critical"
    bad = "Bad"
    good = "Good"
    healthy = "Healthy"


class PetKind(str, Enum):
    """[summary]
        Used to manage supported pets.

    [description]
        Simple enumeration to link the kind of a pet.
    """
    dog = "Dog"
    cat = "Cat"


class PetStatus(str, Enum):
    """[summary]
        Used to manage report found or missing pets.

    [description]
        Simple enumeration to link the status of a pet.
    """
    missing = "Missing"
    found = "Found"
    adoption = "Adoption"
    adopted = "Adopted"
    rescued = "Rescued"


class PetBase(BaseModel):
    """[summary]
        Base pet abstraction model.

    [description]
        Used to abstract out basic pet fields.

    Arguments:
        BaseModel {[type]} -- [description]
    """
    kind: PetKind
    status: PetStatus
    story: str
    name: Optional[str] = None
    location: str
    states: List[PetState] = []
    picture: Optional[str] = None
    in_temp_house: bool = False


class PetOnDB(PetBase):
    """[summary]
    Actual model used at DB level

    [description]
    Extends:
        PetBase
    Adds `id_` field.

    Variables:
        id_: str {[ObjectId]} -- [id at DB]
    """
    id_: str


class PetsOut(BaseModel):
    """[summary]

    [description]

    Extends:
        PetOnDB
    """
    pets: List[PetOnDB]
    count: int
