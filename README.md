# Stripe Cohort Analysis

__Are you retaining customers? Do you have - OMG - [negative churn](https://www.profitwell.com/blog/how-to-achieve-negative-churn-and-why-it-matters)? Are your hands sweating in anticipation? Let's find out! Now!__

The `stripe_cohort_analysis.py` Python script generates 2 heatmaps of Stripe Customer Cohorts:

1. Customer retention over time
2. Revenue retention over time

Heatmaps are saved as PNGs in the current working directory (`total_customers_heatmap.png` and `amount_due_heatmap.png`, respectively).

Heavily inspired by Greg Reda's [Cohort Analysis with Python](http://www.gregreda.com/2015/08/23/cohort-analysis-with-python/). Seriously - he did like almost all the work.

![stripe cohorts](https://cdn-images-1.medium.com/max/1600/1*_lR0k3U8l26Mjc9xFV_ulw.png)


## Usage

```
STRIPE_API_KEY=[YOUR API KEY] python stripe_cohort_analysis.py
```

## Downloading Invoices

[PetalData](https://petaldata.app) is used to download invoices from Stripe.

## Questions? 

Email derek@petaldata.app.
