---
location: post
title: Certified Chebyshev Census Below 10^30
author: Claude Opus 5.5 and JCP
date: 2026-11-08
---

# Certificate: the Chebyshev–Carmichael numbers below $10^{30}$

**Date:** 8 November 2026 (runs 17 October – 8 November)
**Definition:** OEIS A299799, Carmichael numbers that are Chebyshev pseudoprimes: odd composite $n$ with $n \equiv 1$ or $p \pmod{(p^2-1)/2}$ for every prime $p \mid n$. Equivalently (A175530's criterion, with Carmichael's condition), $n$ is squarefree, $p-1 \mid n-1$, and $n \equiv \pm 1$ modulo both $p-1$ and $p+1$, for every $p \mid n$.
**Status:** the computations are complete and every check below passes. The capped and pair engines are the certified ones of the census below $10^{28}$ ([cheb-cn2-census](https://github.com/pudepiedj/cheb-cn2-census), `docs/CN2_Cheb_Certificate_1e28.md`), byte for byte, in their $D = 2$ ("cheb") mode. The $(q,a)$ tail needed one change, because at $10^{30}$ its primes run past $2^{32}$: it was run as two engines that split the primes at $2^{32}$ (§3; proof in `docs/CN2_Tail_Coverage_Proof.md`, §3.1).
**Run directory:** `results/cert_1e30/`

---

## 1. The result

> **There are exactly 196 Chebyshev–Carmichael numbers (A299799) below $10^{30}$** (§4). No assumption is made about table caps or switch primes.

The 196 are:
- **95 Carmichael numbers of order 2**, all rigid. They are the 45 terms of A175531 below $10^{28}$ together with 50 in $[10^{28}, 10^{30})$. Every order-2 Carmichael number is a Chebyshev number, since $(p^2-1)/2$ divides $p^2-1$, so this run is also a census of order-2 numbers below $10^{30}$.
- **101 Chebyshev-only numbers**: Carmichael numbers of order 1 that are Chebyshev but not of order 2. At one or more of its primes each one sits "halfway round" $p^2-1$, that is, $n \equiv 1 + \tfrac{p^2-1}{2}$ or $p + \tfrac{p^2-1}{2} \pmod{p^2-1}$ (the column "halfway at" in §4).

**No non-rigid order-2 number lies below $10^{30}$.** A non-rigid order-2 number satisfies $n \equiv p \pmod{p^2-1}$ at some prime, so it is a Chebyshev number and this census would have found it. The smallest known non-rigid order-2 number is $\approx 4.63\times10^{36}$, so the smallest one lies in $(10^{30}, 4.63\times10^{36}]$.

Against what was known before this run:
- **a(1)–a(87)** are exactly the terms A299799 publishes: its b-file (n = 1..87, submitted 15 October 2026, published 20 October 2026), which is the certified census below $10^{28}$. a(1)–a(12) are also in the entry's DATA, which has room for no more.
- **109 terms are new**, all in $[10^{28}, 10^{30})$:
  - **50 are of order 2.** The conditional Howe run to $10^{30}$ with $T = 10^4$ (a conditional run, not included here; its 95 finds are `results/b175531.txt`) had already found them. That run finds exactly the order-2 numbers whose switch prime is at most $T$, so on its own it proves nothing about completeness. It found **exactly the 95 order-2 numbers below $10^{30}$ that this census finds**, no more and no fewer. So the census discovered no new order-2 number; it proves that the list of 95 is complete. It certifies the 50 as a(46)–a(95) of A175531.
  - **59 are Chebyshev-only** and were not known before this run. The conditional Howe run searched only for order-2 numbers, so it could not have found them.

**Smallest new terms.** The smallest term above $10^{28}$ is a(88) $= 10000966622030520698508186241$, which is also a(46) of A175531. The smallest new Chebyshev-only term is a(89) $= 11134962266231164874362652881 \approx 1.11\times10^{28}$.

**Distribution by decade:**

| decade | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| order 2 | 1 | 0 | 1 | 1 | 2 | 0 | 0 | 1 | 0 | 0 | 8 | 8 | 11 | 12 | 17 | 33 |
| Chebyshev-only | 1 | 0 | 0 | 0 | 0 | 2 | 2 | 1 | 0 | 2 | 4 | 5 | 8 | 17 | 29 | 30 |
| all terms | 2 | 0 | 1 | 1 | 2 | 2 | 2 | 2 | 0 | 2 | 12 | 13 | 19 | 29 | 46 | 63 |

**Other facts from the census:**
- **Halfway primes.** Of the 101 Chebyshev-only terms, 56 are halfway at one prime, 27 at two, 11 at three, 3 at four and 4 at five.
- **Smallest prime.** No term is divisible by 5 or 7. Five terms have 11 as their smallest prime: four of order 2 and one Chebyshev-only. No term has a smallest prime above 113. The only term with smallest prime 113 is a(18) $\approx 2.09\times10^{24}$, and the only one with 101 is a(126) $\approx 7.19\times10^{28}$.
- **Largest prime.** The largest prime factor of any term is still 474,949, in the Chebyshev-only a(82) $\approx 6.69\times10^{27}$. For the order-2 terms it is still 209,089, in a(73). No term above $10^{28}$ has a larger prime.
- **Second-largest prime.** The largest is 19,889, in a(126). Every term therefore has $p_{k-1} \le T = 30{,}000$ and is guaranteed by the capped part (§2). The two tail families were required to find nothing, and they found nothing.

## 2. Why the order-2 engines and proofs apply

This section is unchanged from the censuses below $10^{25}$ and $10^{28}$. The engines take the modulus $g(p) = (p^2-1)/D$ as a parameter: $D = 1$ for Howe's order-2 numbers, and $D = 2$ here. With $D = 2$ they search exactly the A299799 condition. Both proofs are written for general $D \in \lbrace 1, 2\rbrace$, and each fact they use holds for $D = 2$:
- **F1:** $n$ is odd and $3 \nmid n$;
- **F2:** $n/p > g(p)$;
- **F3:** $n$ has at least three primes;
- **F4:** the role bounds;
- **F5:** the admissibility facts;
- **F6:** Chebyshev numbers are Carmichael numbers of order 1, since $p-1 \mid (p-1)(p+1)/2$;
- **F7:** every prime satisfies $p^3 < D\thinspace n$, so $p < (2\times10^{30})^{1/3} \approx 1.26\times10^{10}$ here.

The search is split as at $10^{28}$, with larger $T$ and $q^*$, and with the $(q,a)$ tail divided at $2^{32}$:

| part | which $n$ | engine |
|---|---|---|
| capped | $p_{k-1} \le T = 30{,}000$ | `cn2xh`, `CN2X_MODE=cheb`, `CN2X_TCAP=30000`, `CN2X_LASTCALC=1` |
| pair tail | $p_{k-1} > T$ and $p_k \le q^* = 90{,}000{,}000$ | `cn2pair`, cheb mode |
| $(q,a)$ tail, lower | a prime in $(q^*, 2^{32}-1]$ | `cn2tail`, cheb mode, $R_0 = q^*$, `CN2X_TAIL_CAP32=1` |
| $(q,a)$ tail, upper | a prime in $(2^{32}-1, 1.26\times10^{10}]$ | `cn2tail_top`, cheb mode, $R_0 = 2^{32}-1$ |

**Why the tail had to be split.** The frozen `cn2tail` stores its primes in 32 bits and computes $g(q)$ in 64 bits. It refuses to start if the F7 bound on the primes exceeds $2^{32}-1$, so it can't run at $X = 10^{30}$; it accepts cheb mode only for $X < 2^{95} \approx 3.96\times10^{28}$. The two engines are:
- **`cn2tail` with one added line.** If `CN2X_TAIL_CAP32` is set, it lowers its prime bound to $2^{32}-1$ before the start-up check. Without the setting it behaves exactly as the frozen engine, and it still refuses at $10^{30}$ (checked). Below $2^{32}$ the search is the frozen engine's.
- **`cn2tail_top`**, for primes above $2^{32}$. It holds primes in 64 bits and $g(q)$ in 128 bits, and its start-up check requires $q < 2^{43}$. It also has a validation-only setting, `CN2X_TOP_PMAX`, that lowers the prime bound; the production run didn't use it. Nothing else differs from the frozen engine.

Together the two prime ranges are exactly the frozen engine's, $(q^*, \lfloor(D(X-1))^{1/3}\rfloor]$. `docs/CN2_Tail_Coverage_Proof.md`, §3.1, proves that the two runs together cover the $(q,a)$ case.

**Validation of the two tail engines before the run** (`tail/`, `tail_top/`):

| test | compared with | result |
|---|---|---|
| frozen; patched without the setting; patched with it; `cn2tail_top`, all at $10^{24}$ cheb ($R_0 = 10^7$) | each other | identical (14 survivors, all counters) |
| the same four at $10^{28}$ cheb and $10^{28}$ Howe ($R_0 = 10^9$) | each other | identical counters |
| the overlap $(4289967295, 2^{32}-1]$ at $10^{30}$, cheb and test mode | patched `cn2tail` vs `cn2tail_top` | identical, including 4,620,948 test-mode lines |
| `cn2tail_top` above $2^{32}$: windows $(2^{32}-1, +2\times10^6]$, $(8\times10^9, 8.001\times10^9]$ and $(T-2\times10^6, T]$, in test and cheb modes, and a Howe window | an independent exact Python brute force (`check_top_brute.py`) | PASS: survivors and all four counters agree |

The top window has $g(q) > 2^{64}$, so the brute force exercises the 128-bit arithmetic directly.

## 3. The runs

The hashes are recorded in `ENGINES.sha256` (capped, pair, frozen tail) and `ENGINES_tail_1e30.sha256` (both tail engines and the brute-force checker), and were rechecked after the runs. The capped and pair files have the same sha256 as those of the $10^{28}$ certificate:

| file | sha256 |
|---|---|
| `capped/cn2xh` / `cn2xh.c` | `1a8157d0…` / `d7beea88…` (as at $10^{28}$) |
| `pair/cn2pair` / `cn2pair.c` | `bc3f49c6…` / `ee337b6e…` (as at $10^{28}$) |
| `tail/cn2tail.frozen` / `.frozen.c` | `aa96fb59…` / `c5379c21…` (the certified tail, kept for reference) |
| `tail/cn2tail` / `cn2tail.c` | `db7d324f…` / `48297051…` (frozen plus one line) |
| `tail_top/cn2tail_top` / `.c` | `66d26d27…` / `c9dc2176…` |
| `tail_top/check_top_brute.py` | `4d4ca2cf…` |

`ENGINES.sha256` still lists the frozen tail under `tail/cn2tail`, so `shasum -c` reports those two lines as FAILED. That is expected: the frozen copies now sit beside the patched build as `tail/cn2tail.frozen*` and match.

| | capped | pair tail | $(q,a)$ tail, lower | $(q,a)$ tail, upper |
|---|---|---|---|---|
| shards | 340,065 / 340,065 | 4,096 / 4,096 | 48,702 / 48,702 | 234 / 234 |
| completion record | `"complete":true`, mode 2, `"lastcalc":1`, `skipmask 0` | `"complete":true`, mode 2 | `"complete":true`, mode 2 | `"complete":true`, mode 2 |
| work | $3.85\times10^{13}$ nodes; $2.68\times10^{13}$ LIST candidates | $1.36\times10^{13}$ pairs; $6.51\times10^{12}$ candidates | $1.31\times10^{13}$ tests over 198,063,267 primes $q$ | $3.92\times10^{9}$ tests over 364,068,636 primes $q$ |
| survivors verified (distinct) | 33,314,816 | 123,210 | 315 | 0 |
| numbers below $X$ | 196 | 0 | 0 | 0 |
| search time (30 threads) | 265 h (three sessions) | 100.3 h | 64.5 h (three sessions) | 2 min |

Every shard is recorded exactly once in each `done.log`. The run took 17 October 16:02 to 8 November 03:12, with the stages run one after another.

**Interruptions.**
- Capped ran in three sessions: 99.7 h, 13.1 h and 152.1 h.
- The lower $(q,a)$ tail was interrupted by two power cuts on 6 November and resumed twice. Its three sessions were 24.4 h, 5.7 h and 34.4 h.
- After each restart, the run logs were checked for malformed lines and duplicate shard IDs; there were none.
- A shard is recorded in `done.log` only after its output is flushed, so a shard in progress at a cut is run again in full. Its survivors may then appear twice in `out.txt`. Capped's `out.txt` has 33,629,038 lines and 33,314,816 distinct ones, and the lower tail's has 316 and 315. The verifiers count each number once.

**Verification.**
- **The capped half:** `cn2_split_campaign.py verify --dir results/cert_1e30 --reference ../cheb-cn2-census/results/cert_1e28` (`result.json`, `campaign_verify_final.txt`) finds 196 numbers. Phase consistency is OK, there are no inconsistencies, and all 87 reference terms are re-found with none missing. The "CONDITIONAL" scope line and "tail: False" warning are expected, as at $10^{28}$: `split.json` describes the capped stage only, and the tails are run and verified separately.
- **The tails:** `cn2_tail_verify.py --X 1e30 --mode cheb --pair pair --qa tail tail_top --T 30000 --reference reference_cheb_1e30.json` gives **PASS** (`tail_verify_final.txt`). It checks 123,210 pair survivors and 316 $(q,a)$ survivors, and finds no number below $X$. It needs none: no reference term has its second-largest prime above $T$.
- **The union** of the two halves is the 196 terms.

No `UNPROVEN-PRIMALITY` flag was raised.

**What this run could not test.** At $10^{28}$ the pair family found the one term only it guaranteed, $2.088\times10^{24}$ (whose second-largest prime, 15,391, exceeded $T = 15{,}000$). At $T = 30{,}000$ that term falls in the capped part. So at $10^{30}$ the pair and tail families had no live term to re-find. Their completeness rests on the proof (`docs/CN2_Tail_Coverage_Proof.md`), on the $10^{28}$ run with the same pair engine, and on the validation in §2 for the two tail engines.

**No shard replay** was run at $10^{30}$, unlike at $10^{28}$. A replay re-runs a sample of shards alone and compares their work counters with the record. Here its value would have been small:
- the capped and pair binaries are the ones already replayed at $10^{28}$;
- the capped part re-found all 87 terms below $10^{28}$, spread over many roots;
- the two tail engines were validated against the frozen engine and an independent brute force before the run;
- `done.log` records a shard only after it completes.

## 4. The 196 terms

"Before this run" says where each term was already known: **DATA** for the 12 terms in A299799's DATA, **b-file** for the other terms of A299799's b-file (the census below $10^{28}$), and **new** otherwise. "Guaranteed by" names the part whose theorem covers the term. The b-file is `results/cert_1e30/b299799_1e30.txt`.

| # | $n$ | $\log_{10} n$ | $k$ | prime factors | class | halfway at | before this run | guaranteed by |
|---|---|---|---|---|---|---|---|---|
| 1 | 443372888629441 | 14.65 | 8 | 17 · 31 · 41 · 43 · 89 · 97 · 167 · 331 | CN2 (rigid) |  | DATA | capped |
| 2 | 582920080863121 | 14.77 | 7 | 41 · 53 · 79 · 103 · 239 · 271 · 509 | **cheb only** | 79,239,271 | DATA | capped |
| 3 | 39671149333495681 | 16.60 | 9 | 17 · 37 · 41 · 71 · 79 · 97 · 113 · 131 · 191 | CN2 (rigid) |  | DATA | capped |
| 4 | 842526563598720001 | 17.93 | 8 | 17 · 61 · 71 · 89 · 197 · 311 · 769 · 2729 | CN2 (rigid) |  | DATA | capped |
| 5 | 2380296518909971201 | 18.38 | 9 | 19 · 41 · 43 · 71 · 89 · 127 · 199 · 449 · 991 | CN2 (rigid) |  | DATA | capped |
| 6 | 3188618003602886401 | 18.50 | 8 | 29 · 37 · 79 · 181 · 191 · 449 · 701 · 3457 | CN2 (rigid) |  | DATA | capped |
| 7 | 33711266676317630401 | 19.53 | 9 | 17 · 29 · 37 · 41 · 151 · 199 · 449 · 571 · 5851 | **cheb only** | 449 | DATA | capped |
| 8 | 54764632857801026161 | 19.74 | 9 | 41 · 53 · 79 · 137 · 139 · 181 · 239 · 271 · 1429 | **cheb only** | 79,239,271 | DATA | capped |
| 9 | 122762671289519184001 | 20.09 | 11 | 13 · 17 · 19 · 29 · 41 · 89 · 97 · 127 · 199 · 251 · 449 | **cheb only** | 127 | DATA | capped |
| 10 | 361266866679292635601 | 20.56 | 11 | 17 · 23 · 29 · 37 · 41 · 43 · 61 · 109 · 199 · 419 · 881 | **cheb only** | 17,881 | DATA | capped |
| 11 | 4208895375600667752001 | 21.62 | 10 | 17 · 29 · 31 · 43 · 71 · 79 · 199 · 389 · 2521 · 5851 | CN2 (rigid) |  | DATA | capped |
| 12 | 7673096805497432749441 | 21.88 | 10 | 29 · 31 · 37 · 43 · 53 · 109 · 127 · 571 · 3079 · 4159 | **cheb only** | 127 | DATA | capped |
| 13 | 193966598206145637873001 | 23.29 | 11 | 19 · 23 · 29 · 41 · 71 · 89 · 101 · 103 · 701 · 1429 · 5669 | **cheb only** | 23,41,71,89,103 | b-file | capped |
| 14 | 623655451404913888200241 | 23.79 | 9 | 23 · 79 · 109 · 239 · 881 · 883 · 1223 · 1973 · 7019 | **cheb only** | 79,239,881 | b-file | capped |
| 15 | 1159954316194989017102401 | 24.06 | 9 | 31 · 47 · 109 · 137 · 307 · 2927 · 3079 · 4049 · 4759 | CN2 (rigid) |  | b-file | capped |
| 16 | 1327183446436495124400001 | 24.12 | 11 | 13 · 17 · 23 · 29 · 89 · 97 · 251 · 449 · 641 · 1499 · 9631 | **cheb only** | 641 | b-file | capped |
| 17 | 1457044155748208447259841 | 24.16 | 10 | 79 · 97 · 131 · 139 · 191 · 229 · 379 · 461 · 571 · 2393 | **cheb only** | 191 | b-file | capped |
| 18 | 2088144166339753513992001 | 24.32 | 8 | 113 · 199 · 239 · 263 · 701 · 7919 · 15391 · 17291 | CN2 (rigid) |  | b-file | capped |
| 19 | 2196407820059694924883201 | 24.34 | 9 | 53 · 109 · 127 · 281 · 307 · 379 · 647 · 10529 · 13441 | CN2 (rigid) |  | b-file | capped |
| 20 | 3339611018825185787482801 | 24.52 | 12 | 19 · 41 · 43 · 53 · 67 · 89 · 103 · 131 · 137 · 307 · 389 · 1429 | CN2 (rigid) |  | b-file | capped |
| 21 | 3464334205088776324905601 | 24.54 | 12 | 17 · 31 · 37 · 41 · 43 · 59 · 113 · 181 · 199 · 233 · 521 · 3457 | **cheb only** | 3457 | b-file | capped |
| 22 | 4105879060352839139462401 | 24.61 | 8 | 89 · 239 · 401 · 2143 · 2311 · 3571 · 3761 · 7237 | CN2 (rigid) |  | b-file | capped |
| 23 | 4809665063400557951190601 | 24.68 | 10 | 41 · 53 · 67 · 103 · 151 · 379 · 571 · 701 · 2393 · 5851 | **cheb only** | 41,103,151,2393 | b-file | capped |
| 24 | 5002862939121639632040001 | 24.70 | 11 | 31 · 53 · 79 · 89 · 101 · 151 · 181 · 251 · 379 · 647 · 2549 | CN2 (rigid) |  | b-file | capped |
| 25 | 7865064643837556041286401 | 24.90 | 11 | 23 · 37 · 67 · 89 · 101 · 109 · 181 · 199 · 433 · 571 · 15809 | CN2 (rigid) |  | b-file | capped |
| 26 | 9400084864021826054720641 | 24.97 | 11 | 23 · 31 · 53 · 79 · 103 · 197 · 239 · 379 · 521 · 727 · 4523 | CN2 (rigid) |  | b-file | capped |
| 27 | 12071465216556111317952001 | 25.08 | 12 | 37 · 41 · 53 · 59 · 89 · 109 · 127 · 151 · 191 · 233 · 379 · 811 | CN2 (rigid) |  | b-file | capped |
| 28 | 13935937975195278973392001 | 25.14 | 12 | 23 · 29 · 37 · 71 · 83 · 109 · 113 · 127 · 199 · 251 · 419 · 2927 | **cheb only** | 127 | b-file | capped |
| 29 | 19087839966156095154384001 | 25.28 | 12 | 11 · 17 · 37 · 41 · 79 · 113 · 139 · 181 · 251 · 379 · 911 · 3457 | **cheb only** | 3457 | b-file | capped |
| 30 | 31280524488319495535546401 | 25.50 | 11 | 19 · 23 · 43 · 59 · 71 · 109 · 271 · 311 · 701 · 1301 · 47431 | CN2 (rigid) |  | b-file | capped |
| 31 | 32492501043239735947612801 | 25.51 | 11 | 11 · 31 · 41 · 79 · 103 · 271 · 313 · 389 · 911 · 2521 · 3769 | CN2 (rigid) |  | b-file | capped |
| 32 | 36991212507320386599648001 | 25.57 | 11 | 11 · 31 · 37 · 53 · 97 · 191 · 379 · 883 · 1151 · 2549 · 3041 | CN2 (rigid) |  | b-file | capped |
| 33 | 44774022865681509785985601 | 25.65 | 11 | 19 · 41 · 67 · 89 · 101 · 131 · 139 · 233 · 271 · 1301 · 63799 | CN2 (rigid) |  | b-file | capped |
| 34 | 50473184681492173584023041 | 25.70 | 11 | 37 · 53 · 67 · 131 · 139 · 181 · 229 · 419 · 577 · 911 · 2311 | CN2 (rigid) |  | b-file | capped |
| 35 | 54475112449147532388966721 | 25.74 | 10 | 29 · 97 · 103 · 139 · 181 · 307 · 827 · 1061 · 2393 · 11593 | CN2 (rigid) |  | b-file | capped |
| 36 | 68886771046178424397858801 | 25.84 | 11 | 53 · 71 · 79 · 101 · 109 · 139 · 181 · 461 · 647 · 911 · 3079 | **cheb only** | 79,911 | b-file | capped |
| 37 | 71712112526158742082244801 | 25.86 | 11 | 23 · 29 · 41 · 79 · 101 · 131 · 419 · 449 · 911 · 1223 · 11969 | **cheb only** | 449,11969 | b-file | capped |
| 38 | 76587257660615840312697601 | 25.88 | 11 | 13 · 19 · 31 · 67 · 107 · 139 · 197 · 479 · 1471 · 1801 · 40151 | CN2 (rigid) |  | b-file | capped |
| 39 | 85737999338407807647656401 | 25.93 | 12 | 23 · 29 · 53 · 79 · 101 · 103 · 109 · 181 · 199 · 239 · 647 · 4861 | **cheb only** | 79,239 | b-file | capped |
| 40 | 111356194710608262218643841 | 26.05 | 10 | 41 · 61 · 79 · 113 · 131 · 379 · 683 · 2729 · 4159 · 12959 | CN2 (rigid) |  | b-file | capped |
| 41 | 191970596806626660335913601 | 26.28 | 13 | 17 · 23 · 31 · 37 · 43 · 53 · 71 · 113 · 199 · 241 · 337 · 419 · 3457 | **cheb only** | 3457 | b-file | capped |
| 42 | 213622061697266764349808001 | 26.33 | 12 | 23 · 29 · 31 · 71 · 89 · 97 · 103 · 181 · 251 · 307 · 1871 · 6271 | **cheb only** | 6271 | b-file | capped |
| 43 | 227541194846069456562210001 | 26.36 | 12 | 17 · 19 · 29 · 41 · 53 · 79 · 131 · 139 · 199 · 727 · 4933 · 10889 | **cheb only** | 17,79,4933 | b-file | capped |
| 44 | 244041085292561389352520001 | 26.39 | 11 | 23 · 61 · 113 · 131 · 193 · 251 · 271 · 337 · 701 · 911 · 4159 | **cheb only** | 193,4159 | b-file | capped |
| 45 | 257553076956557894240652001 | 26.41 | 12 | 13 · 29 · 43 · 67 · 71 · 101 · 109 · 197 · 199 · 271 · 3499 · 8161 | **cheb only** | 8161 | b-file | capped |
| 46 | 373851853012084355680131361 | 26.57 | 11 | 37 · 71 · 103 · 109 · 131 · 181 · 239 · 419 · 461 · 3079 · 3761 | CN2 (rigid) |  | b-file | capped |
| 47 | 419746116449969951645203201 | 26.62 | 12 | 17 · 37 · 43 · 53 · 71 · 109 · 151 · 191 · 281 · 881 · 1409 · 3761 | CN2 (rigid) |  | b-file | capped |
| 48 | 472936079653356733106893201 | 26.67 | 10 | 23 · 43 · 197 · 349 · 419 · 521 · 701 · 911 · 5851 · 8527 | **cheb only** | 911,8527 | b-file | capped |
| 49 | 480650413824292471675755841 | 26.68 | 11 | 29 · 41 · 89 · 131 · 197 · 239 · 271 · 727 · 881 · 1429 · 2969 | CN2 (rigid) |  | b-file | capped |
| 50 | 507710311713618241797676801 | 26.71 | 11 | 41 · 47 · 71 · 89 · 127 · 151 · 241 · 967 · 1103 · 2089 · 4049 | CN2 (rigid) |  | b-file | capped |
| 51 | 571197082724681188312817281 | 26.76 | 11 | 29 · 43 · 67 · 71 · 131 · 211 · 307 · 953 · 1021 · 1429 · 8161 | CN2 (rigid) |  | b-file | capped |
| 52 | 598764213578029575774297601 | 26.78 | 13 | 23 · 29 · 43 · 53 · 79 · 109 · 113 · 127 · 181 · 239 · 379 · 433 · 449 | CN2 (rigid) |  | b-file | capped |
| 53 | 667882655094744395121816001 | 26.82 | 10 | 67 · 83 · 131 · 163 · 199 · 239 · 461 · 2393 · 5167 · 20747 | CN2 (rigid) |  | b-file | capped |
| 54 | 749114380387868248644660001 | 26.87 | 10 | 23 · 41 · 67 · 97 · 109 · 379 · 1567 · 4999 · 7309 · 51679 | **cheb only** | 97,1567,51679 | b-file | capped |
| 55 | 768927403921604814222336001 | 26.89 | 10 | 43 · 67 · 137 · 251 · 271 · 349 · 769 · 1427 · 4159 · 17981 | CN2 (rigid) |  | b-file | capped |
| 56 | 847201873829461072769246401 | 26.93 | 11 | 37 · 41 · 43 · 71 · 103 · 239 · 281 · 379 · 2287 · 2549 · 11969 | **cheb only** | 11969 | b-file | capped |
| 57 | 922904786964947393227420801 | 26.97 | 10 | 17 · 37 · 41 · 311 · 929 · 1217 · 1301 · 1601 · 3191 · 15313 | CN2 (rigid) |  | b-file | capped |
| 58 | 946295515632681859275671041 | 26.98 | 11 | 29 · 43 · 89 · 109 · 131 · 181 · 229 · 991 · 1427 · 1429 · 7129 | CN2 (rigid) |  | b-file | capped |
| 59 | 1445961713544933049178794081 | 27.16 | 12 | 23 · 37 · 41 · 43 · 53 · 89 · 109 · 241 · 571 · 929 · 2089 · 7019 | **cheb only** | 929 | b-file | capped |
| 60 | 1480947968491738280801467201 | 27.17 | 10 | 17 · 59 · 71 · 419 · 521 · 683 · 811 · 3191 · 4159 · 12959 | **cheb only** | 4159 | b-file | capped |
| 61 | 1710675679046386360978509841 | 27.23 | 11 | 43 · 59 · 89 · 131 · 233 · 311 · 433 · 463 · 1429 · 1489 · 1871 | **cheb only** | 433,463,1489,1871 | b-file | capped |
| 62 | 1800270906592423387847044321 | 27.26 | 10 | 79 · 97 · 103 · 137 · 211 · 1019 · 1117 · 2861 · 2969 · 8161 | **cheb only** | 97,8161 | b-file | capped |
| 63 | 1800352719110727998002987201 | 27.26 | 13 | 17 · 19 · 59 · 71 · 79 · 89 · 97 · 131 · 233 · 349 · 449 · 463 · 881 | **cheb only** | 449 | b-file | capped |
| 64 | 1862295045464158166966504401 | 27.27 | 11 | 43 · 47 · 71 · 107 · 197 · 239 · 307 · 919 · 1301 · 2311 · 3037 | **cheb only** | 47,239 | b-file | capped |
| 65 | 1941211286859256920630460801 | 27.29 | 12 | 31 · 37 · 41 · 43 · 89 · 101 · 151 · 199 · 307 · 463 · 2089 · 11969 | CN2 (rigid) |  | b-file | capped |
| 66 | 2119047331560739293908113921 | 27.33 | 12 | 17 · 37 · 43 · 47 · 79 · 89 · 113 · 127 · 571 · 911 · 3541 · 8969 | CN2 (rigid) |  | b-file | capped |
| 67 | 2142752298785201165308646401 | 27.33 | 11 | 23 · 37 · 83 · 113 · 163 · 191 · 601 · 701 · 911 · 3079 · 7297 | CN2 (rigid) |  | b-file | capped |
| 68 | 2325041445996414342573536161 | 27.37 | 11 | 19 · 29 · 47 · 71 · 79 · 137 · 557 · 619 · 2729 · 10711 · 11593 | CN2 (rigid) |  | b-file | capped |
| 69 | 2981071306952233928836603201 | 27.47 | 11 | 17 · 41 · 181 · 199 · 349 · 449 · 587 · 599 · 881 · 1171 · 2089 | **cheb only** | 449 | b-file | capped |
| 70 | 3002549563607572248383836801 | 27.48 | 12 | 13 · 29 · 43 · 89 · 109 · 127 · 263 · 353 · 461 · 827 · 1049 · 4049 | **cheb only** | 127 | b-file | capped |
| 71 | 3055408335216475232299905601 | 27.49 | 12 | 23 · 89 · 101 · 103 · 113 · 131 · 151 · 241 · 449 · 571 · 727 · 1429 | **cheb only** | 449 | b-file | capped |
| 72 | 3184712715668896364421268801 | 27.50 | 12 | 31 · 37 · 41 · 71 · 79 · 131 · 191 · 199 · 571 · 661 · 1217 · 5279 | **cheb only** | 191,1217 | b-file | capped |
| 73 | 3213322593860118229475166721 | 27.51 | 10 | 37 · 61 · 67 · 71 · 419 · 433 · 617 · 1103 · 11593 · 209089 | CN2 (rigid) |  | b-file | capped |
| 74 | 4291812303515083594987740001 | 27.63 | 11 | 43 · 47 · 73 · 113 · 151 · 223 · 461 · 571 · 599 · 5851 · 8287 | **cheb only** | 223,8287 | b-file | capped |
| 75 | 4383862422930048259296295201 | 27.64 | 11 | 37 · 53 · 71 · 97 · 163 · 379 · 419 · 491 · 701 · 1709 · 21319 | **cheb only** | 97 | b-file | capped |
| 76 | 4497699707671000342005093601 | 27.65 | 10 | 19 · 59 · 89 · 233 · 431 · 601 · 701 · 7309 · 9631 · 15137 | **cheb only** | 9631,15137 | b-file | capped |
| 77 | 4635427415991948819511107841 | 27.67 | 13 | 23 · 29 · 37 · 53 · 71 · 89 · 113 · 127 · 191 · 271 · 379 · 647 · 3079 | CN2 (rigid) |  | b-file | capped |
| 78 | 4955815709824370817666240001 | 27.70 | 12 | 41 · 67 · 71 · 73 · 103 · 131 · 199 · 239 · 271 · 701 · 1091 · 2617 | **cheb only** | 73 | b-file | capped |
| 79 | 5466953848346666426169619201 | 27.74 | 11 | 37 · 59 · 79 · 109 · 113 · 151 · 229 · 1217 · 2311 · 4523 · 5851 | CN2 (rigid) |  | b-file | capped |
| 80 | 6037031106243073961934109201 | 27.78 | 12 | 23 · 37 · 89 · 109 · 131 · 151 · 181 · 211 · 281 · 397 · 1483 · 5851 | CN2 (rigid) |  | b-file | capped |
| 81 | 6473975735726053723736568001 | 27.81 | 13 | 23 · 31 · 53 · 71 · 79 · 97 · 131 · 151 · 181 · 239 · 419 · 593 · 1481 | CN2 (rigid) |  | b-file | capped |
| 82 | 6689253573790144737930673201 | 27.83 | 10 | 13 · 47 · 67 · 149 · 239 · 307 · 919 · 3673 · 9323 · 474949 | **cheb only** | 47,239 | b-file | capped |
| 83 | 6901344518427089880041692801 | 27.84 | 12 | 29 · 37 · 41 · 43 · 71 · 101 · 127 · 151 · 701 · 1871 · 3457 · 5851 | **cheb only** | 127,3457 | b-file | capped |
| 84 | 7006270310872326698183179201 | 27.85 | 10 | 41 · 71 · 89 · 103 · 199 · 211 · 5851 · 6359 · 8161 · 20593 | CN2 (rigid) |  | b-file | capped |
| 85 | 8601689148505906566116203201 | 27.93 | 10 | 59 · 71 · 109 · 241 · 349 · 521 · 701 · 2053 · 2843 · 105071 | CN2 (rigid) |  | b-file | capped |
| 86 | 8838800136403254764954638201 | 27.95 | 12 | 29 · 43 · 67 · 71 · 101 · 109 · 139 · 151 · 919 · 1427 · 1597 · 3079 | **cheb only** | 71,151,919,3079 | b-file | capped |
| 87 | 9799274291299994931676646401 | 27.99 | 12 | 31 · 41 · 53 · 71 · 101 · 103 · 199 · 239 · 379 · 449 · 4159 · 5851 | CN2 (rigid) |  | b-file | capped |
| 88 | 10000966622030520698508186241 | 28.00 | 12 | 23 · 29 · 31 · 71 · 79 · 83 · 131 · 379 · 911 · 1231 · 1559 · 11969 | CN2 (rigid) |  | **new** | capped |
| 89 | 11134962266231164874362652881 | 28.05 | 11 | 13 · 19 · 71 · 109 · 137 · 373 · 433 · 919 · 953 · 3673 · 81839 | **cheb only** | 433,81839 | **new** | capped |
| 90 | 11743543456705885034950740001 | 28.07 | 11 | 59 · 71 · 97 · 131 · 137 · 229 · 241 · 463 · 727 · 4999 · 17341 | **cheb only** | 97 | **new** | capped |
| 91 | 12096348505751118611470628161 | 28.08 | 12 | 37 · 41 · 43 · 47 · 97 · 109 · 227 · 229 · 379 · 571 · 2003 · 16561 | CN2 (rigid) |  | **new** | capped |
| 92 | 12154703615948336130338851201 | 28.08 | 12 | 29 · 43 · 61 · 79 · 139 · 239 · 311 · 313 · 373 · 461 · 1427 · 2549 | **cheb only** | 313 | **new** | capped |
| 93 | 12280804926059535591106180801 | 28.09 | 11 | 31 · 53 · 131 · 151 · 191 · 271 · 349 · 379 · 1471 · 2393 · 15679 | **cheb only** | 191,1471,15679 | **new** | capped |
| 94 | 12737263817300842658077192801 | 28.11 | 12 | 37 · 47 · 61 · 97 · 101 · 271 · 307 · 379 · 433 · 461 · 683 · 2851 | **cheb only** | 97 | **new** | capped |
| 95 | 12921258224284865643123936001 | 28.11 | 13 | 23 · 29 · 41 · 43 · 53 · 71 · 89 · 109 · 251 · 449 · 701 · 1889 · 2017 | CN2 (rigid) |  | **new** | capped |
| 96 | 12928912537758504200832441601 | 28.11 | 10 | 13 · 109 · 151 · 199 · 577 · 1409 · 2069 · 2161 · 2351 · 35531 | CN2 (rigid) |  | **new** | capped |
| 97 | 13551147801850177161540817921 | 28.13 | 13 | 29 · 31 · 47 · 89 · 113 · 127 · 137 · 181 · 197 · 239 · 307 · 769 · 911 | CN2 (rigid) |  | **new** | capped |
| 98 | 14048188307862781503789388801 | 28.15 | 12 | 31 · 47 · 67 · 89 · 127 · 137 · 139 · 239 · 449 · 769 · 1151 · 7039 | CN2 (rigid) |  | **new** | capped |
| 99 | 15698008387299304739312640001 | 28.20 | 13 | 17 · 23 · 41 · 43 · 73 · 109 · 127 · 199 · 241 · 281 · 701 · 1409 · 1693 | **cheb only** | 73 | **new** | capped |
| 100 | 18823151230401360689537090401 | 28.27 | 10 | 31 · 37 · 197 · 271 · 881 · 2029 · 2089 · 3191 · 4409 · 5851 | **cheb only** | 31 | **new** | capped |
| 101 | 20464553098335414488319900001 | 28.31 | 13 | 17 · 31 · 41 · 43 · 53 · 71 · 151 · 157 · 199 · 631 · 701 · 911 · 3079 | **cheb only** | 31 | **new** | capped |
| 102 | 21601455918312583418275170001 | 28.33 | 11 | 23 · 79 · 83 · 179 · 199 · 251 · 349 · 811 · 1231 · 5741 · 8009 | **cheb only** | 79,1231 | **new** | capped |
| 103 | 21995062699687000159829392801 | 28.34 | 11 | 23 · 41 · 43 · 53 · 269 · 701 · 881 · 2143 · 2549 · 2551 · 4421 | **cheb only** | 2143 | **new** | capped |
| 104 | 23651361712868472625849606801 | 28.37 | 12 | 23 · 41 · 43 · 67 · 101 · 103 · 239 · 331 · 419 · 571 · 1429 · 30941 | **cheb only** | 239 | **new** | capped |
| 105 | 24114300099590121401824683841 | 28.38 | 11 | 19 · 31 · 103 · 181 · 197 · 239 · 461 · 1471 · 1871 · 4159 · 8839 | **cheb only** | 1471,4159 | **new** | capped |
| 106 | 32351613589818545871858609601 | 28.51 | 13 | 17 · 31 · 41 · 53 · 89 · 139 · 151 · 191 · 449 · 461 · 599 · 701 · 911 | **cheb only** | 191,449 | **new** | capped |
| 107 | 34111287958931169952279073761 | 28.53 | 12 | 19 · 31 · 43 · 59 · 67 · 89 · 233 · 509 · 1429 · 1871 · 2287 · 5279 | **cheb only** | 31,5279 | **new** | capped |
| 108 | 36442085590214555168363846401 | 28.56 | 12 | 37 · 59 · 79 · 89 · 113 · 181 · 191 · 271 · 337 · 419 · 1327 · 11969 | CN2 (rigid) |  | **new** | capped |
| 109 | 41863530967813882076637888001 | 28.62 | 14 | 17 · 23 · 31 · 37 · 41 · 71 · 89 · 113 · 131 · 181 · 191 · 251 · 911 · 3079 | CN2 (rigid) |  | **new** | capped |
| 110 | 42025914667200258779342117761 | 28.62 | 12 | 41 · 59 · 61 · 107 · 109 · 127 · 131 · 311 · 433 · 991 · 1567 · 7019 | **cheb only** | 127 | **new** | capped |
| 111 | 43479088325949473226786556801 | 28.64 | 12 | 17 · 47 · 79 · 131 · 181 · 191 · 419 · 461 · 599 · 641 · 857 · 2393 | **cheb only** | 641 | **new** | capped |
| 112 | 46646676334362776013754251841 | 28.67 | 13 | 29 · 37 · 41 · 79 · 109 · 113 · 131 · 181 · 197 · 307 · 461 · 881 · 1871 | CN2 (rigid) |  | **new** | capped |
| 113 | 47073397944825265701015820801 | 28.67 | 11 | 31 · 41 · 109 · 127 · 151 · 307 · 379 · 811 · 2689 · 3079 · 22679 | CN2 (rigid) |  | **new** | capped |
| 114 | 48076467088279989582023640841 | 28.68 | 11 | 37 · 41 · 67 · 131 · 281 · 419 · 571 · 683 · 1223 · 2729 · 23561 | **cheb only** | 41,281,1223,2729,23561 | **new** | capped |
| 115 | 48233855879863040475353865601 | 28.68 | 11 | 31 · 47 · 53 · 89 · 103 · 239 · 463 · 1709 · 1871 · 5279 · 36479 | **cheb only** | 36479 | **new** | capped |
| 116 | 48899165243656630330763899201 | 28.69 | 11 | 11 · 19 · 29 · 79 · 137 · 701 · 1301 · 1427 · 1889 · 3359 · 90271 | CN2 (rigid) |  | **new** | capped |
| 117 | 55654824887414879449045282561 | 28.75 | 11 | 31 · 43 · 47 · 53 · 461 · 463 · 769 · 1429 · 1871 · 3191 · 11969 | **cheb only** | 769 | **new** | capped |
| 118 | 56259612931685661605147040001 | 28.75 | 12 | 29 · 67 · 89 · 103 · 131 · 223 · 229 · 307 · 419 · 701 · 1259 · 4159 | CN2 (rigid) |  | **new** | capped |
| 119 | 56503870441915041752546459521 | 28.75 | 11 | 89 · 103 · 127 · 131 · 197 · 239 · 439 · 521 · 1567 · 4159 · 5279 | **cheb only** | 127 | **new** | capped |
| 120 | 57291200994173796305950694401 | 28.76 | 12 | 29 · 31 · 43 · 89 · 101 · 131 · 137 · 421 · 727 · 919 · 4159 · 7853 | **cheb only** | 421 | **new** | capped |
| 121 | 59364825832110609281599128001 | 28.77 | 12 | 23 · 41 · 89 · 131 · 181 · 191 · 197 · 199 · 251 · 571 · 4751 · 5851 | **cheb only** | 191 | **new** | capped |
| 122 | 60710635887715776967909304401 | 28.78 | 14 | 29 · 37 · 41 · 67 · 79 · 89 · 103 · 113 · 131 · 181 · 199 · 239 · 307 · 727 | **cheb only** | 79,113,239 | **new** | capped |
| 123 | 61718891409749603155862736001 | 28.79 | 11 | 43 · 101 · 113 · 163 · 191 · 419 · 463 · 881 · 1559 · 3191 · 4751 | CN2 (rigid) |  | **new** | capped |
| 124 | 63903529488236770899696729601 | 28.81 | 12 | 19 · 43 · 83 · 109 · 127 · 197 · 199 · 233 · 307 · 881 · 2969 · 9281 | CN2 (rigid) |  | **new** | capped |
| 125 | 67612520959061465487519619201 | 28.83 | 11 | 43 · 79 · 151 · 199 · 239 · 271 · 419 · 727 · 911 · 3079 · 11969 | CN2 (rigid) |  | **new** | capped |
| 126 | 71909096287325582852469302401 | 28.86 | 9 | 101 · 199 · 229 · 521 · 1871 · 3079 · 4159 · 19889 · 62929 | CN2 (rigid) |  | **new** | capped |
| 127 | 75084792811304298963925944961 | 28.88 | 14 | 19 · 31 · 43 · 47 · 67 · 71 · 89 · 103 · 127 · 139 · 181 · 307 · 439 · 3359 | **cheb only** | 127 | **new** | capped |
| 128 | 85113741876256705160256107401 | 28.93 | 13 | 29 · 37 · 41 · 43 · 71 · 89 · 109 · 131 · 311 · 571 · 701 · 1301 · 3079 | **cheb only** | 41,71,89,311,3079 | **new** | capped |
| 129 | 85591811776429200427031246401 | 28.93 | 12 | 19 · 53 · 61 · 79 · 89 · 149 · 181 · 311 · 967 · 1451 · 4049 · 4159 | **cheb only** | 4159 | **new** | capped |
| 130 | 87856315530443123938151724001 | 28.94 | 11 | 29 · 61 · 113 · 139 · 199 · 229 · 251 · 991 · 1427 · 6991 · 27961 | **cheb only** | 991 | **new** | capped |
| 131 | 90688854810222591903117577441 | 28.96 | 11 | 31 · 71 · 103 · 233 · 307 · 409 · 811 · 883 · 1429 · 1567 · 8527 | **cheb only** | 31,1567 | **new** | capped |
| 132 | 93083450169938405767940750401 | 28.97 | 12 | 17 · 31 · 53 · 79 · 113 · 151 · 191 · 593 · 739 · 1231 · 1559 · 15391 | **cheb only** | 191 | **new** | capped |
| 133 | 97073909726951543608461919681 | 28.99 | 12 | 23 · 53 · 103 · 109 · 197 · 241 · 271 · 521 · 727 · 881 · 883 · 1871 | CN2 (rigid) |  | **new** | capped |
| 134 | 102191665496386714854245640001 | 29.01 | 11 | 31 · 41 · 107 · 181 · 239 · 307 · 419 · 449 · 3079 · 8161 · 11969 | **cheb only** | 449,11969 | **new** | capped |
| 135 | 104702415675548646087023411521 | 29.02 | 14 | 29 · 31 · 41 · 43 · 53 · 67 · 71 · 113 · 131 · 191 · 419 · 509 · 571 · 761 | **cheb only** | 191 | **new** | capped |
| 136 | 107755240130126329191082632001 | 29.03 | 12 | 17 · 47 · 53 · 79 · 197 · 251 · 431 · 859 · 881 · 991 · 1301 · 1549 | CN2 (rigid) |  | **new** | capped |
| 137 | 109760545490176816032548520001 | 29.04 | 12 | 23 · 31 · 43 · 71 · 73 · 113 · 199 · 223 · 449 · 1901 · 4751 · 33967 | **cheb only** | 449 | **new** | capped |
| 138 | 110244345805263665512480194001 | 29.04 | 13 | 19 · 29 · 41 · 47 · 89 · 101 · 139 · 197 · 199 · 461 · 881 · 1289 · 4049 | **cheb only** | 47,881,4049 | **new** | capped |
| 139 | 113331895388837044576937280001 | 29.05 | 10 | 31 · 67 · 73 · 167 · 257 · 1889 · 4159 · 4481 · 9461 · 52289 | **cheb only** | 73 | **new** | capped |
| 140 | 116519835693817310596546985281 | 29.07 | 13 | 31 · 37 · 53 · 71 · 79 · 103 · 109 · 113 · 271 · 463 · 521 · 911 · 4523 | CN2 (rigid) |  | **new** | capped |
| 141 | 125008002039355638958400045401 | 29.10 | 13 | 41 · 43 · 53 · 59 · 61 · 71 · 103 · 139 · 373 · 461 · 599 · 1301 · 2729 | **cheb only** | 41,71,103,599,2729 | **new** | capped |
| 142 | 126071045494355453802452906401 | 29.10 | 11 | 11 · 103 · 113 · 139 · 521 · 647 · 911 · 1103 · 1861 · 2549 · 4409 | CN2 (rigid) |  | **new** | capped |
| 143 | 128113086406354488544058553601 | 29.11 | 12 | 41 · 71 · 73 · 79 · 97 · 127 · 131 · 449 · 571 · 883 · 3331 · 6271 | CN2 (rigid) |  | **new** | capped |
| 144 | 133096515722919823805194464001 | 29.12 | 11 | 41 · 47 · 127 · 229 · 461 · 503 · 521 · 769 · 1151 · 2393 · 9281 | **cheb only** | 769 | **new** | capped |
| 145 | 133386824511122157574517318401 | 29.13 | 12 | 29 · 41 · 53 · 79 · 197 · 199 · 419 · 571 · 701 · 769 · 1409 · 3761 | **cheb only** | 769 | **new** | capped |
| 146 | 138087826457302559074727009521 | 29.14 | 13 | 29 · 37 · 41 · 61 · 89 · 113 · 131 · 137 · 379 · 419 · 461 · 1427 · 2729 | **cheb only** | 113 | **new** | capped |
| 147 | 139154421057118472748901878721 | 29.14 | 11 | 23 · 43 · 71 · 131 · 181 · 307 · 883 · 1861 · 1871 · 5167 · 17137 | CN2 (rigid) |  | **new** | capped |
| 148 | 148147081792052830933763116801 | 29.17 | 12 | 29 · 41 · 71 · 89 · 103 · 127 · 131 · 197 · 881 · 883 · 3331 · 22541 | CN2 (rigid) |  | **new** | capped |
| 149 | 148613019371645964789250396801 | 29.17 | 11 | 47 · 103 · 131 · 139 · 181 · 197 · 199 · 1301 · 1871 · 3331 · 29303 | CN2 (rigid) |  | **new** | capped |
| 150 | 149041972771228010298003379201 | 29.17 | 11 | 23 · 31 · 103 · 151 · 191 · 271 · 571 · 1291 · 3457 · 8513 · 11969 | CN2 (rigid) |  | **new** | capped |
| 151 | 150373074984145657966627905601 | 29.18 | 12 | 17 · 31 · 41 · 53 · 71 · 131 · 191 · 911 · 1709 · 1951 · 4159 · 5851 | **cheb only** | 191,4159 | **new** | capped |
| 152 | 151155459152252552512051891201 | 29.18 | 11 | 23 · 71 · 101 · 163 · 307 · 379 · 601 · 769 · 2377 · 5167 · 8513 | CN2 (rigid) |  | **new** | capped |
| 153 | 151737263983478535726543379201 | 29.18 | 11 | 31 · 109 · 113 · 151 · 223 · 463 · 701 · 769 · 2591 · 3457 · 5279 | **cheb only** | 769 | **new** | capped |
| 154 | 158647590842481558288190399681 | 29.20 | 13 | 19 · 23 · 41 · 67 · 71 · 97 · 109 · 181 · 241 · 307 · 991 · 2729 · 4861 | CN2 (rigid) |  | **new** | capped |
| 155 | 160382997245097875278647817201 | 29.21 | 11 | 23 · 37 · 307 · 337 · 463 · 521 · 571 · 701 · 1429 · 2521 · 5237 | **cheb only** | 337,463 | **new** | capped |
| 156 | 166535210436252664410472068001 | 29.22 | 13 | 19 · 29 · 43 · 47 · 107 · 137 · 211 · 239 · 251 · 271 · 701 · 1429 · 2969 | CN2 (rigid) |  | **new** | capped |
| 157 | 167404411915426044283140216001 | 29.22 | 11 | 31 · 47 · 97 · 103 · 229 · 419 · 601 · 1291 · 1871 · 2393 · 34501 | CN2 (rigid) |  | **new** | capped |
| 158 | 168694443984438067449601774081 | 29.23 | 12 | 29 · 37 · 41 · 43 · 67 · 109 · 137 · 197 · 379 · 7039 · 11593 · 14629 | CN2 (rigid) |  | **new** | capped |
| 159 | 178711171266332736447473977921 | 29.25 | 11 | 41 · 79 · 131 · 181 · 271 · 379 · 461 · 883 · 2753 · 4159 · 4861 | **cheb only** | 2753,4159 | **new** | capped |
| 160 | 225127336581668310240380529601 | 29.35 | 12 | 29 · 53 · 71 · 73 · 79 · 101 · 197 · 229 · 577 · 1471 · 5851 · 15809 | **cheb only** | 577,1471,15809 | **new** | capped |
| 161 | 234965040910225870816645032961 | 29.37 | 11 | 37 · 71 · 89 · 109 · 127 · 881 · 1061 · 1483 · 2243 · 2861 · 8161 | CN2 (rigid) |  | **new** | capped |
| 162 | 235317777338413287700412630401 | 29.37 | 12 | 19 · 43 · 59 · 89 · 167 · 181 · 233 · 433 · 463 · 1327 · 4159 · 7039 | **cheb only** | 7039 | **new** | capped |
| 163 | 263087650323805230498352377601 | 29.42 | 10 | 71 · 101 · 229 · 419 · 919 · 1429 · 1471 · 4159 · 6761 · 7039 | CN2 (rigid) |  | **new** | capped |
| 164 | 310938948890898305000359976641 | 29.49 | 12 | 31 · 41 · 43 · 71 · 233 · 241 · 271 · 463 · 937 · 1429 · 1609 · 5279 | CN2 (rigid) |  | **new** | capped |
| 165 | 315917807454112935155692608001 | 29.50 | 12 | 29 · 31 · 41 · 89 · 239 · 271 · 307 · 659 · 701 · 911 · 3329 · 3457 | CN2 (rigid) |  | **new** | capped |
| 166 | 318160964255204908837662062401 | 29.50 | 13 | 29 · 31 · 67 · 71 · 79 · 83 · 151 · 181 · 199 · 409 · 419 · 571 · 21319 | CN2 (rigid) |  | **new** | capped |
| 167 | 334801383081427770973135070401 | 29.52 | 11 | 43 · 59 · 113 · 151 · 197 · 271 · 881 · 1871 · 4003 · 4159 · 5279 | **cheb only** | 4159 | **new** | capped |
| 168 | 336678590904893959268662315201 | 29.53 | 14 | 23 · 31 · 41 · 43 · 71 · 89 · 97 · 131 · 151 · 181 · 191 · 197 · 271 · 11969 | **cheb only** | 191,11969 | **new** | capped |
| 169 | 342935838555568318773540828001 | 29.54 | 12 | 37 · 89 · 101 · 109 · 113 · 181 · 199 · 337 · 521 · 1483 · 2551 · 3499 | CN2 (rigid) |  | **new** | capped |
| 170 | 388409745448891865393360265601 | 29.59 | 13 | 37 · 41 · 59 · 67 · 71 · 113 · 127 · 191 · 239 · 307 · 991 · 1217 · 3761 | **cheb only** | 127 | **new** | capped |
| 171 | 396709382776893730429831545601 | 29.60 | 12 | 23 · 31 · 101 · 127 · 131 · 181 · 239 · 449 · 769 · 911 · 4159 · 5851 | **cheb only** | 769 | **new** | capped |
| 172 | 397806663158730709235676324001 | 29.60 | 11 | 37 · 79 · 89 · 101 · 419 · 701 · 911 · 2069 · 2351 · 2393 · 4861 | CN2 (rigid) |  | **new** | capped |
| 173 | 412874721000725058211545319681 | 29.62 | 12 | 23 · 31 · 59 · 67 · 113 · 173 · 239 · 463 · 509 · 2089 · 7481 · 8513 | CN2 (rigid) |  | **new** | capped |
| 174 | 442875745314302705567788626001 | 29.65 | 13 | 37 · 41 · 43 · 71 · 79 · 101 · 103 · 151 · 239 · 251 · 307 · 5851 · 7151 | **cheb only** | 79,239,7151 | **new** | capped |
| 175 | 511714740095171322506538421681 | 29.71 | 12 | 37 · 67 · 89 · 113 · 181 · 197 · 307 · 571 · 647 · 881 · 1871 · 3079 | **cheb only** | 113,881,1871 | **new** | capped |
| 176 | 511755777458424161725823560801 | 29.71 | 11 | 71 · 73 · 89 · 109 · 163 · 433 · 571 · 2591 · 3433 · 4217 · 6733 | **cheb only** | 2591 | **new** | capped |
| 177 | 526129433476775882561851243201 | 29.72 | 12 | 19 · 53 · 131 · 173 · 179 · 181 · 431 · 449 · 859 · 1429 · 1601 · 1871 | **cheb only** | 449,1601 | **new** | capped |
| 178 | 611735329101309823150226085601 | 29.79 | 12 | 43 · 67 · 89 · 103 · 131 · 151 · 239 · 379 · 521 · 571 · 1223 · 35531 | CN2 (rigid) |  | **new** | capped |
| 179 | 638441256413880049160291184001 | 29.81 | 11 | 13 · 47 · 113 · 199 · 241 · 419 · 461 · 967 · 2111 · 2531 · 193201 | CN2 (rigid) |  | **new** | capped |
| 180 | 665951765284067421160801800001 | 29.82 | 10 | 29 · 197 · 239 · 449 · 491 · 883 · 4159 · 4591 · 4999 · 26249 | **cheb only** | 449,4159 | **new** | capped |
| 181 | 674270485359912793413041460481 | 29.83 | 12 | 23 · 43 · 53 · 71 · 103 · 109 · 127 · 359 · 1429 · 3041 · 3457 · 23561 | CN2 (rigid) |  | **new** | capped |
| 182 | 678617694966364134703577856001 | 29.83 | 12 | 17 · 47 · 71 · 89 · 113 · 251 · 449 · 571 · 967 · 2393 · 2729 · 2927 | CN2 (rigid) |  | **new** | capped |
| 183 | 683402675272767367575156298801 | 29.83 | 12 | 19 · 59 · 101 · 103 · 109 · 199 · 311 · 349 · 491 · 883 · 6733 · 8527 | **cheb only** | 8527 | **new** | capped |
| 184 | 699963023612122306431081825601 | 29.85 | 10 | 41 · 73 · 199 · 223 · 349 · 2551 · 2617 · 5039 · 6323 · 70991 | CN2 (rigid) |  | **new** | capped |
| 185 | 702050650525144183203961020001 | 29.85 | 12 | 41 · 43 · 61 · 89 · 197 · 307 · 349 · 401 · 883 · 1301 · 1429 · 5279 | **cheb only** | 5279 | **new** | capped |
| 186 | 707121894703235251544046943201 | 29.85 | 11 | 67 · 101 · 103 · 137 · 181 · 197 · 349 · 2129 · 2551 · 4409 · 24851 | CN2 (rigid) |  | **new** | capped |
| 187 | 716037428721379223097137378881 | 29.85 | 11 | 53 · 71 · 197 · 223 · 307 · 647 · 683 · 911 · 991 · 2729 · 12959 | CN2 (rigid) |  | **new** | capped |
| 188 | 760110398267085646812926294401 | 29.88 | 12 | 17 · 23 · 37 · 59 · 191 · 349 · 419 · 521 · 727 · 2089 · 5741 · 7019 | CN2 (rigid) |  | **new** | capped |
| 189 | 796172448067484530280828990401 | 29.90 | 12 | 29 · 43 · 79 · 103 · 109 · 149 · 197 · 593 · 883 · 2549 · 2729 · 6733 | CN2 (rigid) |  | **new** | capped |
| 190 | 810871120612495396700816169601 | 29.91 | 13 | 29 · 41 · 53 · 67 · 71 · 79 · 89 · 109 · 271 · 701 · 919 · 4159 · 4861 | CN2 (rigid) |  | **new** | capped |
| 191 | 816392500874711102007781315201 | 29.91 | 11 | 37 · 89 · 127 · 151 · 239 · 353 · 911 · 1429 · 2243 · 5851 · 8969 | **cheb only** | 127 | **new** | capped |
| 192 | 842456946332654926879756550401 | 29.93 | 13 | 29 · 41 · 67 · 97 · 101 · 103 · 113 · 151 · 199 · 419 · 881 · 1429 · 5851 | CN2 (rigid) |  | **new** | capped |
| 193 | 850483831970240418889056000961 | 29.93 | 13 | 13 · 37 · 41 · 43 · 67 · 89 · 109 · 191 · 379 · 647 · 1217 · 2089 · 12959 | **cheb only** | 191,1217 | **new** | capped |
| 194 | 857912856639890712600333794401 | 29.93 | 13 | 19 · 31 · 71 · 73 · 79 · 83 · 101 · 103 · 409 · 593 · 883 · 2549 · 7547 | **cheb only** | 31 | **new** | capped |
| 195 | 858548998580027923447836480001 | 29.93 | 14 | 13 · 29 · 37 · 71 · 89 · 109 · 151 · 167 · 191 · 257 · 419 · 449 · 499 · 769 | CN2 (rigid) |  | **new** | capped |
| 196 | 991450638881493066957728124001 | 30.00 | 13 | 23 · 29 · 31 · 43 · 71 · 113 · 199 · 211 · 239 · 953 · 1259 · 3299 · 3499 | **cheb only** | 31 | **new** | capped |

## 5. Checks

| check | result |
|---|---|
| all four runs complete, every shard recorded exactly once | ✓ |
| capped and pair engine hashes identical to the $10^{28}$ certificate's | ✓ |
| both tail engines agree with the frozen engine where they overlap it, and with an independent brute force above $2^{32}$ | ✓ (§2) |
| capped run in cheb mode with LASTCALC and no skips | ✓ |
| no `UNPROVEN-PRIMALITY` flags | ✓ |
| the tails find exactly the terms only they guarantee (none), and nothing else | ✓ |
| all 12 terms of A299799 (OEIS DATA) are found | ✓ |
| all 87 terms of the certified census below $10^{28}$ are found, as a(1)–a(87) | ✓ |
| the order-2 terms are exactly the 95 found by the conditional Howe run to $10^{30}$ ($T = 10^4$) | ✓ (identical sets) |
| standalone check (`tests/check_cheb_terms.py`, standard library only): every term satisfies the definition | ✓ all 196, 95 of them of order 2 (`check_cheb_terms_1e30.txt`) |
| shard replay | not run (§3) |

The reference lists are independent of this computation: OEIS's A299799, the certified census below $10^{28}$, and the conditional order-2 run. Every reference number was found. The standalone check factors every term again by trial division and checks the definition, without using the engines.

## 6. Reproducing

```bash
cd cheb-cn2-census-2
python3 cn2_split_campaign.py init --X 1e30 --R0 30000 --dir DIR --capped-only --lastcalc --mode cheb
# pair tail: copy and compile the certified cn2x/cn2pair.c into DIR/pair
cd DIR/pair && CN2X_MODE=cheb ./cn2pair 1000000000000000000000000000000 30000 90000000 . 30 0 4096 60 0
# (q,a) tail, lower: the certified cn2x/cn2tail.c plus the one line of §2, compiled into DIR/tail
cd DIR/tail && CN2X_MODE=cheb CN2X_TAIL_CAP32=1 ./cn2tail 1000000000000000000000000000000 90000000 . 30 0 268435456 60 95
# (q,a) tail, upper: cn2tail_top.c compiled into DIR/tail_top
cd DIR/tail_top && CN2X_MODE=cheb ./cn2tail_top 1000000000000000000000000000000 4294967295 . 30 0 16777216 60 95
cd cheb-cn2-census-2 && python3 cn2_split_campaign.py run --dir DIR --now --threads 30
python3 cn2_split_campaign.py verify --dir DIR --reference ../cheb-cn2-census/results/cert_1e28
python3 cn2_tail_verify.py --X 1e30 --mode cheb --pair DIR/pair --qa DIR/tail DIR/tail_top --T 30000 --reference DIR/reference_cheb_1e30.json
python3 tests/check_cheb_terms.py DIR/b299799_1e30.txt
```

`reference_cheb_1e30.json` holds the 137 reference numbers: the 87 of the census below $10^{28}$ and the 50 order-2 numbers in $[10^{28}, 10^{30})$ from the conditional order-2 run.

## 7. Cost

Against the census below $10^{28}$ (40 h in all), this one took about 430 hours of search, roughly 11 times as long. $T$ and $q^*$ were also raised, from 15,000 and 27,500,000 to 30,000 and 90,000,000:

| stage | $10^{28}$ | $10^{30}$ | ratio |
|---|---|---|---|
| capped | 20.6 h | 265 h | 12.9 |
| pair tail | 12.6 h | 100.3 h | 8.0 |
| $(q,a)$ tail | 6.8 h | 64.5 h | 9.5 |

The cost of each capped root grew by 12.6–14.8 times (13.5 overall). It depends on the arithmetic of $p^2-1$ at the root: a smooth $p^2-1$ admits many more $L$-values and so a bushier tree. The $(q,a)$ tail's test rate stayed at $5.7\times10^{7}$ per second.
