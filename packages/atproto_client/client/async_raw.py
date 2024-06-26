import typing as t

from atproto_client.client.base import AsyncClientBase
from atproto_client.namespaces import async_ns

# TODO(MarshalX): This file should be autogenerated!


class AsyncClientRaw(AsyncClientBase):
    """Group all root namespaces."""

    com: 'async_ns.ComNamespace'
    app: 'async_ns.AppNamespace'
    tools: 'async_ns.ToolsNamespace'
    chat: 'async_ns.ChatNamespace'

    def __init__(self, *args: t.Any, **kwargs: t.Any) -> None:
        super().__init__(*args, **kwargs)

        self.com = async_ns.ComNamespace(self)
        self.app = async_ns.AppNamespace(self)
        self.tools = async_ns.ToolsNamespace(self)
        self.chat = async_ns.ChatNamespace(self)
