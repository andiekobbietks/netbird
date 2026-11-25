
<div align="center">
  <p align="center">
    <img width="234" src="docs/media/logo-full.png" alt="NetBird logo"/>
  </p>
  <p align="center">
    <a href="https://sonarcloud.io/dashboard?id=netbirdio_netbird">
      <img src="https://sonarcloud.io/api/project_badges/measure?project=netbirdio_netbird&metric=alert_status" alt="SonarCloud alert status"/>
    </a>
    <a href="https://github.com/netbirdio/netbird/blob/main/LICENSE">
      <img src="https://img.shields.io/badge/license-BSD--3-blue" alt="BSD-3 License"/>
    </a>
    <a href="https://docs.netbird.io/discord-url">
      <img src="https://img.shields.io/badge/discord-@netbird-5865F2.svg?logo=discord&logoColor=white" alt="NetBird Discord"/>
    </a>
    <a href="https://forum.netbird.io">
      <img src="https://img.shields.io/badge/community%20forum-@netbird-red.svg?logo=discourse" alt="Community forum"/>
    </a>
    <a href="https://gurubase.io/g/netbird">
      <img src="https://img.shields.io/badge/Gurubase-Ask%20NetBird%20Guru-006BFF" alt="Gurubase: Ask NetBird Guru"/>
    </a>
  </p>
</div>

<p align="center">
  <strong>
    Start using NetBird at <a href="https://netbird.io/pricing">netbird.io</a>
    <br/>
    See <a href="https://docs.netbird.io/">Documentation</a>
    <br/>
    Join our <a href="https://docs.netbird.io/discord-url">Discord server</a> or our <a href="https://forum.netbird.io">Community forum</a>
  </strong>
  <br/>
  <br/>
  <strong>
    🚀 <a href="https://netbird.io/careers">We are hiring! Join us at https://netbird.io/careers</a>
  </strong>
</p>

