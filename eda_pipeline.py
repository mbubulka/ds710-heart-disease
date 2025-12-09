"""
EDA: Exploratory Data Analysis
Analyzes 867 clean records from ETL pipeline
Generates statistics, distributions, and visualizations
"""

import pandas as pd
import numpy as np
import json
from datetime import datetime

class EDAAnalysis:
    def __init__(self, data):
        self.data = data
        self.report = {}
    
    def analyze_distributions(self):
        """Analyze feature distributions"""
        self.report['feature_statistics'] = {}
        
        for col in self.data.select_dtypes(include=[np.number]).columns:
            self.report['feature_statistics'][col] = {
                'mean': float(self.data[col].mean()),
                'std': float(self.data[col].std()),
                'min': float(self.data[col].min()),
                'max': float(self.data[col].max()),
                'median': float(self.data[col].median())
            }
        
        return self.report
    
    def analyze_missing_data(self):
        """Analyze remaining missing data"""
        self.report['missing_data'] = {
            'total_missing': int(self.data.isna().sum().sum()),
            'percentage': float((self.data.isna().sum().sum() / (self.data.shape[0] * self.data.shape[1])) * 100)
        }
        return self.report
    
    def analyze_target_distribution(self):
        """Analyze disease prevalence"""
        if 'target' in self.data.columns:
            disease_counts = self.data['target'].value_counts()
            self.report['target_distribution'] = {
                'no_disease': int(disease_counts.get(0, 0)),
                'disease': int(disease_counts.get(1, 0)),
                'disease_prevalence': f"{100 * disease_counts.get(1, 0) / len(self.data):.1f}%"
            }
        return self.report
    
    def analyze_demographics(self):
        """Analyze demographic patterns"""
        if 'age' in self.data.columns:
            self.report['age_distribution'] = {
                'mean_age': float(self.data['age'].mean()),
                'age_range': f"{int(self.data['age'].min())}-{int(self.data['age'].max())}"
            }
        
        if 'sex' in self.data.columns:
            gender_counts = self.data['sex'].value_counts()
            self.report['gender_distribution'] = {
                'female': int(gender_counts.get(0, 0)),
                'male': int(gender_counts.get(1, 0))
            }
        
        return self.report
    
    def run(self, data_file='etl_processed_data.csv', output_file='eda_analysis_report.json'):
        """Execute complete EDA"""
        print("=" * 60)
        print("EDA: EXPLORATORY DATA ANALYSIS")
        print("=" * 60)
        
        print("\n[STEP 1] Analyzing feature distributions...")
        self.analyze_distributions()
        print("✓ Feature statistics computed")
        
        print("\n[STEP 2] Checking missing data...")
        self.analyze_missing_data()
        print(f"✓ Missing data: {self.report['missing_data']['percentage']:.2f}%")
        
        print("\n[STEP 3] Analyzing target variable...")
        self.analyze_target_distribution()
        print(f"✓ Disease prevalence: {self.report['target_distribution']['disease_prevalence']}")
        
        print("\n[STEP 4] Analyzing demographics...")
        self.analyze_demographics()
        print(f"✓ Age range: {self.report['age_distribution']['age_range']} years")
        
        self.report['timestamp'] = datetime.now().isoformat()
        self.report['records_analyzed'] = len(self.data)
        
        print("\n" + "=" * 60)
        print("SUMMARY")
        print("=" * 60)
        print(json.dumps(self.report, indent=2))
        
        return self.report


if __name__ == "__main__":
    # Load cleaned data from ETL
    data = pd.read_csv('etl_processed_data.csv')
    
    eda = EDAAnalysis(data)
    report = eda.run()
    
    # Save report
    with open('eda_analysis_report.json', 'w') as f:
        json.dump(report, f, indent=2)
    
    print("\n✅ EDA Complete!")
