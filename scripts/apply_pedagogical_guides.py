import json
import os
from googletrans import Translator

CHAPTERS_DIR = 'app_core/chapters'

MASTER_GUIDES = {
    # Part 1: Partnership
    1: """# Pedagogical Solving Guide: Introduction to Partnership
**Step 1: Profit and Loss Appropriation Account**
- Credit side: Net Profit, Interest on Drawings.
- Debit side: Interest on Capital, Partner Salary/Commission.
**Step 2: Partners' Capital/Current Account**
- Fixed Capital Method: Only capital introduction/withdrawal goes to Capital A/c. Everything else (Interest, Salary, Share of Profit) goes to Current A/c.
- Fluctuating Capital Method: Everything goes to Capital A/c.""",

    2: """# Pedagogical Solving Guide: Final Accounts
**Step 1: Analyze the Trial Balance**
- Sort items: Direct expenses/incomes (Trading), Indirect expenses/incomes (P&L), Appropriations (P&L App), Assets/Liabilities (Balance Sheet).
**Step 2: Process Adjustments (Dual Effects)**
- *Closing Stock:* Credit Trading A/c, Asset in Balance Sheet (Lower of cost or market value).
- *Outstanding Expenses:* Add to expense in Trading/P&L, Liability in Balance Sheet.
- *Depreciation:* Debit P&L A/c, Deduct from Asset in Balance Sheet.
**Step 3: Sequential Flow**
- Close Trading A/c (Gross Profit) -> P&L A/c (Net Profit) -> P&L App A/c (Divisible Profit) -> Capital A/c -> Balance Sheet.""",

    3: """# Pedagogical Solving Guide: Valuation of Goodwill
**Step 1: Average Profit Method**
- Total Profit / Number of Years. Goodwill = Average Profit * Number of Years of Purchase.
**Step 2: Super Profit Method**
- Normal Profit = Capital Employed * Expected Rate of Return.
- Super Profit = Average Profit - Normal Profit.
- Goodwill = Super Profit * Number of Years of Purchase.
**Step 3: Capitalization Method**
- Capitalized Value = (Average Profit / Expected Rate of Return) * 100.
- Goodwill = Capitalized Value - Capital Employed.""",

    4: """# Pedagogical Solving Guide: Reconstruction of Partnership
**Step 1: Calculate Sacrificing/Gaining Ratio**
- Sacrifice Ratio = Old Share - New Share.
- Gain Ratio = New Share - Old Share.
**Step 2: Revaluation Account**
- Debit: Decrease in Assets, Increase in Liabilities.
- Credit: Increase in Assets, Decrease in Liabilities.
- Transfer Revaluation Profit/Loss to Old Partners in Old Ratio.""",

    5: """# Pedagogical Solving Guide: Admission of a Partner
**Step 1: New Profit Sharing Ratio & Sacrifice Ratio**
- Calculate Sacrifice Ratio (Old Share - New Share) to distribute premium for goodwill.
**Step 2: Revaluation Account**
- Record changes in asset/liability values. Distribute profit/loss to old partners in old ratio.
**Step 3: Treatment of Goodwill**
- If new partner brings cash: Debit Cash, Credit Premium for Goodwill. Distribute premium to old partners in sacrificing ratio.
**Step 4: Accumulated Reserves**
- Distribute General Reserve and P&L Credit balance to old partners in old ratio.""",

    6: """# Pedagogical Solving Guide: Retirement / Death of a Partner
**Step 1: Gaining Ratio**
- Gain Ratio = New Share - Old Share. Used for distributing retiring partner's share of goodwill.
**Step 2: Revaluation and Reserves**
- Prepare Revaluation A/c and distribute profit/loss to ALL partners in old ratio.
- Distribute accumulated reserves to ALL partners in old ratio.
**Step 3: Settlement of Retiring Partner**
- Transfer final balance to Retiring Partner's Loan A/c or pay in cash.""",

    7: """# Pedagogical Solving Guide: Dissolution of Partnership
**Step 1: Realisation Account**
- Transfer all Assets (except cash/bank) to Debit side at book value.
- Transfer all external Liabilities to Credit side at book value.
**Step 2: Realising Assets & Paying Liabilities**
- When assets are sold: Credit Realisation A/c (By Cash/Bank).
- When liabilities are paid: Debit Realisation A/c (To Cash/Bank).
- Dissolution expenses: Debit Realisation A/c.
**Step 3: Final Settlement**
- Distribute Realisation Profit/Loss to partners in their profit-sharing ratio. Close Capital A/cs by paying or receiving cash.""",

    # Part 2: Company Accounts
    8: """# Pedagogical Solving Guide: Share Capital
**Step 1: Issue of Shares**
- Bank A/c Dr. to Share Application A/c.
- Share Application A/c Dr. to Share Capital A/c (and Securities Premium if any).
**Step 2: Calls in Arrears / Advance**
- Arrears: Deduct from called-up capital.
- Advance: Show as current liability.
**Step 3: Forfeiture of Shares**
- Share Capital A/c Dr. (with called-up amount)
- To Calls in Arrears A/c (unpaid amount)
- To Share Forfeiture A/c (paid amount)
**Step 4: Re-issue of Forfeited Shares**
- Any discount on re-issue is debited to Share Forfeiture A/c. Balance goes to Capital Reserve.""",

    9: """# Pedagogical Solving Guide: Debentures
**Step 1: Issue of Debentures**
- Can be issued at par, premium, or discount.
- Loss on Issue of Debentures (Premium on redemption + Discount on issue) is debited at the time of allotment.
**Step 2: Interest on Debentures**
- Calculate interest on the face value of debentures, regardless of issue price.
**Step 3: Redemption of Debentures**
- Create Debenture Redemption Reserve (DRR) and Debenture Redemption Investment (DRI) as per statutory limits before redemption.""",

    10: """# Pedagogical Solving Guide: Company Final Accounts
**Step 1: Statement of Profit and Loss (Schedule III)**
- Revenue from Operations + Other Income = Total Revenue.
- Deduct Expenses (Cost of Materials, Employee Benefit Expenses, Finance Costs, Depreciation) to get Profit Before Tax.
**Step 2: Balance Sheet (Schedule III)**
- **Equity and Liabilities:** Shareholders' Funds (Capital, Reserves), Non-Current Liabilities, Current Liabilities.
- **Assets:** Non-Current Assets (Fixed Assets, Non-Current Investments), Current Assets (Inventories, Trade Receivables, Cash).""",

    11: """# Pedagogical Solving Guide: Analysis of Financial Statements
**Step 1: Comparative Statements**
- Calculate absolute change = Current Year - Previous Year.
- Calculate percentage change = (Absolute Change / Previous Year) * 100.
**Step 2: Common-Size Statements**
- Balance Sheet: Base is Total Assets/Liabilities (100%). Express each item as a percentage of the total.
- P&L Statement: Base is Revenue from Operations (100%). Express each item as a percentage of Revenue.""",

    12: """# Pedagogical Solving Guide: Accounting Ratios
**Step 1: Liquidity Ratios**
- Current Ratio = Current Assets / Current Liabilities.
- Liquid Ratio = Liquid Assets / Current Liabilities.
**Step 2: Solvency Ratios**
- Debt to Equity = Long Term Debt / Shareholders' Funds.
**Step 3: Profitability Ratios**
- Gross Profit Ratio = (Gross Profit / Net Sales) * 100.
- Net Profit Ratio = (Net Profit / Net Sales) * 100.""",

    13: """# Pedagogical Solving Guide: Cash Flow Statement (AS-3)
**Step 1: Operating Activities**
- Start with Net Profit before Tax.
- Add non-cash/non-operating expenses (Depreciation, Interest paid, Loss on sale of assets).
- Deduct non-operating incomes (Interest received, Profit on sale of assets).
- Adjust for Working Capital (Add decrease in Current Assets & increase in Current Liabilities; Deduct opposite).
**Step 2: Investing Activities**
- Cash inflows: Sale of fixed assets/investments, Interest/Dividend received.
- Cash outflows: Purchase of fixed assets/investments.
**Step 3: Financing Activities**
- Cash inflows: Issue of shares/debentures, Long-term borrowings.
- Cash outflows: Repayment of loans, Interest paid, Dividend paid."""
}

