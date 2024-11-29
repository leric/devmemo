from datetime import datetime
from typing import List, Literal
from pydantic import BaseModel


class MemoRecord(BaseModel):
    function: str
    timestamp: datetime
    author: str
    summary: str
    change_type: Literal['new', 'update', 'delete', 'rename', 'move']
    source_function: str | None = None


class GitCommit(BaseModel):
    hash: str
    message: str
    author: str
    author_time: datetime


class MemoRow(BaseModel):
    record: MemoRecord
    commit: GitCommit


class MemoFile(BaseModel):
    path: str
    records: List[MemoRow]


class MemoDirectory(BaseModel):
    version: str

