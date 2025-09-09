def twoSum(self, A: List[int], target: int) -> List[int]:
        seen = defaultdict(int)

        for idx, a in enumerate(A):
            if target - a  in seen:
                return [seen[target - a], idx]

            seen[a] = idx
