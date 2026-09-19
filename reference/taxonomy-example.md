# Taxonomy used in the first run (as a model)

Generated from the first analysis repository's `taxonomy/facets.json` (zapret / zapret2, DPI-bypass tooling). It is an **example of the shape and granularity**, not a vocabulary to reuse: the domain facets (`layer`, `cause`, `engine`, `proto`, `target`) and the special facets (`constraint`, `auto`, `z2`) belong to that project. The generic ones (`kind`, `ctype`, `outcome`, `conf`, `os`, `impact`) transfer.

Design notes from the first run:

- Single-valued facets: `kind`, `ctype`, `outcome`, `auto`, `z2` (successor status), `conf`. Everything else is multi-valued.
- `cause` was the largest facet (about 45 values) and grew as threads were read; it always contained `unknown` so a record never had to guess.
- The successor-status facet was named `z2` because the successor project was zapret2; rename it to fit your project.
- `constraint` values describe rules a validator would enforce; they were only assigned when the thread or commit stated or proved the rule.

## `kind` - single-valued, 11 values

What the item is (issues)

| value | meaning |
|---|---|
| `defect-tool` | bug in zapret itself |
| `defect-env` | OS/firmware/driver/network-path defect the tool ran into |
| `adversary-change` | DPI/ISP behaviour changed or was newly discovered |
| `misconfig` | user/config/strategy error (tool behaved as designed) |
| `user-error` | basic usage/skill problem |
| `feature-request` | asks for a new capability |
| `question` | how do I / why does |
| `support-install` | install/build/uninstall/start problems |
| `security-report` | AV flag, vulnerability, supply-chain, scam |
| `meta` | off-topic, licence, donation, translation, packaging |
| `spam-noise` | empty/test/duplicate/noise |

## `ctype` - single-valued, 9 values

Commit type

| value | meaning |
|---|---|
| `fix` | bug fix |
| `feature` | new capability/option |
| `refactor` | internal change, same behaviour |
| `docs` | documentation |
| `build` | build/CI/release/binaries |
| `maintenance` | lists, presets, housekeeping |
| `revert` | revert |
| `release` | version/changelog only |
| `hardening` | robustness/safety/static-analysis fix |

## `layer` - multi-valued, 10 values

Where in the system the problem sits

| value | meaning |
|---|---|
| `probe` | measurement/oracle |
| `search` | strategy search/selection |
| `adversary` | DPI/ISP behaviour |
| `path` | packet path/firewall/kernel/driver |
| `parser` | protocol recognition/reassembly |
| `scope` | lists/profiles/collateral |
| `udp-app` | UDP and app protocols |
| `ops` | install/env/service/resources/observability |
| `dist` | distribution/provenance/upgrade |
| `docs` | documentation only |

## `cause` - multi-valued, 45 values

Root cause (use unknown if not established)

| value | meaning |
|---|---|
| `byte-cutoff` | byte-count stall (e.g. 16KB) |
| `throttle` | rate limiting |
| `dns-tamper` | DNS poisoning/hijack |
| `ip-block` | IP/port level block |
| `sni-whitelist` | protocol/SNI/range whitelist |
| `dpi-reassembly` | DPI reassembly/state behaviour |
| `dpi-detector` | DPI detects the tool/anomalies |
| `route-variance` | per-route/node/CDN-edge variation |
| `qdisc-reorder` | kernel traffic shaping reorders or delays generated packets |
| `client-fingerprint` | DPI reacts to the client TLS/QUIC stack fingerprint |
| `time-decay` | worked before, ISP changed |
| `tool-regression` | tool update changed behaviour |
| `conntrack` | conntrack/NAT interaction |
| `offload` | flow offloading |
| `rule-eviction` | firewall rules removed/reordered |
| `mtu` | packet size/MTU/options |
| `mark-loop` | self-interception/mark/queue deadlock |
| `kernel-bug` | kernel/firmware bug |
| `driver` | NIC/driver/hardware offload |
| `arch-isa` | CPU arch/ISA/binary compat |
| `missing-cap` | missing module/tool/capability |
| `phase0` | SYN-time (phase 0) method vs scope |
| `no-cutoff` | unbounded fakes/dups |
| `fooling-incompat` | fooling method unsuitable for path/server |
| `kyber` | multi-segment ClientHello |
| `seqovl` | sequence-overlap semantics |
| `retrans` | retransmission handling |
| `recognizer-gap` | protocol not/wrongly recognised |
| `parse-bug` | parser logic bug |
| `memory-bug` | leak/OOB/uninitialised |
| `list-semantics` | hostlist/ipset semantics |
| `list-io` | list loading/permissions/format |
| `autohostlist` | autohostlist behaviour/limits |
| `probe-invalid` | invalid/misleading probe |
| `probe-cost` | test time/flood/cost |
| `av-flag` | antivirus/driver flag |
| `install-script` | installer/script defect |
| `resource-limit` | flash/RAM/CPU limit |
| `seccomp` | sandbox/privilege drop |
| `config-error` | wrong user configuration |
| `compat` | OS/version/tool compatibility |
| `not-client-fixable` | cannot be fixed client-side |
| `distribution` | hosting/provenance/scam |
| `doc-gap` | documentation gap |
| `unknown` | not established |

