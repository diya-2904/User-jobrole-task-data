# Feature Importance Hypothesis

## Hypothesis
The "task" feature has the highest importance in predicting "jobrole" due to its descriptive text content that directly relates to role responsibilities.

## Rationale
- From correlation analysis, jobrole shows moderate association with task_type, but text features like "task" contain keywords indicative of specific roles.
- EDA shows distinct task patterns per jobrole, suggesting strong predictive power.
- Other features like "sector" have no variation, thus low importance.

## Expected Rankings
1. task (High)
2. critical_work_function (Medium)
3. task_type (Medium)
4. track (Low)
5. sector (None - constant)

## Validation
- Use feature importance from tree-based models (e.g., Random Forest) to confirm.
- Permutation importance or SHAP values for NLP models.