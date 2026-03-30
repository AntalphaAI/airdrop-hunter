# Output Template Specification

## Required Sections

Every output must include these 5 sections:

---

### Section 1: Date & Overview

```markdown
📅 [DATE] Airdrop Daily Report

🔍 Scanned: [X] sources | Found: [Y] opportunities
⏰ Last updated: [TIMESTAMP]
```

---

### Section 2: S/A Grade Tasks

```markdown
## 🔥 HIGH PRIORITY (Grade S/A)

### 1. [Project Name] - [Grade]
**Action**: [What to do]
**Gas**: $[amount] | **Deadline**: [date or "Ongoing"]
**Why**: [Brief reason - VC backing, funding, etc.]
**Link**: [Official URL]

**Steps**:
1. [Step 1]
2. [Step 2]
3. [Step 3]

⚠️ Risk: [Any specific risk]
```

---

### Section 3: Zero-Cost Testnets

```markdown
## 🧪 ZERO-COST TESTNETS (Grade B)

### 1. [Project Name]
**Time**: [Estimated time]
**Reward**: [Potential airdrop]

**Steps**:
1. Get testnet tokens: [Faucet URL]
2. [Action 1]
3. [Action 2]

🔗 Links: [Official URLs]
```

---

### Section 4: Scam Alerts

```markdown
## ⚠️ SCAM ALERTS

### [Scam Type]
[Warning details following scam-detection.md format]

---
Proceed with caution. Always verify through official channels.
```

*Only include if scams detected. Otherwise, omit this section.*

---

### Section 5: Quick Tips

```markdown
## 💡 QUICK TIPS

- [Tip 1]
- [Tip 2]
- [Tip 3]
```

---

## Formatting Rules

### Links
- All links must be clickable: `[text](URL)`
- Only official domains
- Verify before including

### Costs
- Always disclose gas costs
- Use range: `$1-3` not exact amounts
- Highlight free opportunities

### Deadlines
- Be specific: `March 31, 2026`
- Or indicate: `Ongoing`, `No deadline`

### Risk Warnings
- Use ⚠️ emoji for warnings
- Be specific about risks
- Never downplay dangers

---

## Example Output

```markdown
📅 March 30, 2026 Airdrop Daily Report

🔍 Scanned: 12 sources | Found: 8 opportunities
⏰ Last updated: 2026-03-30 10:00 UTC

---

## 🔥 HIGH PRIORITY (Grade S/A)

### 1. Scroll - Grade A
**Action**: Bridge ETH to Scroll network
**Gas**: $2-5 | **Deadline**: Ongoing (Points active)
**Why**: Polychain backed ($80M), mainnet live, points system running
**Link**: https://scroll.io/bridge

**Steps**:
1. Connect wallet to Scroll bridge
2. Bridge min 0.01 ETH from Ethereum
3. Complete transactions on Scroll

⚠️ Risk: Points system may not convert to tokens

---

## 🧪 ZERO-COST TESTNETS (Grade B)

### 1. Linea Testnet
**Time**: 10 minutes
**Reward**: Potential future airdrop

**Steps**:
1. Get testnet ETH: https://faucet.goerli.linea.build
2. Swap tokens on Linea testnet
3. Mint testnet NFT

🔗 Links: https://linea.build

---

## 💡 QUICK TIPS

- Always verify links on official Twitter before clicking
- Set aside a dedicated wallet for airdrop hunting
- Track your interactions with a spreadsheet
- Never share your seed phrase with anyone
```
