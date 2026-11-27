# IP and Open-Source Compliance Evidence

## Purpose

This repository uses automated CI to collect repeatable software-composition, licensing and source-provenance evidence. The workflow is **evidence collection, not legal clearance**. A passing workflow does not establish ownership, licence compatibility, patent freedom to operate, or permission to publish third-party or Foundation information.

## Automated evidence

The workflow `.github/workflows/ip-supply-chain.yml` runs on pushes to branches, pull requests targeting `main`, a weekly schedule, and manual dispatch.

It uploads two 90-day GitHub Actions artifacts:

- `ip-dependency-evidence`: CycloneDX JSON, SPDX JSON, Go module graph, Go licence report, frontend dependency tree and frontend licence reports.
- `ip-source-provenance-evidence`: fork-only commits, upstream diff, changed-file list, commit authorship metadata, ScanCode output and licence/notice file index.

The reports are generated for the checked-out revision. Preserve release-specific artifacts alongside the release record if long-term evidence is required.

## Current repository licence boundary to verify

The root licensing information identifies BSD-3-Clause as the general licence and identifies AGPLv3-covered subtrees. The README's legal summary must be checked against the actual licence files on every relevant upstream revision. In particular, verify whether `combined/` is listed consistently with `management/`, `signal/` and `relay/`. Do not rely on README prose instead of the actual licence texts.

## Review policy

The pipeline deliberately does **not** fail simply because it detects AGPL, LGPL, GPL, dual-licensed, custom, or unknown components. This repository itself contains differently licensed components, and a simplistic deny-list would generate misleading results.

Reviewers must:

1. Verify each detected licence against the exact component version and its canonical licence text.
2. Review direct and transitive dependencies, including Go modules, JavaScript packages, vendored code, generated code, embedded assets, container images and binaries actually shipped.
3. Distinguish production dependencies from development-only dependencies.
4. Record copyright notices, attribution requirements, source-offer/source-disclosure obligations, patent clauses, trademark exclusions and modification notices where applicable.
5. Manually review `NOASSERTION`, unknown, custom, multiple, conflicting or missing licence detections.
6. Assess AGPLv3 implications against the actual deployment and distribution model. Network use, modification, conveyance and combined/derivative-work questions require legal analysis.
7. Inspect the upstream comparison patch to identify fork-specific changes. A diff is evidence of change, not proof of authorship or ownership.
8. Check contributor agreements, employment terms, consultancy contracts, university policies, client/charity agreements, assignments and permissions before asserting ownership.
9. Maintain a third-party notice bundle for each shipped release and retain the corresponding SBOM.

## Third-party modification register

For each copied or modified third-party component, record:

| Field | Required evidence |
|---|---|
| Component and version | SBOM purl/name/version |
| Original source | Canonical upstream URL and commit/tag |
| Original licence | Exact licence identifier and licence text |
| Local path | Repository path(s) containing the material |
| Modification | Summary and diff/commit reference |
| Author/contributor | Commit and contribution provenance |
| Required notice | Copyright, licence and modification notice |
| Distribution impact | Source availability, notice, offer or other obligations |
| Decision | Approved, rejected or pending legal review |

## Commercial release gate

Do not describe the repository or a product built from it as wholly proprietary. Do not remove upstream copyright or licence notices. Before commercial release, obtain a human-reviewed sign-off that covers the exact release commit, deployment topology, shipped components, SBOM, notices, source-disclosure obligations and ownership evidence.

## Known limitations

- Go licence collection may fail for packages that cannot be resolved or inspected; check the workflow log and report completeness.
- Frontend installation uses `--ignore-scripts` to reduce execution risk; packages that require install-time generation may not be fully represented.
- ScanCode findings are heuristic detections and need manual verification.
- Syft inventories discovered components; it does not by itself prove all files or dependencies are licensed compatibly.
- The upstream comparison fetches NetBird's current `main`, so scheduled reports can change as upstream changes. For release evidence, compare against the precise upstream base commit used by the fork.
- GitHub Actions artifacts expire after 90 days by default in this workflow. Export release evidence to controlled, durable storage where required.
- A branch push should create a workflow run. If it does not, check repository Actions settings and workflow-file validation; do not treat the absence of a run as a successful scan.
