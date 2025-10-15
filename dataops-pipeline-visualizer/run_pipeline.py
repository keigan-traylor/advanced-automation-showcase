# run_pipeline.py - Mock ETL + visualization
import sys, joblib, os
from pathlib import Path
import pandas as pd
from sklearn.ensemble import IsolationForest
import plotly.express as px

OUT = Path('artifacts'); OUT.mkdir(exist_ok=True)

def ingest(path):
    df = pd.read_csv(path, parse_dates=['timestamp'])
    return df

def validate(df):
    # basic validation: no negative values
    issues = []
    if (df[['cpu','mem','net_in','net_out']] < 0).any().any():
        issues.append('Negative values detected')
    return issues

def transform(df):
    # aggregate per minute and compute means
    agg = df.groupby(['timestamp','host']).mean().reset_index()
    return agg

def detect_anomalies(df):
    model = IsolationForest(contamination=0.02, random_state=42)
    X = df[['cpu','mem','net_in','net_out']].fillna(0)
    model.fit(X)
    preds = model.predict(X)
    df['anomaly'] = preds == -1
    joblib.dump(model, OUT / 'isolation_model.pkl')
    df[df['anomaly']].to_csv(OUT / 'anomalies.csv', index=False)
    return df

def visualize(df):
    fig = px.line(df, x='timestamp', y='cpu', color='host', title='CPU Utilization by Host (Mock)')
    fig.write_html(OUT / 'cpu_dashboard.html', include_plotlyjs='cdn')

def main(path):
    df = ingest(path)
    issues = validate(df)
    if issues:
        print('Validation issues:', issues)
    transformed = transform(df)
    analyzed = detect_anomalies(transformed)
    visualize(analyzed)
    print('Artifacts written to', OUT)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python run_pipeline.py sample_data/telemetry.csv')
    else:
        main(sys.argv[1])
