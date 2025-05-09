# AWS Security Alerter 🔍  
![Python](https://img.shields.io/badge/Python-3.9+-blue) 
![Terraform](https://img.shields.io/badge/Terraform-1.0+-purple)  
**Automated detection of AWS security risks: public S3 buckets, stale IAM keys, and suspicious CloudTrail events.**  

## 🚀 Features  
- **Public S3 Scanner**: Finds buckets with accidental public access.  
- **IAM Key Auditor**: Detects unused keys older than 90 days.  
- **CloudTrail Anomalies**: Alerts on high-risk actions (e.g., `DeleteBucket`).  
- **Notifications**: Slack, Email, PagerDuty.  

## 📦 Quick Start  
```bash
git clone https://github.com/yourname/aws-security-alerter.git  
cd aws-security-alerter  
pip install -r requirements.txt  
python src/s3_scanner.py --bucket YOUR_BUCKET
