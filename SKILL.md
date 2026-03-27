---
name: airdrop-hunter
description: Daily Web3 airdrop interaction guide covering Grade S high-value tasks, zero-cost testnets, and trending opportunities aggregation; use when users ask for daily airdrop tasks or zero-cost opportunities
dependency:
  plugin:
    - web_search
    - link_reader
---

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

Ready to hunt? Let's find your next opportunity! 🎯

---

# Airdrop Hunter

**Cut through the noise. Only the most valuable interactions.** An automated intelligence tool designed for Web3 hunters, dehydrating complex airdrop information across the web into a daily streamlined "action checklist".

---

## Prerequisites: Required Plugins

**⚠️ This Skill is blind without plugins.** Configure the following plugins in Coze Plugins page before using:

### Required Plugins

| Plugin | Purpose | Priority |
|--------|---------|----------|
| **Google Search** / **Bing Search** | Search web articles for airdrop news | 🔴 Required |
| **Link Reader** | Read details from long tweets or Medium articles | 🔴 Required |
| **Twitter/X Search** (if available) | Direct access to X for real-time alpha | 🟡 Optional |

### Why These Plugins Matter

1. **Google Search / Bing Search** (Required)
   - Primary source for airdrop articles and announcements
   - Search queries: `"airdrop alpha"`, `"testnet checklist"`, `"site:x.com airdrop"`
   - Without this: Cannot fetch any external airdrop information

2. **Link Reader** (Required)
   - When search finds a long tweet thread or Medium article
   - Extracts key details: funding amounts, deadlines, interaction steps
   - Without this: Cannot deep-dive into articles for actionable info

3. **Twitter/X Search** (Optional but Recommended)
   - Web3's alpha lives on X first
   - Direct search for: `#airdrop`, `#testnet`, project handles
   - Workaround if unavailable: Use Google Search with `site:x.com` prefix

### Plugin Configuration Checklist
```
□ Google Search OR Bing Search enabled
□ Link Reader enabled
□ (Optional) Twitter/X Search enabled if available
□ Test: Search "airdrop alpha today" to verify
```

---

## Core Feature: Scam Alert System

**This Skill automatically detects and warns about the following risks based on search results:**

### 1. Fake Claim Websites

**Detection Pattern:**
```
⚠️ Phishing Alert: Watch for [project-airdrop-claim.xyz] and similar fake domains
✅ Official Domain: [project.io] (verify from Twitter bio)
```

**Common Phishing Patterns:**
- Hyphenated knockoffs: `scroll-airdrop.io`, `arbitrum-claims.com`
- Action words in domain: `claim-`, `free-`, `reward-`, `airdrop-`
- Unusual TLDs: `.xyz`, `.top`, `.click`, `.work` (when not official)
- Number patterns: `airdrop2026.xyz`, `claim-now123.net`

**Verification Rule:**
- Always compare with official domain from project's Twitter bio
- Character-by-character domain check
- Reject if domain contains suspicious patterns above

---

### 2. Social Engineering Scams

**Detection Pattern:**
```
⚠️ Telegram/DM Scam Alert: "You won [X] airdrop, click link to claim"
✅ Official projects NEVER send claim links via DM
✅ Official projects NEVER ask for gas fees or private keys in DM
```

**Red Flags:**
- Unsolicited DM claiming "you won" or "eligible for airdrop"
- Request to click a link to "claim" or "connect wallet"
- Request for gas fee payment or private key
- Impersonation of official support accounts

**Safe Behavior:**
- Never click links from unknown Telegram users
- Never share private keys or seed phrases
- Verify announcements only from official Twitter/Discord
- Block and report suspicious DMs

---

### 3. Fake Token Scams

**Detection Pattern:**
```
⚠️ Counterfeit Token Alert: "XXX" token exists on DEX but is NOT the official token
✅ Official [Project] token is listed on: Binance, OKX, Bybit, Coinbase, etc.
```

**Scam Pattern:**
- Token with same/similar name on DEX before official launch
- Liquidity pool with suspicious contract address
- No verification on CoinGecko/CoinMarketCap
- Only tradable on obscure DEXes

**Verification Rule:**
- Check if token is listed on major exchanges (Binance, OKX, Bybit, Coinbase)
- Verify contract address on official website
- Check CoinGecko/CoinMarketCap for official listing
- Reject tokens that only exist on DEX without major exchange listing

---

### Auto-Warning Output Format

When any risk is detected, this Skill will include a **Scam Alert Section** in the response:

```markdown
## ⚠️ SCAM ALERT - CRITICAL WARNINGS

### Fake Claim Website Detected
⚠️ Phishing Alert: [list suspicious domains]
✅ Official Domain: [verified official domain]

### Social Scam Warning
⚠️ Beware of Telegram/DM messages: "You won [X] airdrop, click link to claim"
✅ Official projects NEVER send claim links via private message
✅ Official projects NEVER ask for gas fees or private keys

### Fake Token Warning
⚠️ Counterfeit token "[XXX]" exists on DEX, NOT affiliated with [Project]
✅ Official token listed on: [Binance, OKX, Bybit, etc.]

---
Proceed with caution. Always verify through official channels.
```

---

## Critical: Self-Reflection Protocol

**If the Bot shows unstable behavior, add this to the System Prompt ending:**

```
Reflect before responding:
1. Did I check the date of the source? (Is it recent or outdated?)
2. Is the step actionable? (Can user actually do this?)
3. If no data is found, admit it instead of hallucinating.
```

**Why This Matters:**

| Problem | Self-Reflection Prevents |
|---------|-------------------------|
| Outdated info | Checks source date before sharing |
| Vague steps | Ensures steps are actionable |
| Hallucination | Admits when data not found |

**Implementation:**

Add to System Prompt:
```
Before generating any response, ask yourself:
- Is this information from the past 24-48 hours?
- Can the user complete these steps today?
- Am I making up details because I couldn't find real data?

If any answer is NO, revise your response:
- For outdated data: Note the date and suggest re-searching
- For vague steps: Request clarification or provide alternatives
- For no data: Say "I couldn't find reliable information" honestly
```

**Red Flags That Require Self-Reflection:**

```
You're about to share information from 2024 or earlier
You're describing steps without specific links
You're guessing funding amounts or deadlines
You're recommending a project you can't verify exists
You're not sure if the faucet link still works
```

**Correct Self-Reflection Example:**

```
Initial thought: "Scroll airdrop requires bridging 0.1 ETH"

After reflection: "Wait, I should verify:
- Is this from an official source?
- Is this the current requirement?
- Let me check if requirements changed recently"

Final response: "Based on [source date], the recommendation was X. 
However, please verify on official Scroll Twitter for latest updates."
```

---

## [Final Integrity Check] - Self-Correction Protocol

**Add this to the BOTTOM of your System Prompt:**

```
[Final Integrity Check]

Before outputting ANY airdrop task, execute this mental verification:

□ DATE VERIFICATION:
  - Is this project still valid in 2026?
  - PROHIBITED: Recommending already-airdropped projects ($ARB, $STRK, $ZK, $OP, etc.)
  - If token already launched → EXCLUDE from recommendations

□ LINK VERIFICATION:
  - Does the link look like an official domain?
  - REJECT obvious phishing patterns:
    * airdrop-claims-2026.net
    * claim-rewards-now.io
    * free-token-xyz.com
  - Official domains match: projectname.io, projectname.com, docs.projectname.xyz

□ ACTIONABILITY VERIFICATION:
  - If Gas required → Have I clearly informed the user of cost?
  - If testnet → Have I provided working faucet link?
  - If deadline → Have I stated it explicitly?

□ UNCERTAINTY HANDLING:
  If ANY point above is uncertain, add this note:
  "⚠️ Requires further verification - please check official channels"
```

