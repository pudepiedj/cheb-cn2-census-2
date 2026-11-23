# Residue-p validation of the pair and (q,a) tail engines (23 November 2026)

**Target:** a(43) = 227541194846069456562210001 ≈ 2.275·10^26
= 17·19·29·41·53·79·131·139·199·727·4933·10889.
It is the smallest term with a prime on the residue-p branch, n ≡ p (mod (p²−1)/2): that prime is p = 4933. Its other eleven primes have residue 1.
In the census run it was found by the capped engine. Here the two tail engines are made to find it through 4933.
The question came from a reader (R. Vakil).

## pair/ — certified `cn2pair` (sha256 `bc3f49c6…`, the 10^28 and 10^30 binary, run as `../../pair/cn2pair`)

```
CN2X_MODE=cheb cn2pair 227600000000000000000000000 4900 10889 . 30 0 256 60 0
```
- X = 2.276·10^26, T = 4900, q* = 10889.
- a(43)'s two largest primes are p = 4933 (residue p) and q = 10889 (residue 1), so it lies in the pair family.
- `done.log` was pre-filled with shards 0–254, so only shard 255 ran. That shard contains q = 10889, the last prime.
- Result: `complete`; 3,335 pairs, 5,311 classes, 1,895,049,777 candidates, 1,436,455,784 Fermat tests and 85 passes.
- Exactly one of the 85 passes is a Chebyshev–Carmichael number, and it is a(43). Time: 1,309 s on one thread.
- An earlier build of the same source (`ee337b6e…`) with a different binary hash gave the identical 85 survivors.

## tail_top/ — `cn2tail_top` (sha256 `66d26d27…`, the 10^30 binary; this build is byte-identical to it)

```
python3 make_done.py done.log
CN2X_MODE=cheb CN2X_TOP_PMAX=4933 cn2tail_top 227600000000000000000000000 4932 . 30 0 268435456 60
```
- The frozen `cn2tail` can't be restricted to one prime: with R₀ < 4933 it would scan every prime above R₀, about 10^18 (p, a) pairs.
- `cn2tail_top` is the same scan with 64/128-bit storage. Its validation-only setting `CN2X_TOP_PMAX` lowers the prime bound, so with R₀ = 4932 and PMAX = 4933 the only prime is 4933.
- a(43) = 4933·m with m = 1 + a·g(4933), g = (4933²−1)/2 and a = 3791025462754109. That is family N (residue p), which is written as a `Q` line. It lies in shard (a−1) div 2^28 = 14122670.
- `make_done.py` marks every shard below 14126000 as done except 14122670, so 322 shards ran: the target and 321 at the top of the a-range. Their records are in `done_run.log`. The 14-million-line pre-filled log is not kept, because `make_done.py` regenerates it.
- Result: `complete`. Over the 322 shards there were 1.72·10^11 tests, 6.48·10^10 Fermat calls and exactly 1 pass: `Q 4933 3791025462754109`, which is a(43). Time: 2,487 s on 30 threads.
