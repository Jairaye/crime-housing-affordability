# Can a Single Person Live Comfortably on $100K Across U.S. Metros?

## Project Overview

This project evaluates whether a single individual earning $100,000 gross annually can live comfortably across U.S. metropolitan areas. The analysis accounts for housing costs, federal and payroll taxes, non housing expenses, and a savings target using recent Zillow housing data and U.S. Census metropolitan population data.

Rather than relying on anecdotes or city level stereotypes, the goal is to quantify where $100K works, where it requires tradeoffs, and where it genuinely falls short.

---

## Core Question

**Is $100,000 enough to support a comfortable adult lifestyle for a single person in most U.S. metros, or only in a shrinking minority of places?**

---

## Methodology Summary

### Geography

- Analysis is conducted at the metropolitan area level.
- This avoids distortions from tiny towns or hyper local neighborhoods while reflecting real housing markets.

### Housing Data

- Zillow Home Value Index (ZHVI)
- Zillow Observed Rent Index (ZORI)
- Most recent available month used consistently across datasets
- Extreme high and low tiers filtered to reflect typical market conditions

### Income and Taxes

- Gross income modeled at $100,000 annually
- Federal income tax modeled using an effective rate
- Payroll taxes (Social Security and Medicare) included
- State income taxes intentionally excluded from the baseline to isolate housing market effects

### Non Housing Costs

A fixed monthly allowance is assumed for:
- Transportation, including a reasonable car payment and insurance
- Food
- Utilities
- Healthcare
- Discretionary spending

A monthly savings target is included to distinguish living from merely surviving.

---

## Affordability Definitions

Housing affordability is evaluated using standard gross income ratios, consistent with industry norms for rent screening and mortgage underwriting.

### Status Bands

**Comfortable**
- Housing costs at or below 30 percent of gross income
- Positive monthly cash flow after taxes, expenses, and savings

**Stretched**
- Housing costs between 30 and 40 percent of gross income
- Limited but non negative monthly cash flow

**Not Viable**
- Housing costs above 40 percent of gross income
- Or negative monthly cash flow even if ratios technically pass

In addition to classification, the model calculates the required annual income needed to break even in each metro.

---

## Key Findings

### 1. Most metros are viable on $100K

The majority of U.S. metros fall into the Comfortable or Stretched categories for both renting and buying. Under realistic assumptions, $100K remains a workable income in most housing markets, though not always with large margins.

### 2. Renting is more broadly accessible than buying

Renting is viable in more metros than buying. Ownership presents a higher fixed cost barrier even when long term affordability may be reasonable. This aligns with current market conditions rather than modeling artifacts.

### 3. Where $100K fails, it fails predictably

Metros where $100K is Not Viable represent a relatively small subset. These metros are heavily concentrated in well known high cost regions and often require incomes meaningfully above $100K.

The issue is not widespread unaffordability, but extreme outliers with unusually high housing costs.

### 4. Not viable does not always mean dramatically unaffordable

Many metros classified as Not Viable are only modestly above the $100K threshold, often requiring $110K to $120K. A much smaller number require dramatically higher incomes, such as $160K or more.

This distinction is frequently lost in public discussion.

---

## Notable Exceptions

The most unaffordable metros are overwhelmingly concentrated in major coastal markets, dense financial or technology hubs, and regions with long standing housing supply constraints.

These results align closely with common expectations rather than revealing surprising new problem areas.

---

## Why State Taxes Are Not Included

State income taxes vary widely and introduce policy effects that are secondary to housing costs. To keep the baseline focused and comparable across metros, state taxes are excluded in the core model.

State tax impacts could be incorporated later as a sensitivity analysis without changing the core conclusions.

---

## Limitations

- Results apply to a single person household only
- Family size, childcare costs, student loans, and medical variability are not modeled
- Metro level averages mask neighborhood level variation
- Housing markets change, and results represent a recent snapshot rather than a forecast

---

## Data Sources

- Zillow Home Value Index (ZHVI)
- Zillow Observed Rent Index (ZORI)
- U.S. Census Bureau metropolitan population estimates

---

## Repository Structure

- `data/raw` contains original source files
- `data/processed` contains cleaned, analysis ready datasets
- `notebooks` contain step by step reproducible analysis
- `outputs` contain summary tables for reporting

---

## Summary

This analysis suggests that $100,000 is neither universally sufficient nor broadly inadequate. It remains enough to support a stable adult lifestyle in most U.S. metros, but fails in a small, predictable set of high cost markets where required incomes are meaningfully higher.


Possible Extensions

Future iterations could explore state tax sensitivity, ZIP-level analysis, or additional cost-of-living factors.

