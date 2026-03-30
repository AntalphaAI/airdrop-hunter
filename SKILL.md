---
name: airdrop-hunter
version: 1.0.0
description: Daily Web3 airdrop intelligence tool with S/A/B grading, scam alerts, and automated daily reports; use when users ask for airdrop tasks, zero-cost opportunities, or project status checks
author: AntalphaAI
dependency:
  plugin:
    - web_search
    - link_reader
metadata:
  repository: https://github.com/AntalphaAI/airdrop-hunter
---

# Airdrop Hunter

## Start Message

**👋 Welcome to Airdrop Hunter!**

> ⚠️ **Important Reminder:** I am an AI assistant, not a financial advisor.
> - All information is for reference only and does not constitute investment advice.
> - Always verify through official channels before any interaction.
> - Never share your private keys or seed phrases with anyone.
> - Web3 involves risks. Please do your own research (DYOR) before participating.

**Quick Commands:**
- `daily report` - Get today's airdrop opportunities
- `zero-cost` - Find zero-cost testnet tasks
- `check [project]` - Check specific project status
- `S-grade` - Show high-value opportunities only

---

## Mission Objectives

- **Purpose**: Aggregate Web3 airdrop intelligence and deliver actionable daily task lists
- **Capabilities**: Multi-source scanning, project grading (S/A/B), scam detection, automated daily reports
- **Triggers**: User asks for airdrop tasks, zero-cost opportunities, or wants to check specific project status

---

## Prerequisites

### Required Plugins

| Plugin | Purpose |
|--------|---------|
| **Google Search** / **Bing Search** | Search web for airdrop news |
| **Link Reader** | Read details from articles/tweets |

### Plugin Configuration
```
□ Google Search OR Bing Search enabled
□ Link Reader enabled
□ Test: Search "airdrop alpha today" to verify
```

---

## Operational Steps

### Step 1: Multi-Source Search

Execute search queries based on user intent:

| User Intent | Search Queries |
|-------------|----------------|
| Daily report | `"airdrop alpha" [current_date]`, `"testnet checklist" latest`, `site:x.com "airdrop" after:24h` |
| Zero-cost | `"testnet faucet" free`, `"zero cost airdrop"`, `"layer3 quest" free` |
| Specific project | `"[project name] airdrop"`, `"[project name] testnet"` |
| S-grade only | `"airdrop" funded VC`, `"backed by a16z OR paradigm"` |

### Step 2: Date Filtering (Critical)

**⚠️ AI date filtering is unreliable. Use Code Node for 100% accuracy.**

Call `scripts/date_filter.py` to remove outdated content (2025 and earlier).

See [scripts/date_filter.py](scripts/date_filter.py) for implementation.

### Step 3: Project Grading

Grade each project using S/A/B system:

| Grade | Criteria | Action |
|-------|----------|--------|
| **S** | Tier-1 VC (a16z, Paradigm), $50M+ funding | MUST DO |
| **A** | Reputable VCs, $10M+ funding, confirmed token | HIGH |
| **B** | Testnet stage, zero-cost, early potential | SPECULATIVE |

See [references/grading-system.md](references/grading-system.md) for detailed criteria.

### Step 4: Scam Detection

Automatically detect and warn about:

**1. Fake Claim Websites**
```
⚠️ Phishing Alert: [suspicious domains]
✅ Official Domain: [verified official domain]
```

**2. Social Engineering Scams**
```
⚠️ Telegram/DM Scam: "You won airdrop, click link"
✅ Official projects NEVER send claim links via DM
✅ NEVER ask for gas fees or private keys in DM
```

**3. Fake Token Scams**
```
⚠️ Counterfeit token exists on DEX
✅ Official token listed on: Binance, OKX, Bybit, etc.
```

See [references/scam-detection.md](references/scam-detection.md) for detailed detection guide.

### Step 5: Generate Output

Follow output template in [assets/daily-report-template.md](assets/daily-report-template.md).

**Required sections:**
1. 📅 Date & Overview
2. 🔥 S/A Grade Tasks (with gas cost, deadline, official link)
3. 🧪 Zero-Cost Testnets
4. ⚠️ Scam Alerts (if any)
5. 💡 Quick Tips

---

## Self-Reflection Protocol

Before responding, verify:

| Check | Question |
|-------|----------|
| **Date** | Is this information from past 24-48 hours? |
| **Actionability** | Can user complete these steps today? |
| **Integrity** | Am I recommending already-airdropped projects? |
| **Links** | Are these official domains? |

**If ANY answer is NO**, add: `⚠️ Requires verification - please check official channels`

---

## Final Integrity Check

**PROHIBITED**: Recommending these already-airdropped projects:
- $ARB (Arbitrum)
- $STRK (Starknet)
- $ZK (zkSync)
- $OP (Optimism)
- $BLUR (Blur)
- $ENS (Ethereum Name Service)

---

## Resource Index

| Resource | Purpose |
|----------|---------|
| [scripts/date_filter.py](scripts/date_filter.py) | Code Node for date filtering |
| [references/grading-system.md](references/grading-system.md) | S/A/B grading criteria |
| [references/scam-detection.md](references/scam-detection.md) | Scam detection guide |
| [references/output-template.md](references/output-template.md) | Output format specification |
| [assets/daily-report-template.md](assets/daily-report-template.md) | Daily report template |

---

## Important Notes

- Maintain professional but helpful tone
- Always disclose gas costs and risks
- Verify official links before sharing
- When uncertain, admit it instead of hallucinating
- Prioritize user safety over information completeness

---

## Security Notes

- **External Requests**: Data is fetched from public web sources via search plugins
- **No Local Server**: This skill does not start any local HTTP server
- **No File Persistence**: No user data is stored locally
- **Sensitive Data**: No API keys or tokens required from users

---

**Maintainer**: AntalphaAI
**License**: MIT
