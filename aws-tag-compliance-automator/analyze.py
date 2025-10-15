# analyze.py - AWS Tag Compliance Automator (simulated)
import sys, json, csv, os
from pathlib import Path
import pandas as pd
from policy import evaluate_resource, remediation_actions
from visualize import generate_dashboard

REPORT_DIR = Path('reports')
PLAYBOOK_DIR = Path('playbooks')
REPORT_DIR.mkdir(exist_ok=True)
PLAYBOOK_DIR.mkdir(exist_ok=True)

def flatten_resources(inv):
    items = []
    for ec2 in inv.get('ec2', []):
        items.append({'type':'ec2','id':ec2['id'],'region':ec2['region'],'tags':ec2.get('tags',{}),'state':ec2.get('state')})
    for s3 in inv.get('s3', []):
        items.append({'type':'s3','id':s3['name'],'region':s3['region'],'tags':s3.get('tags',{})})
    for r in inv.get('rds', []):
        items.append({'type':'rds','id':r['id'],'region':r['region'],'tags':r.get('tags',{})})
    return items

def main(inventory_file):
    inv = json.loads(Path(inventory_file).read_text())
    items = flatten_resources(inv)
    rows = []
    playbook = []
    for r in items:
        missing, present = evaluate_resource(r)
        rows.append({'resource':r['id'],'type':r['type'],'region':r.get('region'),'missing':','.join(missing),'present':','.join(present)})
        actions = remediation_actions(r, missing)
        if actions:
            playbook.extend(actions)
    df = pd.DataFrame(rows)
    df.to_csv(REPORT_DIR / 'compliance_report.csv', index=False)
    # generate visualization
    generate_dashboard(df, REPORT_DIR / 'compliance_dashboard.png')
    # write playbook
    import yaml
    Path(PLAYBOOK_DIR / 'remediation_playbook.yaml').write_text(yaml.dump(playbook))
    print('Reports written to', REPORT_DIR, 'and', PLAYBOOK_DIR)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python analyze.py sample_data/aws_inventory.json')
    else:
        main(sys.argv[1])