**Why This Protocol Matters:**

| Check | Prevents | Example |
|-------|----------|---------|
| Date Check | Recommending dead projects | Arbitrum airdrop ended 2023 |
| Link Check | Phishing scams | `arb-airdrop-claim.net` vs `arbitrum.io` |
| Gas Check | Hidden costs | User surprises with $50 gas fee |
| Uncertainty Note | Misleading confidence | Honest admission vs fake certainty |

---

### Already-Airdropped Projects (DO NOT RECOMMEND)

These projects have already distributed tokens. Do NOT include in daily reports:

```
⛔ COMPLETED AIRDROPS (Token Launched):
- Arbitrum ($ARB) - March 2023
- Optimism ($OP) - June 2022
- Starknet ($STRK) - February 2024
- zkSync ($ZK) - June 2024
- Celestia ($TIA) - October 2023
- Sui ($SUI) - April 2023
- Aptos ($APT) - October 2022
- Bonk ($BONK) - December 2022
- Jupiter ($JUP) - January 2024
- Wormhole ($W) - April 2024
- Eigenlayer ($EIGEN) - October 2024
- Scroll - Token pending but points system active
```

**Exception:** Projects with ongoing points/farming systems CAN be recommended even after token launch, but MUST note: "Token already launched - points may have future value"

---

### Phishing Domain Detection Guide

**Red Flags - DO NOT TRUST:**

```
🚨 Phishing Patterns:
- Contains "claim", "free", "reward", "airdrop" in domain
- Hyphenated knockoffs: scroll-airdrop.io, arbitrum-claims.com
- Random numbers: airdrop2026.xyz, claim-now123.net
- Unusual TLDs: .xyz, .top, .click, .work (when not official)
- Subdomains: claim.official-project.xyz (not real)
```

**Green Flags - LIKELY SAFE:**

```
✅ Official Patterns:
- Matches project Twitter bio link
- Listed in project docs/GitHub
- Uses standard TLDs: .io, .com, .xyz (if official)
- Has SSL certificate (https://)
- Listed on ecosystem page
```

**Verification Steps:**
1. Check project's official Twitter bio for website
2. Compare domains character by character
3. Search "[project name] scam" on Twitter
4. Check if URL is in project's official docs

---

### Actionability Requirements

**When Recommending Tasks:**

| Task Type | Required Information |
|-----------|---------------------|
| Mainnet Interaction | Gas cost estimate, deadline, official link |
| Testnet Task | Working faucet link, step-by-step guide |
| NFT Mint | Mint price, date/time, official collection link |
| Quest/Campaign | Platform (Galxe/Zealy), deadline, reward |

**Example - Complete Task Entry:**

```
✅ COMPLETE:
1. Scroll: Bridge 0.01 ETH to Scroll network
   └─ Gas: $3-5 (L1 to L2 bridge)
   └─ Deadline: No deadline (points ongoing)
   └─ Link: https://scroll.io/bridge (official)
   └─ Note: Points system active, future airdrop potential

❌ INCOMPLETE:
1. Scroll: Bridge ETH
   └─ (Missing: gas cost, link, deadline)
   ⚠️ Requires further verification
```

---

## Advanced: Scheduled Automation (Daily Push)

To make this a true "daily report", configure Coze Workflow for automated daily delivery:

### Workflow Setup: Daily_Airdrop_Push

**Create a new workflow with the following nodes:**

```
┌─────────────────┐
│  Start Node     │ → Scheduled Trigger: Every day at 10:00 AM
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Search Node    │ → Auto-search daily keywords
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  AI Node        │ → Aggregate into daily report format
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  End Node       │ → Output to chat or Telegram via Webhook
└─────────────────┘
```

### Node Configuration Details

#### 1. Start Node: Scheduled Trigger
```
Trigger Type: Scheduled
Schedule: Daily
Time: 10:00 AM (configurable to your timezone)
Timezone: UTC+8 (adjust as needed)
```

#### 2. Search Node: Multi-Query Search
```
Plugin: Google Search / Bing Search

Queries to execute:
1. "airdrop alpha" [current_date] crypto
2. "testnet checklist" latest
3. "galxe campaign" active OR live
4. site:x.com "airdrop" after:24h

Output: List of URLs and snippets
```

---

### ⚠️ CRITICAL: Code Node for Date Filtering

**Why You Need This:**
AI-based date filtering is unreliable and may "cheat" or miss outdated content. A Code Node provides **100% accuracy** with hard filtering.

**Step 1: Insert Code Node**
```
Location: BETWEEN Search Node and AI Node
Click: + button → Select "Code" node → Choose "Python"
```

**Step 2: Add Date Filtering Code**

```python
import re
from datetime import datetime

async def main(args):
    # Input: search results list from Search Node
    results = args.get("search_results", [])
    current_year = datetime.now().year
    filtered_results = []

    for item in results:
        content = str(item.get("snippet", "")) + str(item.get("title", ""))
        
        # Find year patterns like 2024, 2025
        years_found = re.findall(r'202[0-5]', content)
        
        # Keep if: mentions current year OR has no old year references
        if str(current_year) in content or not years_found:
            filtered_results.append(item)
        else:
            # Discard if only contains 2025 or earlier
            continue

    return {
        "final_list": filtered_results[:5]  # Top 5 recent & relevant results
    }
```

**Step 3: Configure Node Connections**

```
Updated Workflow:

┌─────────────────┐
│  Start Node     │ → Scheduled Trigger
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Search Node    │ → Returns search_results
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Code Node      │ → Hard date filter (THIS IS NEW!)
│  (Python)       │ → Output: final_list
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  AI Node        │ → Input: final_list (not raw search_results)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  End Node       │ → Deliver report
└─────────────────┘
```

**Step 4: Variable Mapping**

| From Node | Variable | To Node | Input Name |
|-----------|----------|---------|------------|
| Search Node | `search_results` | Code Node | `args["search_results"]` |
| Code Node | `final_list` | AI Node | `{final_list}` |

**Why This Code Works:**

| Feature | Benefit |
|---------|---------|
| `re.findall(r'202[0-5]')` | Catches ALL years 2020-2025 |
| `current_year` check | Dynamically adapts to current year |
| `filtered_results[:5]` | Prevents token overflow |
| Hard filter | 100% accuracy, no AI "laziness" |

**Testing the Code Node:**

```
Test Input (Search Results):
[
  {"title": "2024 Airdrop Guide", "snippet": "Old guide from 2024"},
  {"title": "Latest 2026 Testnet", "snippet": "New opportunity in 2026"},
  {"title": "Testnet Checklist", "snippet": "No year mentioned"}
]

Expected Output (final_list):
[
  {"title": "Latest 2026 Testnet", "snippet": "New opportunity in 2026"},
  {"title": "Testnet Checklist", "snippet": "No year mentioned"}
]

Result: 2024 article REMOVED ✅
```

