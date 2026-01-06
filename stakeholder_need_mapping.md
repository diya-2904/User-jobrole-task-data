# Stakeholder Need Mapping

## Stakeholders
- AI/ML Interns: Require data for building predictive models on job roles and task categorization.

## Information Needs
- Insights into job role assignments based on tasks.
- Ability to categorize tasks for better understanding of job functions.
- Data suitable for machine learning models to predict roles or cluster similar tasks.

## Translated Analytics Requirements
- **Data Preparation**: Ensure dataset is clean with no missing values in critical columns (e.g., jobrole, task).
- **Feature Engineering**: Use columns like sector, track, critical_work_function, task, task_type, task_category as features.
- **Target Variables**: jobrole for predictive modeling (classification), task_category for categorization tasks.
- **Model Types**: Supervised learning for jobrole prediction, unsupervised for task clustering.
- **Quality Needs**: Consistent data types, standardized text, removal of duplicates to avoid bias in models.