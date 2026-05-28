#!/usr/bin/env bash
# init-pantheon-dir.sh
# Initializes .pantheon/ directory at workspace root with empty state.json.

set -euo pipefail

PANTHEON_DIR=".pantheon"

if [ -d "$PANTHEON_DIR" ]; then
    echo "[PANTHEON] .pantheon/ already exists. Use /pantheon:reset to archive and start fresh." >&2
    exit 1
fi

mkdir -p "$PANTHEON_DIR/findings"
mkdir -p "$PANTHEON_DIR/pocs"
mkdir -p "$PANTHEON_DIR/phase-outputs"

AUDIT_ID=$(uuidgen 2>/dev/null || python3 -c 'import uuid; print(uuid.uuid4())')
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

cat > "$PANTHEON_DIR/state.json" <<EOF
{
  "schema_version": "1.0.0",
  "audit_id": "$AUDIT_ID",
  "started_at": "$TIMESTAMP",
  "updated_at": "$TIMESTAMP",
  "scope": {
    "project_name": "",
    "scope_description": "",
    "exclusions": [],
    "geographic_scope": [],
    "industry": "",
    "compliance_frameworks_in_scope": []
  },
  "current_phase": 0,
  "phases": {
    "0": {"status": "pending"},
    "1": {"status": "pending"},
    "2": {"status": "pending"},
    "3": {"status": "pending"},
    "4": {"status": "pending"},
    "5": {"status": "pending"},
    "6": {"status": "pending"},
    "7": {"status": "pending"},
    "8": {"status": "pending"},
    "9": {"status": "pending"},
    "10": {"status": "pending"},
    "11": {"status": "pending"},
    "12": {"status": "pending"}
  },
  "findings": [],
  "maturity_scorecard": {},
  "deliverables_generated": false,
  "deliverables_path": "",
  "launch_decision": "PENDING"
}
EOF

cp "$PANTHEON_DIR/state.json" "$PANTHEON_DIR/state.json.backup"

# PANTHEON-0014 mitigation: ensure local .gitignore excludes the audit directory.
# The .pantheon/ tree stores exploitation guidance for the audit subject until
# remediation. Accidentally committing or cloud-syncing it leaks third-party harm.
if [ -d .git ] || [ -f .gitignore ]; then
    if ! grep -qE '^\.pantheon/?$|^/\.pantheon/?$' .gitignore 2>/dev/null; then
        printf '\n# PANTHEON audit state (contains exploitation guidance until remediation; do not commit or cloud-sync)\n.pantheon/\n' >> .gitignore
        echo "[PANTHEON] Appended .pantheon/ to .gitignore (audit state must not be committed)" >&2
    fi
fi

echo "[PANTHEON] Initialized .pantheon/ at $(pwd). Audit ID: $AUDIT_ID"
echo "[PANTHEON] Reminder: .pantheon/ and ~/Downloads/pantheon-audit-${AUDIT_ID}/ contain exploitation guidance until remediation. Exclude both from cloud-sync (iCloud, Google Drive, OneDrive, Dropbox). See plugins/pantheon/references/ethics-disclaimer.md." >&2
