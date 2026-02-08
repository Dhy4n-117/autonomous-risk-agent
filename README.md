# Autonomous Vendor Risk Intelligence Agent 🛡️

## 🚀 Overview
A self-hosted, autonomous AI agent that monitors critical third-party vendors for security breaches, outages, and legal threats. It replaces manual threat intelligence gathering with a 24/7 automated pipeline.

## 🏗️ Architecture
**Tech Stack:** n8n (Workflow Engine), Docker, PostgreSQL, Google Gemini 2.0 Flash (LLM), Google Sheets API.

### The Pipeline:
1.  **Ingestion:** Scrapes real-time RSS/XML feeds for vendor-specific news (e.g., "Twilio security breach").
2.  **Analysis (AI):** Uses **Google Gemini 2.0 Flash** to semantically analyze headlines, filtering out marketing fluff and identifying true threats.
3.  **Scoring Engine (Logic):** A custom **JavaScript** module calculates a dynamic risk score (0-10) based on the AI's confidence and the vendor's criticality level stored in Postgres.
4.  **Decision & Alerting:**
    * **High Risk (Score > 7):** Triggers an immediate alert and logs the incident to an audit trail (Google Sheets/Slack).
    * **Low Risk:** Discards noise to prevent alert fatigue.

## 🧠 Key Features
* **Self-Correction:** Includes fallback logic if the AI returns malformed JSON.
* **Context Awareness:** Boosts risk scores by 20% for vendors marked "Critical" in the internal database.
* **Zero-Cost:** Fully self-hosted architecture avoiding expensive SaaS subscriptions.

## 🛠️ Setup
1.  **Deploy n8n:** Run via Docker Compose.
2.  **Database:** Initialize PostgreSQL with the `vendors` table.
3.  **Credentials:** Configure Google Cloud OAuth2 for Sheets and MakerSuite API key for Gemini.
4.  **Run:** Import the `workflow.json` and activate.

## 📊 Sample Output
| Date | Vendor | Risk Score | Summary | Alert |
| :--- | :--- | :--- | :--- | :--- |
| 2026-02-08 | Twilio | **10.8** | Confirmed data breach exposing 800k records via SendGrid. | 🚨 TRUE |
