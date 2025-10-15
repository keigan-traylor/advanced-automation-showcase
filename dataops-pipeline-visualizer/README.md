# DataOps Pipeline Visualizer (Mock ETL)

**Purpose:** Demonstrates an end-to-end data engineering automation and visualization workflow: data ingestion, validation, transformation, quality checks, and interactive visualization artifacts for stakeholders.

**Key concepts demonstrated:**
- Automated ETL orchestration (scripted, idempotent steps)
- Data quality gates and anomaly detection
- Output of analysis to interactive HTML dashboards (Plotly)
- Production-aware design: config-driven, logging, and artifacts versioning

**Run (local):**
```bash
pip install -r requirements.txt
python run_pipeline.py sample_data/telemetry.csv
```
