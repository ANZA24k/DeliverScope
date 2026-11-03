# Live verification — to be completed after Studio deployment

All contract writes use Studionet simulated test GEN and full consensus
(`leaderOnly: false`). No production funds, token approvals, Snap or
private-key imports are used. Deployment uses GenLayer Studio's built-in
wallet account.

**Public website:** _to be filled after publishing_

## Deployment and exact source

- Contract: _to be filled_
- Deployment transaction: _to be filled_
- Studio built-in client: _to be filled_
- Separate browser test-account freelancer: _to be filled_
- Deployed code retrieved through `getContractCode` must match
  `contracts/deliverscope.py` byte-for-byte.
- SHA-256: _to be filled_
- Runtime pinned to Studio-supported v0.2.16. Contract is deployed once.

## Pilot scenarios

All pilots use the same locked brief, exact delivery commit, and
independently retrieved files. This keeps the judgment grounded in source
behaviour rather than trusting a prose report.

| Delivery | Fixture | Final verdict | Review transaction |
|---|---|---|---|
| 1 | Explicit discount-range guard, preserves normal pricing | ACCEPTED | _to be filled_ |
| 2 | Original arithmetic still applies out-of-range discounts | REJECTED | _to be filled_ |
| 3 | Delegation to unavailable external implementation | INCONCLUSIVE | _to be filled_ |

## Reproduce verification

```sh
cd web
node verify-live.mjs
```

This read-only script checks deployed code equality, finalized state, every
pinned evidence hash/length, review hash chains and the transaction receipt
index. It writes `docs/live-state.json`, containing actual retrieved delivery
records, source fingerprints and receipt summaries. It does not submit or
repeat any review.

## Tests and limits

- Direct Mode contract tests plus executable synthetic fixture tests.
- Frontend tests: wallet public-address-only connection, rejection/no-provider
  behaviour, pinned URL constraints, Python-compatible canonical hashing,
  SHA-256 known vector, receipt-chain tampering and transaction lifecycle
  semantics.
- Ruff, GenVM safety lint, pinned SDK semantic validation and production
  frontend build pass.
- Live MetaMask extension confirmation is **not verified** unless exercised
  separately: the test browser has no EIP-1193 extension. The actual live
  writes use Studio's built-in account and a distinct browser-generated test
  signer.
- These are synthetic examples, not production security or adoption evidence.
  No claims of video/post publication are made.