**Common Issues & Fixes:**

| Issue | Cause | Fix |
|-------|-------|-----|
| No results passed | Variable name mismatch | Check `search_results` matches Search Node output |
| All results filtered | Year detection too strict | Adjust regex pattern |
| Code error | Missing import | Ensure `import re` is at top |

---

#### 3. AI Node: Report Generation
```
Prompt Template:
"You are the Airdrop Hunter agent. Based on the search results below, generate a daily airdrop report following this format:

📅 [DATE] Airdrop Daily Report

🔥 TOP PRIORITY (Grade S/A)
[Project]: [Action] | [Cost] | [Deadline]

🧪 ZERO-COST TESTNETS (Grade B)
[Project]: [Faucet] | [Time]

📅 TODAY'S DEADLINES
[Deadlines list]

⚠️ SECURITY ALERTS
[Warnings]

Search Results:
{search_results}"

Output: Formatted daily report
```

#### 4. End Node: Delivery Options
```
Option A: Direct Chat Output
- Output the report directly to the Coze chat interface
- Users can view in the conversation history

Option B: Telegram Push (via Webhook)
- Configure Telegram Bot API
- Webhook URL: https://api.telegram.org/bot[TOKEN]/sendMessage
- Payload:
  {
    "chat_id": "[CHANNEL_ID]",
    "text": "{daily_report}",
    "parse_mode": "Markdown"
  }

Option C: Discord Webhook
- Webhook URL: [Your Discord channel webhook]
- Format: Embed with fields for each section
```

### Workflow Test Checklist
```
□ Start node triggers at scheduled time
□ Search node returns relevant results
□ AI node generates properly formatted report
□ End node delivers to chosen destination
□ Verify report content quality
□ Check timezone is correct
```

### Alternative: Manual Trigger
If scheduled automation is not available, users can manually trigger:
```
User types: "daily report"
Skill executes: Full search → Generate report → Display
```

---

## Core Features

### 1. Network-Wide Scanning
Automatically track earliest airdrop signals from:
- **X (Twitter)**: KOLs, official project accounts, alpha groups
- **Mirror.xyz**: Project blogs and announcements
- **Galxe**: Campaign quests and OATs
- **Research Channels**: RootData, DefiLlama, Messari

### 2. Project Grading System
Dynamic scoring based on:
| Grade | Criteria | Action Priority |
|-------|----------|-----------------|
| **S** | Tier-1 VC backing (a16z, Paradigm), $50M+ funding, mainnet live with points system | MUST DO |
| **A** | Reputable VCs, $10M+ funding, confirmed token or imminent TGE | HIGH |
| **B** | Testnet stage, early potential, zero-cost interaction | SPECULATIVE |

See [references/evaluation-criteria.md](references/evaluation-criteria.md) for detailed grading criteria.

### 3. Minimalist Output
Cut all the fluff. Direct delivery of:
```
[Project] + [Action] + [Cost/Faucet Link]
```

### 4. Security Scanning
Auto-check interaction site safety:
- Verify official domains via Twitter bio
- Flag suspicious similar domains (e.g., "scroll-airdrop.io" vs "scroll.io")
- Contract verification on Etherscan/Arbiscan

---

## Daily Report Template

```
📅 [DATE] Airdrop Daily Report

🔥 TOP PRIORITY (Grade S/A)
1. [Project Name]: [Action] | [Est. Cost] | [Deadline]
   └─ Why: [1-line reasoning]
   └─ Link: [official URL]

🧪 ZERO-COST TESTNETS (Grade B)
1. [Project Name]: [Faucet] | [Time Required]
   └─ Chain: [testnet name]

📅 TODAY'S DEADLINES
- [Project]: [Task] ends in [X hours]
- [Galxe Campaign]: Ends [date]

⚠️ SECURITY ALERTS
- Verify all URLs through official Twitter accounts
- Never share private keys or seed phrases
- [Current phishing warning if applicable]
```

---

## Operational Workflow

### Step 1: Multi-Source Search

**Search Strategy by Source:**

#### 1.1 Web Articles (Google Search / Bing Search)
```
Primary Queries:
- "airdrop alpha" [current month] [current year]
- "testnet checklist" crypto latest
- "galxe campaign" active
- "layer3 quest" current

Date-Restricted Queries (past 24-48 hours):
- "airdrop" after:today
- "testnet faucet" after:yesterday
```

#### 1.2 Twitter/X Search
```
If Twitter/X Search plugin is available:
- #airdrop #alpha
- #testnet #faucet
- from:[KOL_handle] airdrop

Workaround using Google Search:
- site:x.com "airdrop alpha"
- site:x.com "testnet checklist"
- site:x.com from:[handle] airdrop
```

#### 1.3 Deep-Dive Reading (Link Reader)
When search returns:
- Long tweet threads (>5 tweets) → Use Link Reader to extract key points
- Medium articles → Use Link Reader to get full content
- Mirror.xyz posts → Use Link Reader for complete text
- Project documentation → Use Link Reader for interaction guides

**Example Link Reader Usage:**
```
Search finds: "https://mirror.xyz/0x.../airdrop-guide"
Action: Call Link Reader to extract:
  - Funding amount
  - Interaction steps
  - Deadline
  - Cost estimate
```

### Step 2: Filter & Grade
For each opportunity found:
1. Check funding status (RootData, Crunchbase)
2. Verify community traction (Twitter followers, Discord activity)
3. Determine grade (S/A/B)
4. Estimate cost and time requirement

### Step 3: Security Verification
- Cross-check URLs with official Twitter bio
- Verify contract addresses on block explorer
- Search for scam reports in Twitter replies

### Step 4: Generate Report
Format output using the template above, sorted by priority.

---

## Search Query Templates

### Daily Scanning Queries
```bash
# High-value airdrops (S/A grade)
"airdrop alpha" [current_month] funded OR backed OR raised

# Testnet opportunities (B grade)
"testnet faucet" [current_month] free OR zero

# Campaigns and quests
"galxe campaign" active OR live
"layer3 quest" crypto

# Twitter alpha (if using Google Search workaround)
site:x.com "airdrop" "testnet" after:24h
site:x.com from:airdropalert
```

### Project-Specific Queries
```bash
# Check if project has airdrop confirmed
"[project_name]" airdrop token confirmed

# Check funding background
"[project_name]" funding raised series

# Check scam reports
"[project_name]" scam OR rug OR phishing
```

---

## How to Use

### Quick Commands
In Coze/Claw interface, simply type:

| Command | Action |
|---------|--------|
| `daily report` | Get latest 24-hour airdrop checklist |
| `any zero-cost?` | Filter for free testnet opportunities |
| `check [project]` | Get specific project airdrop status |
| `S-grade tasks` | Show only Grade S high-priority tasks |

### Usage Examples

**User**: `daily report`

**Agent Response**:
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

## Resource Index

- **Grading Criteria**: [references/evaluation-criteria.md](references/evaluation-criteria.md)
- **Trusted Sources**: [references/trusted-sources.md](references/trusted-sources.md)

---

## Important Notes

### Before Listing Any Project
- [ ] Funding confirmed via RootData or Crunchbase
- [ ] Official Twitter exists and is active
- [ ] Website has valid SSL certificate
- [ ] Contract verified on block explorer
- [ ] No scam reports in community