## `proto` - multi-valued, 12 values

Protocol involved

| value | meaning |
|---|---|
| `tls` |  |
| `http` |  |
| `quic` |  |
| `udp` |  |
| `tcp` |  |
| `dns` |  |
| `stun` |  |
| `wireguard` |  |
| `dht` |  |
| `vpn` |  |
| `any` |  |
| `na` |  |

## `engine` - multi-valued, 17 values

Component

| value | meaning |
|---|---|
| `nfqws` |  |
| `tpws` |  |
| `winws` |  |
| `dvtws` |  |
| `nfqws2` |  |
| `winws2` |  |
| `dvtws2` |  |
| `lua` |  |
| `blockcheck` |  |
| `init` |  |
| `ipset` |  |
| `mdig` |  |
| `ip2net` |  |
| `installer` |  |
| `docs` |  |
| `ci` |  |
| `other` |  |

## `os` - multi-valued, 8 values

Platform

| value | meaning |
|---|---|
| `linux` |  |
| `openwrt` |  |
| `keenetic` |  |
| `windows` |  |
| `macos` |  |
| `bsd` |  |
| `android` |  |
| `any` |  |

## `target` - multi-valued, 10 values

Service affected

| value | meaning |
|---|---|
| `youtube` |  |
| `discord` |  |
| `telegram` |  |
| `whatsapp` |  |
| `games` |  |
| `cdn` |  |
| `generic` |  |
| `local-net` |  |
| `vpn` |  |
| `other` |  |

## `constraint` - multi-valued, 6 values

Rule a strategy validator would have to enforce (option combinations, capabilities, bounds) - feeds the constraints catalog

| value | meaning |
|---|---|
| `illegal-combo` | two options/modes must not be combined (or combine into nonsense) |
| `phase-order` | phase/ordering rule (SYN-time vs data, reassembly, cutoff position) |
| `needs-cap` | requires a capability (TCP timestamps, conntrack, root, module, post-NAT mode) |
| `param-range` | hard numeric/positional bound (MTU headroom, seqovl vs first piece, absolute-only) |
| `engine-only` | only valid in one engine/OS (packet vs stream mode, Linux-only, BSD quirk) |
| `scope-limit` | cannot be host-scoped, or requires a limiter/cutoff to be safe |

## `impact` - multi-valued, 7 values

Effect

| value | meaning |
|---|---|
| `breaks-target` | bypass does not work |
| `breaks-nontarget` | collateral damage |
| `perf` | speed/latency |
| `crash` | crash/hang/leak |
| `install-blocked` | cannot install/start |
| `cosmetic` |  |
| `na` |  |

## `outcome` - single-valued, 10 values

How it ended

| value | meaning |
|---|---|
| `fixed` | code fix |
| `workaround` | user workaround/config |
| `docs-answer` | answered from docs |
| `wontfix` |  |
| `not-a-bug` |  |
| `cannot-reproduce` |  |
| `open` |  |
| `duplicate` |  |
| `superseded` |  |
| `unknown` |  |

## `auto` - single-valued, 5 values

Could a tool catch and/or handle this automatically

| value | meaning |
|---|---|
| `detect+handle` | can be caught and handled |
| `detect-only` | catchable, handling manual |
| `handle-only` |  |
| `manual-only` |  |
| `na` |  |

## `z2` - single-valued, 5 values

Status of this record's rule/limit in zapret2 (checked against its manual and Lua/C source)

| value | meaning |
|---|---|
| `carried` | still holds in zapret2 (documented or visible in source) |
| `changed` | holds differently: semantics, defaults or mechanism changed |
| `superseded` | no longer applies: removed, replaced or made automatic |
| `unverified` | not checked against zapret2 (yet) |
| `na` | not applicable to zapret2 (packaging, user error, platform noise) |

## `conf` - single-valued, 3 values

Confidence of the root cause

| value | meaning |
|---|---|
| `stated` | maintainer said |
| `reported` | user said |
| `inferred` | my reading |

