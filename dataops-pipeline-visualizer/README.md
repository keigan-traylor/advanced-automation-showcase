# Sample DataOps Pipeline Visualizer 

**Purpose:** Demonstrates an end-to-end data engineering automation and visualization workflow: data ingestion, validation, transformation, quality checks, and interactive visualization.

**Key concepts demonstrated:**
- Automated ETL orchestration 
- Data quality gates and simple anomaly detection
- Output to interactive HTML dashboards (Plotly)
- Production-aware design: config-driven, logging, and artifacts versioning

**Run (locally):**
```bash
pip install -r requirements.txt
python run_pipeline.py sample_data/telemetry.csv
```
