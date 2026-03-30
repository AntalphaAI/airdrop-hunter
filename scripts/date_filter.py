"""
Date Filter for Airdrop Hunter
Removes outdated content from search results

Usage: Call from Code Node in Coze Workflow
Input: search_results (list of dicts with 'title' and 'snippet')
Output: final_list (filtered list, max 5 items)
"""

import re
from datetime import datetime

async def main(args):
    # Input: search results list from Search Node
    results = args.get("search_results", [])
    current_year = datetime.now().year
    filtered_results = []

    for item in results:
        content = str(item.get("snippet", "")) + str(item.get("title", ""))
        
        # Find all year patterns (20XX)
        years_found = re.findall(r'20[0-9]{2}', content)
        
        # Filter out old years (before current year)
        old_years = [y for y in years_found if int(y) < current_year]
        
        # Keep if: mentions current year OR has no old year references
        if str(current_year) in content or not old_years:
            filtered_results.append(item)

    return {
        "final_list": filtered_results[:5]  # Top 5 recent & relevant results
    }


# ========== TEST CASES ==========
if __name__ == "__main__":
    # Test input
    test_input = {
        "search_results": [
            {"title": "2024 Airdrop Guide", "snippet": "Old guide from 2024"},
            {"title": "Latest 2026 Testnet", "snippet": "New opportunity in 2026"},
            {"title": "Testnet Checklist", "snippet": "No year mentioned"},
            {"title": "2025 Summary", "snippet": "Last year's recap 2025"},
            {"title": "2023 DeFi Report", "snippet": "Outdated report"},
            {"title": "2027 Future Airdrop", "snippet": "Upcoming project"},
            {"title": "Item 7", "snippet": "Test truncation"},
            {"title": "Item 8", "snippet": "Test truncation"},
            {"title": "Item 9", "snippet": "Test truncation"},
            {"title": "Item 10", "snippet": "Test truncation"},
            {"title": "Item 11", "snippet": "Should be truncated"},
        ]
    }
    
    # Expected output: items 2, 3, 6, 7, 8 (max 5, filtered out old years)
    import asyncio
    result = asyncio.run(main(test_input))
    print("Filtered results:", result)
    print("Count:", len(result["final_list"]))
    assert len(result["final_list"]) == 5, "Should return max 5 items"
