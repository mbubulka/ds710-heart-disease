# Demo Script

**Duration**: 1-2 minutes  
**Audience**: Technical (hiring managers, colleagues, portfolio viewers)  
**Goal**: Show end-to-end ML system in action

---

## Opening (15 seconds)

*Camera on, smile, confident*

> "Hi, I'm Michael. Today I'm showing you a machine learning project I built that predicts heart disease risk from patient data. This demonstrates end-to-end ML engineering: data processing, model training, fairness auditing, and deployment.
>
> Let me walk you through it."

---

## Problem Statement (15 seconds)

> "The challenge: combine data from 4 different hospitals—920 patient records—and build a reliable predictor for heart disease. But more importantly, make sure the model is fair across different patient demographics.
>
> Why? Because bias in healthcare can have real consequences."

---

## Architecture Overview (20 seconds)

*Show dashboard Overview tab*

> "Here's what I built. The pipeline has 5 stages:
> 1. **ETL**: Combined 920 raw records from Cleveland, Hungarian, Virginia, and Switzerland, cleaned them, handled 1,743 missing values with median imputation. Result: 867 clean records (94.2% retention).
> 2. **EDA**: Analyzed data distribution and quality.
> 3. **Model Training**: Tested 3 algorithms—Logistic Regression, Gradient Boosting, and Random Forest—and selected Random Forest for highest recall.
> 4. **Fairness Audit**: Checked for bias across gender, age, symptom type.
> 5. **Dashboard**: Interactive tool for visualization and risk assessment."

---

## Results & Model Performance (40 seconds)

*Click to Model tab, point to algorithm comparison*

> "The model achieved:
> - **87.4% accuracy**
> - **91.6% recall** (important in medical diagnosis—we catch the sick patients)
> - **0.920 AUC** (strong discrimination)
>
> Random Forest won because it had the highest recall. In healthcare, it's better to have false positives (sending healthy patients for follow-up) than false negatives (missing sick patients).
>
> Here's the comparison: Random Forest 87.4%, Gradient Boosting 86.2%, Logistic Regression 82.1%. Random Forest is clearly ahead."

---

## Fairness Analysis (20 seconds)

*Click to Fairness tab, point to results table*

> "Now the critical part—bias audit. I measured fairness across 4 dimensions:
> - **Gender**: 1.3% gap—excellent, model treats men and women equally
> - **Age**: 2.4% gap—excellent, works across all age groups
> - **Symptom Type**: 7.1% gap—we flagged this. Atypical presentations underperform, but it's due to dataset imbalance (42 atypical vs 168+ typical cases), not model bias
> - **Imputation**: All records have <10% missing, model is safe on our data
>
> The audit shows the model is fair, with one area to monitor."

---

## Interactive Risk Calculator (15 seconds)

*Click to Risk Calculator tab, enter example patient data*

> "Here's the practical tool. Doctors can input patient data and instantly see risk assessment. Let me enter an example patient: 55-year-old male, typical chest pain, BP 140, cholesterol 250, normal heart rate.
>
> *Click calculate*
>
> Risk comes back at 68%—ELEVATED category—with clinical recommendations. This is decision support for physicians, not a diagnosis."

---

## Technical Stack & Deployment (15 seconds)

> "Technical details:
> - Built in Python with scikit-learn
> - Dashboard is pure HTML/CSS/JavaScript—no external dependencies
> - All data files, models, and reports are in Azure Cloud Storage
> - Deployed on Azure Container Instances
> - Ready to deploy to Netlify (live on the internet in 5 minutes)
>
> Full code and documentation on GitHub."

---

## Closing (15 seconds)

> "This project shows real ML engineering skills:
> - Handling messy multi-source data
> - Model selection with clinical context
> - Fairness as a first-class concern
> - Production-ready code and documentation
> - Deployment to cloud platforms
>
> Thanks for watching. Questions?"

---

## Live Demo Checklist

**Before you record:**
- [ ] Dashboard URL is accessible
- [ ] All 6 tabs load quickly
- [ ] Risk Calculator calculates without errors
- [ ] Have example patient data ready (age, gender, BP, etc.)
- [ ] Screen is well-lit
- [ ] Browser is zoomed to 125% for readability
- [ ] Close all other tabs/notifications

**During recording:**
- [ ] Speak clearly and at steady pace
- [ ] Click tabs smoothly (not too fast)
- [ ] Point cursor to specific metrics when mentioning numbers
- [ ] Take a natural pause between sections
- [ ] Don't rush—better to slow down

**Example patient data for Risk Calculator:**
- **Case 1 (Low Risk)**: 35M, non-anginal pain, BP 120, chol 180, HR 75 → ~20% risk
- **Case 2 (Moderate)**: 50M, atypical pain, BP 130, chol 220, HR 85 → ~45% risk
- **Case 3 (Elevated)**: 60F, typical angina, BP 145, chol 260, HR 100 → ~70% risk

---

## Pro Tips for Recording

1. **Use OBS Studio** (free screen recording software) or built-in Windows Screen Recorder
2. **Record at 1080p 30fps** minimum (looks professional)
3. **Clean audio** (use headset mic, not laptop speakers)
4. **Start with 5-second silence** (helps with editing)
5. **One retake is normal** (you probably won't get it perfect first try)
6. **Save as MP4** (compatible with YouTube, LinkedIn, portfolios)

---

## Estimated Timing

- Opening: 15s
- Problem: 15s
- Architecture: 20s
- Results: 40s
- Fairness: 20s
- Calculator: 15s
- Tech Stack: 15s
- Closing: 15s

**Total: ~2 minutes**

If you go slower (more explanation), 2-3 minutes is fine for portfolio purposes.

---

## Where to Share

After recording:
1. **LinkedIn**: "Just completed a machine learning project..." + video
2. **GitHub**: Add link to demo video in README
3. **Personal website**: Embed video in portfolio
4. **YouTube**: Upload as unlisted (shareable link only)

Good luck with the recording! 🎥
