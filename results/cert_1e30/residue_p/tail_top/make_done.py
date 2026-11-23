#!/usr/bin/env python3
"""Write the pre-filled done.log used for the residue-p validation of cn2tail_top (cheb, X = 2.276e26, R0 = 4932,
CN2X_TOP_PMAX = 4933, W = 2^28).  With these settings the only prime is 4933 and the shards are a-ranges of width 2^28.
a(43) = 4933 * (1 + a g(4933)) with a = 3791025462754109, which lies in shard (a - 1) // 2^28 = 14122670.
Every shard id below 14126000 except that one is marked done (with zero counters), so the engine runs shard 14122670
and the 321 shards 14126000..14126320 at the top of the a-range.  Those 322 shards' records are in done_run.log."""
import sys
T, N = 14122670, 14126000
with open(sys.argv[1] if len(sys.argv) > 1 else 'done.log', 'w') as f:
    for i in range(N):
        if i != T:
            f.write(f'D {i} 0 0 0 0\n')
