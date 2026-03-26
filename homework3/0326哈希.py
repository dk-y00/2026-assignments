class MultipleDict:
    def __init__(self, size: int = 100):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key: str) -> int:
        """真正的hash函数"""
        # 使用Python内置的hash函数
        return hash(key) % self.size

    def put(self, key: str, value: int) -> None:
        hash_index: int = self._hash(key)
        bucket: list[tuple[str, int]] = self.table[hash_index]

        for index, (old_key, old_value) in enumerate(bucket):
            # 如果有旧的就替换
            if key == old_key:
                bucket[index] = (key, value)
                return

        # 如果没有就追加
        bucket.append((key, value))

    def get(self, key: str) -> int | None:
        """获取键对应的值"""
        hash_index = self._hash(key)
        bucket = self.table[hash_index]

        for old_key, old_value in bucket:
            if key == old_key:
                return old_value
        return None