> ### 🤖 NetBird Agent Network (Beta)
> Identity-aware access control for AI agents — keyless access to LLM APIs and private
> resources over the encrypted NetBird tunnel. See [`agent-network/`](agent-network/) or
> read the docs at **[netbird.ai](https://netbird.ai)**.

**NetBird combines a configuration-free peer-to-peer private network and a centralized access control system in a single platform, making it easy to create secure private networks for your organization or home.**

**Connect.** NetBird creates a WireGuard-based overlay network that automatically connects your machines over an encrypted tunnel, leaving behind the hassle of opening ports, complex firewall rules, VPN gateways, and so forth.

**Secure.** NetBird enables secure remote access by applying granular access policies while allowing you to manage them intuitively from a single place. Works universally on any infrastructure.

https://github.com/user-attachments/assets/10cec749-bb56-4ab3-97af-4e38850108d2

### Self-host NetBird (video)

[![Watch the video](https://img.youtube.com/vi/bZAgpT6nzaQ/0.jpg)](https://youtu.be/bZAgpT6nzaQ)

### Key features

| Connectivity | Management | Security | Automation | Platforms |
|---|---|---|---|---|
| ✓ [Kernel WireGuard](https://docs.netbird.io/about-netbird/why-wireguard-with-netbird) | ✓ [Admin Web UI](https://github.com/netbirdio/dashboard) | ✓ [SSO & MFA support](https://docs.netbird.io/how-to/installation#running-net-bird-with-sso-login) | ✓ [Public API](https://docs.netbird.io/api) | ✓ [Linux](https://docs.netbird.io/get-started/install/linux) |
| ✓ [Peer-to-peer connections](https://docs.netbird.io/about-netbird/how-netbird-works) | ✓ Auto peer discovery and configuration | ✓ [Access control: groups & rules](https://docs.netbird.io/how-to/manage-network-access) | ✓ [Setup keys for bulk provisioning](https://docs.netbird.io/how-to/register-machines-using-setup-keys) | ✓ [macOS](https://docs.netbird.io/get-started/install/macos) |
| ✓ Connection relay fallback | ✓ [IdP integrations](https://docs.netbird.io/selfhosted/identity-providers) | ✓ [Activity logging](https://docs.netbird.io/how-to/audit-events-logging) | ✓ [Self-hosting quickstart script](https://docs.netbird.io/selfhosted/selfhosted-quickstart) | ✓ [Windows](https://docs.netbird.io/get-started/install/windows) |
| ✓ [Routes to external networks](https://docs.netbird.io/how-to/routing-traffic-to-private-networks) | ✓ [Private DNS](https://docs.netbird.io/how-to/manage-dns-in-your-network) | ✓ [Traffic events](https://docs.netbird.io/manage/activity/traffic-events-logging) | ✓ [IdP groups sync with JWT](https://docs.netbird.io/manage/team/idp-sync) | ✓ [Android](https://docs.netbird.io/get-started/install/android) |
| ✓ [Domain-based DNS routes](https://docs.netbird.io/manage/dns/dns-aliases-for-routed-networks) | ✓ [Custom DNS zones](https://docs.netbird.io/manage/dns/custom-zones) | ✓ [Device posture checks](https://docs.netbird.io/how-to/manage-posture-checks) | ✓ [Terraform provider](https://registry.terraform.io/providers/netbirdio/netbird/latest) | ✓ [Android TV](https://docs.netbird.io/get-started/install/android-tv) |
| ✓ [Exit nodes](https://docs.netbird.io/manage/network-routes/use-cases/exit-nodes) | ✓ [Multiuser support](https://docs.netbird.io/how-to/add-users-to-your-network) | ✓ Peer-to-peer encryption | ✓ [Ansible collection](https://github.com/netbirdio/ansible-netbird) | ✓ [iOS](https://docs.netbird.io/get-started/install/ios) |
| ✓ [IPv6 dual-stack overlay](https://docs.netbird.io/manage/settings/ipv6) | ✓ [Multi-account profile switching](https://docs.netbird.io/client/profiles) | ✓ [SSH with central access policies](https://docs.netbird.io/manage/peers/ssh) | | ✓ [Apple TV](https://docs.netbird.io/get-started/install/tvos) |
| ✓ [Browser SSH & RDP](https://docs.netbird.io/manage/peers/browser-client) | | ✓ [Quantum-resistance with Rosenpass](https://netbird.io/knowledge-hub/the-first-quantum-resistant-mesh-vpn) | | ✓ FreeBSD |
| ✓ [Reverse proxy with auto-TLS](https://docs.netbird.io/manage/reverse-proxy) | | ✓ [Periodic re-authentication](https://docs.netbird.io/how-to/enforce-periodic-user-authentication) | | ✓ [pfSense](https://docs.netbird.io/get-started/install/pfsense) |
| | | | | ✓ [OPNsense](https://docs.netbird.io/get-started/install/opnsense) |
| | | | | ✓ [MikroTik RouterOS](https://docs.netbird.io/use-cases/homelab/client-on-mikrotik-router) |
| | | | | ✓ [OpenWrt](https://docs.netbird.io/get-started/install/openwrt) |
| | | | | ✓ [Synology](https://docs.netbird.io/get-started/install/synology) |
| | | | | ✓ [TrueNAS](https://docs.netbird.io/get-started/install/truenas) |
| | | | | ✓ [Unraid](https://docs.netbird.io/get-started/install/unraid) |
| | | | | ✓ [Proxmox](https://docs.netbird.io/get-started/install/proxmox-ve) |
| | | | | ✓ [Raspberry Pi](https://docs.netbird.io/get-started/install/raspberrypi) |
| | | | | ✓ [Serverless](https://docs.netbird.io/how-to/netbird-on-faas) |
| | | | | ✓ [Container](https://docs.netbird.io/get-started/install/docker) |

### Quickstart with NetBird Cloud

- Download and install NetBird at [https://app.netbird.io/install](https://app.netbird.io/install).
- Follow the steps to sign up with Google, Microsoft, GitHub or your email address.
- Check the NetBird [admin UI](https://app.netbird.io/).

### Quickstart with self-hosted NetBird

This is the quickest way to try self-hosted NetBird. It should take around 5 minutes to get started if you already have a public domain and a VM. Follow the [Advanced guide with a custom identity provider](https://docs.netbird.io/selfhosted/selfhosted-guide#advanced-guide-with-a-custom-identity-provider) for installations with different IdPs.

**Infrastructure requirements:**
- A Linux VM with at least **1 CPU** and **2 GB** of memory.
- The VM should be publicly accessible on TCP ports **80** and **443** and UDP port **3478**.
- A **public domain** name pointing to the VM.

**Software requirements:**
- Docker with the Compose plugin (Compose v2 or higher). See the [Docker installation guide](https://docs.docker.com/engine/install/).

**Steps**
- Download and run the installation script:
```bash
export NETBIRD_DOMAIN=netbird.example.com; curl -fsSL https://github.com/netbirdio/netbird/releases/latest/download/getting-started.sh | bash
```

### A bit on NetBird internals
- Every machine in the network runs the [NetBird client](client/), which manages WireGuard.
- Every client connects to the [Management Service](management/), which holds network state, manages peer IPs, and distributes updates to clients.
- Clients use ICE (via [pion/ice](https://github.com/pion/ice)) to discover connection candidates for peer-to-peer connections.
- Candidates are discovered with the help of [STUN](https://en.wikipedia.org/wiki/STUN) servers.
- Clients negotiate a connection through the [Signal Service](signal/), exchanging end-to-end encrypted messages with candidates.
- When NAT traversal fails (e.g. mobile carrier-grade NAT) and a direct p2p connection isn't possible, the system falls back to a [Relay Service](relay/) and a secure WireGuard tunnel is established through it.

<p float="left" align="middle">
  <img src="https://docs.netbird.io/docs-static/img/about-netbird/high-level-dia.png" width="700" alt="NetBird high-level architecture diagram"/>
</p>

See a complete [architecture overview](https://docs.netbird.io/about-netbird/how-netbird-works#architecture) for details.

### Reporting bugs and requesting features

NetBird uses a discussion-first workflow. Bug reports and feature requests start in
[Discussions](https://github.com/netbirdio/netbird/discussions), not as issues.

| What you want to do | Where to go |
| --- | --- |
| Report a bug, regression, or unexpected behavior | [Issue Triage](https://github.com/netbirdio/netbird/discussions/new?category=issue-triage) |
| Request a feature or share an idea | [Ideas & Feature Requests](https://github.com/netbirdio/netbird/discussions/new?category=ideas-feature-requests) |
| Ask about setup, configuration, or self-hosting | [Q&A / Support](https://github.com/netbirdio/netbird/discussions/new?category=q-a-support) |
| Report a security vulnerability | [Security policy](https://github.com/netbirdio/netbird/security/policy), never a public thread |

Our team and maintainers triage discussions, ask follow-up questions, check for duplicates,
and reproduce bugs. Validated reports are promoted to issues. This keeps the issue tracker a clear
answer to one question: what is the team working on.

Please search existing discussions and issues first, including closed ones. If something similar
already exists, upvote it and add your details there instead of opening a duplicate.

For bug reports, include your NetBird version, operating system, deployment type (Cloud,
self-hosted, Kubernetes, or Docker), reproduction steps, expected and actual behavior, and a debug
bundle where relevant:

```shell
netbird version
netbird status -d -A
netbird debug for 1m -A -S -U
```

`-U` uploads the bundle and prints a file key you can paste instead of attaching the archive.
`-A` anonymizes the output, which matters on a public thread. It masks most identifying details
but is not full redaction, so read the bundle before posting it. Two levels are available:

| Level | How to select | What it masks |
| --- | --- | --- |
| `default` | `-A` / `--anonymize` | Public IP addresses, IPv6 ULA addresses, MAC addresses, and domains other than `netbird.io`, `netbird.cloud`, `netbird.selfhosted`, and `netbird.stage`. IPv4 private, CGNAT, and link-local ranges are kept |
| `strict` | `--anonymize-level strict` (implies `-A`) | The above, plus IPv4 private, CGNAT, and link-local ranges, peer names in front of `netbird.cloud`, `netbird.selfhosted`, and `netbird.stage`, and WireGuard public keys. Labels under `netbird.io` are kept, since it only hosts infrastructure |

See [collecting a debug bundle](https://docs.netbird.io/help/troubleshooting-client#debug-bundle)
and the [CLI reference](https://docs.netbird.io/get-started/cli#debug-for) for details.

See [How to use Discussions, Issues, and Pull Requests](https://github.com/netbirdio/netbird/discussions/6075)
for the full workflow, or [SUPPORT.md](SUPPORT.md) for a shorter version.

### Contributing

Contributions are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) first. NetBird works ticket
first, anything that changes behavior needs an issue the team has agreed on before you open a pull
request.

### Community projects
- [NetBird installer script](https://github.com/physk/netbird-installer)
- [netbird-tui](https://github.com/n0pashkov/netbird-tui) - terminal UI for managing NetBird peers, routes, and settings
- [caddy-netbird](https://github.com/lixmal/caddy-netbird) - Caddy plugin that embeds a NetBird client for proxying HTTP and TCP/UDP traffic through NetBird networks

**Note**: The `main` branch may be in an *unstable or even broken state* during development.
For stable versions, see [releases](https://github.com/netbirdio/netbird/releases).

### Support acknowledgement

In November 2022, NetBird joined the [StartUpSecure program](https://www.forschung-it-sicherheit-kommunikationssysteme.de/foerderung/bekanntmachungen/startup-secure) sponsored by the Federal Ministry of Education and Research of the Federal Republic of Germany. Together with the [CISPA Helmholtz Center for Information Security](https://cispa.de/en), NetBird brings security best practices and simplicity to private networking.

![CISPA_Logo_BLACK_EN_RZ_RGB (1)](https://user-images.githubusercontent.com/700848/203091324-c6d311a0-22b5-4b05-a288-91cbc6cdcc46.png)

### Acknowledgements
We build on open source technologies like [WireGuard®](https://www.wireguard.com/), [Pion ICE](https://github.com/pion/ice), and [Rosenpass](https://rosenpass.eu). We greatly appreciate the work these projects are doing, and we'd love it if you could support them too (e.g., by starring or contributing).

### Legal
This repository is licensed under the BSD-3-Clause license, which applies to all parts of the repository except for the directories management/, signal/ and relay/.
Those directories are licensed under the GNU Affero General Public License version 3.0 (AGPLv3). See the respective LICENSE files inside each directory.

_WireGuard_ and the _WireGuard_ logo are [registered trademarks](https://www.wireguard.com/trademark-policy/) of Jason A. Donenfeld.

---

## Irene Vera Foundation: proposed private-access deployment

> **Project status: planning and documentation only.** This section records a proposed use of NetBird Community Edition for the Irene Vera Foundation (IVF). It does not mean that a VPN server has been provisioned, endpoints enrolled, access policies applied, or the Foundation's website secured by this repository.

### Purpose

The Irene Vera Foundation is a UK charitable organisation. Its staff and authorised technical maintainers may need to administer systems from different locations and devices. NetBird can provide an encrypted, identity-aware private network for approved devices, so that access to internal administration services does not depend on exposing those services directly to the public internet.

The intended outcome is a Foundation-controlled remote-access layer with documented ownership, least-privilege access, device lifecycle management, and a clear separation between public services and internal administration.

- Foundation website: https://ireneverafoundation.com/
- Upstream project: https://github.com/netbirdio/netbird
- Upstream documentation: https://docs.netbird.io/

### Why this matters to the Foundation

Without a centrally managed private-access layer, remote administration can become fragmented across individual VPN configurations, changing IP allowlists, direct SSH exposure, shared credentials, and separate firewall exceptions. Those arrangements can be difficult to review consistently when staff, contractors, devices, or responsibilities change.

If an administration interface or server management port is exposed publicly without adequate controls, it may receive unsolicited connection attempts and face a larger attack surface. This is a general risk statement, not a claim that the Foundation's current website or infrastructure has been tested or found vulnerable.

A correctly designed NetBird deployment can reduce the need to expose selected internal services publicly. It can centralise peer identity and access policy, encrypt traffic between enrolled peers, and make it easier to revoke a device or user's network access. It does not, by itself, secure an application or replace the controls described below.

### What NetBird would and would not protect

| Foundation asset or service | Intended treatment |
| --- | --- |
| Public charity website | Keep publicly reachable over HTTPS. NetBird is not a prerequisite for visitors and must not inadvertently place the public site behind a VPN. |
| Website administration | Restrict to authorised maintainers; use NetBird only if the hosting and application architecture support a private administrative path. Retain strong application authentication and MFA. |
| Deployment interfaces and private dashboards | Prefer private access through approved NetBird peers, where technically supported. |
| SSH and server management | Do not expose broadly to the internet. Permit only named administrator groups and required destinations; retain key-based authentication and server hardening. |
| Staff and contractor devices | Enrol only approved, supported devices. Apply role-based policies and remove access promptly when a person or device no longer requires it. |
| Beneficiary, volunteer, staff, or other sensitive information | Apply data minimisation, application-level authorisation, encryption, retention controls, and the Foundation's safeguarding and data-protection procedures. A VPN is not a substitute for these controls. |

### Proposed architecture

The proposed design is a self-hosted NetBird Community Edition control plane on Foundation-controlled infrastructure, subject to an infrastructure and cost review.

1. **Control plane:** NetBird management, signal, and relay services hosted on a Foundation-owned Linux VM or other supported deployment target. The deployment method and resource sizing must be validated against the current upstream self-hosting documentation.
2. **Identity:** Integrate an approved identity provider where supported. Require MFA for user sign-in and use individual identities rather than shared accounts.
3. **Peers:** Enrol Foundation-approved Windows, macOS, and Linux devices, plus mobile devices only where there is a defined operational need and suitable device controls.
4. **Access policy:** Create explicit groups and narrowly scoped rules. Do not grant every enrolled peer unrestricted access to every other peer.
5. **Private services:** Route only the required internal administration and management traffic. Keep public website traffic and public-facing services outside the private overlay unless a separate, reviewed design explicitly requires otherwise.
6. **Operations:** Maintain documented ownership, backups, upgrades, monitoring, recovery procedures, access reviews, and an emergency revocation process.

Illustrative access groups, to be confirmed with the Foundation:

- **IVF Administrators:** control-plane administration and approved infrastructure management.
- **Technical Operations:** only the systems and ports required for assigned operational duties.
- **Website Maintainers:** website administration and deployment endpoints, not general infrastructure access by default.
- **Staff:** only approved internal services required for their role.
- **Development / Contractors:** time-limited, task-specific access to explicitly named resources.
- **Guests:** no access by default; create exceptions only for a documented purpose and expiry date.

These are proposed policy groups, not groups that currently exist in the Foundation's identity provider or NetBird account.

### Security and safeguarding principles

- **Least privilege:** define access by person, device, destination, protocol, and business need. Avoid broad all-to-all rules.
- **Strong identity:** use individual accounts, MFA, and an approved identity provider where feasible. Protect administrator recovery methods.
- **Device trust:** maintain an inventory of enrolled devices, their owners, operating systems, and approval status. Remove lost, retired, compromised, or out-of-scope devices promptly.
- **Foundation ownership:** the Foundation should own the hosting subscription, DNS, domain, administrative identities, backups, and recovery material. Access should not depend on one volunteer's personal account.
- **Separation of duties:** distinguish control-plane administrators from ordinary users and from website maintainers.
- **Data protection:** do not route or store sensitive beneficiary or vulnerable-person data on personal devices merely because a VPN is available. Apply the Foundation's data-protection, safeguarding, and retention policies at the application and device layers.
- **Audit and review:** record administrative changes and review membership and policies regularly. Confirm which logging capabilities are available in the selected Community Edition release and deployment.
- **Incident response:** document how to disable a user, revoke a peer, rotate credentials, isolate a compromised host, restore the control plane, and notify the appropriate Foundation lead.
- **Secure operations:** patch the host and containers, protect secrets, restrict management ports, back up configuration and required state, test restores, and monitor service health.

### Hosting, licensing, and cost

NetBird Community Edition is open-source software, but self-hosting is not automatically cost-free. The Foundation should budget for the VM or hosting platform, public IP and DNS, storage, bandwidth, backups, monitoring, maintenance time, and incident response.

The upstream repository uses more than one licence. Its root licence is BSD-3-Clause, while the `management/`, `signal/`, and `relay/` directories are licensed under AGPLv3, with their own licence files. Other components may have their own notices. Anyone modifying, redistributing, or offering the software as a service must review the applicable licence files and comply with the obligations for the specific components and use case. Do not assume that every file in this repository is covered by one licence.

This repository is a public fork of the upstream project. It is not a private Foundation repository and should not contain Foundation secrets, credentials, private configuration, personal data, production inventories, or sensitive operational details. Keep deployment secrets and environment-specific configuration outside Git, in an appropriately controlled secrets store.

### Delivery plan and acceptance checks

1. **Discovery:** confirm the Foundation's hosting subscription, available VM capacity, DNS ownership, identity provider, endpoint inventory, data flows, and services that genuinely require private access.
2. **Design approval:** agree the threat model, user groups, access matrix, administrator ownership, backup approach, support responsibility, and operating budget with the Foundation.
3. **Pilot:** deploy a non-production instance on Foundation-controlled infrastructure; enrol a small number of approved test devices; validate direct connectivity and relay fallback.
4. **Policy validation:** test both allowed and denied access paths. Confirm that staff and contractor peers cannot reach administrative services outside their role.
5. **Operational readiness:** test account removal, device revocation, credential rotation, backup restoration, upgrade, and control-plane recovery.
6. **Controlled rollout:** migrate approved users and services in stages, with a rollback plan and named operational owner.
7. **Review:** periodically recertify access, remove unused peers and rules, review logs, and reassess hosting costs and security requirements.

The deployment should not be considered production-ready until the Foundation has approved the design, verified the access controls, tested recovery, and assigned ongoing operational ownership.

### Current boundary and project status

This documentation does **not** assert that NetBird is currently deployed for IVF. It does not assert that the Foundation's public website is behind a VPN, that the website is vulnerable, or that any existing Azure resource is suitable for this workload. No production endpoint, domain, secret, tenant identifier, beneficiary information, or private network configuration should be committed here.

The public website should remain available to the public. NetBird is intended to protect selected private administration and infrastructure paths, not to replace public web hosting, HTTPS, a web application firewall or CDN, secure application authentication, patching, backups, monitoring, or safeguarding controls.

### Upstream project and maintenance

This fork builds on the work of the NetBird project and its contributors. Keep upstream copyright notices, licence files, third-party notices, and component-specific licences intact. Review upstream releases and security advisories before updating this fork. Record local changes separately and avoid modifying upstream application code when Foundation-specific deployment documentation or configuration is sufficient.

- Upstream source: https://github.com/netbirdio/netbird
- Self-hosting documentation: https://docs.netbird.io/selfhosted/selfhosted-quickstart
- NetBird architecture: https://docs.netbird.io/about-netbird/how-netbird-works
- NetBird security documentation: https://docs.netbird.io/

---

## Supply-chain security: Dependabot and SBOM automation

This fork adds repository-level dependency maintenance and repeatable source and release-artifact software inventories while retaining NetBird's upstream application code and existing CI workflows.

### Dependabot coverage

The existing upstream Dependabot configuration was reviewed and extended rather than replaced. It now schedules weekly updates for:

| Ecosystem | Coverage | Why it matters |
| --- | --- | --- |
| GitHub Actions | Workflow action references | Keeps CI and automation dependencies maintained |
| Go modules | Root module and `client/internal/metrics/infra/ingest` | Tracks dependencies in both discovered Go modules |
| npm | `client/ui/frontend`, `proxy/web` | Tracks pnpm/npm lockfiles and frontend dependencies |
| Dev Containers | `.devcontainer` configuration | Tracks Dev Container Features |
| Docker / Compose | `.devcontainer`, `client`, `client/internal/metrics/infra`, `client/internal/metrics/infra/ingest`, `client/ui/build/docker`, `combined`, `e2e/harness`, `management`, `proxy`, `relay`, `signal`, `upload-server` | Tracks supported image references in discovered Dockerfiles and Compose manifests |

Updates are grouped to reduce pull-request noise, with bounded open pull requests and retained upstream compatibility exceptions. Dependabot’s Docker support has important limits: it may only update the first `FROM` directive and does not fully support multi-stage Docker builds or image references supplied through `ARG`. Review all Dockerfiles and build arguments manually, and treat the SBOM/vulnerability reports as a complementary control, not proof that every base image is current. See the [Dependabot Docker limitations](https://docs.github.com/en/code-security/how-tos/secure-your-supply-chain/manage-your-dependency-security/configure-private-registries#notes). The configuration follows the repository's discovered manifests: two Go modules, two JavaScript frontend lockfiles (pnpm and npm), the Dockerfile directories, and the discovered Docker Compose manifest present in the source tree. It does not invent ecosystems or nested modules that are not present.

**What Dependabot does:** checks supported manifests and lockfiles for newer dependency versions and opens pull requests. It does not automatically prove that an update is safe, compatible, vulnerability-free, or ready to merge. CI tests, code review, release notes and security review remain necessary.

The SBOM workflow also runs Grype against the generated SPDX inventory and retains a SARIF vulnerability report with the SBOMs. The scan is initially report-only (fail-build: false) so inherited upstream findings can be triaged before a blocking policy is introduced. It is not a substitute for enabling GitHub native dependency alerts and security updates.

Dependabot version updates are also distinct from Dependabot security alerts and security updates. Repository owners should enable dependency graph, Dependabot alerts and Dependabot security updates in GitHub repository settings where available. Those settings are not enabled merely by committing `.github/dependabot.yml`.

### SBOM generation

The workflow `.github/workflows/sbom.yml` uses Anchore Syft through the pinned `anchore/sbom-action` release to inventory the repository source. The existing release workflow also downloads its core and UI build artifacts and generates a separate inventory for the resulting binaries and packages. Both produce SPDX and CycloneDX machine-readable formats:

- **SPDX JSON** — `netbird.spdx.json`
- **CycloneDX JSON** — `netbird.cyclonedx.json`
- **Grype SARIF** — `grype.sarif` and `grype-release.sarif`, vulnerability scan reports generated from the source and release-artifact SPDX SBOMs

The source workflow runs on pushes to `main` and `release-*`, pull requests targeting those branches, manual dispatch, and a weekly schedule. Source SBOMs and the Grype SARIF vulnerability report are uploaded as a commit-specific artifact. The release workflow generates a second artifact for the built core and UI binaries/packages and scans that inventory with Grype as well. Container image definitions also request BuildKit SBOM attestations through GoReleaser; these attestations travel with the OCI image manifest/index rather than being represented as an unrelated source-tree artifact. Both workflow artifact sets are retained for 90 days.

The generated files are workflow artifacts, not committed snapshots. This avoids stale SBOM files being mistaken for the current source inventory. Download the artifact from the relevant workflow run and retain it with the corresponding commit or release evidence.

### What an SBOM does and does not mean

A Software Bill of Materials is a structured inventory of identified components and dependency metadata. It supports supply-chain transparency, licence review, vulnerability triage and incident response.

The source workflow creates a **source-tree SBOM**, while the release workflow creates an inventory of the core and UI binaries/packages produced by its build jobs. These are separate inventories with different scopes. In addition, all 15 GoReleaser `dockers_v2` image definitions explicitly enable BuildKit SBOM attestations (`sbom: true`). Buildx attaches the generated SBOM attestation to the image manifest/index so it can be retrieved and verified against the immutable image digest. This covers the NetBird, rootless, UBI, relay, signal, management, upload, server, proxy and nblink image variants when those images are actually built and published. A fork's CI must not push to upstream NetBird registries or use upstream signing secrets; its release workflow therefore skips publishing and safely skips RPM signing when the fork has no signing key. The OCI SBOM attestation is inventory evidence, not by itself a vulnerability scan or signature. Host operating-system packages, external SaaS services, dynamically downloaded components and customer-specific deployment layers still require deployment-specific assessment.

An SBOM is not a vulnerability scan, penetration test, provenance attestation, signature, or guarantee that the software is secure. A clean SBOM does not mean that a component has no known vulnerabilities.

### Recommended operating process

1. Review each Dependabot pull request and its changelog.
2. Run the relevant tests, build and licence checks before merging.
3. Prioritise security updates based on severity, reachability, exploitability and exposure.
4. Download and retain the SBOM artifact associated with the exact commit or release.
5. Compare SBOM components with vulnerability advisories and investigate affected versions.
6. Retain the release binary/package SBOM and retrieve each published image's BuildKit SBOM attestation by immutable digest; scan the image and record the digest alongside the vulnerability report.
7. Keep dependency alerts, CI results, SBOM artifacts, release provenance and deployment records together as an auditable evidence trail.

### Inspiration and engineering references from this account

The repository's existing structure remains the primary source of truth. During this enhancement, related repositories in the account were inspected for reusable engineering patterns:

- `andiekobbietks/oss-enterprise`: an open-source programme learning resource; its useful lesson is to treat governance and contributor knowledge as durable repository documentation.
- `andiekobbietks/DevOpsEngine`: a Rust infrastructure-engineering project with a lockfile, tests and contribution guidance; its useful lesson is to preserve reproducible dependency state and explicit contribution practices.
- `andiekobbietks/device-networking-hub`: a networking-oriented application scaffold; it is contextual inspiration, not a security or supply-chain benchmark.

These repositories were not treated as proof of an established SBOM or Dependabot implementation. The automation here is based on the actual NetBird manifests and workflows, with pinned action references and generated evidence.

### Files introduced or extended

- `.github/dependabot.yml` — expanded weekly ecosystem, Go module, frontend, Dev Container, Dockerfile and Compose update coverage.
- `.github/workflows/sbom.yml` — scheduled and event-driven SPDX and CycloneDX source SBOM generation plus Grype vulnerability reporting.
- `.github/workflows/release.yml` — an additive release job that inventories the core and UI binaries/packages built by the existing release jobs, plus fork-safe RPM signing behavior.
- `.goreleaser.yaml` — explicit BuildKit SBOM attestations for every `dockers_v2` container image definition.

No dependency versions in `go.mod` or `go.sum` are changed by this documentation and automation enhancement.
