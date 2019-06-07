# Stripe Cohort Analysis

The `stripe_cohort_analysis.py` Python script generates 2 heatmaps of Stripe Customer Cohorts showing customer and revenue retention over time. Heatmaps are saved as PNGs in the current working directory (total_customers_heatmap amount_due_heatmap.png, respectively).

Heavily inspired by Greg Reda's [Cohort Analysis with Python](http://www.gregreda.com/2015/08/23/cohort-analysis-with-python/).

![stripe cohorts](https://cdn-images-1.medium.com/max/1600/1*_lR0k3U8l26Mjc9xFV_ulw.png)


## Usage

```
STRIPE_API_KEY=[YOUR API KEY] python stripe_cohort_analysis.py
```

## Downloading Invoices

[PetalData](https://petaldata.app) is used to download invoices from Stripe.

## Questions? 

Email derek@petaldata.app.
