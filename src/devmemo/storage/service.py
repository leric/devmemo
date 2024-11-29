from typing import List
from devmemo.storage.models import MemoRecord, CommentUpdate

class StorageService:
    def __init__(self, root: str):
        self.root = root

    def summarize(file: str) -> List[MemoRecord]:
        pass

    def update_comment(file: str) -> List[CommentUpdate]:
        pass