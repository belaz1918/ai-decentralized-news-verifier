# AI-Driven Decentralized News Credibility Verifier

## Overview
This project tackles online misinformation by combining **AI-based credibility analysis** with **blockchain-backed verification**.  
- **AI Layer**: NLP model detects factual inconsistencies by comparing claims with trusted databases.  
- **Blockchain Layer**: Immutable verification results stored on-chain for transparency.  
- **Token Layer**: Validators earn tokens for reviewing AI outputs.

## Problem
Fake news spreads rapidly and erodes public trust. Existing fact-check platforms are centralized and vulnerable to censorship. We need a transparent, tamper-proof, community-driven verification system.

## Solution
1. User submits a news link.
2. AI model analyzes content, generates credibility score + supporting sources.
3. Validators review AI results.
4. Final result stored immutably on blockchain.

## Tech Stack
- **AI**: Hugging Face Transformers (BERT-based)
- **Backend**: Python (Flask)
- **Blockchain**: Solidity Smart Contract (Polygon testnet)
- **Frontend**: HTML/CSS/JavaScript

## Smart Contract Functions
- `storeVerification(articleHash, score, validatorSignatures)`
- `getVerification(articleHash)`

## Setup & Installation
```bash
git clone https://github.com/YOUR_USERNAME/ai-decentralized-news-verifier.git
cd ai-decentralized-news-verifier
pip install -r requirements.txt
python app.py
```

## Demo
- **Live Demo**: *Coming soon*
- **Video Demo**: *To be uploaded*
- **Screenshots**: See `/demo` folder

## Hackathon Submission
- **Event**: HackFinity 2025 (Devpost)
- **Submission Link**: [TBA]
- **Status**: Prototype
