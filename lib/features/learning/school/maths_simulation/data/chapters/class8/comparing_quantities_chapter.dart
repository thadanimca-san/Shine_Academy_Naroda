import '../../../models/chapter_model.dart';
final ChapterModel class8ComparingQuantitiesChapter = ChapterModel(
  standard: 8, subject: "Mathematics", chapterId: "cls8_math_comparingquantities", chapterName: "Comparing Quantities",
  concepts: ["Recalling ratios, percentages, profit, loss and discount.", "Sales tax and GST.", "Compound interest and the relation between CI and SI."],
  formulas: [
    FormulaDerivation(formulaName: "Amount with Compound Interest", expression: "A = P(1 + R/100)ⁿ", derivationSteps: [
      "In compound interest, interest is calculated on the principal plus previously earned interest, for each period.",
      "After 1 year, Amount = P + P×R/100 = P(1 + R/100).",
      "This new amount becomes the principal for the next year, so after n years, Amount = P(1 + R/100)ⁿ.",
    ]),
  ],
  fillInTheBlanks: [
    QuestionItem(id: "cq8_1", question: "Interest calculated on the principal as well as on the interest already earned is called [ compound interest / simple interest ].", answer: "compound interest"),
    QuestionItem(id: "cq8_2", question: "In compound interest, the interest for each period is added to the principal, a process called [ compounding / discounting ].", answer: "compounding"),
    QuestionItem(id: "cq8_3", question: "For the same principal, rate and time, compound interest is generally [ greater than or equal to / less than ] simple interest.", answer: "greater than or equal to"),
    QuestionItem(id: "cq8_4", question: "The tax charged by the government on the sale of goods and services is called [ sales tax / income tax ].", answer: "sales tax"),
    QuestionItem(id: "cq8_5", question: "GST stands for [ Goods and Services Tax / General Sales Tax ].", answer: "Goods and Services Tax"),
    QuestionItem(id: "cq8_6", question: "The price of an item including sales tax/GST is called the [ bill amount / marked price ].", answer: "bill amount"),
    QuestionItem(id: "cq8_7", question: "A reduction on the marked price of goods, to attract buyers, is called a [ discount / tax ].", answer: "discount"),
    QuestionItem(id: "cq8_8", question: "Discount = Marked Price − [ Selling Price / Cost Price ].", answer: "Selling Price"),
    QuestionItem(id: "cq8_9", question: "A quantity expressed as parts per hundred is called a [ percentage / ratio ].", answer: "percentage"),
    QuestionItem(id: "cq8_10", question: "When compounded half-yearly, the rate is [ halved and the number of periods doubled / doubled and periods halved ] compared to yearly compounding.", answer: "halved and the number of periods doubled"),
    QuestionItem(id: "cq8_11", question: "Compound interest itself is calculated as [ Amount − Principal / Amount + Principal ].", answer: "Amount − Principal"),
    QuestionItem(id: "cq8_12", question: "The price at which a shopkeeper buys goods from a manufacturer or wholesaler is the [ cost price / marked price ].", answer: "cost price"),
  ],
  numericalProblems: [
    NumericalProblem(id: "cq8n1", question: "Find the compound interest on ₹10,000 at 10% per annum for 2 years.", given: ["P = ₹10,000", "R = 10%", "n = 2 years"], solutionSteps: ["A = P(1 + R/100)ⁿ", "= 10000(1.1)²", "= 10000 × 1.21 = ₹12,100", "CI = A − P = 12100 − 10000 = ₹2,100"], numericAnswer: 2100, unit: "₹"),
    NumericalProblem(id: "cq8n2", question: "A shirt marked at ₹1200 is sold for ₹960. Find the discount percentage.", given: ["MP = ₹1200", "SP = ₹960"], solutionSteps: ["Discount = 1200 − 960 = ₹240", "Discount % = (240/1200) × 100", "= 20%"], numericAnswer: 20, unit: "%"),
    NumericalProblem(id: "cq8n3", question: "Find the GST amount on a product worth ₹2000 with 12% GST.", given: ["Value = ₹2000", "GST rate = 12%"], solutionSteps: ["GST = 12% of 2000", "= (12/100) × 2000", "= ₹240"], numericAnswer: 240, unit: "₹"),
    NumericalProblem(id: "cq8n4", question: "Find the compound interest on ₹8000 at 5% per annum for 3 years.", given: ["P = ₹8000", "R = 5%", "n = 3 years"], solutionSteps: ["A = 8000(1.05)³", "= 8000 × 1.157625 ≈ ₹9,261", "CI = 9261 − 8000 = ₹1,261"], numericAnswer: 1261, unit: "₹"),
    NumericalProblem(id: "cq8n5", question: "Find the difference between CI and SI on ₹5000 at 10% for 2 years.", given: ["P = ₹5000", "R = 10%", "T/n = 2 years"], solutionSteps: ["SI = (5000×10×2)/100 = ₹1000", "CI = 5000(1.1)² − 5000 = 6050 − 5000 = ₹1050", "Difference = 1050 − 1000 = ₹50"], numericAnswer: 50, unit: "₹"),
    NumericalProblem(id: "cq8n6", question: "A book with marked price ₹500 is sold at a 15% discount, then 5% GST is added. Find the final bill amount.", given: ["MP = ₹500", "Discount = 15%", "GST = 5%"], solutionSteps: ["SP after discount = 500 − 15% of 500 = 500 − 75 = ₹425", "GST = 5% of 425 = ₹21.25", "Bill amount = 425 + 21.25 = ₹446.25"], numericAnswer: 446.25, unit: "₹"),
    NumericalProblem(id: "cq8n7", question: "Find the amount on ₹15000 at 8% per annum compounded annually for 2 years.", given: ["P = ₹15000", "R = 8%", "n = 2 years"], solutionSteps: ["A = 15000(1.08)²", "= 15000 × 1.1664", "= ₹17,496"], numericAnswer: 17496, unit: "₹"),
    NumericalProblem(id: "cq8n8", question: "A mobile phone marked at ₹18000 is sold after two successive discounts of 10% and 5%. Find the final selling price.", given: ["MP = ₹18000", "Discount 1 = 10%", "Discount 2 = 5%"], solutionSteps: ["After first discount: 18000 − 10% = ₹16,200", "After second discount: 16200 − 5% of 16200 = 16200 − 810 = ₹15,390"], numericAnswer: 15390, unit: "₹"),
    NumericalProblem(id: "cq8n9", question: "Find the compound interest on ₹20,000 at 10% per annum for 1 year, compounded half-yearly.", given: ["P = ₹20,000", "R = 10% per annum → 5% per half-year", "n = 2 half-years"], solutionSteps: ["A = 20000(1.05)²", "= 20000 × 1.1025 = ₹22,050", "CI = 22050 − 20000 = ₹2,050"], numericAnswer: 2050, unit: "₹"),
    NumericalProblem(id: "cq8n10", question: "A dealer marks an item 25% above cost price of ₹800 and then gives a 10% discount. Find the selling price.", given: ["CP = ₹800", "Markup = 25%", "Discount = 10%"], solutionSteps: ["MP = 800 + 25% of 800 = ₹1000", "SP = 1000 − 10% of 1000 = ₹900"], numericAnswer: 900, unit: "₹"),
  ],
);