### Red Flags (Never List)
- Anonymous team with no track record
- Domain similar to popular project
- Requires sending ETH to unknown address
- No official Twitter or website
- Urgent "act now" pressure tactics

### Disclaimer
This Skill provides information only, not financial advice. Always:
- Do your own research (DYOR)
- Never invest more than you can afford to lose
- Verify all information before interacting
- Use separate wallets for airdrop hunting

---

## Changelog

### v1.0.0
- Initial release
- Multi-source search capability
- S/A/B grading system
- Daily report template
- Security verification checks

---

## Phase 1: Functionality Testing Guide

Before deploying to production, verify each plugin works correctly.

### Test 1: Search Capability

**Command:**
```
Search for latest airdrop tasks about Linea or Scroll in the past 24 hours.
```

**What to Check:**
- [ ] Right panel logs show Google Search / Bing Search was actually called
- [ ] Returned links are recent (check dates are current month/year)
- [ ] Not returning outdated data from 2024 or older
- [ ] At least 3-5 relevant results returned

**Pass Criteria:**
- Plugin invoked successfully
- Results are time-relevant
- Links are from credible sources

---

### Test 2: Link Reader Capability

**Command:**
```
Read this link and summarize the airdrop tasks: [Insert a recent Mirror or Medium airdrop tutorial URL]
```

**What to Check:**
- [ ] Link Reader plugin is called
- [ ] Returns full article content, not just title
- [ ] Extracts key details: project name, interaction steps, deadlines
- [ ] Correctly identifies if it's a testnet or mainnet task

**Sample Test URL:**
```
https://mirror.xyz/0x... (replace with actual Mirror post)
https://medium.com/... (replace with actual Medium article)
```

**Pass Criteria:**
- Full content extracted
- Key action items identified
- Deadlines and costs captured

---

### Test 3: Format Compliance

**Command:**
```
Generate today's airdrop daily report.
```

**What to Check:**

Compare output against this template:

```
✅ Required Sections:
□ 📅 Date header present
□ 🔥 TOP PRIORITY (Grade S/A) section exists
□ 🧪 ZERO-COST TESTNETS (Grade B) section exists
□ 📅 TODAY'S DEADLINES section exists
□ ⚠️ SECURITY ALERTS section exists

✅ Required Format per Task:
□ Project name present
□ Action steps specified
□ Cost/Time estimate included
□ "Why" reasoning provided
□ Official link included

✅ Security Checks:
□ Phishing warnings present
□ "Verify URLs" reminder included
□ No endorsement of suspicious projects
```

**Pass Criteria:**
- All 5 sections present
- Each task has complete info (name, action, cost, link)
- Security warnings included
- No formatting errors (broken Markdown, missing brackets)

---

### Test 4: Edge Cases

**Test 4a: No Results Found**
```
Command: "Search for airdrop tasks for project xyz123fake"
Check: Returns graceful message, not error
```

**Test 4b: Ambiguous Query**
```
Command: "Is Arbitrum good?"
Check: Asks for clarification or provides balanced info
```

**Test 4c: Security Threat**
```
Command: "Check this link: [suspicious/fake domain]"
Check: Warns user about potential phishing
```

---

### Quick Test Checklist

Run all tests and mark results:

```
□ Test 1: Search Capability      [PASS / FAIL]
□ Test 2: Link Reader           [PASS / FAIL]
□ Test 3: Format Compliance     [PASS / FAIL]
□ Test 4: Edge Cases            [PASS / FAIL]

Overall: ___/4 Passed
```

**If any test fails:**
1. Check plugin is enabled in Coze
2. Verify plugin has proper permissions
3. Review search queries in SKILL.md
4. Test plugin independently outside Skill

---

### Troubleshooting Common Issues

| Issue | Likely Cause | Solution |
|-------|--------------|----------|
| No search results | Plugin not enabled | Enable Google/Bing Search |
| Outdated results | No date filter | Add "after:today" to query |
| Link Reader fails | URL blocked/paywalled | Try different URL source |
| Missing sections | Prompt template issue | Review AI Node prompt |
| Wrong format | Template not followed | Add explicit format examples |

---

## Phase 2: Boundary & Stress Testing

Test how the Skill handles extreme cases to prevent hallucinations or crashes.

### Test 5: Cold Start (No Data Scenario)

**Command:**
```
Search for airdrop information about 'Mars-L2-Protocol' (a non-existent project).
```

**Expected Behavior:**
```
✅ CORRECT Response:
"I couldn't find any information about 'Mars-L2-Protocol'. 
This project either doesn't exist or has no public airdrop information.
If this is a new project, try searching again later."

❌ WRONG Response:
- Fabricating fake interaction steps
- Making up funding amounts
- Creating fake Twitter handles
- Hallucinating a website URL
```

**Pass Criteria:**
- Honestly admits no information found
- Does NOT fabricate any details
- Suggests alternative actions (wait, verify project exists)

---

### Test 6: Information Overload (Token Limit)

**Command:**
```
Summarize ALL airdrop tasks across the entire web today.
```

**What to Check:**

| Checkpoint | Expected Behavior |
|------------|-------------------|
| Token overflow | Response completes without cutting off mid-sentence |
| Priority sorting | Only shows TOP 5-10 most important tasks |
| Grading applied | Tasks are graded S/A/B, not random listing |
| Summary format | Brief 1-line per task, not full articles |

**Expected Response Structure:**
```
Due to the large volume of airdrops, here are the TOP 5 priority tasks:

🔥 TOP 5 (Grade S/A)
1. [Most important] - Brief summary
2. [Second most] - Brief summary
...
5. [Fifth] - Brief summary

💡 For full details on specific projects, ask me to "check [project name]"
```

**Pass Criteria:**
- Response completes successfully
- Tasks are prioritized (not random)
- User is guided to ask for specifics

---

### Test 7: Security Verification (Scam Detection)

**Command:**
```
Is this project safe? [Insert URL of known phishing/scam project]
```

**Sample Scam Indicators to Test:**

| Test Case | Expected Warning |
|-----------|------------------|
| Fake domain (e.g., "arbitrum-airdrop.io") | ⚠️ **WARNING: Suspicious domain detected** |
| No official Twitter | ⚠️ **WARNING: No verified social presence** |
| Anonymous team | ⚠️ **WARNING: Anonymous team, high risk** |
| Requires wallet approval | ⚠️ **WARNING: Suspicious contract interaction** |
| Recent rug pull history | ⚠️ **WARNING: Project flagged for previous scams** |

**Expected Response Format:**
```
⚠️ **SECURITY WARNING** ⚠️

🚩 Red Flags Detected:
- Domain similar to popular project but NOT official
- No verified Twitter account found
- Multiple scam reports in community

✅ Official Project:
- Real URL: [official domain]
- Real Twitter: @official_handle

Recommendation: DO NOT INTERACT with this link.
```

**Pass Criteria:**
- Bold ⚠️ warnings present
- Specific red flags identified
- Official project details provided for comparison
- Clear "DO NOT INTERACT" warning

---

### Test 8: Ambiguous Query Handling

**Test 8a: Vague Request**
```
Command: "Is Arbitrum good?"
Expected: Asks clarifying question OR provides balanced overview
```

