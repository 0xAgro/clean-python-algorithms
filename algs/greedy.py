def canJump(self, A: List[int]) -> bool:
        m = A[0]

        for idx, val in enumerate(A[:-1]):
            if m == idx and not val:
                return False

            m = max(idx + val, m)

        return True
