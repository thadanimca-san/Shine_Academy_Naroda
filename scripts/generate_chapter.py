import json
import os

target_dir = "/home/ubuntu/Shine_Academy_Naroda/app_core/learning_modules/gseb_class9_social_science_ch18"
os.makedirs(target_dir, exist_ok=True)

metadata = {
  "id": "GSEB_SS_9_CH18",
  "title": "People as Resource",
  "subtitle": "Understanding Human Capital in Economics",
  "subject": "Social Science",
  "grade": 9,
  "board": "GSEB",
  "curriculum": ["GSEB"],
  "language": "English",
  "difficulty": "Intermediate",
  "estimated_minutes": 120,
  "version": "1.0.0",
  "author": "Shine Academy EduOS AI",
  "reviewed_by": "System",
  "last_updated": "2026-08-07T00:00:00Z",
  "tags": ["Economics", "Human Resource", "GSEB", "Class 9", "Population"],
  "learning_outcomes": [
    "Understand the concept of human resource.",
    "Analyze the role of education and health in human capital formation.",
    "Evaluate economic and non-economic activities.",
    "Understand the nature of unemployment in India."
  ],
  "ai_context": {
    "learning_goal": "To make the student realize that a population is an asset (human resource) rather than a liability.",
    "common_misconceptions": [
      "Population is always a burden.",
      "Only physical labor is considered a resource."
    ],
    "tutor_hint": "Ask the student how their current education is making them a 'resource' for the future.",
    "next_topics": ["KOBJ_UNEMPLOYMENT", "KOBJ_POVERTY"]
  }
}

question_bank = [
  {
    "id": "Q_CH18_01",
    "chapter_id": "GSEB_SS_9_CH18",
    "topic_id": "KOBJ_HUMAN_RESOURCE",
    "type": "mcq",
    "difficulty": "Beginner",
    "board": ["GSEB"],
    "marks": 1,
    "bloom_taxonomy": "Understanding",
    "keywords": ["human capital", "resource"],
    "estimated_time_minutes": 1,
    "exam_frequency": "High",
    "question_text": "What turns a population into human capital?",
    "answer": "Investment in education and health",
    "explanation": "Investment in education, training, and medical care turns population into human capital, enabling them to be more productive.",
    "distractor_rationale": "Land and having more children do not inherently increase human capability. Physical labor alone without skills is not optimal human capital.",
    "ai_context": {
      "learning_goal": "Understand the drivers of human capital.",
      "common_misconceptions": ["Human capital is just physical strength."],
      "hint": "Think about what makes you capable of taking up a highly skilled job in the future."
    }
  },
  {
    "id": "Q_CH18_02",
    "chapter_id": "GSEB_SS_9_CH18",
    "topic_id": "KOBJ_ECONOMIC_ACTIVITIES",
    "type": "mcq",
    "difficulty": "Intermediate",
    "board": ["GSEB"],
    "marks": 1,
    "bloom_taxonomy": "Applying",
    "keywords": ["economic activities", "sectors"],
    "estimated_time_minutes": 1,
    "exam_frequency": "Medium",
    "question_text": "Which of the following falls under the tertiary sector?",
    "answer": "Banking",
    "explanation": "The tertiary sector involves providing services rather than goods. Banking, trade, transport, and education are part of this sector.",
    "distractor_rationale": "Agriculture and mining are primary, and manufacturing is secondary.",
    "ai_context": {
      "learning_goal": "Identify activities in different economic sectors.",
      "common_misconceptions": ["Tertiary sector produces physical goods."],
      "hint": "Which option represents a service provided to people rather than a physical good?"
    }
  },
  {
    "id": "Q_CH18_03",
    "chapter_id": "GSEB_SS_9_CH18",
    "topic_id": "KOBJ_UNEMPLOYMENT",
    "type": "mcq",
    "difficulty": "Intermediate",
    "board": ["GSEB"],
    "marks": 1,
    "bloom_taxonomy": "Understanding",
    "keywords": ["unemployment", "seasonal"],
    "estimated_time_minutes": 1,
    "exam_frequency": "High",
    "question_text": "What type of unemployment is most common in rural areas?",
    "answer": "Seasonal and disguised unemployment",
    "explanation": "In rural areas, agriculture is the main occupation which is seasonal, leading to seasonal unemployment. Also, more people work on land than necessary, causing disguised unemployment.",
    "distractor_rationale": "Educated unemployment is more common in urban areas. Frictional and cyclical relate more to industrial/macro-economic shifts.",
    "ai_context": {
      "learning_goal": "Differentiate unemployment types by region.",
      "common_misconceptions": ["Unemployment is the same everywhere."],
      "hint": "Think about the nature of farming and how it depends on rainfall."
    }
  },
  {
    "id": "Q_CH18_04",
    "chapter_id": "GSEB_SS_9_CH18",
    "topic_id": "KOBJ_HEALTH",
    "type": "mcq",
    "difficulty": "Beginner",
    "board": ["GSEB"],
    "marks": 1,
    "bloom_taxonomy": "Remembering",
    "keywords": ["health", "quality of population"],
    "estimated_time_minutes": 1,
    "exam_frequency": "Medium",
    "question_text": "Which factor significantly determines the quality of the population along with education?",
    "answer": "Life expectancy and health",
    "explanation": "Health, indicated by life expectancy and skill formation, are major determinants of the quality of a population.",
    "distractor_rationale": "Wealth and vehicles are material possessions, not indicators of human capability.",
    "ai_context": {
      "learning_goal": "Identify key metrics for human capital quality.",
      "common_misconceptions": ["Rich populations are always high quality human capital."],
      "hint": "If a highly educated person is constantly sick, can they work effectively?"
    }
  }
]

