# Usage:
# STRIPE_API_KEY=[YOUR API KEY] python stripe_cohort_analysis.py
#
# Generates 2 heatmaps of Stripe Customer Cohorts showing customer and revenue retention over time. 
# Heatmaps are saved as PNGs in the current working directory (total_customers_heatmap amount_due_heatmap.png, respectively).

import petaldata
import pandas as pd
import numpy as np
import os
from utils import *

# https://stripe.com/docs/keys#api-keys
petaldata.datasets.stripe.api_key = os.getenv("STRIPE_API_KEY")

df = download_or_use_cached_invoices()

# Create period column
df['invoice_period'] = df.created.apply(lambda x: x.strftime('%Y-%m'))

# Customer cohort group
df.set_index('customer_email', inplace=True)
df['cohort_group'] = df.groupby(level=0)['created'].min().apply(lambda x: x.strftime('%Y-%m'))
df.reset_index(inplace=True)

# Rollup data by cohort_group & invoice_period
grouped = df.groupby(['cohort_group', 'invoice_period'])

# count the unique customers, invoices, and total revenue per Group + Period
cohorts = grouped.agg({'customer': pd.Series.nunique,
                       'created': "count",
                       'amount_due': np.sum})

# make the column names more meaningful
cohorts.rename(columns={'customer': 'total_customers',
                        'created': 'total_invoices'}, inplace=True)

# Label the cohort_period for each cohort_group
cohorts = cohorts.groupby(level=0).apply(cohort_period)
cohorts.head()

cohort_heatmap(cohorts,"total_customers","Customer Retention")
cohort_heatmap(cohorts,"amount_due","Revenue Retention")
