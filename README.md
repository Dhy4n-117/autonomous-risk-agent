# Autonomous Vendor Risk Intelligence Agent 🛡️

![Status](https://img.shields.io/badge/Status-Active-success)
![Tech](https://img.shields.io/badge/Tech-n8n%20|%20Docker%20|%20Gemini%20AI-blue)

## 🚀 Overview
A self-hosted, autonomous AI agent that automates **Third-Party Risk Management (TPRM)**. It monitors critical vendors 24/7, ingesting real-time news to detect security breaches, outages, and legal threats before they hit the mainstream news.

Unlike static monitoring tools, this agent uses **Google Gemini 2.0 Flash** to semantically understand news headlines, filtering out marketing noise and assigning a dynamic **Risk Score (0-10)** based on severity and internal vendor criticality.

## 🏗️ Architecture
The system runs as a containerized microservice stack:

* **Orchestrator:** [n8n](https://n8n.io/) (Self-hosted via Docker)
* **Intelligence:** Google Gemini 2.0 Flash (LLM for semantic analysis)
* **Database:** PostgreSQL (Stores vendor profiles & criticality levels)
* **Ingestion:** RSS/XML Feeds (Real-time data gathering)
* **Audit Trail:** Google Sheets API (Logging & Reporting)

## 🧠 Workflow Logic
1.  **Database Lookup:** Fetches active vendors and their "Criticality" status (Critical/High/Low) from PostgreSQL.
2.  **News Scraper:** Queries Google News RSS for real-time headlines related to security breaches.
3.  **AI Analysis:** Passes headlines to **Gemini**, which acts as a Cyber Threat Analyst to:
    * Filter out irrelevant news.
    * Summarize the threat.
    * Assign a raw severity score.
4.  **Scoring Engine (JavaScript):**
    * Normalizes the AI score.
    * Applies a **20% risk boost** if the vendor is marked "Critical" in the DB.
5.  **Decision Gate:**
    * **IF** Score > 7.0 **AND** Risk Confirmed: **TRIGGER ALERT**.
    * **ELSE**: Log as low priority.
6.  **Action:** Appends the incident to the corporate Risk Log (Google Sheets).

## Prerequisites
1. Docker Desktop installed.
2. Google Cloud Console Project (for Sheets API).
3. Google AI Studio Key (for Gemini).
