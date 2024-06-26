##################################################################
# THIS IS THE AUTO-GENERATED CODE. DON'T EDIT IT BY HANDS!
# Copyright (C) 2024 Ilya (Marshal) <https://github.com/MarshalX>.
# This file is part of Python atproto SDK. Licenced under MIT.
##################################################################


import typing as t

import typing_extensions as te

from atproto_client.models import base


class Params(base.ParamsModelBase):
    """Parameters model for :obj:`com.atproto.sync.getRepo`."""

    did: str  #: The DID of the repo.
    since: t.Optional[str] = None  #: The revision ('rev') of the repo to create a diff from.


class ParamsDict(t.TypedDict):
    did: str  #: The DID of the repo.
    since: te.NotRequired[t.Optional[str]]  #: The revision ('rev') of the repo to create a diff from.


#: Response raw data type.
Response: te.TypeAlias = bytes
