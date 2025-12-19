# config/financial_assumptions.py

"""
Financial assumptions for affordability analysis.

Scope:
- Single adult
- No dependents
- No roommates
- Market-rate housing (1–2 BR apartment OR modest SFH)
- Financed vehicle with full coverage
- Goal: live independently and comfortably, not merely survive
"""

# =========================
# Income
# =========================
ANNUAL_GROSS_INCOME = 100_000
MONTHLY_GROSS_INCOME = ANNUAL_GROSS_INCOME / 12

# =========================
# Taxes (effective rates)
# =========================
# Approximate effective federal rate for single filer at ~$100k
FEDERAL_EFFECTIVE_TAX = 0.18

# Social Security + Medicare
PAYROLL_TAX = 0.0765

# State tax handled later (varies by state)
# STATE_EFFECTIVE_TAX = 0.0  # placeholder

# =========================
# Savings Requirement
# =========================
# Minimum savings to qualify as "living, not just surviving"
SAVINGS_RATE = 0.10  # 10% of gross income
MONTHLY_SAVINGS_TARGET = MONTHLY_GROSS_INCOME * SAVINGS_RATE

# =========================
# Housing — Buying
# =========================
MORTGAGE_RATE = 0.065        # 6.5%
MORTGAGE_TERM_YEARS = 30
DOWN_PAYMENT_RATE = 0.20
PROPERTY_TAX_RATE = 0.012   # 1.2% annually
HOME_INSURANCE_MONTHLY = 150

# =========================
# Housing — Renting
# =========================
# Non-rent housing costs for renters
RENT_UTILITIES_BUFFER = 200  # utilities not captured in rent

# =========================
# Transportation
# =========================
# Reasonable, non-luxury, financed vehicle
CAR_PAYMENT_MONTHLY = 450      # conservative vs ~$520 avg used car payment
CAR_INSURANCE_MONTHLY = 150   # full coverage
GAS_MONTHLY = 150

TRANSPORTATION_MONTHLY = (
    CAR_PAYMENT_MONTHLY +
    CAR_INSURANCE_MONTHLY +
    GAS_MONTHLY
)

# =========================
# Living Expenses (Single Adult)
# =========================
UTILITIES_MONTHLY = 300       # electric, gas, water, trash, basic internet
FOOD_MONTHLY = 600            # groceries + modest dining out
PHONE_INTERNET_MONTHLY = 140
HEALTH_INSURANCE_MONTHLY = 350
MISC_MONTHLY = 200             # clothing, personal care, light entertainment

NON_HOUSING_MONTHLY = (
    TRANSPORTATION_MONTHLY +
    UTILITIES_MONTHLY +
    FOOD_MONTHLY +
    PHONE_INTERNET_MONTHLY +
    HEALTH_INSURANCE_MONTHLY +
    MISC_MONTHLY
)

# =========================
# Affordability Thresholds
# =========================
# Industry-standard housing burden rules
HOUSING_COMFORTABLE_RATIO = 0.30
HOUSING_STRETCHED_RATIO = 0.40

