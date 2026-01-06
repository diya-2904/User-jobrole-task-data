# Data Quality Report (DQR)

## Dataset Overview
- **File**: s_users_jobrole_task.csv
- **Estimated Rows**: 21,000+ (based on file size)
- **Columns**: 14
  - sector
  - track
  - jobrole
  - critical_work_function
  - task
  - task_type
  - sub_institute_id
  - created_by
  - updated_by
  - deleted_by
  - created_at
  - updated_at
  - deleted_at
  - task_category

## Data Types
- **String/Object**: sector, track, jobrole, critical_work_function, task, task_type, created_at, updated_at, deleted_at, task_category
- **Integer**: sub_institute_id, created_by, updated_by, deleted_by

## Missing Values
- **updated_by**: 100% missing (all rows in sample)
- **deleted_by**: 100% missing
- **updated_at**: 100% missing
- **deleted_at**: 100% missing
- **Other columns**: No missing values observed in sample

## Duplicates
- **Duplicate Rows**: Present (e.g., identical task entries found in sample)
- **Estimated Count**: Unknown, but significant based on sample

## Outliers and Anomalies
- **Dates**: All consistent (2025-07-16 18:30:00 in sample), no invalid dates
- **IDs**: Valid integers, no outliers
- **Text Fields**: No apparent anomalies

## Schema Inconsistencies
- Consistent column structure across sample
- No invalid data types or formats identified

## Quality Issues
- High missing values in audit-related columns (updated_by, deleted_by, updated_at, deleted_at)
- Duplicate entries may skew analytics

## Recommendations for Cleaning
- Remove duplicate rows to ensure unique data
- Drop columns with 100% missing values (updated_by, deleted_by, updated_at, deleted_at) as they provide no value
- Verify no missing values in key columns (jobrole, task) for ML models
- Standardize text fields if needed (e.g., trim whitespace)
- Filter out any irrelevant rows (none identified)