# Airdrop Hunter

**Daily Web3 Airdrop Task Aggregator**

[![Skill Version](https://img.shields.io/badge/version-2.0.0-blue.svg)](https://github.com/AntalphaAI/airdrop-hunter)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

---

> **Note**: This repository contains the **Coze/OpenClaw version** of Airdrop Hunter.
> The **MCP Server version** (NestJS) has been migrated to [antalpha-com/antalpha-skills](https://github.com/antalpha-com/antalpha-skills) and is available as an MCP tool via the Antalpha MCP Server.

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

### 1. Data-Driven Scanning (MCP Version)
The MCP Server version fetches structured data directly from:
- **DefiLlama API** - Protocol TVL, categories, chain info
- **Hard-coded Funding Database** - VC backing, funding amounts
- **Airdrop Watchlist** - Curated S/A-grade projects

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
- Domain verification against known official domains
- Phishing pattern detection (hyphenated knockoffs, subdomain phishing)
- Fake claim website detection

---

## MCP Server Version (Recommended)

The latest version of Airdrop Hunter runs as an MCP tool on the Antalpha MCP Server.

**5 MCP Tools:**
| Tool | Description |
|------|-------------|
| `airdrop-scan` | Scan current airdrop opportunities |
| `airdrop-daily-report` | Generate structured daily report |
| `airdrop-check-project` | Check specific project airdrop status |
| `airdrop-zero-cost` | Find zero-cost testnet opportunities |
| `airdrop-scam-check` | Check URL/project for scam risks |

**Repository**: [antalpha-com/antalpha-skills](https://github.com/antalpha-com/antalpha-skills) (`feat/airdrop-hunter` branch)

**No plugins or API keys required.** All data is fetched from public APIs (DefiLlama).

---

## Coze/OpenClaw Version (Legacy)

This repository contains the original Coze skill version. It requires search plugins and is no longer actively maintained.

### Installation (Coze Version)

1. Download `airdrop-hunter.skill`
2. Upload to Coze Skill library
3. Test with command: `daily report`

### Quick Commands

| Command | Action |
|---------|--------|
| `daily report` | Get latest 24-hour airdrop checklist |
| `any zero-cost?` | Filter for free testnet opportunities |
| `check [project]` | Get specific project airdrop status |
| `S-grade tasks` | Show only Grade S high-priority tasks |

---

## Sample Output

```
Airdrop Scan Results (2026-04-13)

TOP PRIORITY (Grade S)
1. Monad: Testnet interaction | $0 | No deadline
   Why: Paradigm + Electric Capital ($444M funding), Tier-1 VC
   Link: https://monad.xyz

2. Abstract: Bridge + Swap tasks | $1-5 | Ongoing
   Why: Founders Fund + Paradigm ($107M funding)
   Link: https://abstract.xyz

ZERO-COST (Grade B)
1. Initia: Testnet participation | Free | Ongoing
   Why: Binance Labs backed, testnet live
   Link: https://initia.xyz

SCAM ALERTS
- Phishing: "scroll-airdrop-claim.xyz" is NOT official
- Official: scroll.io
```

---

## Project Structure

### MCP Server Version
```
libs/skills/airdrop-hunter/
├── src/
│   ├── airdrop-hunter.config.ts     # Configuration
│   ├── airdrop-hunter.module.ts     # NestJS module
│   ├── constants/
│   │   ├── prohibited-tokens.ts     # Completed airdrops (exact match)
│   │   ├── funding-database.ts      # Hard-coded VC/funding data
│   │   ├── airdrop-watchlist.ts     # Curated S/A-grade projects
│   │   ├── vc-tiers.ts             # VC tier classification
│   │   └── scam-patterns.ts        # Phishing detection patterns
│   ├── model/
│   │   └── airdrop-project.model.ts # Data interfaces
│   ├── service/
│   │   ├── defillama.service.ts     # DefiLlama API client
│   │   ├── grading.service.ts       # S/A/B/C grading engine
│   │   ├── scam-detector.service.ts # Scam detection
│   │   └── airdrop-scanner.service.ts # Scan orchestrator
│   └── tools/
│       └── airdrop-hunter.tools.ts  # 5 MCP tool registrations
└── test/
    └── airdrop-hunter.test.ts       # 35 unit tests
```

### Coze Version (Legacy)
```
airdrop-hunter/
├── SKILL.md                          # Main skill definition
├── references/
│   ├── evaluation-criteria.md        # Project grading criteria
│   └── trusted-sources.md            # Trusted information sources
└── README.md                         # This file
```

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
