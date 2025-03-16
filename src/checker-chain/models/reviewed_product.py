from typing import List
from typing import Any
from dataclasses import dataclass
from .common import Category, CreatedBy, Owner, Operation, Reward


@dataclass
class ReviewedProduct:
    _id: str
    name: str
    currentReviewCycle: int
    category: Category
    description: str
    url: str
    location: str
    operation: Operation
    specialReviewRequest: str
    discountCode: str
    offer: str
    subcategories: List[str]
    slug: str
    gallery: List[object]
    teams: List[object]
    twitterProfile: str
    isClaimed: bool
    isClaiming: bool
    network: str
    createdBy: CreatedBy
    owners: List[object]
    status: str
    reviewDeadline: float
    rewards: List[Reward]
    createdAt: str
    updatedAt: str
    __v: int
    logo: str
    coverImage: str
    epoch: int
    consensusScore: float
    normalizedTrustScore: float
    trustScore: float
    lastReviewed: str
    ratingScore: float
    reward: float
    id: str
    reviewCount: int
    subscribersCount: int
    isSubscribed: bool

    @staticmethod
    def from_dict(obj: Any) -> 'ReviewedProduct':
        __id = str(obj.get("_id"))
        _name = str(obj.get("name"))
        _currentReviewCycle = int(obj.get("currentReviewCycle"))
        _category = Category.from_dict(obj.get("category"))
        _description = str(obj.get("description"))
        _url = str(obj.get("url"))
        _location = str(obj.get("location"))
        _operation = Operation.from_dict(obj.get("operation"))
        _specialReviewRequest = str(obj.get("specialReviewRequest"))
        _discountCode = str(obj.get("discountCode"))
        _offer = str(obj.get("offer"))
        _subcategories = [str(y) for y in obj.get("subcategories", [])]
        _slug = str(obj.get("slug"))
        _gallery = [str(y) for y in obj.get("gallery", [])]
        _teams = []
        _twitterProfile = str(obj.get("twitterProfile"))
        _isClaimed = bool(obj.get("isClaimed"))
        _isClaiming = bool(obj.get("isClaiming"))
        _network = str(obj.get("network"))
        _createdBy = CreatedBy.from_dict(obj.get("createdBy"))
        _owners = [Owner.from_dict(y) for y in obj.get("owners")]
        _status = str(obj.get("status"))
        _reviewDeadline = float(obj.get("reviewDeadline"))
        _rewards = [Reward.from_dict(y) for y in obj.get("rewards")]
        _createdAt = str(obj.get("createdAt"))
        _updatedAt = str(obj.get("updatedAt"))
        ___v = int(obj.get("__v"))
        _logo = str(obj.get("logo"))
        _coverImage = str(obj.get("coverImage"))
        _epoch = int(obj.get("epoch"))
        _consensusScore = float(obj.get("consensusScore"))
        _normalizedTrustScore = float(obj.get("normalizedTrustScore"))
        _trustScore = float(obj.get("trustScore"))
        _lastReviewed = str(obj.get("lastReviewed"))
        _ratingScore = float(obj.get("ratingScore"))
        _reward = float(obj.get("reward"))
        _id = str(obj.get("id"))
        _reviewCount = int(obj.get("reviewCount"))
        _subscribersCount = int(obj.get("subscribersCount"))
        _isSubscribed = bool(obj.get("isSubscribed"))
        return ReviewedProduct(__id, _name, _currentReviewCycle, _category, _description, _url, _location, _operation, _specialReviewRequest, _discountCode, _offer, _subcategories, _slug, _gallery, _teams, _twitterProfile, _isClaimed, _isClaiming, _network, _createdBy, _owners, _status, _reviewDeadline, _rewards, _createdAt, _updatedAt, ___v, _logo, _coverImage, _epoch, _consensusScore, _normalizedTrustScore, _trustScore, _lastReviewed, _ratingScore, _reward, _id, _reviewCount, _subscribersCount, _isSubscribed)


@dataclass
class ReviewedData:
    products: List[ReviewedProduct]

    @staticmethod
    def from_dict(obj: Any) -> 'ReviewedData':
        _products = [ReviewedProduct.from_dict(y) for y in obj.get("products")]
        return ReviewedData(_products)


@dataclass
class ReviewedProductsApiResponse:
    message: str
    data: ReviewedData

    @staticmethod
    def from_dict(obj: Any) -> 'ReviewedProductsApiResponse':
        _message = str(obj.get("message"))
        _data = ReviewedData.from_dict(obj.get("data"))
        return ReviewedProductsApiResponse(_message, _data)


@dataclass
class ReviewedProductApiResponse:
    message: str
    data: ReviewedProduct

    @staticmethod
    def from_dict(obj: Any) -> 'ReviewedProductApiResponse':
        _message = str(obj.get("message"))
        _data = ReviewedProduct.from_dict(obj.get("data"))
        return ReviewedProductApiResponse(_message, _data)
