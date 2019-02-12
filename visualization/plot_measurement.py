import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import generate_experimentId
import group_plot

def plot_measurementdata(DataFilePath, ConditionFilePath):
    '''
    plot measurement data grouped by variable ID

    Parameters:
    ----------

    DataFilePath: string, file path of measurement data
    ConditionFilePath: string, file path of condition file

    Return:
    ----------

    axis: axis of figures
    '''

    # import measurement data
    measurement_data = pd.DataFrame.from_csv(
        DataFilePath, sep="\t", index_col=None)
    # import experimental condition
    experimental_condition = pd.DataFrame.from_csv(
        ConditionFilePath, sep="\t")
    # check if there is experimentId in the data frame, if not, generate
    if not hasattr(measurement_data, 'experimentId'):
        measurement_data = generate_experimentId.generate_experimentId(measurement_data)
        print('experimentId does not exist, generating!')

    ax = group_plot.group_plot(measurement_data, experimental_condition)
    return ax