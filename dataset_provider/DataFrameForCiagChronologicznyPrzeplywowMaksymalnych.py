import pandas as pd


def provide(dataset_for_years, years_range):
    max_Q_by_years = pd.Series()

    for current_year in years_range:
        max_Q_by_years.loc[current_year] = dataset_for_years[current_year]['Q'].max()
    return max_Q_by_years
