# Airdrop Hunter

**Daily Web3 Airdrop Task Aggregator**

[![Skill Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/elvali-collab/airdrop-hunter)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

---

## Overview

Airdrop Hunter is an automated intelligence tool designed for Web3 hunters. It cuts through the noise of crypto airdrop information and delivers a daily streamlined action checklist.

**Key Value Proposition:**
- Save 2+ hours daily on research
- Never miss high-value airdrop opportunities
- Risk-graded tasks (S/A/B) for informed decisions
- Zero-cost testnet opportunities highlighted
- Security warnings to avoid scams

---

## Features

### 1. Multi-Source Scanning
Automatically tracks airdrop signals from:
- X (Twitter) - KOLs and project accounts
- Mirror.xyz - Project blogs
- Galxe/Zealy/Layer3 - Campaign platforms
- Research channels - RootData, DefiLlama, Messari

### 2. Project Grading System

| Grade | Criteria | Action |
|-------|----------|--------|
| **S** | Tier-1 VC backing (a16z, Paradigm), $50M+ funding | MUST DO |
| **A** | Reputable VCs, $10M+ funding, confirmed token | HIGH |
| **B** | Testnet stage, zero-cost, early potential | SPECULATIVE |

### 3. Minimalist Output
No fluff. Direct delivery of:
```
[Project] + [Action] + [Cost/Faucet Link]
```

### 4. Security Scanning
- Domain verification via Twitter bio
- Phishing detection (similar domain warnings)
- Contract verification on block explorers

### 5. Scheduled Automation
Configurable daily push at your preferred time via Coze Workflow.

---

## Installation

### Prerequisites
- Coze account with plugin access
- Required plugins:
  - Google Search OR Bing Search
  - Link Reader
  - (Optional) Twitter/X Search

### Install Steps

1. Download `airdrop-hunter.skill`
2. Upload to Coze Skill library
3. Enable required plugins
4. Test with command: `daily report`

---

## Quick Commands

| Command | Action |
|---------|--------|
| `daily report` | Get latest 24-hour airdrop checklist |
| `any zero-cost?` | Filter for free testnet opportunities |
| `check [project]` | Get specific project airdrop status |
| `S-grade tasks` | Show only Grade S high-priority tasks |

---

## Sample Output

```
📅 March 27, 2026 Airdrop Daily Report

🔥 TOP PRIORITY (Grade S/A)
1. Scroll: Bridge 0.01 ETH to Scroll network | $2-5 gas | No deadline
   └─ Why: Polychain backed ($80M), mainnet live, points active
   └─ Link: https://scroll.io/bridge

2. zkSync Era: Mint NFT + Swap | $1-3 | Ongoing
   └─ Why: a16z backed ($458M), confirmed token
   └─ Link: https://era.zksync.io

🧪 ZERO-COST TESTNETS (Grade B)
1. Linea: Claim testnet ETH → Swap tokens | Free | 10 min
   └─ Faucet: https://faucet.goerli.linea.build
   └─ Why: ConsenSys backed, mainnet imminent

📅 TODAY'S DEADLINES
- zkSync Galxe Campaign: Ends in 6 hours
- Scroll OAT Claim: Ends March 28

⚠️ SECURITY ALERTS
- Phishing alert: "scrolls-airdrop.io" is NOT official
- Always verify: scroll.io (check Twitter @Scroll_ZKP)
```

---

## Configuration

### Plugin Setup
Navigate to Coze Plugins page and enable:

1. **Google Search** or **Bing Search**
   - Required for fetching airdrop articles
   - Test: Search "airdrop alpha today"

2. **Link Reader**
   - Required for deep-diving articles
   - Extracts key details from long content

3. **Twitter/X Search** (Optional)
   - Direct access to X for real-time alpha
   - Workaround: Use Google Search with `site:x.com`

### Workflow Setup (Daily Automation)
Configure scheduled trigger:
1. Create workflow: `Daily_Airdrop_Push`
2. Set trigger: Daily at 10:00 AM (configurable)
3. Configure output: Chat / Telegram / Discord

See [SKILL.md](airdrop-hunter/SKILL.md) for detailed configuration.

---

## Project Structure

```
airdrop-hunter/
├── SKILL.md                          # Main skill definition
├── references/
│   ├── evaluation-criteria.md        # Project grading criteria
│   └── trusted-sources.md            # Trusted information sources
└── README.md                         # This file
```

---

## Resources

- [Evaluation Criteria](airdrop-hunter/references/evaluation-criteria.md) - Detailed grading methodology
- [Trusted Sources](airdrop-hunter/references/trusted-sources.md) - Where to find airdrop alpha

---

## Disclaimer

**This tool is for informational purposes only. Not financial advice.**

- Always DYOR (Do Your Own Research)
- Never invest more than you can afford to lose
- Verify all information before interacting
- Use separate wallets for airdrop hunting
- Never share private keys or seed phrases

---

## License

MIT License - See [LICENSE](LICENSE) for details.

---

## Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create feature branch
3. Submit pull request

---

## Support

- Open an issue for bugs
- Join discussions for feature requests
- Star the repo if you find it useful!