**Test 8b: Conflicting Info**
```
Command: "Project X says they have airdrop but their Twitter is suspended."
Expected: Highlights the red flag, suggests caution
```

**Test 8c: Time-Sensitive Request**
```
Command: "What airdrops are ending TODAY?"
Expected: Filters by deadline, shows only urgent tasks
```

---

### Quick Boundary Test Checklist

```
□ Test 5: Cold Start (No Data)       [PASS / FAIL]
□ Test 6: Information Overload        [PASS / FAIL]
□ Test 7: Security/Scam Detection     [PASS / FAIL]
□ Test 8: Ambiguous Queries           [PASS / FAIL]

Overall: ___/4 Passed
```

**Critical Failure Indicators:**
- 🚨 Fabricates information when none exists
- 🚨 Response cuts off mid-sentence (token overflow)
- 🚨 Fails to warn about obvious scams
- 🚨 Provides dangerous wallet interaction advice

If any critical failure occurs, DO NOT deploy to production.

---

### Edge Case Response Templates

Use these templates when encountering edge cases:

**Template 1: Project Not Found**
```
I couldn't find reliable information about [project name]. 

Possible reasons:
- Project may not exist or is very new
- May be misspelled
- Could be a private/test project

Suggestions:
- Verify the project name
- Check if they have an official Twitter
- Wait for more public information
```

**Template 2: Suspected Scam**
```
⚠️ **SECURITY ALERT** ⚠️

This project has been flagged for:
- [Specific red flag 1]
- [Specific red flag 2]

Official alternatives:
- [Official project name]: [Official URL]

**DO NOT** interact with suspicious links or approve unknown contracts.
```

**Template 3: Information Overload**
```
Found [X] airdrop opportunities today.

To prevent information overload, here are the **TOP 5 priority tasks**:

1. [Project] - [Grade] - [Brief action]
...

For full details on any specific project, ask: "check [project name]"
```

---

## Phase 3: Automation Workflow Testing

Test the scheduled automation to ensure reliable daily delivery.

### Test 9: Manual Workflow Trigger

**Purpose:** Verify the workflow executes correctly without waiting for scheduled time.

**Steps:**
```
1. Navigate to Workflow editor in Coze
2. Click "Run" or "Test" button (top right corner)
3. Monitor execution in real-time
```

**What to Check:**

| Node | Expected Status | Checkpoint |
|------|-----------------|------------|
| Start Node | 🟢 Green | Triggered successfully |
| Search Node | 🟢 Green | Returned search results |
| AI Node | 🟢 Green | Generated formatted report |
| End Node | 🟢 Green | Delivered output |

**Visual Check:**
```
All nodes should show GREEN checkmarks:

┌─────────────┐
│  Start ✅   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Search ✅   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   AI ✅     │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   End ✅    │
└─────────────┘
```

**Pass Criteria:**
- All 4 nodes show green status
- No red/yellow error indicators
- Execution completes in < 30 seconds

---

### Test 10: Variable Passing Verification

**Purpose:** Ensure data flows correctly between nodes.

**Critical Check: Search → AI Node**

**Common Bug:**
```
❌ WRONG: AI node only receives titles
Search returns: [
  "Scroll Airdrop Guide",
  "zkSync Testnet Tutorial"
]

AI generates: Generic/empty report (no details)

---

✅ CORRECT: AI node receives full content
Search returns: [
  {
    "title": "Scroll Airdrop Guide",
    "url": "https://...",
    "snippet": "Bridge 0.01 ETH to Scroll network...",
    "content": "Full article text with steps, costs, deadlines..."
  }
]

AI generates: Detailed report with actionable steps
```

**How to Verify:**
```
1. Click on Search node after execution
2. Check "Output" or "Results" panel
3. Verify full content is present, not just titles
4. Click on AI node
5. Check "Input" panel - should match Search output
6. Check "Output" panel - should have complete report
```

**Debug Checklist:**
```
□ Search node output contains "content" or "body" field
□ AI node input matches Search node output
□ AI node output contains all 5 sections
□ No empty/missing data in final report
```

---

### Test 11: Scheduled Trigger Timing

**Purpose:** Verify automation runs at correct time.

**Steps:**
```
1. Set trigger to a near-future time (e.g., 5 minutes from now)
2. Wait for automated execution
3. Check execution logs
```

**Time Configuration Checklist:**
```
□ Timezone is correct (UTC+8 or your local timezone)
□ Trigger is set to DAILY frequency
□ Time is set correctly (e.g., 10:00 AM)
□ Workflow is ENABLED (not paused)
```

**Common Issues:**

| Issue | Cause | Solution |
|-------|-------|----------|
| Workflow doesn't trigger | Workflow paused | Enable workflow |
| Wrong time execution | Timezone mismatch | Adjust timezone |
| Skipped execution | Rate limiting | Reduce frequency |
| Multiple executions | Duplicate triggers | Check for duplicates |

---

### Test 12: Output Delivery Verification

**Purpose:** Verify report is delivered to the correct destination.

**Test by Destination Type:**

#### Option A: Chat Output
```
Check: Report appears in Coze chat interface
Verify: All sections visible, formatting correct
```

#### Option B: Telegram Webhook
```
Check: Message delivered to Telegram channel
Verify: Markdown renders correctly
Test: Emojis display properly (🔥 🧪 ⚠️)
```

#### Option C: Discord Webhook
```
Check: Embed appears in Discord channel
Verify: Links are clickable
Test: Fields are properly formatted
```

**Telegram Webhook Test:**
```bash
# Manual test command (replace tokens)
curl -X POST "https://api.telegram.org/bot[TOKEN]/sendMessage" \
  -d chat_id="[CHAT_ID]" \
  -d text="📅 Test Report\n\n🔥 Test successful!" \
  -d parse_mode="Markdown"
```

---

### Workflow Debugging Guide

**If Search Node Fails:**
```
1. Check plugin permissions
2. Verify search query syntax
3. Test query manually in Google/Bing
4. Check rate limiting status
```

**If AI Node Produces Empty Report:**
```
1. Check Search node output format
2. Verify variable passing: {search_results} → AI input
3. Check AI prompt template
4. Look for token limit errors in logs
```

**If End Node Fails:**
```
1. Verify webhook URL is correct
2. Check Telegram/Discord bot permissions
3. Test webhook with curl command
4. Check for firewall/network issues
```

---

### Quick Automation Test Checklist

```
□ Test 9: Manual Trigger          [PASS / FAIL]
□ Test 10: Variable Passing       [PASS / FAIL]
□ Test 11: Scheduled Timing       [PASS / FAIL]
□ Test 12: Output Delivery        [PASS / FAIL]

Overall: ___/4 Passed
```

**Critical Checks Before Production:**
```
✅ All 4 nodes execute with green status
✅ Variable passing verified (content not just titles)
✅ Test execution at scheduled time successful
✅ Output delivered to correct destination
```

---

### Full Testing Summary

