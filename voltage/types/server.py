from __future__ import annotations
from typing import Dict, TypedDict, TYPE_CHECKING, List, Tuple, Literal
from typing_extensions import NotRequired

from voltage.types.channel import CategoryPayload

if TYPE_CHECKING:
    from .file import FilePayload

class MemberPayload(TypedDict):
    _id: str
    server: str
    user: str
    nickname: NotRequired[str]
    avatar: NotRequired[FilePayload]
    roles: NotRequired[List[str]]

PermissionPayload = Tuple[int, int]

class RolePayload(TypedDict):
    name: str
    permissions: PermissionPayload
    
class InvitePayload(TypedDict):
    type: Literal["SERVER"]
    serer_id: str
    server_name: str
    server_icon: NotRequired[str]
    server_banner: NotRequired[str]
    channel_id: str
    channel_name: str
    channel_description: NotRequired[str]
    user_name: str
    user_avatar: NotRequired[str]
    member_count: int

class PartialInvitePayload(TypedDict):
    _id: str
    server: str
    channel: str
    creator: str

class SystemMessagesConfigPayload(TypedDict):
    user_joined: NotRequired[str]
    user_left: NotRequired[str]
    user_kicked: NotRequired[str]
    user_banned: NotRequired[str]

class ServerPayload(TypedDict):
    _id: str
    name: str
    owner: str
    channels: List[str]
    default_permissions: PermissionPayload
    nonce: NotRequired[str]
    description: NotRequired[str]
    categories: NotRequired[List[CategoryPayload]]
    system_messages: NotRequired[SystemMessagesConfigPayload]
    roles: NotRequired[Dict[str, RolePayload]]
    icon: NotRequired[FilePayload]
    banner: NotRequired[FilePayload]
    nsfw: NotRequired[bool]
    flags: NotRequired[int]
    analytics: NotRequired[bool]
    discoverable: NotRequired[bool]

class BannedUserPayload(TypedDict):
    _id: str
    username: str
    avatar: NotRequired[FilePayload]

class BanIdPayload(TypedDict):
    server: str
    user: str

class BanPayload(TypedDict):
    _id: BanIdPayload
    reason: NotRequired[str]

class ServerBansPayload(TypedDict):
    users: List[BannedUserPayload]
    bans: List[BanPayload]