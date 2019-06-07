import petaldata
import pandas as pd
from datetime import datetime
from datetime import date
import seaborn as sns
sns.set(style='white')
import numpy as np
import matplotlib.pyplot as plt

def download_or_use_cached_invoices():
    invoices = petaldata.datasets.stripe.Invoices()
    if invoices.df is None:
        invoices.download()
        invoices.save()

    df = invoices.df
    # change from cents to dollars
    df.amount_due = df.amount_due/100
    # exclude the current, incomplete month.
    df = df[df.created < (datetime.utcnow() - pd.offsets.MonthBegin()).normalize().tz_localize("UTC")]

    return df

def cohort_period(df):
    """
    Creates a `cohort_period` column, which is the Nth period based on the customer's first invoice.
    
    Example
    -------
    Say you want to get the 3rd month for every customer:
        df.sort(['customer', 'created', inplace=True)
        df = df.groupby('customer').apply(cohort_period)
        df[df.cohort_period == 3]
    """
    df['cohort_period'] = np.arange(len(df)) + 1
    return df

def cohort_heatmap(cohorts,col,title):
    size = group_size(cohorts,col)
    over_time = cohort_over_time(cohorts,size,col)
    _cohort_heatmap(over_time,title)
    plt.savefig(col+"_heatmap")
    
def group_size(cohorts,col):
    # reindex the DataFrame
    cohorts.reset_index(inplace=True)
    cohorts.set_index(['cohort_group', 'cohort_period'], inplace=True)

    # create a Series holding the total size of each cohort_group
    return cohorts[col].groupby(level=0).first()

def cohort_over_time(cohorts,group_size,col):
    return cohorts[col].unstack(0).divide(group_size, axis=1)

def _cohort_heatmap(cohort_over_time,title):
    # Creating heatmaps in matplotlib is more difficult than it should be.
    # Thankfully, Seaborn makes them easy for us.
    # http://stanford.edu/~mwaskom/software/seaborn/
    plt.figure(figsize=(24, 16))
    plt.title(title)
    sns.heatmap(cohort_over_time.T, mask=cohort_over_time.T.isnull(), annot=True, fmt='.0%');