```
==========================================
AIRDROP HUNTER - COMPLETE TEST RESULTS
==========================================

Phase 1: Functionality Testing (4 tests)
□ Test 1: Search Capability
□ Test 2: Link Reader
□ Test 3: Format Compliance
□ Test 4: Edge Cases
Phase 1 Score: ___/4

Phase 2: Boundary & Stress Testing (4 tests)
□ Test 5: Cold Start (No Data)
□ Test 6: Information Overload
□ Test 7: Security/Scam Detection
□ Test 8: Ambiguous Queries
Phase 2 Score: ___/4

Phase 3: Automation Workflow (4 tests)
□ Test 9: Manual Trigger
□ Test 10: Variable Passing
□ Test 11: Scheduled Timing
□ Test 12: Output Delivery
Phase 3 Score: ___/4

==========================================
TOTAL SCORE: ___/12 PASSED
==========================================

Deployment Recommendation:
✅ 12/12: Ready for production
⚠️ 9-11/12: Minor fixes needed
🚨 <9/12: Critical issues, do not deploy
```

---

## Post-Deployment Monitoring

After deploying to production, monitor:

**Daily Checks:**
- [ ] Workflow executes on time
- [ ] Report quality is consistent
- [ ] No user complaints about missing info
- [ ] No security incidents reported

**Weekly Checks:**
- [ ] Review search query effectiveness
- [ ] Update grading criteria if needed
- [ ] Check for new phishing patterns
- [ ] Gather user feedback

---

## Phase 4: User Simulation Testing

Simulate real user scenarios to verify natural language understanding and filtering logic.

### Test 13: Cost-Based Recommendation

**Command:**
```
I only have 0.01 ETH, which project is suitable for me?
```

**Expected Behavior:**

**✅ CORRECT Response:**
```
Based on your 0.01 ETH budget (~$30-40), here are suitable options:

🧪 ZERO-COST TESTNETS (Recommended for your budget)
1. [Project A]: Free testnet interaction
   └─ Faucet: [URL]
   └─ Time: 10 min

2. [Project B]: Free testnet swap
   └─ Faucet: [URL]
   └─ Time: 15 min

💰 LOW-COST MAINNET (Within your budget)
1. [Project C]: Bridge to Layer 2
   └─ Cost: $2-5 gas
   └─ Potential: Grade A project

⚠️ BUDGET TIP:
- Keep 0.005 ETH reserve for future gas fees
- Start with testnets to build transaction history
- Consider spreading across 2-3 projects for diversification
```

**❌ WRONG Responses:**
- Suggesting projects requiring 0.1+ ETH
- No budget consideration at all
- Ignoring user's financial constraints
- No risk management advice

**Evaluation Criteria:**
```
□ Identifies user's budget constraint
□ Recommends projects within budget
□ Suggests zero-cost alternatives
□ Provides budget management tips
□ Prioritizes testnets for low-budget users
```

---

### Test 14: Tag-Based Filtering

**Command:**
```
Give me a zero-cost testnet link.
```

**Expected Behavior:**

**✅ CORRECT Response:**
```
Here's a zero-cost testnet opportunity:

🧪 [Project Name] Testnet
├─ Faucet: https://faucet.example.com
├─ Network: [Testnet Name]
├─ Time Required: ~10 minutes
├─ Steps:
│   1. Claim testnet tokens from faucet
│   2. Connect wallet to [URL]
│   3. Complete swap/bridge task
│   4. Claim OAT/NFT reward
│
└─ Why Recommended:
   - Backed by [VC names]
   - Mainnet launch expected [date]
   - Zero cost, potential future airdrop

📌 Quick Start:
1. Visit faucet link above
2. Follow steps in order
3. No real funds needed
```

**❌ WRONG Responses:**
- Returns mainnet projects requiring gas fees
- No direct faucet/testnet link provided
- Generic response without actionable steps
- Forgets to explain WHY this specific project

**Evaluation Criteria:**
```
□ Direct faucet/testnet link provided
□ Marked as "zero-cost" clearly
□ Step-by-step instructions included
□ Time estimate given
□ Project background explained
□ No mainnet projects suggested (user asked for zero-cost)
```

---

### Test 15: Specific Project Inquiry

**Command:**
```
What do you think about Scroll airdrop?
```

**Expected Behavior:**

**✅ CORRECT Response:**
```
📊 Scroll Airdrop Analysis

🔥 Grade: A (High Priority)

💼 Background:
- Funding: $80M (Polychain, Sequoia)
- Stage: Mainnet live (Oct 2023)
- TVL: $1.2B+

🎯 Current Status:
- Points system active
- Multiple campaigns running
- No confirmed airdrop date yet

💡 Recommended Actions:
1. Bridge ETH to Scroll: $3-5 gas
2. Use DEXs (SyncSwap, Uniswap)
3. Mint NFT collections
4. Complete Galxe campaigns

💰 Cost Estimate: $10-30 total
⏰ Time Required: 2-3 hours
📈 Airdrop Probability: High (75%+)

⚠️ Risks:
- No guaranteed airdrop
- Opportunity cost of locked liquidity
- Competition from sybils
```

**❌ WRONG Responses:**
- No grading or evaluation
- Missing action steps
- No cost/time estimates
- Ignores risks
- Fabricates airdrop date

**Evaluation Criteria:**
```
□ Project graded (S/A/B)
□ Funding/background provided
□ Actionable steps listed
□ Cost and time estimated
□ Risks clearly stated
□ No fabricated information
```

---

### Test 16: Multi-Intent Query

**Command:**
```
I want zero-cost testnets but also interested in high-ROI mainnet projects under $10.
```

**Expected Behavior:**

**✅ CORRECT Response:**
```
I'll provide both options for you:

🧪 ZERO-COST TESTNETS (Start Here)
1. [Project A]: [Faucet Link] | 10 min
2. [Project B]: [Faucet Link] | 15 min

💰 MAINNET UNDER $10 (High ROI Potential)
1. [Project C]: Bridge + Swap | $5-8 gas | Grade A
   └─ Why: Confirmed airdrop, low entry cost

2. [Project D]: NFT Mint | $3-5 | Grade B
   └─ Why: Low cost, speculative upside

📊 Strategy Recommendation:
1. Start with testnets (free, build history)
2. Then try 1-2 low-cost mainnet projects
3. Total budget: ~$10-15
4. Diversify across ecosystems

⚠️ Remember: Never spend more than you can afford to lose.
```

**Evaluation Criteria:**
```
□ Both parts of query addressed
□ Zero-cost options provided
□ Mainnet options under $10 provided
□ Logical prioritization given
□ Clear separation of categories
```

---

### Test 17: Conflicting Information

**Command:**
```
Project X's Twitter says airdrop is confirmed, but their Discord says it's not. Which is true?
```

**Expected Behavior:**

**✅ CORRECT Response:**
```
⚠️ CONFLICTING INFORMATION DETECTED

🔍 Investigation Results:
- Twitter (@ProjectX): Posted "Airdrop confirmed" [date]
- Discord: Mod said "No airdrop planned" [date]

📊 Analysis:
1. Twitter marketing may be misleading
2. Discord statement is likely more accurate
3. Official docs have no token info

💡 Recommendation:
- WAIT for official announcement
- Check project's blog/docs for tokenomics
- Verify team statements before interacting
- Avoid high-cost interactions until confirmed

🔐 Safety First:
- Don't trust Twitter-only announcements
- Cross-reference with official channels
- When in doubt, ask in Discord with verified role
```

**Evaluation Criteria:**
```
□ Acknowledges conflicting information
□ Investigates both sources
□ Provides neutral analysis
□ Recommends caution
□ Suggests verification steps
□ No biased assumption
```

