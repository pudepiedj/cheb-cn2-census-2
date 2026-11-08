# Chebyshev–Carmichael numbers below 10³⁰: a certified census

This repository contains the programs, the run records, the proofs and the checks behind a complete list of the Chebyshev–Carmichael numbers (OEIS [A299799](https://oeis.org/A299799)) below $10^{30}$:

> **There are exactly 196 Chebyshev–Carmichael numbers below 10³⁰.**

**In brief.**
- **What they are:** composite numbers that pass two primality tests for every base. One is Fermat's test, $a^n \equiv a \pmod n$, and the other uses Chebyshev polynomials, $T_n(a) \equiv a \pmod n$. The next section explains what this means.
- **The 196 terms:**
  - 95 are Carmichael numbers of order 2, all rigid. Every Carmichael number of order 2 is a Chebyshev–Carmichael number, so this is also a complete list of the terms of [A175531](https://oeis.org/A175531) below $10^{30}$ (`results/b175531.txt`).
  - 101 are Chebyshev only: Carmichael numbers of order 1 that pass Chebyshev's test but are not of order 2.
- **Against earlier work:**
  - a(1)–a(87) are exactly the terms A299799 now publishes: its b-file (n = 1..87), which is the certified census below $10^{28}$ ([cheb-cn2-census](https://github.com/pudepiedj/cheb-cn2-census)). a(1)–a(12) are also in the entry's DATA, which has room for no more;
  - **109 terms lie between $10^{28}$ and $10^{30}$**. 50 are of order 2: a conditional search had already found exactly these 50, and this census proves there are no others. **59 are Chebyshev-only numbers found here for the first time.**
- **No non-rigid order-2 number lies below $10^{30}$.** The smallest one is therefore in $(10^{30}, 4.63\times10^{36}]$.

**Status.** The computation is complete and every check passes ([certificate](docs/CN2_Cheb_Certificate_1e30.md)). The capped and pair engines are byte for byte those that certified the censuses below $10^{28}$, both of order 2 ([carmichael-order2-census-2](https://github.com/pudepiedj/carmichael-order2-census-2)) and Chebyshev ([cheb-cn2-census](https://github.com/pudepiedj/cheb-cn2-census)). They run here with the Chebyshev modulus $(p^2-1)/2$. At $10^{30}$ the largest prime of a term can exceed $2^{32}$, so the third engine runs as two: the certified one, below $2^{32}$, and a 128-bit version above ([tail proof](docs/CN2_Tail_Coverage_Proof.md), §3.1).

**Not A175530.** The larger sequence [A175530](https://oeis.org/A175530) (Chebyshev pseudoprimes) also contains numbers that are not Carmichael numbers of any kind, such as $79397009999$, which is $\equiv -1$ modulo every $p \pm 1$. This census covers only those that are also Carmichael numbers of order 1, A299799 $=$ A175530 $\cap$ A002997.

## What is a Chebyshev–Carmichael number?

### Fermat's test, and the numbers that fool it

If $p$ is prime, then $a^p \equiv a \pmod p$ for every whole number $a$ (Fermat's little theorem). It is tempting to use this as a primality test, but some composite numbers pass it for every $a$. These are the **Carmichael numbers of order 1** (A002997), usually just called Carmichael numbers. The Carmichael numbers of order 2 (below) are a much rarer kind, so in this README each kind is always named by its order. The smallest is $561 = 3\cdot 11\cdot 17$. Korselt's criterion says exactly which numbers they are: a composite $n$ is a Carmichael number of order 1 when it is squarefree and $p-1$ divides $n-1$ for every prime $p \mid n$.

### The same test with Chebyshev polynomials

The **Chebyshev polynomials** are defined by $T_n(\cos\theta) = \cos n\theta$. Equivalently, $T_0 = 1$, $T_1 = x$ and $T_{n+1} = 2x\thinspace T_n - T_{n-1}$, which gives
$$T_2 = 2x^2 - 1, \qquad T_3 = 4x^3 - 3x, \qquad T_5 = 16x^5 - 20x^3 + 5x, \ \dots$$
They behave like powers: just as $(x^m)^n = x^{mn}$, so $T_m(T_n(x)) = T_{mn}(x)$. They also obey their own version of Fermat's theorem: **if $p$ is an odd prime, then $T_p(a) \equiv a \pmod p$ for every whole number $a$.** (For $p = 2$ it fails, since $T_2(0) = -1$.) For example, with $p = 3$, $T_3(a) = 4a^3 - 3a \equiv a^3 \equiv a \pmod 3$.

A composite $n$ with $T_n(a) \equiv a \pmod n$ for every $a$ is a **Chebyshev pseudoprime** (A175530). A **Chebyshev–Carmichael number** (A299799) passes both tests for every $a$: it is a Carmichael number of order 1 and a Chebyshev pseudoprime. Neither test can tell it from a prime.

### The rule that decides it

For a squarefree $n$, the Chebyshev test holds exactly when every prime $p \mid n$ satisfies
$$n \equiv \pm 1 \pmod{p-1} \quad\text{and}\quad n \equiv \pm 1 \pmod{p+1}.$$
Being a Carmichael number of order 1 as well forces the $+$ sign mod $p-1$. That leaves two cases for each prime:

| mod $p-1$ | mod $p+1$ | together |
|---|---|---|
| $n \equiv 1$ | $n \equiv 1$ | $n \equiv 1 \pmod{(p^2-1)/2}$ |
| $n \equiv 1$ | $n \equiv -1$ | $n \equiv p \pmod{(p^2-1)/2}$ |

The modulus is $(p^2-1)/2$, not $p^2-1$, because $p-1$ and $p+1$ are consecutive even numbers. Their only common factor is 2, so their least common multiple is half their product. This gives the definition OEIS states:
$$n \text{ is a Chebyshev–Carmichael number} \iff n \text{ is odd and composite, and } n \equiv 1 \text{ or } p \pmod{\tfrac{p^2-1}{2}} \text{ for every prime } p \mid n.$$

**Where the $\pm$ comes from.** Substitute $a = (u + u^{-1})/2$. Then $T_n(a) = (u^n + u^{-n})/2$, so Chebyshev's test only ever sees $u$ through $u + u^{-1}$, and it cannot tell $u$ from $1/u$. Modulo $p$, the numbers $u$ that arise are of two kinds:
- the non-zero residues mod $p$, a group of $p-1$ elements;
- elements of "norm 1" in the field of $p^2$ elements, a group of $p+1$ elements.

So the test asks only that $u^n = u$ or $u^n = u^{-1}$ in each of these groups. That is the $\pm 1$ mod $p-1$ and mod $p+1$.

### How it differs from a Carmichael number of order 2

A **Carmichael number of order 2** (Howe's definition, A175531) satisfies the same congruence with the *full* modulus:
$$n \equiv 1 \text{ or } p \pmod{p^2-1} \quad\text{for every prime } p \mid n.$$
This says that $n$ imitates a prime in the whole field of $p^2$ elements: raising to the $n$-th power fixes every element or acts as Frobenius ($a \mapsto a^p$) on all of them. Chebyshev's test asks less. It looks only at the two subgroups above, each up to the swap $u \leftrightarrow 1/u$, and the two subgroups together make up only half of the field's $p^2 - 1$ non-zero elements.

| | Carmichael of order 2 (A175531) | Chebyshev–Carmichael (A299799) |
|---|---|---|
| condition at each prime $p \mid n$ | $n \equiv 1$ or $p \pmod{p^2-1}$ | $n \equiv 1$ or $p \pmod{(p^2-1)/2}$ |
| in the commonest case, $n - 1$ must be divisible by | $(p-1)(p+1)$, the product | $\mathrm{lcm}(p-1,\thinspace p+1)$, half the product |
| imitates a prime for | powers $a^n$ in the whole field of $p^2$ elements | Chebyshev polynomials $T_n(a)$ |

**So every Carmichael number of order 2 is a Chebyshev–Carmichael number, but not the other way round.** The difference is exactly one factor of 2 in the modulus. At some prime, a Chebyshev–Carmichael number that is not of order 2 sits exactly halfway round the larger modulus: $n \equiv 1 + \tfrac{p^2-1}{2}$ or $p + \tfrac{p^2-1}{2} \pmod{p^2-1}$.

The three conditions are nested, each stricter than the one before:

| sequence | condition at every prime $p \mid n$ | in words |
|---|---|---|
| A002997, Carmichael numbers of order 1 | $n \equiv 1 \pmod{p-1}$ | passes Fermat's test for every base |
| A299799, Chebyshev–Carmichael numbers | $n \equiv 1$ or $p \pmod{(p^2-1)/2}$ | passes Chebyshev's test as well |
| A175531, Carmichael numbers of order 2 | $n \equiv 1$ or $p \pmod{p^2-1}$ | imitates a prime in the whole field of $p^2$ elements |

A Chebyshev-only term satisfies the first two rows and fails the third.

**Example.** $a(2) = 582920080863121 = 41\cdot 53\cdot 79\cdot 103\cdot 239\cdot 271\cdot 509$ is the smallest Chebyshev–Carmichael number that is not of order 2.
- At $p = 79$: $p - 1 = 78$, $p + 1 = 80$, $(p^2-1)/2 = 3120$ and $p^2 - 1 = 6240$.
  - $n - 1$ is divisible by 78, by 80 and so by 3120. That makes $79$ a Chebyshev prime of $n$.
  - However, $n \equiv 3121 = 1 + 3120 \pmod{6240}$. That is halfway, so $n$ fails the order-2 condition at 79.
- The same happens at $239$ and at $271$.
- At the other four primes $n \equiv 1 \pmod{p^2-1}$.

By contrast, the smallest term, $a(1) = 443372888629441 = 17\cdot 31\cdot 41\cdot 43\cdot 89\cdot 97\cdot 167\cdot 331$, satisfies $n \equiv 1 \pmod{p^2-1}$ at all eight primes. So it is of order 2 as well, and it is also the first term of A175531.

**A note on the word "order".** "Order 2" refers to the field of $p^2$ elements, and Howe defines Carmichael numbers of every order $m$ using fields of $p^m$ elements. The Chebyshev–Carmichael numbers form a single family, with no order attached. They sit between the Carmichael numbers of order 1 and those of order 2:
- every Carmichael number of order 2 is a Chebyshev–Carmichael number;
- every Chebyshev–Carmichael number is a Carmichael number of order 1, by definition.

**"Chebyshev only"**, in the tables here, means a Chebyshev–Carmichael number that is not of order 2. It is still a Carmichael number of order 1, because being halfway round $p^2-1$ moves $n$ by $\tfrac{p^2-1}{2} = (p-1)\cdot\tfrac{p+1}{2}$, a multiple of $p-1$, so $n \equiv 1 \pmod{p-1}$ still holds at every prime. So the Chebyshev-only terms below $10^{22}$ appear in complete tables of Carmichael numbers, such as Goutier's, but none is in A175531.

**Why the order-2 numbers appear in this list.** A299799 is defined by the Chebyshev condition alone, so every term of A175531 is automatically a term of A299799. This census lists them all. In the table below each term is marked as order 2 (it is in both sequences) or Chebyshev only.

## The terms below 10³⁰

Also in `results/b299799.txt`. "Halfway at" lists the primes where a Chebyshev-only term sits halfway round $p^2-1$, that is, $n \equiv 1 + \tfrac{p^2-1}{2}$ or $p + \tfrac{p^2-1}{2} \pmod{p^2-1}$, so it fails the order-2 condition there. "First listed" names where the term first appeared as part of a complete list: A299799's original DATA (a(1)–a(12)), the [census below 10²⁸](https://github.com/pudepiedj/cheb-cn2-census) that is now A299799's b-file (a(13)–a(87)), or this census (a(88)–a(196)).

| n | a(n) | log10 | class | halfway at | prime factors | first listed |
|---|---|---|---|---|---|---|
| 1 | 443372888629441 | 14.65 | order 2 |  | 17 · 31 · 41 · 43 · 89 · 97 · 167 · 331 | A299799 DATA |
| 2 | 582920080863121 | 14.77 | Chebyshev only | 79, 239, 271 | 41 · 53 · 79 · 103 · 239 · 271 · 509 | A299799 DATA |
| 3 | 39671149333495681 | 16.60 | order 2 |  | 17 · 37 · 41 · 71 · 79 · 97 · 113 · 131 · 191 | A299799 DATA |
| 4 | 842526563598720001 | 17.93 | order 2 |  | 17 · 61 · 71 · 89 · 197 · 311 · 769 · 2729 | A299799 DATA |
| 5 | 2380296518909971201 | 18.38 | order 2 |  | 19 · 41 · 43 · 71 · 89 · 127 · 199 · 449 · 991 | A299799 DATA |
| 6 | 3188618003602886401 | 18.50 | order 2 |  | 29 · 37 · 79 · 181 · 191 · 449 · 701 · 3457 | A299799 DATA |
| 7 | 33711266676317630401 | 19.53 | Chebyshev only | 449 | 17 · 29 · 37 · 41 · 151 · 199 · 449 · 571 · 5851 | A299799 DATA |
| 8 | 54764632857801026161 | 19.74 | Chebyshev only | 79, 239, 271 | 41 · 53 · 79 · 137 · 139 · 181 · 239 · 271 · 1429 | A299799 DATA |
| 9 | 122762671289519184001 | 20.09 | Chebyshev only | 127 | 13 · 17 · 19 · 29 · 41 · 89 · 97 · 127 · 199 · 251 · 449 | A299799 DATA |
| 10 | 361266866679292635601 | 20.56 | Chebyshev only | 17, 881 | 17 · 23 · 29 · 37 · 41 · 43 · 61 · 109 · 199 · 419 · 881 | A299799 DATA |
| 11 | 4208895375600667752001 | 21.62 | order 2 |  | 17 · 29 · 31 · 43 · 71 · 79 · 199 · 389 · 2521 · 5851 | A299799 DATA |
| 12 | 7673096805497432749441 | 21.88 | Chebyshev only | 127 | 29 · 31 · 37 · 43 · 53 · 109 · 127 · 571 · 3079 · 4159 | A299799 DATA |
| 13 | 193966598206145637873001 | 23.29 | Chebyshev only | 23, 41, 71, 89, 103 | 19 · 23 · 29 · 41 · 71 · 89 · 101 · 103 · 701 · 1429 · 5669 | A299799 b-file |
| 14 | 623655451404913888200241 | 23.79 | Chebyshev only | 79, 239, 881 | 23 · 79 · 109 · 239 · 881 · 883 · 1223 · 1973 · 7019 | A299799 b-file |
| 15 | 1159954316194989017102401 | 24.06 | order 2 |  | 31 · 47 · 109 · 137 · 307 · 2927 · 3079 · 4049 · 4759 | A299799 b-file |
| 16 | 1327183446436495124400001 | 24.12 | Chebyshev only | 641 | 13 · 17 · 23 · 29 · 89 · 97 · 251 · 449 · 641 · 1499 · 9631 | A299799 b-file |
| 17 | 1457044155748208447259841 | 24.16 | Chebyshev only | 191 | 79 · 97 · 131 · 139 · 191 · 229 · 379 · 461 · 571 · 2393 | A299799 b-file |
| 18 | 2088144166339753513992001 | 24.32 | order 2 |  | 113 · 199 · 239 · 263 · 701 · 7919 · 15391 · 17291 | A299799 b-file |
| 19 | 2196407820059694924883201 | 24.34 | order 2 |  | 53 · 109 · 127 · 281 · 307 · 379 · 647 · 10529 · 13441 | A299799 b-file |
| 20 | 3339611018825185787482801 | 24.52 | order 2 |  | 19 · 41 · 43 · 53 · 67 · 89 · 103 · 131 · 137 · 307 · 389 · 1429 | A299799 b-file |
| 21 | 3464334205088776324905601 | 24.54 | Chebyshev only | 3457 | 17 · 31 · 37 · 41 · 43 · 59 · 113 · 181 · 199 · 233 · 521 · 3457 | A299799 b-file |
| 22 | 4105879060352839139462401 | 24.61 | order 2 |  | 89 · 239 · 401 · 2143 · 2311 · 3571 · 3761 · 7237 | A299799 b-file |
| 23 | 4809665063400557951190601 | 24.68 | Chebyshev only | 41, 103, 151, 2393 | 41 · 53 · 67 · 103 · 151 · 379 · 571 · 701 · 2393 · 5851 | A299799 b-file |
| 24 | 5002862939121639632040001 | 24.70 | order 2 |  | 31 · 53 · 79 · 89 · 101 · 151 · 181 · 251 · 379 · 647 · 2549 | A299799 b-file |
| 25 | 7865064643837556041286401 | 24.90 | order 2 |  | 23 · 37 · 67 · 89 · 101 · 109 · 181 · 199 · 433 · 571 · 15809 | A299799 b-file |
| 26 | 9400084864021826054720641 | 24.97 | order 2 |  | 23 · 31 · 53 · 79 · 103 · 197 · 239 · 379 · 521 · 727 · 4523 | A299799 b-file |
| 27 | 12071465216556111317952001 | 25.08 | order 2 |  | 37 · 41 · 53 · 59 · 89 · 109 · 127 · 151 · 191 · 233 · 379 · 811 | A299799 b-file |
| 28 | 13935937975195278973392001 | 25.14 | Chebyshev only | 127 | 23 · 29 · 37 · 71 · 83 · 109 · 113 · 127 · 199 · 251 · 419 · 2927 | A299799 b-file |
| 29 | 19087839966156095154384001 | 25.28 | Chebyshev only | 3457 | 11 · 17 · 37 · 41 · 79 · 113 · 139 · 181 · 251 · 379 · 911 · 3457 | A299799 b-file |
| 30 | 31280524488319495535546401 | 25.50 | order 2 |  | 19 · 23 · 43 · 59 · 71 · 109 · 271 · 311 · 701 · 1301 · 47431 | A299799 b-file |
| 31 | 32492501043239735947612801 | 25.51 | order 2 |  | 11 · 31 · 41 · 79 · 103 · 271 · 313 · 389 · 911 · 2521 · 3769 | A299799 b-file |
| 32 | 36991212507320386599648001 | 25.57 | order 2 |  | 11 · 31 · 37 · 53 · 97 · 191 · 379 · 883 · 1151 · 2549 · 3041 | A299799 b-file |
| 33 | 44774022865681509785985601 | 25.65 | order 2 |  | 19 · 41 · 67 · 89 · 101 · 131 · 139 · 233 · 271 · 1301 · 63799 | A299799 b-file |
| 34 | 50473184681492173584023041 | 25.70 | order 2 |  | 37 · 53 · 67 · 131 · 139 · 181 · 229 · 419 · 577 · 911 · 2311 | A299799 b-file |
| 35 | 54475112449147532388966721 | 25.74 | order 2 |  | 29 · 97 · 103 · 139 · 181 · 307 · 827 · 1061 · 2393 · 11593 | A299799 b-file |
| 36 | 68886771046178424397858801 | 25.84 | Chebyshev only | 79, 911 | 53 · 71 · 79 · 101 · 109 · 139 · 181 · 461 · 647 · 911 · 3079 | A299799 b-file |
| 37 | 71712112526158742082244801 | 25.86 | Chebyshev only | 449, 11969 | 23 · 29 · 41 · 79 · 101 · 131 · 419 · 449 · 911 · 1223 · 11969 | A299799 b-file |
| 38 | 76587257660615840312697601 | 25.88 | order 2 |  | 13 · 19 · 31 · 67 · 107 · 139 · 197 · 479 · 1471 · 1801 · 40151 | A299799 b-file |
| 39 | 85737999338407807647656401 | 25.93 | Chebyshev only | 79, 239 | 23 · 29 · 53 · 79 · 101 · 103 · 109 · 181 · 199 · 239 · 647 · 4861 | A299799 b-file |
| 40 | 111356194710608262218643841 | 26.05 | order 2 |  | 41 · 61 · 79 · 113 · 131 · 379 · 683 · 2729 · 4159 · 12959 | A299799 b-file |
| 41 | 191970596806626660335913601 | 26.28 | Chebyshev only | 3457 | 17 · 23 · 31 · 37 · 43 · 53 · 71 · 113 · 199 · 241 · 337 · 419 · 3457 | A299799 b-file |
| 42 | 213622061697266764349808001 | 26.33 | Chebyshev only | 6271 | 23 · 29 · 31 · 71 · 89 · 97 · 103 · 181 · 251 · 307 · 1871 · 6271 | A299799 b-file |
| 43 | 227541194846069456562210001 | 26.36 | Chebyshev only | 17, 79, 4933 | 17 · 19 · 29 · 41 · 53 · 79 · 131 · 139 · 199 · 727 · 4933 · 10889 | A299799 b-file |
| 44 | 244041085292561389352520001 | 26.39 | Chebyshev only | 193, 4159 | 23 · 61 · 113 · 131 · 193 · 251 · 271 · 337 · 701 · 911 · 4159 | A299799 b-file |
| 45 | 257553076956557894240652001 | 26.41 | Chebyshev only | 8161 | 13 · 29 · 43 · 67 · 71 · 101 · 109 · 197 · 199 · 271 · 3499 · 8161 | A299799 b-file |
| 46 | 373851853012084355680131361 | 26.57 | order 2 |  | 37 · 71 · 103 · 109 · 131 · 181 · 239 · 419 · 461 · 3079 · 3761 | A299799 b-file |
| 47 | 419746116449969951645203201 | 26.62 | order 2 |  | 17 · 37 · 43 · 53 · 71 · 109 · 151 · 191 · 281 · 881 · 1409 · 3761 | A299799 b-file |
| 48 | 472936079653356733106893201 | 26.67 | Chebyshev only | 911, 8527 | 23 · 43 · 197 · 349 · 419 · 521 · 701 · 911 · 5851 · 8527 | A299799 b-file |
| 49 | 480650413824292471675755841 | 26.68 | order 2 |  | 29 · 41 · 89 · 131 · 197 · 239 · 271 · 727 · 881 · 1429 · 2969 | A299799 b-file |
| 50 | 507710311713618241797676801 | 26.71 | order 2 |  | 41 · 47 · 71 · 89 · 127 · 151 · 241 · 967 · 1103 · 2089 · 4049 | A299799 b-file |
| 51 | 571197082724681188312817281 | 26.76 | order 2 |  | 29 · 43 · 67 · 71 · 131 · 211 · 307 · 953 · 1021 · 1429 · 8161 | A299799 b-file |
| 52 | 598764213578029575774297601 | 26.78 | order 2 |  | 23 · 29 · 43 · 53 · 79 · 109 · 113 · 127 · 181 · 239 · 379 · 433 · 449 | A299799 b-file |
| 53 | 667882655094744395121816001 | 26.82 | order 2 |  | 67 · 83 · 131 · 163 · 199 · 239 · 461 · 2393 · 5167 · 20747 | A299799 b-file |
| 54 | 749114380387868248644660001 | 26.87 | Chebyshev only | 97, 1567, 51679 | 23 · 41 · 67 · 97 · 109 · 379 · 1567 · 4999 · 7309 · 51679 | A299799 b-file |
| 55 | 768927403921604814222336001 | 26.89 | order 2 |  | 43 · 67 · 137 · 251 · 271 · 349 · 769 · 1427 · 4159 · 17981 | A299799 b-file |
| 56 | 847201873829461072769246401 | 26.93 | Chebyshev only | 11969 | 37 · 41 · 43 · 71 · 103 · 239 · 281 · 379 · 2287 · 2549 · 11969 | A299799 b-file |
| 57 | 922904786964947393227420801 | 26.97 | order 2 |  | 17 · 37 · 41 · 311 · 929 · 1217 · 1301 · 1601 · 3191 · 15313 | A299799 b-file |
| 58 | 946295515632681859275671041 | 26.98 | order 2 |  | 29 · 43 · 89 · 109 · 131 · 181 · 229 · 991 · 1427 · 1429 · 7129 | A299799 b-file |
| 59 | 1445961713544933049178794081 | 27.16 | Chebyshev only | 929 | 23 · 37 · 41 · 43 · 53 · 89 · 109 · 241 · 571 · 929 · 2089 · 7019 | A299799 b-file |
| 60 | 1480947968491738280801467201 | 27.17 | Chebyshev only | 4159 | 17 · 59 · 71 · 419 · 521 · 683 · 811 · 3191 · 4159 · 12959 | A299799 b-file |
| 61 | 1710675679046386360978509841 | 27.23 | Chebyshev only | 433, 463, 1489, 1871 | 43 · 59 · 89 · 131 · 233 · 311 · 433 · 463 · 1429 · 1489 · 1871 | A299799 b-file |
| 62 | 1800270906592423387847044321 | 27.26 | Chebyshev only | 97, 8161 | 79 · 97 · 103 · 137 · 211 · 1019 · 1117 · 2861 · 2969 · 8161 | A299799 b-file |
| 63 | 1800352719110727998002987201 | 27.26 | Chebyshev only | 449 | 17 · 19 · 59 · 71 · 79 · 89 · 97 · 131 · 233 · 349 · 449 · 463 · 881 | A299799 b-file |
| 64 | 1862295045464158166966504401 | 27.27 | Chebyshev only | 47, 239 | 43 · 47 · 71 · 107 · 197 · 239 · 307 · 919 · 1301 · 2311 · 3037 | A299799 b-file |
| 65 | 1941211286859256920630460801 | 27.29 | order 2 |  | 31 · 37 · 41 · 43 · 89 · 101 · 151 · 199 · 307 · 463 · 2089 · 11969 | A299799 b-file |
| 66 | 2119047331560739293908113921 | 27.33 | order 2 |  | 17 · 37 · 43 · 47 · 79 · 89 · 113 · 127 · 571 · 911 · 3541 · 8969 | A299799 b-file |
| 67 | 2142752298785201165308646401 | 27.33 | order 2 |  | 23 · 37 · 83 · 113 · 163 · 191 · 601 · 701 · 911 · 3079 · 7297 | A299799 b-file |
| 68 | 2325041445996414342573536161 | 27.37 | order 2 |  | 19 · 29 · 47 · 71 · 79 · 137 · 557 · 619 · 2729 · 10711 · 11593 | A299799 b-file |
| 69 | 2981071306952233928836603201 | 27.47 | Chebyshev only | 449 | 17 · 41 · 181 · 199 · 349 · 449 · 587 · 599 · 881 · 1171 · 2089 | A299799 b-file |
| 70 | 3002549563607572248383836801 | 27.48 | Chebyshev only | 127 | 13 · 29 · 43 · 89 · 109 · 127 · 263 · 353 · 461 · 827 · 1049 · 4049 | A299799 b-file |
| 71 | 3055408335216475232299905601 | 27.49 | Chebyshev only | 449 | 23 · 89 · 101 · 103 · 113 · 131 · 151 · 241 · 449 · 571 · 727 · 1429 | A299799 b-file |
| 72 | 3184712715668896364421268801 | 27.50 | Chebyshev only | 191, 1217 | 31 · 37 · 41 · 71 · 79 · 131 · 191 · 199 · 571 · 661 · 1217 · 5279 | A299799 b-file |
| 73 | 3213322593860118229475166721 | 27.51 | order 2 |  | 37 · 61 · 67 · 71 · 419 · 433 · 617 · 1103 · 11593 · 209089 | A299799 b-file |
| 74 | 4291812303515083594987740001 | 27.63 | Chebyshev only | 223, 8287 | 43 · 47 · 73 · 113 · 151 · 223 · 461 · 571 · 599 · 5851 · 8287 | A299799 b-file |
| 75 | 4383862422930048259296295201 | 27.64 | Chebyshev only | 97 | 37 · 53 · 71 · 97 · 163 · 379 · 419 · 491 · 701 · 1709 · 21319 | A299799 b-file |
| 76 | 4497699707671000342005093601 | 27.65 | Chebyshev only | 9631, 15137 | 19 · 59 · 89 · 233 · 431 · 601 · 701 · 7309 · 9631 · 15137 | A299799 b-file |
| 77 | 4635427415991948819511107841 | 27.67 | order 2 |  | 23 · 29 · 37 · 53 · 71 · 89 · 113 · 127 · 191 · 271 · 379 · 647 · 3079 | A299799 b-file |
| 78 | 4955815709824370817666240001 | 27.70 | Chebyshev only | 73 | 41 · 67 · 71 · 73 · 103 · 131 · 199 · 239 · 271 · 701 · 1091 · 2617 | A299799 b-file |
| 79 | 5466953848346666426169619201 | 27.74 | order 2 |  | 37 · 59 · 79 · 109 · 113 · 151 · 229 · 1217 · 2311 · 4523 · 5851 | A299799 b-file |
| 80 | 6037031106243073961934109201 | 27.78 | order 2 |  | 23 · 37 · 89 · 109 · 131 · 151 · 181 · 211 · 281 · 397 · 1483 · 5851 | A299799 b-file |
| 81 | 6473975735726053723736568001 | 27.81 | order 2 |  | 23 · 31 · 53 · 71 · 79 · 97 · 131 · 151 · 181 · 239 · 419 · 593 · 1481 | A299799 b-file |
| 82 | 6689253573790144737930673201 | 27.83 | Chebyshev only | 47, 239 | 13 · 47 · 67 · 149 · 239 · 307 · 919 · 3673 · 9323 · 474949 | A299799 b-file |
| 83 | 6901344518427089880041692801 | 27.84 | Chebyshev only | 127, 3457 | 29 · 37 · 41 · 43 · 71 · 101 · 127 · 151 · 701 · 1871 · 3457 · 5851 | A299799 b-file |
| 84 | 7006270310872326698183179201 | 27.85 | order 2 |  | 41 · 71 · 89 · 103 · 199 · 211 · 5851 · 6359 · 8161 · 20593 | A299799 b-file |
| 85 | 8601689148505906566116203201 | 27.93 | order 2 |  | 59 · 71 · 109 · 241 · 349 · 521 · 701 · 2053 · 2843 · 105071 | A299799 b-file |
| 86 | 8838800136403254764954638201 | 27.95 | Chebyshev only | 71, 151, 919, 3079 | 29 · 43 · 67 · 71 · 101 · 109 · 139 · 151 · 919 · 1427 · 1597 · 3079 | A299799 b-file |
| 87 | 9799274291299994931676646401 | 27.99 | order 2 |  | 31 · 41 · 53 · 71 · 101 · 103 · 199 · 239 · 379 · 449 · 4159 · 5851 | A299799 b-file |
| 88 | 10000966622030520698508186241 | 28.00 | order 2 |  | 23 · 29 · 31 · 71 · 79 · 83 · 131 · 379 · 911 · 1231 · 1559 · 11969 | **this census** |
| 89 | 11134962266231164874362652881 | 28.05 | Chebyshev only | 433, 81839 | 13 · 19 · 71 · 109 · 137 · 373 · 433 · 919 · 953 · 3673 · 81839 | **this census** |
| 90 | 11743543456705885034950740001 | 28.07 | Chebyshev only | 97 | 59 · 71 · 97 · 131 · 137 · 229 · 241 · 463 · 727 · 4999 · 17341 | **this census** |
| 91 | 12096348505751118611470628161 | 28.08 | order 2 |  | 37 · 41 · 43 · 47 · 97 · 109 · 227 · 229 · 379 · 571 · 2003 · 16561 | **this census** |
| 92 | 12154703615948336130338851201 | 28.08 | Chebyshev only | 313 | 29 · 43 · 61 · 79 · 139 · 239 · 311 · 313 · 373 · 461 · 1427 · 2549 | **this census** |
| 93 | 12280804926059535591106180801 | 28.09 | Chebyshev only | 191, 1471, 15679 | 31 · 53 · 131 · 151 · 191 · 271 · 349 · 379 · 1471 · 2393 · 15679 | **this census** |
| 94 | 12737263817300842658077192801 | 28.11 | Chebyshev only | 97 | 37 · 47 · 61 · 97 · 101 · 271 · 307 · 379 · 433 · 461 · 683 · 2851 | **this census** |
| 95 | 12921258224284865643123936001 | 28.11 | order 2 |  | 23 · 29 · 41 · 43 · 53 · 71 · 89 · 109 · 251 · 449 · 701 · 1889 · 2017 | **this census** |
| 96 | 12928912537758504200832441601 | 28.11 | order 2 |  | 13 · 109 · 151 · 199 · 577 · 1409 · 2069 · 2161 · 2351 · 35531 | **this census** |
| 97 | 13551147801850177161540817921 | 28.13 | order 2 |  | 29 · 31 · 47 · 89 · 113 · 127 · 137 · 181 · 197 · 239 · 307 · 769 · 911 | **this census** |
| 98 | 14048188307862781503789388801 | 28.15 | order 2 |  | 31 · 47 · 67 · 89 · 127 · 137 · 139 · 239 · 449 · 769 · 1151 · 7039 | **this census** |
| 99 | 15698008387299304739312640001 | 28.20 | Chebyshev only | 73 | 17 · 23 · 41 · 43 · 73 · 109 · 127 · 199 · 241 · 281 · 701 · 1409 · 1693 | **this census** |
| 100 | 18823151230401360689537090401 | 28.27 | Chebyshev only | 31 | 31 · 37 · 197 · 271 · 881 · 2029 · 2089 · 3191 · 4409 · 5851 | **this census** |
| 101 | 20464553098335414488319900001 | 28.31 | Chebyshev only | 31 | 17 · 31 · 41 · 43 · 53 · 71 · 151 · 157 · 199 · 631 · 701 · 911 · 3079 | **this census** |
| 102 | 21601455918312583418275170001 | 28.33 | Chebyshev only | 79, 1231 | 23 · 79 · 83 · 179 · 199 · 251 · 349 · 811 · 1231 · 5741 · 8009 | **this census** |
| 103 | 21995062699687000159829392801 | 28.34 | Chebyshev only | 2143 | 23 · 41 · 43 · 53 · 269 · 701 · 881 · 2143 · 2549 · 2551 · 4421 | **this census** |
| 104 | 23651361712868472625849606801 | 28.37 | Chebyshev only | 239 | 23 · 41 · 43 · 67 · 101 · 103 · 239 · 331 · 419 · 571 · 1429 · 30941 | **this census** |
| 105 | 24114300099590121401824683841 | 28.38 | Chebyshev only | 1471, 4159 | 19 · 31 · 103 · 181 · 197 · 239 · 461 · 1471 · 1871 · 4159 · 8839 | **this census** |
| 106 | 32351613589818545871858609601 | 28.51 | Chebyshev only | 191, 449 | 17 · 31 · 41 · 53 · 89 · 139 · 151 · 191 · 449 · 461 · 599 · 701 · 911 | **this census** |
| 107 | 34111287958931169952279073761 | 28.53 | Chebyshev only | 31, 5279 | 19 · 31 · 43 · 59 · 67 · 89 · 233 · 509 · 1429 · 1871 · 2287 · 5279 | **this census** |
| 108 | 36442085590214555168363846401 | 28.56 | order 2 |  | 37 · 59 · 79 · 89 · 113 · 181 · 191 · 271 · 337 · 419 · 1327 · 11969 | **this census** |
| 109 | 41863530967813882076637888001 | 28.62 | order 2 |  | 17 · 23 · 31 · 37 · 41 · 71 · 89 · 113 · 131 · 181 · 191 · 251 · 911 · 3079 | **this census** |
| 110 | 42025914667200258779342117761 | 28.62 | Chebyshev only | 127 | 41 · 59 · 61 · 107 · 109 · 127 · 131 · 311 · 433 · 991 · 1567 · 7019 | **this census** |
| 111 | 43479088325949473226786556801 | 28.64 | Chebyshev only | 641 | 17 · 47 · 79 · 131 · 181 · 191 · 419 · 461 · 599 · 641 · 857 · 2393 | **this census** |
| 112 | 46646676334362776013754251841 | 28.67 | order 2 |  | 29 · 37 · 41 · 79 · 109 · 113 · 131 · 181 · 197 · 307 · 461 · 881 · 1871 | **this census** |
| 113 | 47073397944825265701015820801 | 28.67 | order 2 |  | 31 · 41 · 109 · 127 · 151 · 307 · 379 · 811 · 2689 · 3079 · 22679 | **this census** |
| 114 | 48076467088279989582023640841 | 28.68 | Chebyshev only | 41, 281, 1223, 2729, 23561 | 37 · 41 · 67 · 131 · 281 · 419 · 571 · 683 · 1223 · 2729 · 23561 | **this census** |
| 115 | 48233855879863040475353865601 | 28.68 | Chebyshev only | 36479 | 31 · 47 · 53 · 89 · 103 · 239 · 463 · 1709 · 1871 · 5279 · 36479 | **this census** |
| 116 | 48899165243656630330763899201 | 28.69 | order 2 |  | 11 · 19 · 29 · 79 · 137 · 701 · 1301 · 1427 · 1889 · 3359 · 90271 | **this census** |
| 117 | 55654824887414879449045282561 | 28.75 | Chebyshev only | 769 | 31 · 43 · 47 · 53 · 461 · 463 · 769 · 1429 · 1871 · 3191 · 11969 | **this census** |
| 118 | 56259612931685661605147040001 | 28.75 | order 2 |  | 29 · 67 · 89 · 103 · 131 · 223 · 229 · 307 · 419 · 701 · 1259 · 4159 | **this census** |
| 119 | 56503870441915041752546459521 | 28.75 | Chebyshev only | 127 | 89 · 103 · 127 · 131 · 197 · 239 · 439 · 521 · 1567 · 4159 · 5279 | **this census** |
| 120 | 57291200994173796305950694401 | 28.76 | Chebyshev only | 421 | 29 · 31 · 43 · 89 · 101 · 131 · 137 · 421 · 727 · 919 · 4159 · 7853 | **this census** |
| 121 | 59364825832110609281599128001 | 28.77 | Chebyshev only | 191 | 23 · 41 · 89 · 131 · 181 · 191 · 197 · 199 · 251 · 571 · 4751 · 5851 | **this census** |
| 122 | 60710635887715776967909304401 | 28.78 | Chebyshev only | 79, 113, 239 | 29 · 37 · 41 · 67 · 79 · 89 · 103 · 113 · 131 · 181 · 199 · 239 · 307 · 727 | **this census** |
| 123 | 61718891409749603155862736001 | 28.79 | order 2 |  | 43 · 101 · 113 · 163 · 191 · 419 · 463 · 881 · 1559 · 3191 · 4751 | **this census** |
| 124 | 63903529488236770899696729601 | 28.81 | order 2 |  | 19 · 43 · 83 · 109 · 127 · 197 · 199 · 233 · 307 · 881 · 2969 · 9281 | **this census** |
| 125 | 67612520959061465487519619201 | 28.83 | order 2 |  | 43 · 79 · 151 · 199 · 239 · 271 · 419 · 727 · 911 · 3079 · 11969 | **this census** |
| 126 | 71909096287325582852469302401 | 28.86 | order 2 |  | 101 · 199 · 229 · 521 · 1871 · 3079 · 4159 · 19889 · 62929 | **this census** |
| 127 | 75084792811304298963925944961 | 28.88 | Chebyshev only | 127 | 19 · 31 · 43 · 47 · 67 · 71 · 89 · 103 · 127 · 139 · 181 · 307 · 439 · 3359 | **this census** |
| 128 | 85113741876256705160256107401 | 28.93 | Chebyshev only | 41, 71, 89, 311, 3079 | 29 · 37 · 41 · 43 · 71 · 89 · 109 · 131 · 311 · 571 · 701 · 1301 · 3079 | **this census** |
| 129 | 85591811776429200427031246401 | 28.93 | Chebyshev only | 4159 | 19 · 53 · 61 · 79 · 89 · 149 · 181 · 311 · 967 · 1451 · 4049 · 4159 | **this census** |
| 130 | 87856315530443123938151724001 | 28.94 | Chebyshev only | 991 | 29 · 61 · 113 · 139 · 199 · 229 · 251 · 991 · 1427 · 6991 · 27961 | **this census** |
| 131 | 90688854810222591903117577441 | 28.96 | Chebyshev only | 31, 1567 | 31 · 71 · 103 · 233 · 307 · 409 · 811 · 883 · 1429 · 1567 · 8527 | **this census** |
| 132 | 93083450169938405767940750401 | 28.97 | Chebyshev only | 191 | 17 · 31 · 53 · 79 · 113 · 151 · 191 · 593 · 739 · 1231 · 1559 · 15391 | **this census** |
| 133 | 97073909726951543608461919681 | 28.99 | order 2 |  | 23 · 53 · 103 · 109 · 197 · 241 · 271 · 521 · 727 · 881 · 883 · 1871 | **this census** |
| 134 | 102191665496386714854245640001 | 29.01 | Chebyshev only | 449, 11969 | 31 · 41 · 107 · 181 · 239 · 307 · 419 · 449 · 3079 · 8161 · 11969 | **this census** |
| 135 | 104702415675548646087023411521 | 29.02 | Chebyshev only | 191 | 29 · 31 · 41 · 43 · 53 · 67 · 71 · 113 · 131 · 191 · 419 · 509 · 571 · 761 | **this census** |
| 136 | 107755240130126329191082632001 | 29.03 | order 2 |  | 17 · 47 · 53 · 79 · 197 · 251 · 431 · 859 · 881 · 991 · 1301 · 1549 | **this census** |
| 137 | 109760545490176816032548520001 | 29.04 | Chebyshev only | 449 | 23 · 31 · 43 · 71 · 73 · 113 · 199 · 223 · 449 · 1901 · 4751 · 33967 | **this census** |
| 138 | 110244345805263665512480194001 | 29.04 | Chebyshev only | 47, 881, 4049 | 19 · 29 · 41 · 47 · 89 · 101 · 139 · 197 · 199 · 461 · 881 · 1289 · 4049 | **this census** |
| 139 | 113331895388837044576937280001 | 29.05 | Chebyshev only | 73 | 31 · 67 · 73 · 167 · 257 · 1889 · 4159 · 4481 · 9461 · 52289 | **this census** |
| 140 | 116519835693817310596546985281 | 29.07 | order 2 |  | 31 · 37 · 53 · 71 · 79 · 103 · 109 · 113 · 271 · 463 · 521 · 911 · 4523 | **this census** |
| 141 | 125008002039355638958400045401 | 29.10 | Chebyshev only | 41, 71, 103, 599, 2729 | 41 · 43 · 53 · 59 · 61 · 71 · 103 · 139 · 373 · 461 · 599 · 1301 · 2729 | **this census** |
| 142 | 126071045494355453802452906401 | 29.10 | order 2 |  | 11 · 103 · 113 · 139 · 521 · 647 · 911 · 1103 · 1861 · 2549 · 4409 | **this census** |
| 143 | 128113086406354488544058553601 | 29.11 | order 2 |  | 41 · 71 · 73 · 79 · 97 · 127 · 131 · 449 · 571 · 883 · 3331 · 6271 | **this census** |
| 144 | 133096515722919823805194464001 | 29.12 | Chebyshev only | 769 | 41 · 47 · 127 · 229 · 461 · 503 · 521 · 769 · 1151 · 2393 · 9281 | **this census** |
| 145 | 133386824511122157574517318401 | 29.13 | Chebyshev only | 769 | 29 · 41 · 53 · 79 · 197 · 199 · 419 · 571 · 701 · 769 · 1409 · 3761 | **this census** |
| 146 | 138087826457302559074727009521 | 29.14 | Chebyshev only | 113 | 29 · 37 · 41 · 61 · 89 · 113 · 131 · 137 · 379 · 419 · 461 · 1427 · 2729 | **this census** |
| 147 | 139154421057118472748901878721 | 29.14 | order 2 |  | 23 · 43 · 71 · 131 · 181 · 307 · 883 · 1861 · 1871 · 5167 · 17137 | **this census** |
| 148 | 148147081792052830933763116801 | 29.17 | order 2 |  | 29 · 41 · 71 · 89 · 103 · 127 · 131 · 197 · 881 · 883 · 3331 · 22541 | **this census** |
| 149 | 148613019371645964789250396801 | 29.17 | order 2 |  | 47 · 103 · 131 · 139 · 181 · 197 · 199 · 1301 · 1871 · 3331 · 29303 | **this census** |
| 150 | 149041972771228010298003379201 | 29.17 | order 2 |  | 23 · 31 · 103 · 151 · 191 · 271 · 571 · 1291 · 3457 · 8513 · 11969 | **this census** |
| 151 | 150373074984145657966627905601 | 29.18 | Chebyshev only | 191, 4159 | 17 · 31 · 41 · 53 · 71 · 131 · 191 · 911 · 1709 · 1951 · 4159 · 5851 | **this census** |
| 152 | 151155459152252552512051891201 | 29.18 | order 2 |  | 23 · 71 · 101 · 163 · 307 · 379 · 601 · 769 · 2377 · 5167 · 8513 | **this census** |
| 153 | 151737263983478535726543379201 | 29.18 | Chebyshev only | 769 | 31 · 109 · 113 · 151 · 223 · 463 · 701 · 769 · 2591 · 3457 · 5279 | **this census** |
| 154 | 158647590842481558288190399681 | 29.20 | order 2 |  | 19 · 23 · 41 · 67 · 71 · 97 · 109 · 181 · 241 · 307 · 991 · 2729 · 4861 | **this census** |
| 155 | 160382997245097875278647817201 | 29.21 | Chebyshev only | 337, 463 | 23 · 37 · 307 · 337 · 463 · 521 · 571 · 701 · 1429 · 2521 · 5237 | **this census** |
| 156 | 166535210436252664410472068001 | 29.22 | order 2 |  | 19 · 29 · 43 · 47 · 107 · 137 · 211 · 239 · 251 · 271 · 701 · 1429 · 2969 | **this census** |
| 157 | 167404411915426044283140216001 | 29.22 | order 2 |  | 31 · 47 · 97 · 103 · 229 · 419 · 601 · 1291 · 1871 · 2393 · 34501 | **this census** |
| 158 | 168694443984438067449601774081 | 29.23 | order 2 |  | 29 · 37 · 41 · 43 · 67 · 109 · 137 · 197 · 379 · 7039 · 11593 · 14629 | **this census** |
| 159 | 178711171266332736447473977921 | 29.25 | Chebyshev only | 2753, 4159 | 41 · 79 · 131 · 181 · 271 · 379 · 461 · 883 · 2753 · 4159 · 4861 | **this census** |
| 160 | 225127336581668310240380529601 | 29.35 | Chebyshev only | 577, 1471, 15809 | 29 · 53 · 71 · 73 · 79 · 101 · 197 · 229 · 577 · 1471 · 5851 · 15809 | **this census** |
| 161 | 234965040910225870816645032961 | 29.37 | order 2 |  | 37 · 71 · 89 · 109 · 127 · 881 · 1061 · 1483 · 2243 · 2861 · 8161 | **this census** |
| 162 | 235317777338413287700412630401 | 29.37 | Chebyshev only | 7039 | 19 · 43 · 59 · 89 · 167 · 181 · 233 · 433 · 463 · 1327 · 4159 · 7039 | **this census** |
| 163 | 263087650323805230498352377601 | 29.42 | order 2 |  | 71 · 101 · 229 · 419 · 919 · 1429 · 1471 · 4159 · 6761 · 7039 | **this census** |
| 164 | 310938948890898305000359976641 | 29.49 | order 2 |  | 31 · 41 · 43 · 71 · 233 · 241 · 271 · 463 · 937 · 1429 · 1609 · 5279 | **this census** |
| 165 | 315917807454112935155692608001 | 29.50 | order 2 |  | 29 · 31 · 41 · 89 · 239 · 271 · 307 · 659 · 701 · 911 · 3329 · 3457 | **this census** |
| 166 | 318160964255204908837662062401 | 29.50 | order 2 |  | 29 · 31 · 67 · 71 · 79 · 83 · 151 · 181 · 199 · 409 · 419 · 571 · 21319 | **this census** |
| 167 | 334801383081427770973135070401 | 29.52 | Chebyshev only | 4159 | 43 · 59 · 113 · 151 · 197 · 271 · 881 · 1871 · 4003 · 4159 · 5279 | **this census** |
| 168 | 336678590904893959268662315201 | 29.53 | Chebyshev only | 191, 11969 | 23 · 31 · 41 · 43 · 71 · 89 · 97 · 131 · 151 · 181 · 191 · 197 · 271 · 11969 | **this census** |
| 169 | 342935838555568318773540828001 | 29.54 | order 2 |  | 37 · 89 · 101 · 109 · 113 · 181 · 199 · 337 · 521 · 1483 · 2551 · 3499 | **this census** |
| 170 | 388409745448891865393360265601 | 29.59 | Chebyshev only | 127 | 37 · 41 · 59 · 67 · 71 · 113 · 127 · 191 · 239 · 307 · 991 · 1217 · 3761 | **this census** |
| 171 | 396709382776893730429831545601 | 29.60 | Chebyshev only | 769 | 23 · 31 · 101 · 127 · 131 · 181 · 239 · 449 · 769 · 911 · 4159 · 5851 | **this census** |
| 172 | 397806663158730709235676324001 | 29.60 | order 2 |  | 37 · 79 · 89 · 101 · 419 · 701 · 911 · 2069 · 2351 · 2393 · 4861 | **this census** |
| 173 | 412874721000725058211545319681 | 29.62 | order 2 |  | 23 · 31 · 59 · 67 · 113 · 173 · 239 · 463 · 509 · 2089 · 7481 · 8513 | **this census** |
| 174 | 442875745314302705567788626001 | 29.65 | Chebyshev only | 79, 239, 7151 | 37 · 41 · 43 · 71 · 79 · 101 · 103 · 151 · 239 · 251 · 307 · 5851 · 7151 | **this census** |
| 175 | 511714740095171322506538421681 | 29.71 | Chebyshev only | 113, 881, 1871 | 37 · 67 · 89 · 113 · 181 · 197 · 307 · 571 · 647 · 881 · 1871 · 3079 | **this census** |
| 176 | 511755777458424161725823560801 | 29.71 | Chebyshev only | 2591 | 71 · 73 · 89 · 109 · 163 · 433 · 571 · 2591 · 3433 · 4217 · 6733 | **this census** |
| 177 | 526129433476775882561851243201 | 29.72 | Chebyshev only | 449, 1601 | 19 · 53 · 131 · 173 · 179 · 181 · 431 · 449 · 859 · 1429 · 1601 · 1871 | **this census** |
| 178 | 611735329101309823150226085601 | 29.79 | order 2 |  | 43 · 67 · 89 · 103 · 131 · 151 · 239 · 379 · 521 · 571 · 1223 · 35531 | **this census** |
| 179 | 638441256413880049160291184001 | 29.81 | order 2 |  | 13 · 47 · 113 · 199 · 241 · 419 · 461 · 967 · 2111 · 2531 · 193201 | **this census** |
| 180 | 665951765284067421160801800001 | 29.82 | Chebyshev only | 449, 4159 | 29 · 197 · 239 · 449 · 491 · 883 · 4159 · 4591 · 4999 · 26249 | **this census** |
| 181 | 674270485359912793413041460481 | 29.83 | order 2 |  | 23 · 43 · 53 · 71 · 103 · 109 · 127 · 359 · 1429 · 3041 · 3457 · 23561 | **this census** |
| 182 | 678617694966364134703577856001 | 29.83 | order 2 |  | 17 · 47 · 71 · 89 · 113 · 251 · 449 · 571 · 967 · 2393 · 2729 · 2927 | **this census** |
| 183 | 683402675272767367575156298801 | 29.83 | Chebyshev only | 8527 | 19 · 59 · 101 · 103 · 109 · 199 · 311 · 349 · 491 · 883 · 6733 · 8527 | **this census** |
| 184 | 699963023612122306431081825601 | 29.85 | order 2 |  | 41 · 73 · 199 · 223 · 349 · 2551 · 2617 · 5039 · 6323 · 70991 | **this census** |
| 185 | 702050650525144183203961020001 | 29.85 | Chebyshev only | 5279 | 41 · 43 · 61 · 89 · 197 · 307 · 349 · 401 · 883 · 1301 · 1429 · 5279 | **this census** |
| 186 | 707121894703235251544046943201 | 29.85 | order 2 |  | 67 · 101 · 103 · 137 · 181 · 197 · 349 · 2129 · 2551 · 4409 · 24851 | **this census** |
| 187 | 716037428721379223097137378881 | 29.85 | order 2 |  | 53 · 71 · 197 · 223 · 307 · 647 · 683 · 911 · 991 · 2729 · 12959 | **this census** |
| 188 | 760110398267085646812926294401 | 29.88 | order 2 |  | 17 · 23 · 37 · 59 · 191 · 349 · 419 · 521 · 727 · 2089 · 5741 · 7019 | **this census** |
| 189 | 796172448067484530280828990401 | 29.90 | order 2 |  | 29 · 43 · 79 · 103 · 109 · 149 · 197 · 593 · 883 · 2549 · 2729 · 6733 | **this census** |
| 190 | 810871120612495396700816169601 | 29.91 | order 2 |  | 29 · 41 · 53 · 67 · 71 · 79 · 89 · 109 · 271 · 701 · 919 · 4159 · 4861 | **this census** |
| 191 | 816392500874711102007781315201 | 29.91 | Chebyshev only | 127 | 37 · 89 · 127 · 151 · 239 · 353 · 911 · 1429 · 2243 · 5851 · 8969 | **this census** |
| 192 | 842456946332654926879756550401 | 29.93 | order 2 |  | 29 · 41 · 67 · 97 · 101 · 103 · 113 · 151 · 199 · 419 · 881 · 1429 · 5851 | **this census** |
| 193 | 850483831970240418889056000961 | 29.93 | Chebyshev only | 191, 1217 | 13 · 37 · 41 · 43 · 67 · 89 · 109 · 191 · 379 · 647 · 1217 · 2089 · 12959 | **this census** |
| 194 | 857912856639890712600333794401 | 29.93 | Chebyshev only | 31 | 19 · 31 · 71 · 73 · 79 · 83 · 101 · 103 · 409 · 593 · 883 · 2549 · 7547 | **this census** |
| 195 | 858548998580027923447836480001 | 29.93 | order 2 |  | 13 · 29 · 37 · 71 · 89 · 109 · 151 · 167 · 191 · 257 · 419 · 449 · 499 · 769 | **this census** |
| 196 | 991450638881493066957728124001 | 30.00 | Chebyshev only | 31 | 23 · 29 · 31 · 43 · 71 · 113 · 199 · 211 · 239 · 953 · 1259 · 3299 · 3499 | **this census** |

**By decade:**

| decade | 14 | 16 | 17 | 18 | 19 | 20 | 21 | 23 | 24 | 25 | 26 | 27 | 28 | 29 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| order 2 | 1 | 1 | 1 | 2 | 0 | 0 | 1 | 0 | 8 | 8 | 11 | 12 | 17 | 33 |
| Chebyshev only | 1 | 0 | 0 | 0 | 2 | 2 | 1 | 2 | 4 | 5 | 8 | 17 | 29 | 30 |
| all terms | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 12 | 13 | 19 | 29 | 46 | 63 |

The census also shows:
- **No term is divisible by 5 or 7**, and no term has a smallest prime above 113.
- **The largest prime factor of any term is still 474,949**, in a(82), below $10^{28}$. Among the order-2 terms the largest is still 209,089. No term above $10^{28}$ has a larger prime.
- **The largest second-largest prime is 19,889**, in a(126). So every term lies in the capped part of the search, described below.
- **Halfway primes:** of the 101 Chebyshev-only terms, 56 are halfway at one prime, 27 at two, 11 at three, 3 at four and 4 at five.

## How the search works

Every Chebyshev–Carmichael $n < X$, with primes $p_1 < \dots < p_k$, falls into one part of the search below. Each part has its own engine and its own completeness theorem. The proofs are written for both moduli, $g(p) = (p^2-1)/D$ with $D = 1$ (order 2) or $D = 2$ (Chebyshev). The engines run in Chebyshev mode with `CN2X_MODE=cheb`.

| part | which $n$ | engine | why it misses nothing |
|---|---|---|---|
| capped | $p_{k-1} \le T$ | `cn2xh.c`: depth-first search over the primes up to $T$, with LASTCALC | [LASTCALC proof](docs/CN2_LastCalc_Coverage_Proof.md) |
| pair tail | $p_{k-1} > T$, $p_k \le q^*$ | `cn2pair.c`: one residue class per prime pair $T < p < q \le q^*$ | [tail proof](docs/CN2_Tail_Coverage_Proof.md), Lemma B |
| $(q, a)$ tail, lower | a prime in $(q^*, 2^{32})$ | `cn2tail.c` with `CN2X_TAIL_CAP32=1`: $n = q(q + a\thinspace g(q))$ or $q(1 + a\thinspace g(q))$ | [tail proof](docs/CN2_Tail_Coverage_Proof.md), Lemmas A and C |
| $(q, a)$ tail, upper | a prime above $2^{32}$ | `cn2tail_top.c`: the same search in 128-bit arithmetic | [tail proof](docs/CN2_Tail_Coverage_Proof.md), Lemmas A and C |

Below $10^{30}$ the split used $T = 30{,}000$ and $q^* = 90{,}000{,}000$. The search took about 430 hours on 30 threads, from 17 October to 8 November 2026: 265 h capped, 100.3 h pair tail, 64.5 h lower $(q,a)$ tail and 2 minutes upper. Every candidate from every engine is factorised and checked against the definition. Each find is classed as order 2 or Chebyshev only against the full modulus $p^2-1$.

`cn2x/cn2tail.c` is the certified engine of the earlier censuses plus one line. That line lets it stop at $2^{32}$ when `CN2X_TAIL_CAP32` is set, and without the setting it behaves exactly as before. `cn2x/cn2tail_top.c` differs from it only in holding primes in 64 bits and $g(q)$ in 128 bits. Before the run, both were checked against the certified engine and against an independent brute force, `tests/check_top_brute.py`; the [certificate](docs/CN2_Cheb_Certificate_1e30.md), §2, gives the results.

## Checking it

```bash
pip install -r requirements.txt
python3 tests/check_cheb_terms.py results/b299799.txt     # every term against the definition, standard library only
python3 tests/check_cheb_terms.py results/b175531.txt     # the 95 order-2 terms
python3 cn2_tail_verify.py --X 1e30 --mode cheb --pair results/cert_1e30/pair \
        --qa results/cert_1e30/tail results/cert_1e30/tail_top --T 30000 --reference results/b299799.txt   # PASS
```

`check_cheb_terms.py` factorises each term afresh by trial division and checks:
- that the term is odd, composite and squarefree;
- that it is a Carmichael number of order 1 (Korselt's criterion);
- the $(p^2-1)/2$ condition;
- the $\pm 1$ criterion separately.

It also reports which terms are of order 2. `cn2_tail_verify.py` re-verifies every survivor the tail engines wrote, about a minute's work.

The run records in `results/cert_1e30/` include:
- parameters (`split.json`);
- engine hashes (`ENGINES.sha256`, `ENGINES_tail_1e30.sha256`);
- the completion records and shard logs of all four runs;
- the tails' raw survivors;
- the verified results (`result.json`, `campaign_verify_final.txt`, `tail_verify_final.txt`, `check_cheb_terms_1e30.txt`).

The capped run's raw survivor file (1.38 GB) is not included. The certificate's §6 gives the commands to reproduce the run.

## Layout

| path | contents |
|---|---|
| `cn2x/` | the engines (C): `cn2xh.c` and `cn2pair.c` as certified, `cn2tail.c` with the one added line, `cn2tail_top.c` |
| `cn2_split_campaign.py` | driver for the capped search (`init`, `run`, `verify`); in Chebyshev mode it classes each find as order 2 or Chebyshev only |
| `cn2_tail_verify.py`, `cn2_capped_peek.py` | verifiers for the tails and for a capped run in progress |
| `cn2_results_table.py` | the wide one-line-per-term table |
| `cn2_replay_run.py` | re-runs sampled production shards alone on one thread (not used at $10^{30}$; see the certificate's §3) |
| `cn2_order2_defs.py` | the definitions (rigid, Howe, Chebyshev) and the candidate verifier |
| `docs/` | the certificate and the two proofs |
| `results/` | the terms (`b299799.txt`, `b175531.txt`) and the run records |
| `tests/` | `check_cheb_terms.py`, a standalone check of a b-file; `check_top_brute.py`, the brute-force check of `cn2tail_top` |

The censuses below $10^{25}$ and $10^{28}$ are in [cheb-cn2-census](https://github.com/pudepiedj/cheb-cn2-census).

## Licence

MIT; see `LICENSE`.
