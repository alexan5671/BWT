def bwt(s: str) -> tuple[str, int]:
    rotations = [s[i:] + s[:i] for i in range(len(s))]
    rotations.sort()
    bwt_str = "".join(row[-1] for row in rotations)
    original_index = rotations.index(s)
    return bwt_str, original_index


def ibwt(bwt_str: str, original_index: int) -> str:
    table = [""] * len(bwt_str)
    for _ in range(len(bwt_str)):
        table = sorted([bwt_str[i] + table[i] for i in range(len(bwt_str))])
    return table[original_index]
