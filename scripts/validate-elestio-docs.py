#!/usr/bin/env python3
"""Guard the fork-specific Elestio deployment guide against broken local links and unsafe status claims."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

def require(condition: bool, message: str) -> None:
    if not condition:
        print(f"FAIL: {message}", file=sys.stderr)
        raise SystemExit(1)
    print(f"PASS: {message}")

readme = (ROOT / "README.md").read_text(encoding="utf-8")
guide_path = ROOT / "elestio.md"
guide = guide_path.read_text(encoding="utf-8")
adr_index = (ROOT / "docs/adr/README.md").read_text(encoding="utf-8")
adr_path = ROOT / "docs/adr/0013-use-elestio-byovm-only-after-network-validation.md"

require(guide_path.is_file(), "Elestio deployment guide exists")
require("[Elestio BYOVM deployment guide](elestio.md)" in readme, "README links to the Elestio guide")
require(".github/workflows/elestio-validation.yml" in readme, "README links to Elestio validation CI")
require(".github/workflows/elestio-deploy.yml" in readme, "README links to manual Elestio CD")
require(adr_path.is_file(), "Elestio networking ADR exists")
require("0013-use-elestio-byovm-only-after-network-validation.md" in adr_index, "ADR index includes ADR-0013")

ci_workflow_path = ROOT / ".github/workflows/elestio-validation.yml"
cd_workflow_path = ROOT / ".github/workflows/elestio-deploy.yml"
require(ci_workflow_path.is_file(), "Elestio CI workflow exists")
require(cd_workflow_path.is_file(), "Elestio CD workflow exists")
cd_workflow = cd_workflow_path.read_text(encoding="utf-8")
for marker in (
    "workflow_dispatch",
    "refs/heads/main",
    "inputs.confirm_deploy",
    "environment: elestio-production",
    "ELESTIO_API_TOKEN",
    "ELESTIO_VM_ID",
    "ELESTIO_PIPELINE_ID",
    "elestio cicd pipeline-restart",
    "elestio-validation.yml",
):
    require(marker in cd_workflow, f"CD retains required deployment guard: {marker}")

for phrase in (
    "conditional GO",
    "not yet validated on an Elestio BYOVM host",
    "UDP 3478",
    "TCP 443",
    "Do not start the default NetBird Traefik stack unchanged",
    "underlying cloud VM",
):
    require(phrase.casefold() in guide.casefold(), f"guide retains required deployment caveat: {phrase}")

# Verify the README's fork-specific relative links used by this deployment guide.
for relative in ("elestio.md", "docs/adr/README.md"):
    require((ROOT / relative).is_file(), f"README target exists: {relative}")

print("Elestio documentation validation completed.")
