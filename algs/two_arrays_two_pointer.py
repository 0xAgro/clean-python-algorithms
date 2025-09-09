def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        i, j = 0, 0
        res = []

        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                res.append(A[i])
                i += 1
            else:
                res.append(B[j])
                j += 1

        res.extend(A[i:])
        res.extend(B[j:])
        
        return res
