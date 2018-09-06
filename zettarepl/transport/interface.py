# -*- coding=utf-8 -*-
import logging

from .shell.interface import Shell

logger = logging.getLogger(__name__)

__all__ = ["Transport"]


class Transport:
    @classmethod
    def from_data(cls, data):
        raise NotImplementedError

    def __hash__(self):
        raise NotImplementedError

    def create_shell(self) -> Shell:
        raise NotImplementedError

    def push_snapshot(self, shell: Shell, source_dataset: str, target_dataset: str, snapshot: str,
                      incremental_base: str, receive_resume_token: str):
        raise NotImplementedError
