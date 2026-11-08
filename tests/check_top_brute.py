#!/usr/bin/env python3
"""check_top_brute.py -- independent check of cn2tail_top on a window of primes, in exact Python integers.

    python3 check_top_brute.py ENGINE X R0 PMAX MODE WORKDIR     (MODE: cheb, howe, or test2 = cheb's modulus with Fermat off)

Works out the pairs, the small-prime rejections and the Fermat survivors from the definitions, shares no code with the
engine, runs the engine on the same window, and compares the survivor lines and all four counters.  Exits 0 on agreement.
"""
import json, os, subprocess, sys
from multiprocessing import Pool
from sympy import primerange

ENGINE, X, R0, PMAX, MODE, WD = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5], sys.argv[6]
D = 1 if MODE == 'howe' else 2
FERMAT = MODE != 'test2'
SMALL = list(primerange(5, 10 ** 4))[:95]


def one(p):
    out, tests, sieved, calls, passes = [], 0, 0, 0, 0
    g = (p * p - 1) // D
    for fam, r0 in (('P', p), ('Q', 1)):
        # the engine's range for a family is the larger family's limit cut down by that family's own: p (r0 + a g) <= X - 1
        a = 1
        while p * (r0 + a * g) <= X - 1:
            m = r0 + a * g
            n = p * m
            tests += 1
            bad = m % p == 0
            for s in SMALL:
                if bad:
                    break
                if m % s == 0:
                    gs = (s * s - 1) // D
                    if n % gs not in (1 % gs, s % gs) or m % (s * s) == 0:
                        bad = True
            if bad:
                sieved += 1
            else:
                calls += 1
                if not FERMAT or pow(2, n - 1, m) == 1:
                    passes += 1
                    out.append(f"{fam} {p} {a}")
            a += 1
    return out, tests, sieved, calls, passes


if __name__ == '__main__':
    with Pool(24) as pl:
        rs = pl.map(one, list(primerange(R0 + 1, PMAX + 1)), chunksize=2000)
    want = sorted(l for r in rs for l in r[0])
    cnt = [sum(r[i] for r in rs) for i in range(1, 5)]
    os.makedirs(WD, exist_ok=True)
    for f in ('out.txt', 'done.log'):
        if os.path.exists(os.path.join(WD, f)):
            os.remove(os.path.join(WD, f))
    env = dict(os.environ, CN2X_TOP_PMAX=str(PMAX))
    env.update({'CN2X_MODE': 'test', 'CN2X_D': '2'} if MODE == 'test2' else {'CN2X_MODE': MODE})
    r = subprocess.run([ENGINE, str(X), str(R0), WD, '30', '0', '16777216', '0', '95'], env=env, capture_output=True, text=True)
    j = json.loads(r.stdout)
    got = sorted(l.strip() for l in open(os.path.join(WD, 'out.txt')))
    gc = [j['tests'], j['sieved'], j['fermat_calls'], j['fermat_passes']]
    ok = got == want and gc == cnt and j['complete'] and j['T'] == PMAX
    print(f"{'PASS' if ok else 'FAIL'} {MODE} ({R0},{PMAX}]: python {cnt}, engine {gc}, survivors {len(want)}/{len(got)}", flush=True)
    sys.exit(0 if ok else 1)
