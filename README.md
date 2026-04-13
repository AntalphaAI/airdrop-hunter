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

## Case Review

### Case 1: Daily Airdrop Scan

**User**: "What airdrop opportunities are available right now?"

**Tool**: `airdrop-scan`

```json
{
  "airdrops": [
    {
      "name": "Monad",
      "slug": "monad",
      "chains": ["Monad"],
      "category": "Chain",
      "status": "active",
      "token_name": null,
      "grade": "S",
      "tvl_usd": null,
      "funding_usd": 444000000,
      "vc_backers": ["Paradigm", "Electric Capital"],
      "community_score": 65,
      "cost_estimate": "$0",
      "official_url": "https://monad.xyz",
      "scam_risk_level": "safe"
    },
    {
      "name": "Abstract",
      "slug": "abstract",
      "chains": ["Ethereum"],
      "category": "Chain",
      "status": "upcoming",
      "token_name": null,
      "grade": "S",
      "tvl_usd": 52000000,
      "funding_usd": 107000000,
      "vc_backers": ["Founders Fund", "Paradigm"],
      "community_score": 70,
      "cost_estimate": "$1-5",
      "official_url": "https://abstract.xyz",
      "scam_risk_level": "safe"
    },
    {
      "name": "Initia",
      "slug": "initiadex",
      "chains": ["Initia"],
      "category": "Dexs",
      "status": "upcoming",
      "token_name": null,
      "grade": "A",
      "tvl_usd": 8500000,
      "funding_usd": 7500000,
      "vc_backers": ["Binance Labs"],
      "community_score": 55,
      "cost_estimate": "$0",
      "official_url": "https://initia.xyz",
      "scam_risk_level": "safe"
    }
  ],
  "total_count": 18,
  "scanned_at": "2026-04-13T10:30:00Z"
}
```

**Rendered output**:
```
Airdrop Scan (2026-04-13) — 18 opportunities found

[S] Monad | Chain | $0 | monad.xyz
    Paradigm + Electric Capital ($444M) | No token yet

[S] Abstract | Chain | $1-5 | abstract.xyz
    Founders Fund + Paradigm ($107M) | TVL $52M

[A] Initia | DEX | $0 | initia.xyz
    Binance Labs ($7.5M) | Testnet live

... and 15 more
```

---

### Case 2: Daily Report

**User**: "Give me today's airdrop report"

**Tool**: `airdrop-daily-report`

```json
{
  "date": "2026-04-13",
  "sections": {
    "top_priority": [
      {
        "name": "Monad",
        "grade": "S",
        "funding_usd": 444000000,
        "vc_backers": ["Paradigm", "Electric Capital"],
        "cost_estimate": "$0"
      }
    ],
    "zero_cost": [
      {
        "name": "Initia",
        "interaction_type": "testnet",
        "grade": "B"
      },
      {
        "name": "MegaETH",
        "interaction_type": "testnet",
        "grade": "B"
      }
    ],
    "deadlines": [
      {
        "name": "Berachain",
        "status": "upcoming",
        "grade": "A"
      }
    ],
    "scam_alerts": [
      {
        "type": "fake_claim_website",
        "description": "Watch for hyphenated knockoff domains (e.g., project-airdrop.io)",
        "severity": "high"
      },
      {
        "type": "social_engineering",
        "description": "Official projects NEVER send claim links via DM",
        "severity": "high"
      }
    ]
  },
  "metadata": {
    "total_scanned": 42,
    "data_sources": ["defillama", "funding-database"],
    "generated_at": "2026-04-13T08:00:00Z"
  }
}
```

**Rendered output**:
```
Airdrop Daily Report — 2026-04-13

TOP PRIORITY (S/A Grade)
 1. Monad [S] | Testnet | $0 | Paradigm + Electric Capital ($444M)
 2. Abstract [S] | Bridge+Swap | $1-5 | Founders Fund + Paradigm ($107M)

ZERO-COST OPPORTUNITIES
 1. Initia — Testnet participation (free)
 2. MegaETH — Testnet interaction (free)

UPCOMING DEADLINES
 1. Berachain [A] — BGT staking active, token likely

SCAM ALERTS
 ! Hyphenated knockoff domains (e.g., project-airdrop.io) — ALWAYS verify
 ! Official projects NEVER DM claim links
```

---

### Case 3: Check Specific Project

**User**: "Is Scroll still worth doing?"

**Tool**: `airdrop-check-project` with `project_name: "Scroll"`

