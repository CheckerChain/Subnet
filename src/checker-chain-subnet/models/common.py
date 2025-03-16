from typing import List
from typing import Any
from dataclasses import dataclass


@dataclass
class Category:
    _id: str
    name: str

    @staticmethod
    def from_dict(obj: Any) -> 'Category':
        __id = str(obj.get("_id"))
        _name = str(obj.get("name"))
        return Category(__id, _name)


@dataclass
class CreatedBy:
    _id: str
    wallet: str
    username: str
    profileScore: float
    bio: str
    name: str
    profilePicture: str

    @staticmethod
    def from_dict(obj: Any) -> 'CreatedBy':
        __id = str(obj.get("_id"))
        _wallet = str(obj.get("wallet"))
        _username = str(obj.get("username"))
        _profileScore = float(obj.get("profileScore"))
        _bio = str(obj.get("bio"))
        _name = str(obj.get("name"))
        _profilePicture = str(obj.get("profilePicture"))
        return CreatedBy(__id, _wallet, _username, _profileScore, _bio, _name, _profilePicture)


@dataclass
class Day:
    @staticmethod
    def from_dict(obj: Any) -> 'Day':
        return Day()


@dataclass
class Owner:
    @staticmethod
    def from_dict(obj: Any) -> 'Owner':
        return Owner()


@dataclass
class Operation:
    availableAllTime: bool
    _id: str
    days: List[object]

    @staticmethod
    def from_dict(obj: Any) -> 'Operation':
        _availableAllTime = bool(obj.get("availableAllTime"))
        __id = str(obj.get("_id"))
        _days = [Day.from_dict(y) for y in obj.get("days")]
        return Operation(_availableAllTime, __id, _days)


@dataclass
class Reward:
    _id: str
    epoch: int
    product: str
    reviewCycle: int
    __v: int
    createdAt: str
    reward: float
    updatedAt: str

    @staticmethod
    def from_dict(obj: Any) -> 'Reward':
        __id = str(obj.get("_id"))
        _epoch = int(obj.get("epoch"))
        _product = str(obj.get("product"))
        _reviewCycle = int(obj.get("reviewCycle"))
        ___v = int(obj.get("__v"))
        _createdAt = str(obj.get("createdAt"))
        _reward = float(obj.get("reward"))
        _updatedAt = str(obj.get("updatedAt"))
        return Reward(__id, _epoch, _product, _reviewCycle, ___v, _createdAt, _reward, _updatedAt)
