"""
Model Training: Train 3 algorithms and select best
Tests Logistic Regression, Gradient Boosting, Random Forest
Outputs trained models and performance metrics
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.metrics import accuracy_score, recall_score, roc_auc_score
import pickle
import json
from datetime import datetime

class ModelTrainer:
    def __init__(self, data):
        self.data = data
        self.X = data.drop('target', axis=1)
        self.y = data['target']
        self.models = {}
        self.results = {}
        self.scaler = StandardScaler()
    
    def prepare_data(self):
        """Split and scale data"""
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=0.2, random_state=42, stratify=self.y
        )
        
        self.X_train_scaled = self.scaler.fit_transform(self.X_train)
        self.X_test_scaled = self.scaler.transform(self.X_test)
        
        print(f"✓ Train set: {len(self.X_train)} samples")
        print(f"✓ Test set: {len(self.X_test)} samples")
        
        return self.X_train_scaled, self.X_test_scaled
    
    def train_logistic_regression(self):
        """Train Logistic Regression"""
        lr = LogisticRegression(max_iter=1000, random_state=42)
        lr.fit(self.X_train_scaled, self.y_train)
        
        y_pred = lr.predict(self.X_test_scaled)
        y_pred_proba = lr.predict_proba(self.X_test_scaled)[:, 1]
        
        self.models['logistic_regression'] = lr
        self.results['logistic_regression'] = {
            'accuracy': accuracy_score(self.y_test, y_pred),
            'recall': recall_score(self.y_test, y_pred),
            'auc_roc': roc_auc_score(self.y_test, y_pred_proba)
        }
        
        return self.results['logistic_regression']
    
    def train_gradient_boosting(self):
        """Train Gradient Boosting"""
        gb = GradientBoostingClassifier(n_estimators=100, random_state=42)
        gb.fit(self.X_train_scaled, self.y_train)
        
        y_pred = gb.predict(self.X_test_scaled)
        y_pred_proba = gb.predict_proba(self.X_test_scaled)[:, 1]
        
        self.models['gradient_boosting'] = gb
        self.results['gradient_boosting'] = {
            'accuracy': accuracy_score(self.y_test, y_pred),
            'recall': recall_score(self.y_test, y_pred),
            'auc_roc': roc_auc_score(self.y_test, y_pred_proba)
        }
        
        return self.results['gradient_boosting']
    
    def train_random_forest(self):
        """Train Random Forest"""
        rf = RandomForestClassifier(n_estimators=100, random_state=42, max_depth=15)
        rf.fit(self.X_train_scaled, self.y_train)
        
        y_pred = rf.predict(self.X_test_scaled)
        y_pred_proba = rf.predict_proba(self.X_test_scaled)[:, 1]
        
        self.models['random_forest'] = rf
        self.results['random_forest'] = {
            'accuracy': accuracy_score(self.y_test, y_pred),
            'recall': recall_score(self.y_test, y_pred),
            'auc_roc': roc_auc_score(self.y_test, y_pred_proba)
        }
        
        return self.results['random_forest']
    
    def select_best_model(self):
        """Select model with highest recall (medical priority)"""
        recalls = {name: metrics['recall'] for name, metrics in self.results.items()}
        best_model_name = max(recalls, key=recalls.get)
        
        print(f"\n✓ Best model: {best_model_name.upper()}")
        print(f"  Recall: {recalls[best_model_name]:.4f} (medical priority: minimize false negatives)")
        
        return best_model_name, self.models[best_model_name]
    
    def run(self, data_file='etl_processed_data.csv', output_file='model_training_report.json'):
        """Execute complete model training"""
        print("=" * 60)
        print("MODEL TRAINING: 3 ALGORITHMS COMPARISON")
        print("=" * 60)
        
        print("\n[STEP 1] Preparing data...")
        self.prepare_data()
        
        print("\n[STEP 2] Training Logistic Regression...")
        lr_results = self.train_logistic_regression()
        print(f"  Accuracy: {lr_results['accuracy']:.4f}")
        print(f"  Recall: {lr_results['recall']:.4f}")
        print(f"  AUC-ROC: {lr_results['auc_roc']:.4f}")
        
        print("\n[STEP 3] Training Gradient Boosting...")
        gb_results = self.train_gradient_boosting()
        print(f"  Accuracy: {gb_results['accuracy']:.4f}")
        print(f"  Recall: {gb_results['recall']:.4f}")
        print(f"  AUC-ROC: {gb_results['auc_roc']:.4f}")
        
        print("\n[STEP 4] Training Random Forest...")
        rf_results = self.train_random_forest()
        print(f"  Accuracy: {rf_results['accuracy']:.4f}")
        print(f"  Recall: {rf_results['recall']:.4f}")
        print(f"  AUC-ROC: {rf_results['auc_roc']:.4f}")
        
        print("\n[STEP 5] Selecting best model...")
        best_model_name, best_model = self.select_best_model()
        
        # Save models
        for name, model in self.models.items():
            with open(f'model_{name}.pkl', 'wb') as f:
                pickle.dump(model, f)
        
        # Save scaler
        with open('model_scaler.pkl', 'wb') as f:
            pickle.dump(self.scaler, f)
        
        report = {
            'timestamp': datetime.now().isoformat(),
            'algorithms': self.results,
            'best_model': best_model_name,
            'best_model_metrics': self.results[best_model_name],
            'selection_rationale': 'Highest recall (medical diagnosis priority: minimize false negatives)',
            'models_saved': list(self.models.keys()),
            'test_set_size': len(self.X_test)
        }
        
        print("\n" + "=" * 60)
        print("SUMMARY")
        print("=" * 60)
        print(json.dumps(report, indent=2, default=str))
        
        return report


if __name__ == "__main__":
    # Load cleaned data from ETL
    data = pd.read_csv('etl_processed_data.csv')
    
    trainer = ModelTrainer(data)
    report = trainer.run()
    
    # Save report
    with open('model_training_report.json', 'w') as f:
        json.dump(report, f, indent=2, default=str)
    
    print("\n✅ Model Training Complete!")
