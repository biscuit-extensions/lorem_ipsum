from __future__ import annotations

import typing

from biscuit.extensions import Extension

if typing.TYPE_CHECKING:
    from biscuit.api import ExtensionsAPI


class LoremIpsum(Extension):
    """Lorem Ipsum placeholder text and paragraph generator"""

    def __init__(self, api: "ExtensionsAPI") -> None:
        super().__init__(api)
        self.api = api
        self.api.logger.info("Lorem Ipsum extension initialised.")

    def install(self) -> None:
        """Run when extension is loaded."""
        self.api.logger.info("Lorem Ipsum installed successfully.")
