##################################################################
# THIS IS THE AUTO-GENERATED CODE. DON'T EDIT IT BY HANDS!
# Copyright (C) 2024 Ilya (Marshal) <https://github.com/MarshalX>.
# This file is part of Python atproto SDK. Licenced under MIT.
##################################################################


import typing as t

import typing_extensions as te

from atproto_client.models import base


class Params(base.ParamsModelBase):
    """Parameters model for :obj:`tools.ozone.moderation.getRecord`."""

    uri: str  #: Uri.
    cid: t.Optional[str] = None  #: Cid.


class ParamsDict(t.TypedDict):
    uri: str  #: Uri.
    cid: te.NotRequired[t.Optional[str]]  #: Cid.
