class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):

        area1 = (C - A) * (D - B)
        area2 = (G - E) * (H - F)

        overlap_width = max(0, min(C, G) - max(A, E))
        overlap_height = max(0, min(D, H) - max(B, F))

        overlap = overlap_width * overlap_height

        return area1 + area2 - overlap