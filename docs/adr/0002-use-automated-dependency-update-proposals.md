# ADR-0002: Use automated dependency update proposals

- **Status:** Proposed
- **Date:** 2026-11-25
- **Decision owners:** NetBird fork maintainers
- **Related:** `.github/dependabot.yml`, dependency update PRs #3–#23, [PR #2](https://github.com/andiekobbietks/netbird/pull/2)

## Context

NetBird contains Go modules, JavaScript packages, GitHub Actions, Docker build contexts and Dev Container configuration. Manual tracking across these ecosystems is error-prone. Automated updates improve visibility but can also introduce incompatible or vulnerable combinations if merged without review.

## Decision

We will use Dependabot to propose scheduled updates for the repository's declared ecosystems. Updates will arrive as pull requests and will be reviewed, tested and merged deliberately. Grouping will be used where packages have a shared release or compatibility boundary; security-sensitive or independently versioned packages may remain separate for clearer attribution.

## Options considered

| Option | Benefits | Costs / risks |
|---|---|---|
| Dependabot proposals with review gates | Broad ecosystem coverage and auditable changes | Requires triage and CI capacity |
| Manual dependency tracking | Full control over timing | High omission and delay risk |
| Automatically merge all updates | Low maintenance overhead | Unsafe for a complex multi-platform application |

## Consequences

### Positive
- Dependency drift becomes visible through routine PRs.
- Each update has a diff, review discussion and CI result.
- Ecosystem coverage is explicit in version control.

### Negative / trade-offs
- Grouped updates can make regressions harder to attribute.
- Update volume can overwhelm maintainers if limits and grouping are poorly tuned.
- Dependabot does not replace vulnerability scanning or compatibility testing.

### Operational implications
- Never enable blanket auto-merge for all dependency updates.
- Review major/minor updates for API and runtime compatibility.
- Keep lockfiles and Go checksums in sync.
- Revisit ignored dependencies and grouping rules during maintenance reviews.

## Validation and evidence

The proposed configuration covers GitHub Actions, Go modules, npm, Dev Container Features and verified Docker contexts. Actual Dependabot execution and the resulting PR checks must be verified after the configuration is merged.
