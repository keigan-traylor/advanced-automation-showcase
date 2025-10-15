# High Level AWS Tag Compliance Automation Script 

**Purpose:** Demonstrates cloud automation for governance — discovering AWS resources, evaluating tag compliance, generating remediation playbooks, and visualizing resource states across accounts/regions.

**Key concepts demonstrated:**
- Basic inventory analysis and compliance rules engine
- Automated remediation plan generation (IaC/playbook style)
- Simple visualization of resource ownership and compliance rates
- Logging, config-driven behavior, and testable modules

**How it works:**
- `sample_data/aws_inventory.json` contains mocked EC2, S3, RDS resources with tags and metadata.
- `analyze.py` loads inventory, applies compliance policy (required tags: Owner, Project, Environment), produces:
  - `reports/compliance_report.csv`
  - `reports/compliance_dashboard.png`
  - `playbooks/remediation_playbook.yaml` (simulated actions)

**Run (locally without any AWS Credintials):**
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python analyze.py sample_data/aws_inventory.json
```

**Files:**
- `analyze.py` — main analysis script
- `policy.py` — policy engine with remediation logic
- `visualize.py` — dashboard generation (matplotlib)
- `sample_data/aws_inventory.json` — Sample created inventory
- `requirements.txt`

**Real world application:**
- You can replace `sample_data` loader with your real `boto3` inventory calls 
