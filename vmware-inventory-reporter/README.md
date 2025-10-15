# VMware Inventory Reporter (Simulated)

**Purpose:** Demonstrates virtualization automation and reporting for vSphere environments: inventory parsing, risk detection (orphans, snapshots, power state drift), automated remediation suggestions, and technical/ executive reporting.

**Key concepts demonstrated:**
- Inventory model parsing and analysis
- Risk scoring algorithm and prioritized remediation guidance
- HTML technical report generation and PNG visualizations
- Simulation-friendly design so recruiters can run locally

**Run (local):**
```bash
pip install -r requirements.txt
python vmware_report.py sample_data/vm_inventory.json
```
