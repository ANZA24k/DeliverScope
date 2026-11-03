# Synthetic fixture report
The accepted delivery validates the discount range before applying it.
A discount of 100 returns 0, a discount of 0 returns the original price,
and a normal discount returns price reduced by that percentage.
Local fixture tests check (100, 0) -> 100, (100, 50) -> 50 and (100, 100) -> 0,
and that discounts of -10 and 150 are rejected.
These are synthetic examples, not independently attested production results.
The rejected fixture still applies out-of-range discounts. The unknown fixture
references an unavailable external_pricing_engine; its behaviour cannot be verified here.
