# Official API references checked 2026-11-03

- https://docs.genlayer.com/developers/intelligent-contracts/equivalence-principle
- https://docs.genlayer.com/developers/intelligent-contracts/features/web-access
- https://docs.genlayer.com/developers/intelligent-contracts/features/calling-llms
- https://docs.genlayer.com/developers/intelligent-contracts/features/transaction-context
- https://docs.genlayer.com/developers/intelligent-contracts/testing
- https://docs.genlayer.com/api-references/genlayer-test/direct
- https://github.com/genlayerlabs/genvm/releases/tag/v0.2.16
- https://github.com/genlayerlabs/genlayer-studio/blob/main/frontend/src/stores/accounts.ts

Current developer docs require substance verification through independently retrieved evidence, not schema-only validator approval. DeliverScope repeats the whole assessment and compares stable fields.

Compatibility: Studio's deployed templates use GenVM v0.2.16 and runner 1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6. The moving latest prerelease (v0.3.0-rc7) does not load through genlayer-test 0.29.2 / genvm-linter 0.11.0. Contract, test fixture loader and linter checks are therefore pinned to Studio's runtime. Its web response uses `status`; current prose examples use `status_code`. SDK validation, direct tests and the deployed source verification establish the actual supported combination.