blocks = [
  {
    "id": "KOBJ_CH18_B01",
    "type": "theory",
    "content": "In economics, 'People as Resource' is a way of referring to a country's working people in terms of their existing productive skills and abilities.",
    "knowledge_graph_links": {
      "related_topics": [],
      "prerequisites": [],
      "next_topics": ["KOBJ_CH18_B02"]
    },
    "ai_context": {
      "learning_goal": "Introduce the concept of population as a resource.",
      "common_misconceptions": ["Population is just a count of people."],
      "tutor_hint": "Ask the student how their skills make them a resource."
    },
    "difficulty": "Beginner",
    "estimated_minutes": 5,
    "bloom": "Understand"
  },
  {
    "id": "KOBJ_CH18_B02",
    "type": "definition",
    "content": "Etymology: The word 'Resource' comes from the Old French 'resourse', meaning 'a source, spring', and from Latin 'resurgere' (to rise again). A human resource is a wellspring of potential that rises to meet challenges.",
    "knowledge_graph_links": {
      "related_topics": ["KOBJ_CH18_B01"],
      "prerequisites": ["KOBJ_CH18_B01"],
      "next_topics": ["KOBJ_CH18_B03"]
    },
    "ai_context": {
      "learning_goal": "Understand the root meaning of the word 'resource' (Etymology).",
      "common_misconceptions": [],
      "tutor_hint": "How does a spring 'rising again' relate to human potential?"
    },
    "difficulty": "Beginner",
    "estimated_minutes": 5,
    "bloom": "Remember"
  },
  {
    "id": "KOBJ_CH18_B03",
    "type": "history",
    "content": "Cultural Integration: In ancient Indian philosophy, the concept of 'Purushartha' (Object of human pursuit) highlights 'Artha' (economic values/wealth). The ancient texts like the Arthashastra emphasized that a kingdom's true wealth lies in the capability, skill, and health of its populace, treating people as the ultimate resource for societal prosperity.",
    "knowledge_graph_links": {
      "related_topics": [],
      "prerequisites": ["KOBJ_CH18_B01"],
      "next_topics": ["KOBJ_CH18_B04"]
    },
    "ai_context": {
      "learning_goal": "Connect modern economic concepts to ancient Indian philosophy.",
      "common_misconceptions": ["Economics is only a modern Western construct."],
      "tutor_hint": "Mention Chanakya's Arthashastra to the student."
    },
    "difficulty": "Intermediate",
    "estimated_minutes": 10,
    "bloom": "Analyze"
  },
  {
    "id": "KOBJ_CH18_B04",
    "type": "theory",
    "content": "Population becomes 'human capital' when there is investment made in the form of education, training, and medical care. It is the stock of skill and productive knowledge embodied in them.",
    "knowledge_graph_links": {
      "related_topics": [],
      "prerequisites": ["KOBJ_CH18_B01"],
      "next_topics": ["KOBJ_CH18_B05"]
    },
    "ai_context": {
      "learning_goal": "Differentiate between population and human capital.",
      "common_misconceptions": ["All population is automatically human capital."],
      "tutor_hint": "Ask what investments are needed to turn population into capital."
    },
    "difficulty": "Beginner",
    "estimated_minutes": 5,
    "bloom": "Understand"
  },
  {
    "id": "KOBJ_CH18_B05",
    "type": "real_world_example",
    "content": "Case Study: Japan. Japan did not have significant natural resources, yet they became a developed country. How? By investing heavily in their human resource, specifically in education and health. This step-by-step investment transformed their population into highly productive capital.",
    "knowledge_graph_links": {
      "related_topics": ["KOBJ_CH18_B04"],
      "prerequisites": ["KOBJ_CH18_B04"],
      "next_topics": ["KOBJ_CH18_B06"]
    },
    "ai_context": {
      "learning_goal": "See the practical impact of human capital investment in a real country.",
      "common_misconceptions": ["Natural resources are strictly required for a country to be rich."],
      "tutor_hint": "Ask if a country with zero natural resources can still be wealthy."
    },
    "difficulty": "Intermediate",
    "estimated_minutes": 8,
    "bloom": "Apply"
  },
  {
    "id": "KOBJ_CH18_B06",
    "type": "theory",
    "content": "Economic activities are those activities that add value to the national income. They are broadly classified into three sectors: Primary, Secondary, and Tertiary.",
    "knowledge_graph_links": {
      "related_topics": [],
      "prerequisites": ["KOBJ_CH18_B04"],
      "next_topics": ["KOBJ_CH18_B07"]
    },
    "ai_context": {
      "learning_goal": "Define economic activities and their sectors.",
      "common_misconceptions": ["All activities we do daily are economic activities."],
      "tutor_hint": "Is cooking at home for your family an economic activity?"
    },
    "difficulty": "Beginner",
    "estimated_minutes": 5,
    "bloom": "Understand"
  },
  {
    "id": "KOBJ_CH18_B07",
    "type": "diagram",
    "content": "Sectors of Economy: \n1. Primary (Agriculture, Forestry, Mining)\n2. Secondary (Manufacturing, Construction)\n3. Tertiary (Trade, Transport, Communication, Banking, Education)",
    "knowledge_graph_links": {
      "related_topics": ["KOBJ_CH18_B06"],
      "prerequisites": ["KOBJ_CH18_B06"],
      "next_topics": ["KOBJ_CH18_B08"]
    },
    "ai_context": {
      "learning_goal": "Visualize the three sectors of the economy.",
      "common_misconceptions": ["Mining is in the secondary sector."],
      "tutor_hint": "Ask the student to categorize a doctor's profession."
    },
    "difficulty": "Beginner",
    "estimated_minutes": 5,
    "bloom": "Understand"
  },
  {
    "id": "KOBJ_CH18_B08",
    "type": "worked_example",
    "content": "Step-by-step Build: Categorizing an Activity.\nStep 1: Identify the activity (e.g., Making jaggery from sugarcane).\nStep 2: Determine if it involves extracting raw materials directly from nature. (Sugarcane farming = Yes, Primary).\nStep 3: Determine if it involves processing raw materials into a new product. (Making jaggery = Yes, Secondary).\nStep 4: Conclusion: Making jaggery is a Secondary sector activity.",
    "knowledge_graph_links": {
      "related_topics": ["KOBJ_CH18_B07"],
      "prerequisites": ["KOBJ_CH18_B07"],
      "next_topics": ["KOBJ_CH18_B09"]
    },
    "ai_context": {
      "learning_goal": "Apply the step-by-step method to classify economic activities.",
      "common_misconceptions": ["All agriculture-related processing is primary."],
      "tutor_hint": "Walk the student through classifying 'Making cotton shirts from cotton'."
    },
    "difficulty": "Intermediate",
    "estimated_minutes": 10,
    "bloom": "Apply"
  },
  {
    "id": "KOBJ_CH18_B09",
    "type": "theory",
    "content": "Economic activities are further divided into Market activities (performed for pay or profit) and Non-market activities (production for self-consumption).",
    "knowledge_graph_links": {
      "related_topics": ["KOBJ_CH18_B06"],
      "prerequisites": ["KOBJ_CH18_B06"],
      "next_topics": ["KOBJ_CH18_B10"]
    },
    "ai_context": {
      "learning_goal": "Distinguish between market and non-market activities.",
      "common_misconceptions": ["Unpaid domestic work is an economic activity."],
      "tutor_hint": "Is growing vegetables in your backyard for your own meal a market activity?"
    },
    "difficulty": "Beginner",
    "estimated_minutes": 5,
    "bloom": "Understand"
  },
  {
    "id": "KOBJ_CH18_B10",
    "type": "definition",
    "content": "Etymology: 'Unemployment' comes from the prefix 'un-' (not) + 'employ' (from Latin 'implicare', meaning to involve or engage) + '-ment' (state of). So it is the state of not being engaged in productive work despite being willing to do so.",
    "knowledge_graph_links": {
      "related_topics": [],
      "prerequisites": ["KOBJ_CH18_B04"],
      "next_topics": ["KOBJ_CH18_B11"]
    },
    "ai_context": {
      "learning_goal": "Understand the literal meaning of unemployment.",
      "common_misconceptions": ["Anyone not working is unemployed (e.g., kids, retired people)."],
      "tutor_hint": "Is a person who doesn't want to work considered unemployed?"
    },
    "difficulty": "Beginner",
    "estimated_minutes": 5,
    "bloom": "Remember"
  },
  {
    "id": "KOBJ_CH18_B11",
    "type": "theory",
    "content": "Unemployment is said to exist when people who are willing to work at the going wages cannot find jobs. The workforce population includes people from 15 years to 59 years.",
    "knowledge_graph_links": {
      "related_topics": ["KOBJ_CH18_B10"],
      "prerequisites": ["KOBJ_CH18_B10"],
      "next_topics": ["KOBJ_CH18_B12"]
    },
    "ai_context": {
      "learning_goal": "Define unemployment officially.",
      "common_misconceptions": ["Children who don't work are unemployed."],
      "tutor_hint": "Ask what the working age group is."
    },
    "difficulty": "Beginner",
    "estimated_minutes": 5,
    "bloom": "Understand"
  },
  {
    "id": "KOBJ_CH18_B12",
    "type": "image",
    "content": "In rural areas of India, the two main types of unemployment are Seasonal and Disguised unemployment.",
    "knowledge_graph_links": {
      "related_topics": ["KOBJ_CH18_B11"],
      "prerequisites": ["KOBJ_CH18_B11"],
      "next_topics": ["KOBJ_CH18_B13"]
    },
    "ai_context": {
      "learning_goal": "Identify rural unemployment types.",
      "common_misconceptions": [],
      "tutor_hint": "Ask the student to define 'seasonal'."
    },
    "difficulty": "Beginner",
    "estimated_minutes": 5,
    "bloom": "Understand"
  },
  {
    "id": "KOBJ_CH18_B13",
    "type": "theory",
    "content": "Step-by-step breakdown: Disguised Unemployment.\nStep 1: A piece of agricultural land requires 5 people to cultivate it fully.\nStep 2: A family has 8 members, and all 8 work on the same land.\nStep 3: The contribution made by the extra 3 people does not add to the total production.\nStep 4: If these 3 people are removed, production remains the same.\nStep 5: Thus, these 3 people are 'disguisedly unemployed'.",
    "knowledge_graph_links": {
      "related_topics": ["KOBJ_CH18_B12"],
      "prerequisites": ["KOBJ_CH18_B12"],
      "next_topics": ["KOBJ_CH18_B14"]
    },
    "ai_context": {
      "learning_goal": "Understand disguised unemployment through a step-by-step logical build.",
      "common_misconceptions": ["If people are working on a farm, they are all fully employed."],
      "tutor_hint": "Ask what happens to the crop yield if the 3 extra people stop working."
    },
    "difficulty": "Intermediate",
    "estimated_minutes": 10,
    "bloom": "Analyze"
  },
  {
    "id": "KOBJ_CH18_B14",
    "type": "theory",
    "content": "Educated Unemployment is a major problem in urban areas. Many youth with matriculation, graduation, and post-graduation degrees are unable to find jobs, leading to a massive waste of human resources.",
    "knowledge_graph_links": {
      "related_topics": ["KOBJ_CH18_B11"],
      "prerequisites": ["KOBJ_CH18_B11"],
      "next_topics": ["KOBJ_CH18_B15"]
    },
    "ai_context": {
      "learning_goal": "Understand the urban unemployment issue.",
      "common_misconceptions": ["Education guarantees employment."],
      "tutor_hint": "Why might an educated person remain unemployed?"
    },
    "difficulty": "Beginner",
    "estimated_minutes": 5,
    "bloom": "Understand"
  },
  {
    "id": "KOBJ_CH18_B15",
    "type": "summary",
    "content": "In summary, a population is an asset (human resource) when invested in through health and education. The ancient Indian concept of 'Purushartha' reminds us that societal wealth stems from capable humans. However, unemployment, whether seasonal, disguised, or educated, wastes this precious resource.",
    "knowledge_graph_links": {
      "related_topics": [],
      "prerequisites": ["KOBJ_CH18_B13", "KOBJ_CH18_B14"],
      "next_topics": []
    },
    "ai_context": {
      "learning_goal": "Synthesize the entire chapter's learnings.",
      "common_misconceptions": [],
      "tutor_hint": "Ask the student to summarize the chapter in one sentence."
    },
    "difficulty": "Beginner",
    "estimated_minutes": 5,
    "bloom": "Evaluate"
  }
]

with open(f"{target_dir}/metadata.json", "w") as f:
    json.dump(metadata, f, indent=2)
with open(f"{target_dir}/question_bank.json", "w") as f:
    json.dump(question_bank, f, indent=2)
with open(f"{target_dir}/blocks.json", "w") as f:
    json.dump(blocks, f, indent=2)

print("SUCCESS: JSON files generated successfully.")
