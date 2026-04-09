class CountSquares:

    def __init__(self):
        self.points = []

    def add(self, point: List[int]) -> None:
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        # sol 1: find all 4 point combinations
        ans = 0
        for diag_point in self.points:
            # [1, 2]  [2, 2]
            # [1, 1]  [2, 1]
            
            # [1, 2]  [3, 2]
            # [1, 0]  [3, 0]
            # find diag point
            w = point[0] - diag_point[0]
            h = point[1] - diag_point[1]
            if w == 0 and h == 0:
                # diag point is the same point so skip
                continue
            if abs(w) == abs(h):
                # look for corner pairs
                for corner_point1 in self.points:
                    if corner_point1[0] == diag_point[0] and corner_point1[1] == point[1]:
                        for corner_point2 in self.points:
                            if corner_point2[1] == diag_point[1] and corner_point2[0] == point[0]:
                                ans += 1

        return ans

