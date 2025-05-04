import streamlit as st
import pandas as pd
import os

# For sensitive data, better aproach is to load data from object storage (AWS S3, Azure Blob, MinIO etc.) and API keys from environment variables.

# When loading environment variables (if needed, for exmple with docker)
# from dotenv import load_dotenv

# load_dotenv()
# dataset_path = os.getenv('dataset_path')
dataset_path = "./app/data/"

# Below mapping can be transferred to a config file or a database for better maintainability (mounted volumes in docker)
COLUMN_ALIGNMENT_MAPPING = {
    "GDP per capita": "Economy (GDP per Capita)",
    "Social support": "Family",
    "Healthy life expectancy": "Health (Life Expectancy)",
    "Freedom to make life choices": "Freedom",
    "Perceptions of corruption": "Trust (Government Corruption)",
    "Country or region": "Country",
    "Score": "Happiness Score",
    "Hapiness Score": "Happiness Score",
    "Hapiness Rank": "Happiness Rank",
    "Overall rank": "Happiness Rank",
    "Happiness.Score": "Happiness Score",
    "Happiness.Rank": "Happiness Rank",
    "Economy..GDP.per.Capita.": "Economy (GDP per Capita)",
    "Health..Life.Expectancy.": "Health (Life Expectancy)",
    "Trust..Government.Corruption.": "Trust (Government Corruption)",
}

COUNTRY_ALIGNMENT_MAPPING = {
    "North Cyprus": "Northern Cyprus",
    "Taiwan Province of China": "Taiwan",
    "Hong Kong S.A.R., China": "Hong Kong",
    "Trinidad and Tobago": "Trinidad & Tobago",
    "Macedonia": "North Macedonia",
}


def load_data(dataset_path: str) -> dict:
    """
    Load datasets from the specified path and return a dictionary of DataFrames.
    """
    datasets = {}
    for filename in os.listdir(dataset_path):
        if filename.endswith(".csv"):
            year = int(filename.split(".")[0])
            datasets[year] = pd.read_csv(os.path.join(dataset_path, filename))
    return datasets


def prepare_data(datasets_dict: dict) -> pd.DataFrame:
    """
    Prepare the data by renaming columns, aligning country names, cleaning and merging the DataFrames.
    """
    global COLUMN_ALIGNMENT_MAPPING, COUNTRY_ALIGNMENT_MAPPING

    # initialize the DataFrame with the correct columns
    df = pd.DataFrame(
        columns=[
            "Year",
            "Country",
            "Region",
            "Happiness Score",
            "Happiness Rank",
            "Economy (GDP per Capita)",
            "Family",
            "Health (Life Expectancy)",
            "Freedom",
            "Trust (Government Corruption)",
            "Generosity",
        ]
    )
    region_mapping = {}
    for year, dataset in datasets_dict.items():
        # Rename columns
        dataset["Year"] = year
        for column in dataset.columns:
            if column in COLUMN_ALIGNMENT_MAPPING.keys():
                dataset.rename(
                    columns={column: COLUMN_ALIGNMENT_MAPPING[column]}, inplace=True
                )

        # Align country names
        dataset.loc[
            dataset["Country"].isin(COUNTRY_ALIGNMENT_MAPPING.keys()), "Country"
        ] = dataset["Country"].map(COUNTRY_ALIGNMENT_MAPPING)

        # Align region names
        if "Region" in dataset.columns:
            region_mapping.update(dict(zip(dataset["Country"], dataset["Region"])))

        # Fill missing values in "Happiness Rank" based on "Happiness Score"
        if "Happiness Rank" in dataset.columns:
            if dataset.loc[dataset["Happiness Rank"].isna(), "Happiness Rank"].any():
                dataset.sort_values(by="Happiness Score", ascending=False, inplace=True)
                dataset["Happiness Rank"] = range(1, len(dataset) + 1)

        # Align decimal values
        dataset["Happiness Rank"] = dataset["Happiness Rank"].astype(int)
        for col in [
            "Happiness Score",
            "Economy (GDP per Capita)",
            "Family",
            "Health (Life Expectancy)",
            "Freedom",
            "Trust (Government Corruption)",
            "Generosity",
        ]:
            dataset[col] = dataset[col].astype(float).round(3)

        dataset = dataset[[col for col in df.columns if col in dataset.columns]]
        df = pd.concat([df, dataset], ignore_index=True)

    # Get the set of common countries across all datasets
    common_countries = set(list(datasets_dict.values())[0]["Country"]).intersection(
        *[set(dataset["Country"]) for dataset in datasets_dict.values()]
    )

    # Filter the DataFrame to include only common countries
    df = df[df["Country"].isin(common_countries)]

    # Fill missing values in "Region" based on the mapping
    df.loc[df["Region"].isna(), "Region"] = df.loc[df["Region"].isna(), "Country"].map(
        region_mapping
    )

    return df


@st.cache_data
def get_data() -> pd.DataFrame:
    """
    Load and prepare the DataFrame.
    """
    global dataset_path
    # Load the data from the specified path
    df_dict = load_data(dataset_path)
    # Prepare the data by renaming columns, aligning country names, and merging DataFrames
    df = prepare_data(df_dict)
    # Reset the index of the DataFrame
    df.reset_index(drop=True, inplace=True)
    # Return the prepared DataFrame
    return df
