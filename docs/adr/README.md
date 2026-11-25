# Architecture Decision Records

This directory is the decision log for the AndieKobbieTech-maintained NetBird fork.

The records follow the lightweight, one-decision-per-document approach described by [Spotify Engineering](https://engineering.atspotify.com/2020/4/when-should-i-write-an-architecture-decision-record/): capture the context, the decision and its consequences, including decisions that have become implicit standards. Significant proposals should be discussed in a PR or RFC first; the resulting decision is recorded here.

## How to use this log

- Read the records in numerical order for the evolution of the maintenance architecture.
- Each ADR covers one decision. Implementation detail belongs in code, workflow files or operational runbooks.
- Status describes the decision in this fork, not the upstream NetBird project.
- **Proposed** means the change is present on the maintenance branch but has not yet been accepted by merging its pull request.
- **Accepted** means the decision has been accepted for this fork.
- **Superseded** records remain in place and link to the replacing ADR. Do not rewrite history.
- Link implementation PRs, test evidence and security reports from the relevant ADR when they exist. Never describe a check as passing unless its run is green and current for the relevant commit.

## Decision index

| ADR | Decision | Status |
|---|---|---|
| [0001](0001-maintain-a-traceable-upstream-fork.md) | Maintain a traceable upstream fork | Proposed |
| [0002](0002-use-automated-dependency-update-proposals.md) | Use automated dependency update proposals | Proposed |
| [0003](0003-pin-ci-actions-to-immutable-commits.md) | Pin CI actions to immutable commits | Proposed |
| [0004](0004-publish-source-sboms-in-two-standard-formats.md) | Publish source SBOMs in SPDX and CycloneDX | Proposed |
| [0005](0005-scan-sboms-and-stage-enforcement.md) | Scan SBOMs and stage enforcement | Proposed |
| [0006](0006-review-new-dependencies-in-pull-requests.md) | Review newly introduced dependencies in PRs | Proposed |
| [0007](0007-attest-container-image-sboms-at-build-time.md) | Attach SBOM attestations to container images | Proposed |
| [0008](0008-preserve-release-signing-when-key-is-configured.md) | Preserve release signing when a key is configured | Proposed |
| [0009](0009-use-a-single-maintenance-integration-branch.md) | Integrate maintenance changes on a dedicated branch | Proposed |
| [0010](0010-retain-machine-readable-security-evidence.md) | Retain machine-readable security evidence | Proposed |
| [0011](0011-progressively-enforce-vulnerability-gates.md) | Progressively enforce vulnerability gates | Proposed |\n| [0012](0012-keep-fork-validation-separate-from-upstream-release-publishing.md) | Keep fork validation separate from upstream release publishing | Proposed |
| [0013](0013-use-elestio-byovm-only-after-network-validation.md) | Use Elestio BYOVM only after direct UDP and proxy validation | Proposed |

## Template

Use [template.md](template.md) for new records. Add a row to this index and link the implementation PR or evidence where available.
