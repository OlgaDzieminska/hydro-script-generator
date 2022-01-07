import numpy as np
import pandas as pd


def provide(dataset_for_years, years_range):
    max_Q_with_probability_by_years = pd.DataFrame(columns=['max_Q'])

    for current_year in years_range:
        max_Q_with_probability_by_years.loc[current_year] = dataset_for_years[current_year]['Q'].max()

    max_Q_with_probability_by_years = max_Q_with_probability_by_years.sort_values(by=['max_Q'], ascending=False)

    probabilities = []

    number_of_years = len(years_range)
    for i in range(1, number_of_years + 1):
        probability = round(100 * i / (number_of_years + 1), 2)
        probabilities = np.append(probabilities, probability)

    max_Q_with_probability_by_years['probability'] = probabilities

    return max_Q_with_probability_by_years
