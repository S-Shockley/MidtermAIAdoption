import pandas as pd


def load_ai_data():
    """
    Loads AI adoption project datasets.

    Returns:
        df_company, df_industry, df_country
    """

    df_company = pd.read_csv("../data/company.csv")

    df_industry = pd.read_csv("../data/industry.csv")

    df_country = pd.read_csv("../data/country.csv")

    return (df_company,df_industry,df_country)


if __name__ == "__main__":
    company, industry, country = load_ai_data()

    print(company.head())
    print(industry.head())
    print(country.head())