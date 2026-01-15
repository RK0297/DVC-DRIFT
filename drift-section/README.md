# Drift Detection

Detect when ML models degrade in production.

## Notebooks

| Notebook | Technique | Use Case |
|----------|-----------|----------|
| `MD_1.ipynb` | KS Test | Feature distribution shift |
| `label_drift.ipynb` | F1 Decay | Target label shift |
| `multivariate_drift_pca.ipynb` | PCA Reconstruction | Correlation structure change |

## Quick Reference

**Model Drift**: Features change → KS test on distributions  
**Label Drift**: Targets change → Monitor F1/accuracy decay  
**Multivariate Drift**: Correlations change → PCA reconstruction error

## Usage

```python
from scipy.stats import ks_2samp
stat, p = ks_2samp(train_data, prod_data)
if p < 0.05:
    print("Drift detected!")
```

## Resources
- `Model_Drift_.pdf` - Theory
- `Model_Drift__Advanced_.pdf` - Advanced techniques
