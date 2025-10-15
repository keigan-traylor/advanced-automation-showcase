# visualize.py - generate compliance dashboard (matplotlib)
import matplotlib.pyplot as plt

def generate_dashboard(df, outpath):
    # simple compliance rate by resource type
    df['compliant'] = df['missing'].apply(lambda x: 1 if x=='' else 0)
    summary = df.groupby('type')['compliant'].agg(['sum','count'])
    summary['rate'] = summary['sum'] / summary['count']
    fig, ax = plt.subplots(figsize=(6,4))
    summary['rate'].plot(kind='bar', ax=ax)
    ax.set_ylim(0,1)
    ax.set_ylabel('Compliance Rate')
    ax.set_title('Tag Compliance Rate by Resource Type')
    fig.tight_layout()
    fig.savefig(outpath)
