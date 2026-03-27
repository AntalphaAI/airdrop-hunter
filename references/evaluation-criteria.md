# Airdrop Project Evaluation Criteria

## Overview
This document provides detailed criteria for grading airdrop opportunities from S (highest) to C (lowest).

---

## Table of Contents
- [Grade S - Must Do](#grade-s---must-do)
- [Grade A - High Priority](#grade-a---high-priority)
- [Grade B - Testnet/Speculative](#grade-b---testnetspeculative)
- [Grade C - Low Priority](#grade-c---low-priority)
- [VC Tier Classification](#vc-tier-classification)
- [Red Flags](#red-flags)

---

## Grade S - Must Do

**Definition**: Highest confidence opportunities with strong backing and low cost.

### Required Criteria (ALL must be met)

| Criterion | Requirement | How to Verify |
|-----------|-------------|---------------|
| **VC Backing** | Tier-1 VC lead | RootData, Crunchbase |
| **Funding Amount** | $10M+ raised | RootData, Messari |
| **Community** | 10k+ Twitter followers | Twitter profile |
| **Token Status** | Confirmed airdrop allocation | Tokenomics docs, Twitter |
| **Cost** | <$5 or free | Gas estimation |

### Tier-1 VCs (Automatic S if lead investor)
- a16z (Andreessen Horowitz)
- Paradigm
- Polychain Capital
- Sequoia Capital
- Founders Fund
- Electric Capital
- Dragonfly Capital

### Example Grade S Projects
1. **Arbitrum (Completed)**
   - Funding: $143M from Pantera, Lightspeed
   - Airdrop: Confirmed and executed
   - Cost: Free testnet interactions

2. **zkSync Era**
   - Funding: $458M from a16z, Union Square
   - Airdrop: Confirmed token
   - Cost: Low gas on zkSync

---

## Grade A - High Priority

**Definition**: Strong opportunities with good risk/reward ratio.

### Required Criteria (at least 3 of 4)

| Criterion | Requirement |
|-----------|-------------|
| **VC Backing** | Tier-1 or Tier-2 VC involved |
| **Funding Amount** | $5M+ raised |
| **Community** | 5k+ Twitter followers OR active Discord |
| **Stage** | Mainnet live OR TGE imminent |

### Tier-2 VCs
- Pantera Capital
- Coinbase Ventures
- Binance Labs
- HashKey Capital
- Framework Ventures
- Bain Capital Crypto

### Additional A Factors
- Points system active (speculative but low cost)
- Partner integrations with major protocols
- Strong GitHub activity (weekly commits)
- Team from reputable projects (Uniswap, Polygon, etc.)

### Cost Guidelines for Grade A
- Mainnet: $5-20 acceptable
- Testnet: Free always
- Time: Under 30 minutes

---

## Grade B - Testnet/Speculative

**Definition**: Early-stage opportunities with potential but no guarantees.

### Criteria

| Criterion | Requirement |
|-----------|-------------|
| **Funding** | Any confirmed OR strong team background |
| **Stage** | Testnet OR early mainnet |
| **Cost** | Free (testnet) OR <$2 (mainnet) |
| **Risk** | May not have token |

### When to Include
1. **Testnet with strong backers** (even if funding unknown)
2. **New L2/L3 from reputable team** (e.g., Base from Coinbase)
3. **Ecosystem campaigns** (Galxe, Zealy, Layer3 quests)
4. **Points/farming systems** (but mark as speculative)

### B → A Upgrade Path
- Announces funding round → Upgrade to A
- Confirms token → Upgrade to A
- Mainnet launch with incentives → Upgrade to A

---

## Grade C - Low Priority

**Definition**: Included for completeness but with clear warnings.

### Criteria

| Criterion | Situation |
|-----------|-----------|
| **Team** | Anonymous OR unknown background |
| **Community** | <1k followers OR low engagement |
| **Cost** | High gas ($20+) with no clear value |
| **Risk** | High scam probability |

### Must Include Warning
```
⚠️ DYOR: This project has limited info. Proceed with caution.
```

### Never List
- No official Twitter
- No website
- Known scams (check Twitter replies for reports)
- Copycat projects (similar names to popular ones)

---

## VC Tier Classification

### Tier-1 (Automatic S grade if lead)
- a16z
- Paradigm
- Polychain
- Sequoia
- Founders Fund
- Electric Capital
- Dragonfly

### Tier-2 (Automatic A grade if involved)
- Pantera
- Coinbase Ventures
- Binance Labs
- HashKey
- Framework
- Bain Crypto
- Haun Ventures

### Tier-3 (Adds credibility)
- CoinFund
- Distributed Global
- Robot Ventures
- Nascent

### Not VC-Backed
- Check team background instead
- Look for: ex-Uniswap, ex-Polygon, ex-Ethereum devs
- Open source with strong GitHub activity

---

## Red Flags

### Immediate Disqualification
- No official Twitter account
- Website with no SSL certificate
- Contract not verified on Etherscan
- Team with history of rug pulls
- Token contract similar to known scams

### Warning Signs (Include in report)
- Urgent "act now" messaging
- Requests for private keys
- Requires sending ETH to unknown address
- Domain similar to popular project
  - Example: `arbitrum-airdrop.io` (fake)
  - Real: `arbitrum.io`
- Unverified Telegram as main channel
- Anonymous team with no track record

### Community Reports
- Check Twitter replies for scam reports
- Search: `[project name] scam` or `[project name] rug`
- Check: r/ethfinance, r/defi for warnings

---

## Quick Evaluation Checklist

Before grading any project:

```
□ Funding confirmed? (RootData/Crunchbase)
  └─ If yes: What tier VC? How much?

□ Community size? (Twitter followers)
  └─ 10k+ = S/A candidate
  └─ 5k-10k = A/B candidate
  └─ <5k = B/C candidate

□ Official channels? (Twitter, Discord, Docs)
  └─ All present? = Good sign
  └─ Missing Discord? = Caution
  └─ Only Telegram? = Warning

□ Token status?
  └─ Confirmed airdrop? = +1 grade
  └─ Points system? = Neutral
  └─ No token info? = Speculative

□ Cost analysis?
  └─ Free testnet? = Low risk
  └─ <$5 mainnet? = Acceptable
  └─ >$20? = Explain clearly

□ Security check?
  └─ Official URLs verified?
  └─ Contract verified?
  └─ No red flags?
```

---

## Example Evaluations

### Example 1: Scroll
```
Funding: $80M from Polychain (Tier-1) ✓
Community: 250k Twitter followers ✓
Stage: Mainnet live ✓
Token: Points system, confirmed future token ✓
Cost: <$5 for bridge ✓
→ Grade: S
```

### Example 2: New Layer 3
```
Funding: $5M from Tier-2 VC ✓
Community: 3k Twitter followers △
Stage: Testnet ✓
Token: Not confirmed △
Cost: Free ✓
→ Grade: B (upgrade to A after mainnet)
```

### Example 3: Unknown Project
```
Funding: None found ✗
Community: 500 Twitter followers ✗
Stage: Claim "mainnet" but no users ✗
Token: "Airdrop confirmed" but no details ⚠️
Cost: Requires 0.1 ETH deposit 🚩
→ Grade: EXCLUDE (likely scam)
```
