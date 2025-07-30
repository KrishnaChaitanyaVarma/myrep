# Water Quality Prediction for Aquaculture

This project predicts water quality based on few parameters in the datset using a Voting Ensemble model deployed on Azure Machine Learning Studio.

## Features
- Real-time prediction via REST API
- Built with Azure ML Studio and Python
- Uses public dataset from [Mendeley Data](https://data.mendeley.com/datasets/y78ty2g293/1)

## Steps
1. Prepare dataset and upload to Azure ML Studio
2. Train Voting Ensemble model
3. Deploy model as real-time endpoint
4. Model predicts water quality levels—0 (Excellent), 1 (Good), 2 (Poor)—based on parameters such as Temperature, Turbidity, DO, BOD, CO₂, pH, Alkalinity, Hardness, Calcium, Ammonia, Nitrite, Phosphorus, H₂S, and Plankton count.
5. Use Python script to send prediction requests

## Setup
- Store API key and endpoint in `.env` file
- Run `inference_script.py` to test predictions

## Author
PENMETSA Krishna Chaithanya Varma
