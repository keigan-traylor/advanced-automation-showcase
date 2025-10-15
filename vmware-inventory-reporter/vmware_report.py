# vmware_report.py - analyze VM inventory and produce HTML report
import json, sys
from pathlib import Path
import pandas as pd
from jinja2 import Template
import matplotlib.pyplot as plt

REPORT_DIR = Path('reports'); REPORT_DIR.mkdir(exist_ok=True)

def risk_score(vm):
    score = 0
    if vm.get('power_state') != 'poweredOn':
        score += 5
    snaps = vm.get('snapshots',0)
    score += min(snaps,10)
    if not vm.get('host'):
        score += 20  # orphan severity
    if vm.get('disks_gb',0) > 200:
        score += 3
    return score

def generate_plots(df):
    fig, ax = plt.subplots(figsize=(6,4))
    df_sorted = df.sort_values('risk', ascending=False).head(10)
    df_sorted.plot.bar(x='name', y='risk', ax=ax, legend=False)
    ax.set_ylabel('Risk Score')
    ax.set_title('Top VM Risk Scores')
    fig.tight_layout()
    fig.savefig(REPORT_DIR / 'vm_risk_scores.png')

def generate_html_report(df, outpath):
    tmpl = Template("""
    <html><head><title>VMware Inventory Report</title></head><body>
    <h1>VMware Inventory Report</h1>
    <h2>Summary</h2>
    <p>Total VMs: {{ total }}</p>
    <img src="vm_risk_scores.png" alt="risk chart"/>
    <h2>Top Risk VMs</h2>
    <table border="1"><tr><th>Name</th><th>Host</th><th>Power</th><th>Snapshots</th><th>Disks(GB)</th><th>Risk</th></tr>
    {% for r in rows %}<tr><td>{{ r.name }}</td><td>{{ r.host or 'N/A' }}</td><td>{{ r.power_state }}</td><td>{{ r.snapshots }}</td><td>{{ r.disks_gb }}</td><td>{{ r.risk }}</td></tr>{% endfor %}
    </table>
    </body></html>
    """)
    html = tmpl.render(total=len(df), rows=df.sort_values('risk', ascending=False).to_dict('records'))
    Path(outpath).write_text(html)

def main(inventory):
    inv = json.loads(Path(inventory).read_text())
    df = pd.DataFrame(inv['vms'])
    df['risk'] = df.apply(risk_score, axis=1)
    df.to_csv(REPORT_DIR / 'vm_inventory_report.csv', index=False)
    generate_plots(df)
    generate_html_report(df, REPORT_DIR / 'vm_inventory_report.html')
    print('VM report generated in', REPORT_DIR)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python vmware_report.py sample_data/vm_inventory.json')
    else:
        main(sys.argv[1])