---

### User Simulation Test Checklist

```
□ Test 13: Cost-Based Recommendation    [PASS / FAIL]
□ Test 14: Tag-Based Filtering          [PASS / FAIL]
□ Test 15: Specific Project Inquiry     [PASS / FAIL]
□ Test 16: Multi-Intent Query           [PASS / FAIL]
□ Test 17: Conflicting Information      [PASS / FAIL]

Phase 4 Score: ___/5
```

---

### User Simulation Best Practices

**When User Asks About Budget:**
1. Always acknowledge their constraint
2. Recommend options WITHIN budget
3. Suggest zero-cost alternatives first
4. Provide budget management tips
5. Never recommend over-budget options

**When User Requests Specific Tags:**
1. Filter results by requested tag (zero-cost, testnet, etc.)
2. Provide direct links immediately
3. Include step-by-step instructions
4. Add time/cost estimates
5. Explain WHY it matches their request

**When User Asks About Specific Project:**
1. Provide comprehensive analysis
2. Include grade, funding, status
3. List actionable steps
4. Mention risks and probability
5. Don't fabricate information

**When User Has Multiple Intents:**
1. Address EACH part of the query
2. Use clear section headers
3. Provide strategy/recommendation
4. Help user prioritize
5. Consider their constraints

---

## Complete Testing Framework Summary

```
===============================================
AIRDROP HUNTER - FULL TEST FRAMEWORK (28 Tests)
===============================================

Phase 1: Functionality Testing (4 tests)
□ Test 1: Search Capability
□ Test 2: Link Reader
□ Test 3: Format Compliance
□ Test 4: Edge Cases
Phase 1 Score: ___/4

Phase 2: Boundary & Stress Testing (4 tests)
□ Test 5: Cold Start (No Data)
□ Test 6: Information Overload
□ Test 7: Security/Scam Detection
□ Test 8: Ambiguous Queries
Phase 2 Score: ___/4

Phase 3: Automation Workflow (4 tests)
□ Test 9: Manual Trigger
□ Test 10: Variable Passing
□ Test 11: Scheduled Timing
□ Test 12: Output Delivery
Phase 3 Score: ___/4

Phase 5: Integration Testing (4 tests)
□ Test 18: End-to-End Workflow
□ Test 19: Plugin Failure Recovery
□ Test 20: Rate Limiting Handling
□ Test 21: Concurrent Request Handling
Phase 5 Score: ___/4

Phase 6: Production Readiness (7 tests)
□ Test 22: Data Freshness Validation
□ Test 23: False Positive Detection
□ Test 24: Language & Tone Consistency
□ Test 25: Memory & Context Retention
□ Test 26: Output Formatting Edge Cases
□ Test 27: Security Stress Test
□ Test 28: Code Node Integration
Phase 6 Score: ___/7

===============================================
TOTAL SCORE: ___/28 PASSED
===============================================

Deployment Recommendation:
✅ 28/28: Production ready, enterprise-grade quality
✅ 25-27/28: Production ready, minor improvements needed
⚠️ 20-24/28: Testing needed, not recommended for production
🚨 <20/28: Critical issues, requires major fixes
===============================================
```

---

## Phase 5: Integration Testing

Test all components working together as a complete system.

### Test 18: End-to-End Workflow

**Command:**
```
Generate today's daily airdrop report with all checks.
```

**Test Flow:**
```
1. Search Node → Fetches 10 results
2. Code Node → Filters to 5 recent results
3. AI Node → Generates formatted report
4. End Node → Delivers to destination
```

**Verification Checklist:**
```
□ Search returns results within 10 seconds
□ Code Node filters out 2024-2025 content
□ AI Node generates all 5 required sections
□ Report includes at least 3 valid projects
□ All links are clickable/valid
□ No broken Markdown formatting
□ Execution completes in < 60 seconds total
```

**Pass Criteria:**
- All 4 nodes execute successfully
- Report quality meets standards
- No errors in execution logs

---

### Test 19: Plugin Failure Recovery

**Simulate:** Disable one plugin temporarily

**Test Case A: Search Plugin Disabled**
```
Command: "Find airdrop tasks"
Expected: "Unable to search. Please enable Google Search or Bing Search plugin."
```

**Test Case B: Link Reader Disabled**
```
Command: "Read details of [article URL]"
Expected: "Unable to read article content. Please enable Link Reader plugin."
```

**Verification Checklist:**
```
□ Graceful error message shown
□ Does NOT crash or hang
□ Suggests solution to user
□ Logs show clear error indication
```

---

### Test 20: Rate Limiting Handling

**Command:** Execute 10 rapid requests in succession

**Expected Behavior:**
```
Request 1-5: Normal responses
Request 6-10: May see rate limiting

Correct handling:
- "Search temporarily limited, please wait 30 seconds"
- NOT: Empty response or crash
```

**Verification Checklist:**
```
□ Rate limit message is user-friendly
□ System recovers automatically after cooldown
□ No data corruption
□ Logs show rate limit event
```

---

### Test 21: Concurrent Request Handling

**Simulate:** Multiple users requesting reports simultaneously

**Test Setup:**
```
User A: "daily report"
User B: "zero-cost testnets"
User C: "check Scroll airdrop"
```

**Expected Behavior:**
```
□ Each user receives correct response
□ No cross-contamination between requests
□ All responses properly formatted
□ No timeout errors
```

---

## Phase 6: Production Readiness Testing

Final validation before deployment.

### Test 22: Data Freshness Validation

**Command:**
```
Show me the date of your most recent airdrop information.
```

**Expected Response:**
```
✅ CORRECT:
"My most recent search was conducted on [current date].
The latest airdrop opportunities are from the past 24-48 hours."

❌ WRONG:
- Cannot determine date
- Information is clearly outdated
- No date mentioned
```

**Verification Checklist:**
```
□ Date is within past 48 hours
□ User can see when data was fetched
□ Outdated data is flagged
```

---

### Test 23: False Positive Detection

**Command:**
```
Is there an airdrop for Bitcoin? (There is no Bitcoin airdrop)
```

**Expected Response:**
```
✅ CORRECT:
"There is no Bitcoin airdrop. Bitcoin is already fully distributed 
through mining. Be wary of any 'Bitcoin airdrop' claims - they are 
likely scams."

❌ WRONG:
- Fabricating fake Bitcoin airdrop
- Not clarifying that BTC has no airdrop
- Missing scam warning
```

**Verification Checklist:**
```
□ Correctly identifies false claims
□ Warns about potential scams
□ Does not hallucinate opportunities
```

---

### Test 24: Language & Tone Consistency

**Test Multiple Queries for Tone:**
```
Query 1: "Give me airdrop tasks"
Query 2: "Can you please help me find zero-cost opportunities?"
Query 3: "URGENT: need airdrop NOW"
```

**Expected Behavior:**
```
□ Professional but helpful tone across all
□ Does not mirror user's aggressive/informal tone
□ Consistent formatting regardless of query style
□ Same quality output for all query types
```

---

### Test 25: Memory & Context Retention

**Multi-Turn Conversation:**
```
Turn 1: "What's the best airdrop today?"
Response: Recommends Project A

Turn 2: "Is it zero-cost?"
Expected: Knows "it" refers to Project A

Turn 3: "Any alternatives?"
Expected: Suggests different projects, doesn't repeat Project A
```

