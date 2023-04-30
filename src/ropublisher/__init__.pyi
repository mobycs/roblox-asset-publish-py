from _typeshed import Incomplete
from mutagen.wave import WAVE as WAVE
from requests import Response as Response, Session
from tempfile import TemporaryDirectory as TemporaryDirectory
from typing import TypedDict, Union

OpenCloudAssetTypeName: Incomplete
OpenCloudAssetTypeValue: Incomplete
HttpMethod: Incomplete
LEGACY_AUDIO_URL: str
LEGACY_IMAGE_URL: str
LEGACY_MODEL_URL: str
LEGACY_PACKAGE_URL: str
LEGACY_ANIMATION_URL: str
LEGACY_MESH_URL: str
ASSET_URL: str
ASSET_TYPE: dict[OpenCloudAssetTypeName, OpenCloudAssetTypeValue]
LIMITS: Incomplete
OPEN_CONTENT_CLOUD_TYPE: Incomplete
StatusCode: Incomplete

class OpenCloudCreator(TypedDict):
    userId: int | None
    groupId: int | None

class OpenCloudCreationContext(TypedDict):
    creator: OpenCloudCreator
    expectedPrice: int

class OpenCloudAssetInfo(TypedDict):
    path: str | None
    revisionId: str | None
    revisionCreateTime: str | None

class OpenCloudCreationAsset(OpenCloudAssetInfo):
    description: str
    displayName: str
    assetType: OpenCloudAssetTypeValue
    creationContext: OpenCloudCreationContext

class OpenCloudUpdateAsset(OpenCloudAssetInfo):
    assetId: int
    description: str | None
    displayName: str | None
OpenCloudAsset = Union[OpenCloudUpdateAsset, OpenCloudCreationAsset]

class OpenCloudStatus(TypedDict):
    code: StatusCode
    message: str
    details: list[str]

class OpenCloudOperation(TypedDict):
    path: str
    metadata: str
    done: bool
    error: str
    response: OpenCloudStatus

class Publisher:
    group_id: int | None
    user_id: int | None
    place_key: str | None
    asset_key: str | None
    universe_registry: dict[int, int]
    session: Session
    def __init__(self, cookie: str | None = ..., place_key: str | None = ..., asset_key: str | None = ..., group_id: int | None = ..., user_id: int | None = ...) -> None: ...
    def get_universe_id_from_place_id(self, place_id: int) -> int: ...
    def get_asset_id_from_operations_id(self, operations_id: str) -> int | None: ...
    def update_place(self, file_path: str, place_id: str): ...
    def post_decal(self, file_path: str, name: str | None = ..., publish_to_group: bool = ..., description: str | None = ...) -> int | None: ...
    def post_audio(self, file_path: str, name: str | None = ..., publish_to_group: bool = ..., description: str | None = ...) -> int | None: ...
    def post_mesh_as_model(self, file_path: str, name: str | None = ..., publish_to_group: bool = ..., description: str | None = ...) -> int | None: ...
    def legacy_publish_decal(self, file_path: str, name: str | None = ..., publish_to_group: bool = ...) -> int | None: ...
    def legacy_publish_audio(self, file_path: str, name: str | None = ..., publish_to_group: bool = ...) -> int | None: ...
