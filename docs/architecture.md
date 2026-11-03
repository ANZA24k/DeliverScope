# DeliverScope trust and state model

The problem is disagreement between a client and a freelancer about whether a
deliverable satisfies a previously agreed brief and preserves required
behaviour. DeliverScope locks that standard before evidence arrives, binds a
delivery to exact public bytes and makes a consensus-backed assessment
inspectable.

## Deterministic contract boundary

`lock_brief(brief_json)` creates a monotonic brief ID, canonical SHA-256 lock,
owner (the client), authorized freelancer, repository, reference commit, 2–6
criteria (at least one deliverable and one quality guard), evidence roles and
deadline. All inputs are public and immutable except the append-only delivery
index. The caller's ownership is recorded, not independently authenticated as
repository ownership.

`submit_deliverable(brief_id, commit, evidence_json)` permits only the
preauthorized freelancer and requires a different exact commit from the
reference commit. It validates canonical raw.githubusercontent.com URLs under
the locked repository and commit, lowercase SHA-256 values, integer lengths,
roles, unique URLs and unique content digests. Limits: 1–4 files, 12,000 bytes
per file, 24,000 total; 8 deliveries per brief; 128 briefs in this public
pilot. Paths reject empty components, traversal, percent encoding, queries,
fragments, ports, userinfo and arbitrary hosts. The contract's content limits
are checked after retrieval; transport-level streaming limits are not provided
by this SDK.

`review(delivery_id, expected_revision)` permits any caller for the first
review; only owner/freelancer can recheck. It enforces compare-and-swap
revision, at most three reviews, a seven-day review grace period after the
submission deadline, and terminal ACCEPTED. Other final outcomes describe the
latest review, and can change on an authorized recheck. New evidence requires
a new delivery; no historical review is edited or removed.

## Nondeterministic boundary

Leader and each validator independently fetch all files through
`gl.nondet.web.get`. The deployed Studio runtime uses `Response.status`, not
the newer documentation's `status_code`. Each computes SHA-256 and length
before UTF-8 decoding. Integrity mismatch, invalid UTF-8 or forbidden control
characters create a grounded INCONCLUSIVE review with per-source error codes.
HTTP/transport and malformed LLM execution errors leave state unchanged and
can be retried. They cannot turn unavailable evidence into a false definitive
verdict.

When exact text is available, `gl.nondet.exec_prompt(..., response_format='json')`
assesses each criterion. Inputs are explicitly untrusted data; embedded
instructions and verdict requests must be ignored. Strict schema validation
requires one ordered PASS / FAIL / UNKNOWN per criterion, bounded reasons and
exact source quotations for decisive findings. UNKNOWN requires no invented
citation.

`gl.vm.run_nondet_unsafe` uses a custom validator that repeats retrieval and
semantic assessment, verifies the leader's exact quotations against
independently retrieved bytes, and compares every source digest/length/error
code, each criterion classification and the derived verdict. Reasons and quote
selection need not be identical. Validator intermediate opinions are not
separately persisted; the accepted leader findings are stored after consensus.
Source documents traverse the nondeterministic return for citation validation
but are not stored as separate document bodies in contract state.

Rules: any FAIL → REJECTED; every PASS → ACCEPTED; some PASS with remaining
UNKNOWN → PARTIAL; all UNKNOWN → INCONCLUSIVE. Quality criteria express
preservation requirements, so FAIL means the prohibited behaviour occurred.
Review records include caller, pinned transaction time, revision, previous
hash and canonical review hash.

## Frontend

The frontend uses genlayer-js 1.1.8 and explicitly reads `latest-final`. It
requests no wallet action on page load. EIP-1193 connection uses only
eth_requestAccounts; no signing, approvals or Snaps. Writes require a local
preview showing method, exact arguments, network, contract and signer,
followed by the wallet's own confirmation. Account and network changes
invalidate a pending preview. External wallet writes require Studionet 61999.

The optional local test account uses the same SDK primitives as Studio,
stores its generated key only in sessionStorage, and never asks users to
provide an existing key. It is distinct from the Studio tab's own built-in
account. Confirmed writes can request simulated test-GEN faucet funds, then
send a zero-value full-consensus transaction. Transaction hashes are tracked
to ACCEPTED and then FINALIZED; errors, undetermined outcomes, status-fetch
errors and pending timeouts are visible. Public transaction records survive
refresh and support resume tracking. Test account keys never enter the repo or
server.

## Limits and continued use

This is evidence assessment, not code execution, formal verification, a full
security audit or repository-origin attestation. Source review cannot prove all
runtime behaviour or absence of undisclosed defects. Test reports can be false
even when their bytes are authentic. Prompt injection is reduced with narrow
roles, bounded data, strict outputs, grounded quotes and independent models,
not mathematically eliminated. GitHub availability and GenLayer model/consensus
behaviour remain dependencies. This public pilot is capacity limited and open
creation can exhaust its 128 brief slots; it has no escrow or payments.

A credible next step is authenticated CI attestations binding tests,
environment and artifacts to the delivery SHA, with project-scoped creation
quotas and operational metering. The current workflow is already useful for
explicit client acceptance checklists and auditable freelance triage where
these limits are acceptable.