**Verification Checklist:**
```
□ Maintains context across conversation
□ Pronouns resolved correctly
□ No repetitive suggestions
□ Builds on previous responses
```

---

### Test 26: Output Formatting Edge Cases

**Test Case A: No Projects Found**
```
Command: "Find airdrops for project-xyz-nonexistent"
Expected: Clean message, no broken formatting
```

**Test Case B: Single Project Found**
```
Expected: Proper formatting even with only 1 result
```

**Test Case C: Many Projects Found (>10)**
```
Expected: Properly formatted list, no overflow
```

**Verification Checklist:**
```
□ Markdown renders correctly in all cases
□ No broken tables or lists
□ Emojis display properly
□ Links are clickable
□ Section headers properly separated
```

---

### Test 27: Security Stress Test

**Command:**
```
"I found this link: arbitrum-free-claim-2026.xyz - is it safe?"
```

**Expected Response:**
```
✅ CORRECT:
"⚠️ SECURITY WARNING ⚠️

🚨 RED FLAGS DETECTED:
- Domain contains 'free-claim' (phishing pattern)
- Domain not from official Arbitrum
- Suspicious hyphenated naming pattern

✅ OFFICIAL Arbitrum:
- Website: arbitrum.io
- Twitter: @arbitrum

❌ DO NOT visit the link you provided.
❌ DO NOT connect wallet or sign transactions.

This is a likely phishing attempt."
```

**Verification Checklist:**
```
□ Multiple red flags identified
□ Official alternative provided
□ Clear DO NOT instructions
□ Urgent warning tone
□ Explains WHY it's dangerous
```

---

### Test 28: Code Node Integration

**Verify Code Node Execution:**

**Test Input:**
```json
{
  "search_results": [
    {"title": "2024 Airdrop Guide", "snippet": "Old content"},
    {"title": "2026 New Testnet", "snippet": "Fresh opportunity"},
    {"title": "Generic Guide", "snippet": "No year mentioned"}
  ]
}
```

**Expected Code Node Output:**
```json
{
  "final_list": [
    {"title": "2026 New Testnet", "snippet": "Fresh opportunity"},
    {"title": "Generic Guide", "snippet": "No year mentioned"}
  ]
}
```

**Verification:**
```
□ 2024 content filtered OUT
□ 2026 content kept
□ Undated content kept
□ Output limited to 5 items
□ No Python errors in logs
```

---

## Phase 7: Final Acceptance Testing

### Complete Acceptance Checklist

```
===============================================
PRE-DEPLOYMENT ACCEPTANCE CHECKLIST
===============================================

CORE FUNCTIONALITY (Must Pass ALL):
□ Search plugin returns relevant results
□ Code Node filters outdated content
□ Link Reader extracts full article content
□ Report generates with all 5 sections
□ All quick commands work (daily report, zero-cost, check, S-grade)

SECURITY (Must Pass ALL):
□ Phishing domains detected and warned
□ No recommendation of already-airdropped projects
□ Gas costs always disclosed
□ Official links verified
□ Scam warnings prominent

RELIABILITY (Must Pass ALL):
□ Graceful handling of missing plugins
□ No crashes on empty/invalid input
□ Rate limiting handled gracefully
□ Concurrent requests handled correctly
□ All error messages user-friendly

OUTPUT QUALITY (Must Pass ALL):
□ Markdown formatting correct
□ All links clickable
□ Dates within 48 hours
□ No hallucinated information
□ Consistent professional tone

AUTOMATION (Must Pass ALL):
□ Workflow triggers on schedule
□ Variable passing verified
□ Output delivers to correct destination
□ All 4 nodes show green status
□ Execution time < 60 seconds

INTEGRITY CHECKS (Must Pass ALL):
□ Self-reflection protocol executed
□ Final integrity check performed
□ "Requires verification" note when uncertain
□ No outdated (2024-2025) projects recommended

===============================================
PASS CRITERIA: ALL items above must be checked
FAIL: ANY unchecked item = NOT ready for production
===============================================
```

---

### Deployment Sign-Off

```
===============================================
DEPLOYMENT APPROVAL
===============================================

Test Date: ________________
Tester Name: ________________
Skill Version: airdrop-hunter v1.0.0

Test Results Summary:
□ Phase 1: Functionality (4/4 passed)
□ Phase 2: Boundary (4/4 passed)
□ Phase 3: Automation (4/4 passed)
□ Phase 4: User Simulation (5/5 passed)
□ Phase 5: Integration (4/4 passed)
□ Phase 6: Production Readiness (7/7 passed)
□ Phase 7: Acceptance (ALL checked)

Total Score: ___/28 tests passed

Issues Found: ________________________________
Issues Resolved: □ Yes □ No □ N/A

APPROVED FOR PRODUCTION: □ Yes □ No

Sign-off: ________________ Date: ________________
===============================================
```

---

## Troubleshooting Guide

### Common Issues & Solutions

| Issue | Likely Cause | Solution |
|-------|--------------|----------|
| Empty search results | Plugin not enabled | Enable Google/Bing Search |
| Outdated content | Code Node missing | Add Code Node with date filter |
| Missing sections | AI prompt incomplete | Update prompt template |
| Broken links | Link Reader failed | Check plugin permissions |
| Rate limiting | Too many requests | Add delay between requests |
| Token overflow | Too many results | Limit Code Node output to 5 |
| Format errors | Markdown issues | Check template formatting |
| No output delivered | Webhook misconfigured | Verify Telegram/Discord settings |

### Performance Benchmarks

| Metric | Target | Status |
|--------|--------|--------|
| Search execution | < 5 seconds | □ |
| Code Node execution | < 1 second | □ |
| AI generation | < 20 seconds | □ |
| Total workflow | < 60 seconds | □ |
| Memory usage | < 100MB | □ |
| Token usage | < 10,000 | □ |

---

## Maintenance Schedule

### Daily Tasks
- [ ] Verify workflow executed on time
- [ ] Check report quality
- [ ] Monitor for user complaints

### Weekly Tasks
- [ ] Update completed airdrops list
- [ ] Review search query effectiveness
- [ ] Check for new phishing patterns
- [ ] Update grading criteria if needed

### Monthly Tasks
- [ ] Full regression test (all 28 tests)
- [ ] Update dependencies
- [ ] Review and update references
- [ ] Performance optimization review

## Quick Reference: Test Commands

```bash
# Phase 1: Functionality
"Search for latest airdrop tasks about Linea or Scroll in the past 24 hours."
"Read this link and summarize the airdrop tasks: [URL]"
"Generate today's airdrop daily report."

# Phase 2: Boundary
"Search for airdrop information about 'Mars-L2-Protocol'."
"Summarize ALL airdrop tasks across the entire web today."
"Is this project safe? [suspicious URL]"

# Phase 3: Automation (Manual workflow test)
# Navigate to Workflow editor → Click "Run"

# Phase 4: User Simulation
"I only have 0.01 ETH, which project is suitable for me?"
"Give me a zero-cost testnet link."
"What do you think about Scroll airdrop?"
"I want zero-cost testnets but also interested in high-ROI mainnet projects under $10."
"Project X's Twitter says airdrop confirmed but Discord says no. Which is true?"
```
