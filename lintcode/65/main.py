def findMedianSortedArrays(self, A, B):
    m, n = len(A), len(B)
    p1, p2 = 0, 0
    v1, v2 = -1, -1

    for i in range((m + n) // 2 + 1):
        v1 = v2
        if p1 >= len(A) or p2 < len(B) and A[p1] > B[p2]:
            v2 = B[p2]
            p2 += 1
        else:
            v2 = A[p1]
            p1 += 1
    if (m + n) % 2 == 0:
        return v2
    return (v1+v2)/2