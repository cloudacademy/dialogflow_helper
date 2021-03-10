#!/bin/bash

set -x
/opt/conda/bin/python -m venv /app/env
PATH="/app/env/bin:$PATH"

cd /repo
GCP_PROJECT=$(gcloud config get-value project) python3 -c "import dialogflow_helper; dialogflow_helper.teardown()"
