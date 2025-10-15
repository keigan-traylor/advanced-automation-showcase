# AWS Tag Compliance Automator (Simulated)

**Purpose:** Demonstrates cloud automation for governance — discovering AWS resources, evaluating tag compliance, generating remediation playbooks, and visualizing resource state across accounts/regions.

**Key concepts demonstrated:**
- Inventory analysis and compliance rules engine
- Automated remediation plan generation (IaC/playbook style)
- Visualization of resource ownership and compliance rates
- Robust logging, config-driven behavior, and testable modules

**How it works (local, simulated):**
- `sample_data/aws_inventory.json` contains mocked EC2, S3, RDS resources with tags and metadata.
- `analyze.py` loads inventory, applies compliance policy (required tags: Owner, Project, Environment), produces:
  - `reports/compliance_report.csv`
  - `reports/compliance_dashboard.png`
  - `playbooks/remediation_playbook.yaml` (simulated actions)

**Run (local, no AWS credentials required):**
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python analyze.py sample_data/aws_inventory.json
```

**Files:**
- `analyze.py` — main analysis script
- `policy.py` — policy engine and remediation logic
- `visualize.py` — dashboard generation (matplotlib)
- `sample_data/aws_inventory.json` — mocked inventory
- `requirements.txt`

**Employer talking points:**
- Explain how this translates to real AWS: replace `sample_data` loader with `boto3` inventory calls (DescribeInstances, ListBuckets, DescribeDBInstances), add role-based remediation via SSM/Step Functions, and integrate with Service Catalog/Governance tooling.
