# ADR-0005: Scan SBOMs and stage enforcement

- **Status:** Proposed
- **Date:** 2026-11-25
- **Decision owners:** NetBird fork maintainers
- **Related:** `.github/workflows/sbom.yml`, Grype SARIF output

## Context

A vulnerability scanner can identify known vulnerable components, but an inherited repository may begin with existing findings. Turning on a hard failure before establishing a fresh, reproducible baseline can block all maintenance without distinguishing pre-existing risk from newly introduced risk. Conversely, a report-only scanner must not be mistaken for a security gate.

## Decision

We will scan the generated SPDX source SBOM with Grype, emit SARIF, and retain the report as a workflow artifact. During baseline establishment the scan is report-only (`fail-build: false`) with a high severity cutoff. Findings will be triaged and remediated. Enforcement will be tightened through a separately reviewed policy change once the baseline and exception process are understood.

## Options considered

| Option | Benefits | Costs / risks |
|---|---|---|
| Report first, then introduce gates | Makes inherited and newly introduced risk visible | Temporary period without a blocking source-SBOM gate |
| Fail immediately on all findings | Strong immediate blocking behaviour | Can block all changes due to inherited or untriaged findings |
| Do not scan | No CI cost | No repeatable vulnerability evidence |

## Consequences

### Positive
- Vulnerability evidence is generated on a schedule and for relevant changes.
- SARIF can be consumed by GitHub Code Scanning where permissions and repository settings allow.
- The team can establish a baseline before choosing an enforceable threshold.

### Negative / trade-offs
- Report-only mode does not prevent vulnerable dependencies from merging.
- A high severity cutoff omits lower-severity findings from this report.

### Operational implications
- Publish the current finding counts only from a fresh successful run.
- Triage by package, fixed version, reachability and exploitability; do not equate every CVE with equal practical risk.
- Track accepted exceptions with an owner, rationale and expiry.
- Do not promote report-only results as a passing security gate.

## Validation and evidence

The workflow is configured to scan SPDX and retain SARIF. The latest successful run and its artifact must be inspected before establishing a baseline or reporting counts.