```json
{
  "project": {
    "name": "Scroll",
    "slug": "scroll",
    "grade": "C",
    "status": "completed",
    "token_name": "SCR",
    "tvl_usd": 620000000,
    "funding_usd": 80000000,
    "vc_backers": ["Polychain", "Sequoia"]
  },
  "grade": "C",
  "status": "completed",
  "details": "Scroll airdrop completed. Token $SCR already distributed and trading.",
  "scam_risks": {
    "risk_level": "medium",
    "warnings": [
      {
        "type": "social_engineering",
        "description": "\"Scroll\" may be confused with official project. Verify: scroll.io"
      }
    ]
  },
  "recommendation": "AVOID - Airdrop already completed"
}
```

**Rendered output**:
```
Scroll — Grade C | Airdrop COMPLETED

Token: $SCR (already trading)
TVL: $620M | Funding: $80M (Polychain, Sequoia)

Status: Airdrop already distributed. SCR is live.
Warning: Beware of fake "Scroll airdrop" websites — official is scroll.io

Recommendation: SKIP — no further airdrop opportunity
```

---

### Case 4: Zero-Cost Opportunities

**User**: "Any free airdrops I can do without spending gas?"

**Tool**: `airdrop-zero-cost`

```json
{
  "opportunities": [
    {
      "name": "Monad",
      "slug": "monad",
      "chains": ["Monad"],
      "category": "Chain",
      "grade": "B",
      "tvl_usd": null,
      "interaction_type": "testnet",
      "official_url": "https://monad.xyz"
    },
    {
      "name": "Initia",
      "slug": "initiadex",
      "chains": ["Initia"],
      "category": "Dexs",
      "grade": "B",
      "tvl_usd": 8500000,
      "interaction_type": "testnet",
      "official_url": "https://initia.xyz"
    },
    {
      "name": "MegaETH",
      "slug": "megaeth",
      "chains": ["Ethereum"],
      "category": "Chain",
      "grade": "B",
      "tvl_usd": null,
      "interaction_type": "testnet",
      "official_url": "https://megaeth.com"
    }
  ],
  "summary": "Found 3 zero-cost airdrop opportunities",
  "total_found": 3
}
```

**Rendered output**:
```
Zero-Cost Airdrops — 3 found

1. Monad (Testnet) | monad.xyz
   Interact with testnet dApps — no real ETH needed

2. Initia (Testnet) | initia.xyz
   Testnet swaps + LP — free test tokens from faucet

3. MegaETH (Testnet) | megaeth.com
   Early testnet participation — free to join
```

---

### Case 5: Scam Check

**User**: "Is scroll-airdrop-claim.xyz legit?"

**Tool**: `airdrop-scam-check` with `url: "https://scroll-airdrop-claim.xyz"`

```json
{
  "risk_level": "critical",
  "warnings": [
    {
      "type": "fake_claim_website",
      "pattern": "[a-z0-9]+-(?:airdrop|claim|claims|free|reward)\\.[a-z]+",
      "description": "Hyphenated knockoff: project name with airdrop/claim suffix (e.g., scroll-airdrop.com)",
      "severity": "critical"
    },
    {
      "type": "fake_claim_website",
      "pattern": "scroll",
      "description": "Domain contains \"scroll\" but is not an official domain. Official: scroll.io",
      "severity": "critical"
    }
  ],
  "safe_alternatives": ["scroll.io"],
  "analysis_details": "Domain scroll-airdrop-claim.xyz triggered 2 warning(s): Hyphenated knockoff; Domain contains 'scroll' but not official"
}
```

**Rendered output**:
```
SCAM ALERT — Risk Level: CRITICAL

URL: scroll-airdrop-claim.xyz

Warnings:
 [CRITICAL] Hyphenated knockoff domain — "scroll-airdrop" pattern detected
 [CRITICAL] Uses "scroll" name but is NOT the official project

Safe alternative: scroll.io

DO NOT connect your wallet. This is a phishing site.
```

---

### Case 6: Scam Check (Safe URL)

**User**: "Is berachain.com the real site?"

**Tool**: `airdrop-scam-check` with `url: "https://berachain.com"`, `project_name: "Berachain"`

```json
{
  "risk_level": "safe",
  "warnings": [],
  "safe_alternatives": [],
  "analysis_details": "Domain berachain.com is verified official for berachain."
}
```

**Rendered output**:
```
SAFE — berachain.com is the verified official domain for Berachain.

No warnings detected. You can proceed with caution.
Always verify URLs independently before connecting your wallet.
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
