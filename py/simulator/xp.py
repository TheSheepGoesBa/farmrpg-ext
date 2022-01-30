LEVEL_TO_XP = {
    # This is an assumption.
    1: 0,
    # There are the explicitly known values.
    42: 3525402,
    43: 3920195,
    44: 4360783,
    45: 4852479,
    46: 5401211,
    47: 6013595,
    48: 6697015,
    49: 7459711,
    50: 8310879,
    51: 9260782,
    52: 10320873,
    53: 11503934,
    54: 12824230,
    55: 14297680,
    56: 15942050,
    57: 17777166,
    58: 19825155,
    59: 22110710,
    60: 24661389,
    61: 27507946,
    62: 30684703,
    63: 34229963,
    64: 38186473,
    65: 42601938,
    66: 47529596,
    67: 53666776,
    68: 60515868,
    69: 68159454,
    70: 76689695,
    71: 86209443,
    72: 96833481,
    73: 108689907,
    74: 121921678,
    75: 136688334,
    76: 153167922,
    77: 171559142,
    78: 192083743,
    79: 214989197,
    80: 240551683,
    81: 269079417,
    82: 300916368,
    83: 336446405,
    84: 376097926,
    85: 420349023,
    86: 469733247,
    87: 524846040,
    88: 586351916,
    89: 654992473,
    90: 731595334,
    91: 817084126,
    92: 912489617,
    93: 1018962144,
    94: 1137785484,
    95: 1270392331,
    96: 1418381572,
    97: 1583537564,
    98: 1767851651,
    99: 2000000000,
}

# Calculate the 2-41 values.
for level in range(2, 42):
    LEVEL_TO_XP[level] = round(31580.7731508038 * (1.118029202147977 ** level))


XP_TO_LEVEL = sorted(((v, k) for k, v in LEVEL_TO_XP.items()), key=lambda kv: kv[1])