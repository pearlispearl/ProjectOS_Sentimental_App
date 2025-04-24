# ProjectOS_Sentimental_App

## Explanation
- `_FinalProject_OS_Sentimental.ipynb` : This notebook contains the initial implementation of the project, developed and tested within the Google Colaboratory environment prior to operating system optimization.
- `_FinalProject_OS_Sentimental_Polar.ipynb` : This notebook represents the optimized version of the project, utilizing the Polars DataFrame library for enhanced performance within a Jupyter Notebook environment.

## Tutorial
To execute this project, please follow these steps:
1. Download all file included in the `ProjectOS_Sentimental_App` directory.
2. Open file by using Jupyter Notebook or Google Colaboratory **(Recommend to use Google Colab)**.
3. Make sure you download the sentimentdataset.csv to your file and correctly put the path.
4. Before running the notebook, ensure that you uncomment all `!pip` commands to install the necessary libraries.
5. Execute the notebooks in the following order: first, `_FinalProject_OS_Sentimental.ipynb` (Before OS optimization) with the correct file paths to the `sentimentdataset.csv` (Dataset) and `app_sentiment.py` (App using streamlit by uncomment the command !streamlit run app_sentiment.py) , followed by the notebook `_FinalProject_OS_Sentimental_Polar.ipynb` (Code after OS optimization).