def apply_guides():
    translator = Translator()
    # Cache translations to save time and API calls
    translation_cache = {}
    
    print("Translating Master Guides...")
    for ch_num, guide_en in MASTER_GUIDES.items():
        try:
            guide_hi = translator.translate(guide_en, src='en', dest='hi').text
            guide_gu = translator.translate(guide_en, src='en', dest='gu').text
        except Exception as e:
            print(f"Translation failed for Ch {ch_num}: {e}")
            guide_hi = guide_en
            guide_gu = guide_en
        translation_cache[ch_num] = (guide_en, guide_hi, guide_gu)
        print(f"Translated Guide for Chapter {ch_num}")

    total_injected = 0
    
    for f_name in os.listdir(CHAPTERS_DIR):
        if not (f_name.startswith('gseb_class12_accounts_ch') and f_name.endswith('.json')):
            continue
            
        try:
            # Extract chapter number from filename (e.g., gseb_class12_accounts_ch13.json -> 13)
            ch_str = f_name.split('_ch')[1].split('.')[0].split('_')[0]
            ch_num = int(ch_str)
        except:
            continue
            
        if ch_num not in translation_cache:
            continue
            
        file_path = os.path.join(CHAPTERS_DIR, f_name)
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        blocks = data.get('blocks', [])
        modified = False
        
        guide_en, guide_hi, guide_gu = translation_cache[ch_num]
        
        for block in blocks:
            sol = block.get('solution', '')
            if sol and len(sol) < 200:
                block['solution'] = guide_en
                block['solution_hi'] = guide_hi
                block['solution_gu'] = guide_gu
                modified = True
                total_injected += 1
                
        if modified:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
                f.write('\n')
            print(f"Injected Master Guide into {f_name}")
            
    print(f"Successfully injected Pedagogical Master Guides into {total_injected} lazy solutions!")

if __name__ == '__main__':
    apply_guides()
