"""CBSE Class 10 History Ch 2: Nationalism in India (fully in the 2025-26 board syllabus; carries the History map items)."""
import sys
from ss_common import make, header, path, SQP, SHINE

ROOT = sys.argv[1]
SUBJ, N = "history", 2
PATH = path(SUBJ, "ch02_nationalism_in_india")
C = make(SUBJ, N, "his10ch02")
blk, M, W = C.blk, C.m, C.w
WAR, NCM, CDM, PART, BEL = ["war_and_satyagraha"], ["non_cooperation"], ["civil_disobedience"], ["participants_and_limits"], ["collective_belonging"]
MAP = ["map_work"]
def ex(n): return {"kind": "ncert_exercise", "exercise": "Chapter 2 exercises", "question": n}

TIMELINE = ("| Year | Event |\n|---|---|\n| 1915 (January) | Gandhiji returns to India from South Africa |\n| 1917 | Champaran satyagraha (Bihar), Kheda satyagraha (Gujarat) |\n"
            "| 1918 | Ahmedabad cotton mill workers' satyagraha |\n| 1919 | Rowlatt Act; Jallianwala Bagh massacre (13 April); Khilafat Committee (March) |\n"
            "| 1920 | Calcutta session (September) and Nagpur session (December) adopt Non-Cooperation |\n| 1922 (February) | Chauri Chaura; Non-Cooperation withdrawn |\n"
            "| 1928 | Simon Commission arrives: \"Go back Simon\" |\n| 1929 (December) | Lahore Congress demands Purna Swaraj |\n| 1930 | 26 January: Independence Day; Salt March, 12 March to 6 April; Civil Disobedience begins |\n"
            "| 1931 (5 March) | Gandhi–Irwin Pact; Gandhiji attends the Second Round Table Conference (December) |\n| 1932 (September) | Poona Pact |")
MOVES = ("| | Non-Cooperation (1921–22) | Civil Disobedience (1930–34) |\n|---|---|---|\n| Aim | swaraj, and support for the Khilafat | Purna Swaraj (complete independence) |\n"
         "| Method | refuse to cooperate: give up titles, boycott schools, courts, councils and foreign goods | break colonial laws: make salt, refuse taxes, violate forest laws |\n"
         "| Start | January 1921 | Salt March, 12 March 1930 |\n| End | Withdrawn in February 1922 after Chauri Chaura | Called off after the Gandhi–Irwin Pact (1931); relaunched, lost momentum by 1934 |\n"
         "| Hindu–Muslim unity | strong (with the Khilafat movement) | weak: many Muslims stayed away |")
GROUPS = ("| Group | Why they joined / what swaraj meant to them |\n|---|---|\n| Middle class in towns | left government schools and courts; boycotted foreign cloth |\n"
          "| Peasants of Awadh (Baba Ramchandra) | against talukdars' high rents and begar; reduction of revenue |\n| Tribals of the Gudem Hills (Alluri Sitarama Raju) | against closed forests and forced begar |\n"
          "| Plantation workers of Assam | the right to move freely in and out of the tea gardens and to go back to their villages |\n"
          "| Rich peasants (Patidars, Jats) in 1930 | fall in prices; demanded reduction of revenue |\n| Business classes (FICCI, 1927) | protection against foreign imports; a rupee–sterling ratio that discouraged imports |\n"
          "| Women | protest marches, salt making, picketing liquor and foreign-cloth shops |")
MAPT = ("| Map item (2025-26 list) | Where | Why it is famous |\n|---|---|---|\n| Champaran | Bihar | Gandhiji's satyagraha for indigo peasants, 1917 |\n| Kheda | Gujarat | satyagraha for peasants who could not pay revenue, 1917 |\n"
        "| Ahmedabad | Gujarat | satyagraha for cotton mill workers, 1918 |\n| Amritsar (Jallianwala Bagh) | Punjab | massacre of 13 April 1919 |\n| Calcutta | Bengal | Congress session, September 1920: Non-Cooperation accepted |\n"
        "| Nagpur | Maharashtra | Congress session, December 1920: Non-Cooperation programme adopted |\n| Madras | Tamil Nadu | Congress session, 1927 |\n| Dandi | Gujarat | end of the Salt March, 6 April 1930: start of Civil Disobedience |")

sections = [
 {"id": "s1", "title": "A nation in the making", "blocks": [
  blk("s1.hook", "hook", title="A handful of salt",
    body="On the morning of 6 April 1930, a 60-year-old man in a simple dhoti bent down on the beach at Dandi in Gujarat, picked up a lump of natural salt and broke the law of the British Empire.\n\n"
         "It looked like a tiny act. But millions of Indians understood its message: the salt every family needs is taxed by a foreign government, and we will obey that law no more. "
         "How did Indians from towns, villages, forests and tea gardens, from different castes, religions and classes, come to feel that they belonged to **one nation**? That is the story of this chapter, and it carries the History **map questions** of your board paper."),
  blk("s1.inspiration", "inspiration", title="The woman who would not stay home", person="Kamaladevi Chattopadhyay", years="1903–1988",
    body="When Gandhiji first planned the Salt March only for men, Kamaladevi Chattopadhyay persuaded him to let women take part. She went on to break the salt law in Bombay, sold packets of 'freedom salt' near the High Court, and was jailed.\n\n"
         "She was the first Indian woman to contest a legislative election (1926). After Independence she rebuilt India's handicrafts and handloom industry and founded institutions for theatre and crafts. She received the Padma Bhushan in 1955 and the Padma Vibhushan in 1987.",
    future="The history of the national movement prepares you for civil services, politics, law, journalism, teaching and public policy."),
  C.socratic("s1.socratic", "In Europe, nationalism grew around the creation of nation-states. In India, around what did the sense of nationalism mainly grow?",
    ["The struggle against colonial rule", "A war between Indian kingdoms", "A customs union like the Zollverein"], 0,
    "In India, as in many colonies, modern nationalism grew with the anti-colonial movement: people discovered their unity in their struggle against British rule."),
 ]},
 {"id": "s2", "title": "The First World War, Khilafat and satyagraha", "blocks": [
  blk("s2.thm", "theory", title="War, hardship and a new idea", revision=True,
    body="**Effects of the First World War (1914–18):**\n- Huge rise in defence expenditure, financed by war loans and increased taxes: customs duties were raised and **income tax** was introduced.\n"
         "- Prices **doubled between 1913 and 1918**, causing extreme hardship for common people.\n- Villages were called upon to supply soldiers, and **forced recruitment** in rural areas caused widespread anger.\n"
         "- Crops failed in 1918–19 and 1920–21, causing acute food shortages, along with an influenza epidemic. According to the 1921 census, **12 to 13 million people died** due to famines and the epidemic.\n\n"
         "**The idea of satyagraha:** Mahatma Gandhi returned to India in **January 1915** from South Africa, where he had successfully fought the racist regime with a novel method of mass agitation. "
         "Satyagraha emphasised the **power of truth** and the need to search for truth. If the cause was true and the fight was against injustice, physical force was not necessary to fight the oppressor; a satyagrahi could win the battle through **non-violence**, by appealing to the conscience of the oppressor.\n\n"
         "**First satyagrahas in India:**\n- **1917, Champaran (Bihar):** to inspire peasants to struggle against the oppressive plantation system.\n"
         "- **1917, Kheda (Gujarat):** to support peasants affected by crop failure and a plague epidemic, who could not pay revenue and demanded its relaxation.\n- **1918, Ahmedabad:** to organise a satyagraha among cotton mill workers."),
  blk("s2.rowlatt", "theory", title="Rowlatt Act and Jallianwala Bagh", revision=True,
    body="**Rowlatt Act (1919):** hurriedly passed through the Imperial Legislative Council despite the united opposition of the Indian members. It gave the government enormous powers to repress political activities, and allowed **detention of political prisoners without trial for two years**.\n\n"
         "Gandhiji launched a nationwide satyagraha, starting with a **hartal on 6 April**. Rallies were organised, railway workshop workers went on strike and shops closed. The British cracked down; local leaders were arrested in Amritsar, and martial law was imposed under **General Dyer**.\n\n"
         "**Jallianwala Bagh (13 April 1919):** a large crowd gathered in the enclosed ground of Jallianwala Bagh in Amritsar. Some came to protest against the government's repression; others came for the annual **Baisakhi fair** and did not know about martial law. "
         "Dyer entered the area, **blocked the exit points and opened fire**, killing hundreds. His aim, he declared later, was to 'produce a moral effect', to create fear and awe in the minds of satyagrahis.\n\n"
         "As the news spread, crowds took to the streets; there were strikes and clashes. The government responded brutally: satyagrahis were forced to rub their noses on the ground, crawl on the streets and salaam to all sahibs; villages around Gujranwala in Punjab were bombed. Seeing violence spread, **Gandhiji called off the movement**."),
  blk("s2.khilafat", "theory", title="Khilafat and the call for Non-Cooperation", revision=True,
    body="The First World War ended with the defeat of **Ottoman Turkey**, and there were rumours that a harsh peace treaty would be imposed on the Ottoman emperor, the spiritual head of the Islamic world (the **Khalifa**). "
         "To defend the Khalifa's powers, a **Khilafat Committee** was formed in Bombay in **March 1919**. Young Muslim leaders like the brothers **Muhammad Ali and Shaukat Ali** began discussing united mass action with Gandhiji.\n\n"
         "Gandhiji saw this as an opportunity to bring Muslims under the umbrella of a unified national movement. At the **Calcutta session of the Congress in September 1920**, he convinced other leaders to start a non-cooperation movement in support of Khilafat as well as for swaraj.\n\n"
         "**Why non-cooperation?** In his book ***Hind Swaraj*** (1909), Gandhiji declared that British rule was established in India with the cooperation of Indians and had survived only because of it. If Indians refused to cooperate, British rule would collapse within a year, and swaraj would come.\n\n"
         "**Proposed stages:** surrender of government titles; boycott of civil services, army, police, courts and legislative councils, schools and foreign goods; and, if the government used repression, a full civil disobedience campaign. "
         "After much debate, the Non-Cooperation programme was adopted at the **Nagpur session in December 1920**."),
  C.kc("s2.check", "Why were Indians outraged by the Rowlatt Act of 1919?",
    [("It allowed detention of political prisoners without trial for two years", ""), ("It introduced income tax for the first time", "Income tax came with the war expenditure; the Rowlatt Act was about repression."),
     ("It banned the Khilafat Committee", "It did not; the Khilafat Committee was formed in 1919 itself."), ("It imposed a salt tax", "The salt tax was the issue of 1930.")],
    "The Act was passed despite united Indian opposition and gave the government power to repress political activity and detain prisoners without trial for two years."),
  C.kc("s2.check2", "Where did Gandhiji organise a satyagraha for cotton mill workers in 1918?",
    [("Ahmedabad", ""), ("Champaran", "Champaran (1917) was for peasants against the plantation system."), ("Kheda", "Kheda (1917) was for peasants who could not pay revenue."), ("Amritsar", "Amritsar is the site of the Jallianwala Bagh massacre.")],
    "Ahmedabad, 1918: satyagraha among cotton mill workers."),
 ]},
 {"id": "s3", "title": "Differing strands within the Non-Cooperation Movement", "blocks": [
  blk("s3.towns", "theory", title="In the towns", revision=True,
    body="The movement started in **January 1921** with middle-class participation in the cities:\n- Thousands of students left government-controlled schools and colleges; headmasters and teachers resigned; lawyers gave up their legal practices.\n"
         "- Council elections were boycotted in most provinces except **Madras**, where the **Justice Party**, the party of the non-Brahmans, felt that entering the council was one way of gaining power.\n\n"
         "**Economic effects:** foreign goods were boycotted, liquor shops picketed, and foreign cloth burnt in huge bonfires. The **import of foreign cloth halved between 1921 and 1922**, its value dropping from **Rs 102 crore to Rs 57 crore**. "
         "Merchants and traders refused to trade in foreign goods. As the boycott spread, the production of Indian textile mills and handlooms went up.\n\n"
         "**Why it slowed down in the cities:** khadi cloth was often more expensive than mass-produced mill cloth, and poor people could not afford it. Alternative Indian institutions were slow to come up, so students and teachers began trickling back to government schools and lawyers went back to the courts."),
  blk("s3.country", "theory", title="Rebellion in the countryside, forests and plantations", revision=True,
    body="**Awadh peasants:** led by **Baba Ramchandra**, a sanyasi who had earlier been to Fiji as an indentured labourer. The movement was against **talukdars and landlords** who demanded very high rents and other cesses, and **begar** (forced labour without payment); peasants had no security of tenure. "
         "They demanded reduction of revenue, abolition of begar and a social boycott of oppressive landlords (**nai–dhobi bandhs**: barbers and washermen refused to serve them). In June 1920 **Jawaharlal Nehru** began going around the villages of Awadh; by October the **Oudh Kisan Sabha** was set up, headed by Nehru, Baba Ramchandra and others. "
         "In 1921 the movement spread, and houses of talukdars and merchants were attacked, bazaars looted and grain hoards taken over. Local leaders told peasants that Gandhiji had declared no taxes were to be paid and land was to be redistributed: the name of the Mahatma was being invoked for actions far from his ideas.\n\n"
         "**Tribal peasants of the Gudem Hills (Andhra Pradesh):** a militant guerrilla movement spread in the early 1920s. The colonial government had **closed large forest areas**, stopping people from grazing cattle and collecting fuelwood and fruits, and forced them to do begar for road building. "
         "Their leader **Alluri Sitarama Raju** claimed special powers and was inspired by the Non-Cooperation Movement; he persuaded people to give up drinking, but believed India could be liberated only by the **use of force**, not non-violence. The rebels attacked police stations. Raju was captured and executed in **1924**.\n\n"
         "**Plantation workers of Assam:** under the **Inland Emigration Act of 1859**, plantation workers were not permitted to leave the tea gardens without permission, which was rarely given. For them, swaraj meant the right to move freely and to retain a link with their village. "
         "When they heard of the Non-Cooperation Movement, thousands defied the authorities, left the plantations and headed home. They were stranded on the way by a railway and steamer strike, caught by the police and brutally beaten."),
  blk("s3.groups", "markdown_table", title="Different groups, different meanings of swaraj", revision=True, body=GROUPS),
  C.kc("s3.check", "Who led the peasant movement in Awadh?",
    [("Baba Ramchandra", ""), ("Alluri Sitarama Raju", "He led the tribal rebels of the Gudem Hills."), ("Purshottamdas Thakurdas", "He was a business leader."), ("Abdul Ghaffar Khan", "He was a leader in the North-West Frontier.")],
    "Baba Ramchandra, a sanyasi who had been an indentured labourer in Fiji."),
  C.kc("s3.check2", "Why did the Non-Cooperation Movement slow down in the cities?",
    [("Khadi was more expensive than mill cloth and alternative Indian institutions were slow to come up", ""),
     ("The British abolished the Rowlatt Act", "That was not the reason."), ("All the students passed their exams", "Students returned because there were no alternative institutions."), ("The Justice Party joined the boycott", "The Justice Party contested the council elections in Madras.")],
    "The poor could not afford khadi, and without Indian schools and courts students, teachers and lawyers drifted back."),
 ]},
 {"id": "s4", "title": "Towards Civil Disobedience", "blocks": [
  blk("s4.thm", "theory", title="From Chauri Chaura to Purna Swaraj", revision=True,
    body="In **February 1922** Gandhiji decided to withdraw the Non-Cooperation Movement. He felt it was turning violent in many places (a peaceful demonstration at **Chauri Chaura** in Gorakhpur turned into a violent clash with the police) and that satyagrahis needed proper training before mass struggles.\n\n"
         "**Within the Congress:** some leaders were tired of mass struggles and wanted to take part in elections to the provincial councils set up by the **Government of India Act of 1919**. **C. R. Das and Motilal Nehru** formed the **Swaraj Party** within the Congress to argue for a return to council politics. "
         "Younger leaders like **Jawaharlal Nehru and Subhas Chandra Bose** pressed for more radical mass agitation and full independence.\n\n"
         "**Economic depression:** agricultural prices began to fall from 1926 and collapsed after 1930; peasants found it hard to sell their harvests and pay revenue.\n\n"
         "**Simon Commission:** the new Tory government in Britain set up a Statutory Commission under **Sir John Simon** to look into the functioning of the constitutional system in India. The commission did **not have a single Indian member**. When it arrived in **1928**, it was greeted with the slogan **'Go back Simon'**. "
         "In October 1929 Viceroy **Lord Irwin** announced a vague offer of **'dominion status'** for India in an unspecified future, and a Round Table Conference. This did not satisfy the Congress leaders.\n\n"
         "**Purna Swaraj:** in **December 1929**, under **Jawaharlal Nehru**, the **Lahore Congress** formalised the demand of 'Purna Swaraj' (complete independence). **26 January 1930** was declared Independence Day."),
  blk("s4.salt", "theory", title="The Salt March and Civil Disobedience", revision=True,
    body="Gandhiji found in **salt** a powerful symbol that could unite the nation: salt was consumed by the rich and poor alike, and was one of the most essential items of food. On **31 January 1930** he sent a letter to Viceroy Irwin stating **eleven demands**; the most stirring was the demand to **abolish the salt tax**. If the demands were not fulfilled by 11 March, the Congress would launch a civil disobedience campaign.\n\n"
         "**The Salt March:** Gandhiji started with **78 trusted volunteers**. They walked over **240 miles** from his ashram at **Sabarmati** to the Gujarati coastal town of **Dandi**, in **24 days**, about 10 miles a day. Thousands came to hear him on the way. "
         "On **6 April** he reached Dandi and ceremonially violated the law, **manufacturing salt by boiling sea water**.\n\n"
         "**How Civil Disobedience differed:** people were now asked not only to refuse cooperation with the British, as in 1921–22, but also to **break colonial laws**. Thousands broke the salt law and manufactured salt; foreign cloth was boycotted and liquor shops picketed; peasants refused to pay revenue and chaukidari taxes; village officials resigned; and forest people violated forest laws.\n\n"
         "**Repression and the pact:** the colonial government began arresting leaders. When **Abdul Ghaffar Khan**, a devout disciple of Gandhiji, was arrested in April 1930, angry crowds demonstrated in Peshawar, facing armoured cars and police firing; many were killed. A month later Gandhiji himself was arrested. Industrial workers in **Sholapur** attacked police posts, municipal buildings, law courts and railway stations. "
         "The government responded with brutal repression; about **100,000 people were arrested**. Gandhiji called off the movement and entered into a pact with Irwin on **5 March 1931**: he agreed to take part in a **Round Table Conference** in London, and the government agreed to release political prisoners. "
         "In December 1931 he went to London for the conference, but the negotiations broke down and he returned disappointed. The government began a new cycle of repression; the Congress was declared illegal. Gandhiji relaunched Civil Disobedience; it continued for over a year, but by **1934 it lost its momentum**."),
  blk("s4.compare", "markdown_table", title="Non-Cooperation and Civil Disobedience compared", revision=True, body=MOVES),
  C.kc("s4.check", "Why did Gandhiji choose salt as the symbol of the 1930 movement?",
    [("Salt was used by the rich and poor alike, so a tax on it hurt everyone", ""), ("Salt was imported from Britain only", "Salt was produced in India; the issue was the tax and government monopoly."),
     ("The Simon Commission had banned salt", "The Simon Commission was about constitutional reform."), ("Only the rich used salt", "Salt was essential for everyone.")],
    "Salt was one of the most essential items of food for every Indian, so breaking the salt law united the nation."),
  C.kc("s4.check2", "The Gandhi–Irwin Pact (1931) led to:",
    [("Gandhiji agreeing to attend the Round Table Conference and the release of political prisoners", ""), ("India getting dominion status immediately", "Dominion status was only a vague offer."),
     ("The end of the salt tax", "The salt tax was not abolished by the pact."), ("The Poona Pact", "The Poona Pact (1932) was between Gandhiji and Ambedkar.")],
    "Gandhiji agreed to participate in the Round Table Conference in London and the government agreed to release political prisoners."),
 ]},
 {"id": "s5", "title": "How participants saw the movement, and its limits", "blocks": [
  blk("s5.thm", "theory", title="Many hopes under one movement", revision=True,
    body="**Rich peasants:** the **Patidars of Gujarat** and the **Jats of Uttar Pradesh** grew commercial crops and were hit hard by the trade depression and falling prices. When the government refused to reduce revenue, they became active supporters of Civil Disobedience. "
         "They were deeply disappointed when the movement was called off in 1931 without the revenue rates being revised, and many refused to participate when it was restarted in 1932.\n\n"
         "**Poorer peasants:** small tenants who rented land from landlords wanted the **unpaid rent to be remitted**. They joined radical movements, often led by Socialists and Communists. The Congress, afraid of upsetting rich peasants and landlords, was unwilling to support 'no rent' campaigns.\n\n"
         "**Business classes:** they wanted protection against imports of foreign goods and a rupee–sterling foreign exchange ratio that would discourage imports. They formed the **Indian Industrial and Commercial Congress (1920)** and the **Federation of the Indian Chamber of Commerce and Industries (FICCI) (1927)**, led by prominent industrialists like **Purshottamdas Thakurdas and G. D. Birla**. "
         "They supported Civil Disobedience at first, but after the failure of the Round Table Conference they were less enthusiastic; they feared prolonged disruption of business and the growing influence of socialism among younger Congress members.\n\n"
         "**Industrial workers:** they did not participate in large numbers, except in the **Nagpur** region. Some adopted the boycott of foreign goods; railway and dock workers went on strike in 1930 and 1932; in 1930 thousands of workers in the **Chotanagpur tin mines** wore Gandhi caps and joined protest rallies. The Congress was reluctant to include workers' demands, fearing it would alienate industrialists.\n\n"
         "**Women:** they participated in large numbers: in protest marches, manufacturing salt, and picketing foreign-cloth and liquor shops; many went to jail. In cities they were mostly from high-caste families; in rural areas from rich peasant households. "
         "Yet Gandhiji was convinced that it was the duty of women to look after home and hearth, and the Congress was reluctant to allow women to hold positions of authority within the organisation."),
  blk("s5.limits", "theory", title="The limits of Civil Disobedience", revision=True,
    body="**Dalits ('untouchables'):** the Congress had long ignored the dalits for fear of offending conservative high-caste Hindus. Gandhiji called them ***harijans*** (children of God), organised satyagraha to secure their entry into temples and access to public wells, tanks, roads and schools, and himself cleaned toilets to dignify the work of the *bhangi* (sweeper). "
         "But many dalit leaders wanted a political solution: reserved seats in educational institutions and a **separate electorate**. **Dr B. R. Ambedkar** organised the dalits into the **Depressed Classes Association in 1930** and clashed with Gandhiji at the **Second Round Table Conference** by demanding separate electorates. "
         "When the British government conceded Ambedkar's demand, Gandhiji began a **fast unto death**, believing that separate electorates would slow down the integration of dalits into society. Ambedkar ultimately accepted Gandhiji's position, and the result was the **Poona Pact of September 1932**: it gave the Depressed Classes (later the Scheduled Castes) **reserved seats** in provincial and central legislative councils, but they were to be **voted in by the general electorate**.\n\n"
         "**Muslims:** after the decline of the Non-Cooperation–Khilafat movement, a large section of Muslims felt alienated from the Congress. From the mid-1920s the Congress came to be visibly associated with openly Hindu religious nationalist groups like the **Hindu Mahasabha**, and relations worsened with communal clashes and riots. "
         "**Muhammad Ali Jinnah** was willing to give up the demand for separate electorates if Muslims were assured reserved seats in the Central Assembly and representation in proportion to population in the Muslim-dominated provinces (**Bengal and Punjab**). "
         "At the **All Parties Conference in 1928**, **M. R. Jayakar** of the Hindu Mahasabha strongly opposed efforts at compromise. When Civil Disobedience started, there was an atmosphere of suspicion and distrust, and large sections of Muslims did not respond to the call for united struggle."),
  C.kc("s5.check", "What did the Poona Pact of 1932 give the Depressed Classes?",
    [("Reserved seats in legislative councils, to be filled by voting of the general electorate", ""), ("Separate electorates", "Ambedkar gave up separate electorates in the Poona Pact."),
     ("Dominion status", "Dominion status was offered to India, not to a group."), ("A separate province", "No province was created.")],
    "Reserved seats, but voted in by the general electorate."),
  C.kc("s5.check2", "Why were business groups less enthusiastic about Civil Disobedience after 1931?",
    [("They feared prolonged disruption of business and the spread of socialist ideas in the Congress", ""), ("The British had abolished all import duties", "Business groups wanted protection from imports, which they did not get."),
     ("Gandhiji asked them to stop all trade", "That was not the reason."), ("They had all joined the Swaraj Party", "That was not the reason.")],
    "After the failed Round Table Conference they worried about disruption and the growing influence of socialism among younger Congress leaders."),
 ]},
 {"id": "s6", "title": "The sense of collective belonging", "blocks": [
  blk("s6.thm", "theory", title="Images, songs, flags and history", revision=True,
    body="Nationalism spreads when people begin to believe that they are all part of the same nation. This sense of collective belonging came partly through united struggles, and partly through cultural processes:\n\n"
         "- **Image of Bharat Mata:** in the 1870s **Bankim Chandra Chattopadhyay** wrote **'Vande Mataram'** as a hymn to the motherland; it was later included in his novel ***Anandamath*** and widely sung during the **Swadeshi movement** in Bengal. "
         "**Abanindranath Tagore** painted his famous image of **Bharat Mata**: calm, composed, divine and spiritual. Later images showed Bharat Mata with a trishul, standing beside a lion and an elephant: symbols of power and authority.\n"
         "- **Folklore:** nationalists recorded folk tales sung by bards and toured villages to collect folk songs and legends, believing they gave a true picture of traditional culture damaged by outside forces. In Bengal **Rabindranath Tagore** led the revival of folklore by collecting ballads, nursery rhymes and myths. "
         "In Madras, **Natesa Sastri** published a massive four-volume collection of Tamil folk tales, ***The Folklore of Southern India***.\n"
         "- **Icons and flags:** during the Swadeshi movement in Bengal, a **tricolour flag (red, green and yellow)** was designed, with **eight lotuses** representing the eight provinces of British India and a **crescent moon** representing Hindus and Muslims. "
         "By **1921** Gandhiji had designed the **Swaraj flag**: a tricolour (**red, green and white**) with a **spinning wheel** at the centre, representing the Gandhian ideal of self-help. Carrying the flag during marches became a symbol of defiance.\n"
         "- **Reinterpretation of history:** nationalists wrote about India's glorious past achievements in art, architecture, science, mathematics, religion, law and philosophy, and urged readers to take pride in them and to change the miserable conditions of life under British rule.\n\n"
         "But a past glorified as Hindu, with images drawn from Hindu iconography, made people of other communities feel left out. Despite such problems, by the 1940s a confident nationalist movement had built a sense of collective belonging across India."),
  blk("s6.map", "markdown_table", title="Map work for this chapter (CBSE 2025-26 list)", revision=True, body=MAPT),
  blk("s6.timeline", "markdown_table", title="Timeline of the chapter", revision=True, body=TIMELINE),
  C.kc("s6.check", "Who painted the famous image of Bharat Mata?",
    [("Abanindranath Tagore", ""), ("Bankim Chandra Chattopadhyay", "He wrote 'Vande Mataram'."), ("Natesa Sastri", "He collected Tamil folk tales."), ("Rabindranath Tagore", "He collected ballads, rhymes and myths; the painting was by Abanindranath Tagore.")],
    "Abanindranath Tagore painted Bharat Mata as calm, composed, divine and spiritual."),
  C.kc("s6.check2", "On the CBSE map list, which place marks the end of the Salt March?",
    [("Dandi, Gujarat", ""), ("Sabarmati, Gujarat", "Sabarmati is where the march started."), ("Kheda, Gujarat", "Kheda is the site of the 1917 peasant satyagraha."), ("Champaran, Bihar", "Champaran is the site of the 1917 indigo satyagraha.")],
    "The Salt March ended at Dandi on 6 April 1930."),
 ]},
 {"id": "s7", "title": "Remember, avoid, practise", "blocks": [
  blk("s7.memory", "memory_trick", title="Memory tricks",
    body="- **First satyagrahas: \"C-K-A, 17-17-18\":** **C**hamparan 1917, **K**heda 1917, **A**hmedabad 1918.\n- **1919 = R-J-K:** **R**owlatt Act, **J**allianwala Bagh (13 April, Baisakhi), **K**hilafat Committee.\n"
         "- **Two 1920 sessions: \"Calcutta convinces, Nagpur nails it\":** September Calcutta accepts Non-Cooperation; December Nagpur adopts the programme.\n"
         "- **Salt March numbers: 78 – 240 – 24 – 6 April:** volunteers, miles, days, date at Dandi.\n- **Swaraj flag 1921:** red, green, white + charkha. **Swadeshi flag:** red, green, yellow + 8 lotuses + crescent."),
  blk("s7.mistakes", "common_mistakes", title="Common mistakes",
    body="1. Writing that Jallianwala Bagh happened in Lahore: it was in **Amritsar**, on **13 April 1919**.\n2. Confusing the Calcutta session (September 1920, Non-Cooperation accepted) with the Nagpur session (December 1920, programme adopted).\n"
         "3. Saying the Simon Commission had Indian members: it had **none**.\n4. Saying the Poona Pact gave separate electorates: it gave **reserved seats** with a general electorate.\n"
         "5. Mixing up Baba Ramchandra (Awadh) and Alluri Sitarama Raju (Gudem Hills).\n6. Saying Gandhiji withdrew Civil Disobedience after Chauri Chaura: Chauri Chaura (1922) ended **Non-Cooperation**.\n"
         "7. Saying the Swaraj Party left the Congress: it was formed **within** the Congress."),
  blk("s7.tip", "teacher_tip", title="Try this in class",
    body="Make a 'living map': give each group a card (Champaran, Kheda, Ahmedabad, Amritsar, Calcutta, Nagpur, Madras, Dandi). Students place themselves on a big outline map of India drawn on the floor and tell the class, in 30 seconds, what happened there and when. "
         "Then hold a 'Round Table' role play with Gandhiji, Ambedkar, Jinnah, a Patidar farmer, a mill owner and a woman satyagrahi, each explaining what swaraj means to them."),
  blk("s7.reflection", "reflection", title="Think and explain",
    body="Why do you think a march to make a handful of salt became more powerful than many speeches? Write three reasons."),
  blk("s7.connection", "connection", title="Where this leads",
    body="- **Chapter 1:** compare Bharat Mata with Marianne and Germania, and Indian nationalism with European nationalism.\n- **Chapter 5, Print Culture:** newspapers and pamphlets spread nationalist ideas.\n"
         "- **Political Science, Gender, Religion and Caste:** the questions of separate electorates and reservations continue in today's democracy."),
  blk("s7.mastery", "mastery", title="Mastery challenge",
    body="Explain in about 120 words why different social groups joined the Civil Disobedience Movement and why some lost interest.\n\n"
         "**Model answer:** Rich peasants like the Patidars and Jats joined because falling prices made revenue impossible to pay, but left when the movement was called off in 1931 without revenue being reduced. "
         "Poor peasants wanted rents remitted and joined radical movements, but the Congress would not support no-rent campaigns. Business classes, organised in FICCI, wanted protection from imports and supported the movement at first, but after the failed Round Table Conference feared disruption and socialism. "
         "Industrial workers joined only in places like Nagpur and Chotanagpur. Women participated in large numbers. Dalits and many Muslims kept their distance because of the questions of separate electorates and communal tensions."),
  blk("s7.summary", "summary", title="Chapter summary",
    body="- The First World War brought taxes, price rises, forced recruitment, famine and epidemic, increasing anger against British rule.\n- Gandhiji's satyagraha: Champaran, Kheda (1917), Ahmedabad (1918); the Rowlatt satyagraha and the Jallianwala Bagh massacre (1919).\n"
         "- Khilafat and Non-Cooperation (Calcutta, September 1920; Nagpur, December 1920): different groups joined with their own hopes; withdrawn after Chauri Chaura (1922).\n"
         "- Simon Commission (1928), Lahore Congress and Purna Swaraj (1929), Salt March (1930) and Civil Disobedience; Gandhi–Irwin Pact (1931); Poona Pact (1932).\n"
         "- Participation and limits: rich and poor peasants, business classes, workers and women had different aims; dalits and many Muslims stayed away.\n- Collective belonging grew through Bharat Mata, Vande Mataram, folklore, flags and the reinterpretation of history."),
  blk("s7.examtips", "exam_tips", title="Board exam tips",
    body="- The **2-mark map question** in History comes from this chapter: learn all eight places and their dates.\n- 3/5-mark questions often ask: why Non-Cooperation was launched/withdrawn, the Salt March as a symbol, groups in the movements, separate electorates, cultural processes.\n"
         "- Always link a group to its aim (Awadh peasants → begar and rents; plantation workers → freedom to move).\n- Use exact terms: satyagraha, begar, Purna Swaraj, Poona Pact."),
  blk("s7.flash1", "flashcard", front="What did the Rowlatt Act (1919) allow?", back="Detention of political prisoners without trial for two years."),
  blk("s7.flash2", "flashcard", front="Where and when did Gandhiji break the salt law?", back="At Dandi, Gujarat, on 6 April 1930."),
  blk("s7.flash3", "flashcard", front="What was the Poona Pact (September 1932)?", back="Reserved seats for the Depressed Classes in legislatures, elected by the general electorate."),
  blk("s7.flash4", "flashcard", front="Who formed the Swaraj Party and why?", back="C. R. Das and Motilal Nehru, to return to council politics."),
 ]},
]

# ---------------- Sample paper ----------------
M("sqp2", PART, "Which one option from the following is the appropriate reason for the formation of the Swaraj Party?",
  [("To ask for Poorna Swaraj for Indians.", "Purna Swaraj was demanded by the Lahore Congress in 1929."), ("To return to Council Politics.", ""),
   ("To ask Dominion State for India.", "Dominion status was a British offer of 1929."), ("To oppose Simon Commission.", "The Simon Commission came in 1928; the Swaraj Party was formed earlier.")],
  "C. R. Das and Motilal Nehru formed the Swaraj Party within the Congress to argue for a return to council politics.", "medium", SQP("2 (VI version)"), correct=1)
W("sqp6a", "short_answer", BEL, "'A variety of cultural processes played an important role in developing a sense of nationalism in India.' Support the statement with suitable examples.",
  ["Image of Bharat Mata: Bankim Chandra Chattopadhyay's hymn 'Vande Mataram' (in Anandamath) was sung during the Swadeshi movement, and Abanindranath Tagore painted Bharat Mata as a calm, divine figure.",
   "Folklore: Rabindranath Tagore collected ballads, nursery rhymes and myths, and Natesa Sastri published The Folklore of Southern India, giving people pride in their traditional culture.",
   "Icons and history: the Swadeshi tricolour and Gandhiji's Swaraj flag (1921) became symbols of defiance, and nationalists rewrote history to take pride in India's past achievements."], source=SQP("6A"))
W("sqp6b", "short_answer", CDM, "'The Salt March became an effective tool of resistance against colonialism.' Analyse the statement with suitable reasons.",
  ["Salt was consumed by rich and poor alike, so the tax on salt and the government monopoly over its production affected every Indian; breaking the salt law united people of all classes.",
   "The march of 240 miles from Sabarmati to Dandi with 78 volunteers in 24 days drew thousands of people and wide publicity; on 6 April 1930 Gandhiji broke the law by making salt.",
   "It started the Civil Disobedience Movement: people now broke colonial laws, boycotted foreign cloth, picketed liquor shops and refused taxes, showing open defiance of British rule."], source=SQP("6B"))
W("sqp9", "very_short_answer", MAP, "On an outline map of India, two places A and B are marked. Identify them: (A) the place where the Civil Disobedience Movement was launched; (B) the city where the Indian National Congress session was held in September 1920.",
  ["(A) Dandi, Gujarat.", "(B) Calcutta (Kolkata), Bengal."], ["1 mark: (A)", "1 mark: (B)"], source=SQP(9), difficulty="easy")

# ---------------- NCERT exercises ----------------
W("ex1a", "short_answer", WAR, "Explain why the growth of nationalism in the colonies is linked to an anti-colonial movement.",
  ["In the colonies, people began discovering their unity in the process of their struggle with colonialism.",
   "The sense of being oppressed under colonial rule provided a shared bond that tied many different groups together.",
   "Each group felt the effects of colonialism differently and had its own idea of freedom, but a leader like Gandhiji forged them together into one movement against British rule."], source=ex("1(a)"))
W("ex1b", "short_answer", WAR, "How did the First World War help in the growth of the National Movement in India?",
  ["The war created a new economic situation: defence expenditure rose, financed by war loans, higher customs duties and the new income tax; prices doubled between 1913 and 1918.",
   "Villages were forced to supply soldiers, and forced recruitment caused widespread anger.",
   "Crop failures, food shortages and the influenza epidemic killed 12 to 13 million people; this hardship made people ready to join a mass movement against British rule."], source=ex("1(b)"))
W("ex1c", "short_answer", WAR, "Why were Indians outraged by the Rowlatt Act?",
  ["The Act was hurriedly passed in 1919 through the Imperial Legislative Council despite the united opposition of the Indian members.",
   "It gave the government enormous powers to repress political activities.",
   "It allowed the detention of political prisoners without trial for two years, which Indians saw as a denial of basic civil rights."], source=ex("1(c)"))
W("ex1d", "short_answer", NCM, "Why did Gandhiji decide to withdraw the Non-Cooperation Movement?",
  ["In February 1922 a peaceful demonstration at Chauri Chaura in Gorakhpur turned into a violent clash with the police.",
   "Gandhiji felt the movement was turning violent in many places, against his principle of non-violence.",
   "He believed satyagrahis needed proper training before they would be ready for mass struggles."], source=ex("1(d)"))
W("ex2", "short_answer", WAR, "What is meant by the idea of satyagraha?",
  ["Satyagraha emphasised the power of truth and the need to search for truth.",
   "If the cause was true and the fight was against injustice, physical force was not necessary to fight the oppressor.",
   "Without seeking vengeance or being aggressive, a satyagrahi could win the battle through non-violence, by appealing to the conscience of the oppressor; Gandhiji believed this could unite all Indians."], source=ex(2))
W("ex3a", "short_answer", WAR, "Write a newspaper report on the Jallianwala Bagh massacre.",
  ["Amritsar, 13 April 1919: a large crowd gathered in the enclosed ground of Jallianwala Bagh; some came to protest against government repression, others for the annual Baisakhi fair, unaware of martial law.",
   "General Dyer entered the area, blocked the exit points and opened fire on the crowd, killing hundreds of men, women and children.",
   "Dyer said his aim was to 'produce a moral effect' and create terror in the minds of satyagrahis; the news led to strikes and clashes across north India."], source=ex("3(a)"))
W("ex3b", "short_answer", CDM, "Write a newspaper report on the Simon Commission.",
  ["1928: a Statutory Commission under Sir John Simon, set up by the Tory government in Britain, has arrived in India to look into the functioning of the constitutional system and suggest changes.",
   "The commission does not have a single Indian member, which Indians see as an insult.",
   "It was greeted with the slogan 'Go back Simon'; all parties, including the Congress and the Muslim League, joined the demonstrations."], source=ex("3(b)"))
W("ex4", "short_answer", BEL, "Compare the images of Bharat Mata in this chapter with the image of Germania in Chapter 1.",
  ["Both are female allegories that give the abstract idea of the nation a concrete form and inspire patriotism.",
   "Germania wears a crown of oak leaves (heroism) and holds a sword, with symbols of strength, readiness to fight and a new era.",
   "Abanindranath Tagore's Bharat Mata is calm, composed, divine and spiritual, an ascetic figure bestowing learning, food and clothing; later images with a trishul, lion and elephant showed power, closer in spirit to Germania."], source=ex(4))
W("ex5", "long_answer", NCM, "List all the different social groups which joined the Non-Cooperation Movement of 1921. Then choose any three and write about their hopes and struggles to show why they joined the movement.",
  ["Groups: the urban middle class (students, teachers, lawyers), merchants and traders, peasants of Awadh, tribal peasants of the Gudem Hills, and plantation workers of Assam.",
   "Middle class in towns: students left government schools, lawyers gave up practice and traders refused foreign goods; they hoped swaraj would end foreign economic control.",
   "Awadh peasants (Baba Ramchandra): they struggled against talukdars who demanded high rents and begar; they wanted reduction of revenue and abolition of begar.",
   "Gudem Hills tribals (Alluri Sitarama Raju): the government had closed forests and forced them into begar; they fought to regain their traditional forest rights.",
   "Assam plantation workers: under the Inland Emigration Act (1859) they could not leave the gardens; for them swaraj meant freedom to move and return to their villages."], source=ex("discuss 1"))
W("ex6", "long_answer", CDM, "Discuss the Salt March to make clear why it was an effective symbol of resistance against colonialism.",
  ["On 31 January 1930 Gandhiji sent Viceroy Irwin eleven demands; the most stirring was the abolition of the salt tax, which hurt rich and poor alike.",
   "He walked 240 miles from Sabarmati to Dandi with 78 volunteers in 24 days; thousands joined meetings on the way, giving the march huge publicity.",
   "On 6 April 1930 he broke the salt law by boiling sea water to make salt, a simple act that every Indian could repeat.",
   "It started the Civil Disobedience Movement: people broke colonial laws, made salt, boycotted foreign cloth, picketed liquor shops and refused taxes.",
   "The salt law was the symbol of an unjust foreign government; breaking it showed that Indians would no longer obey British rule."], source=ex("discuss 2"))
W("ex7", "long_answer", PART, "Why did political leaders differ sharply over the question of separate electorates?",
  ["Separate electorates meant that a community would elect its own representatives; leaders differed on whether this protected or divided Indians.",
   "Dr B. R. Ambedkar believed political empowerment would solve the problems of the dalits and demanded separate electorates at the Second Round Table Conference.",
   "Gandhiji believed separate electorates would slow down the integration of dalits into society and went on a fast unto death; the Poona Pact (1932) gave reserved seats with a general electorate instead.",
   "Muslim leaders like Jinnah wanted guarantees of representation for Muslims; Jinnah was willing to give up separate electorates for reserved seats in the Central Assembly and representation in proportion to population in Bengal and Punjab.",
   "Hindu Mahasabha leaders like M. R. Jayakar opposed such compromises at the All Parties Conference of 1928; the issue increased mistrust between communities."], source=ex("discuss 4"))

# ---------------- Shine MCQs ----------------
M("mcq01", WAR, "Which tax was introduced in India to meet the expenses of the First World War?", [("Income tax", ""), ("Salt tax", "The salt tax already existed; it became the issue of 1930."), ("Chaukidari tax", "Chaukidari tax was a village tax, not a war measure."), ("Begar", "Begar was forced labour, not a tax.")], "Customs duties were raised and income tax was introduced.")
M("mcq02", WAR, "According to the census of 1921, how many people died due to famines and the epidemic?", [("12 to 13 million", ""), ("1 to 2 million", "The figure was much higher."), ("50 million", "The figure was 12 to 13 million."), ("100 thousand", "The figure was 12 to 13 million.")], "12 to 13 million people died.", "medium")
M("mcq03", WAR, "When did Gandhiji return to India from South Africa?", [("January 1915", ""), ("January 1919", "By 1919 he was leading the Rowlatt satyagraha."), ("April 1930", "April 1930 is the Salt March."), ("August 1920", "He had returned five years earlier.")], "January 1915.")
M("mcq04", WAR, "The Champaran satyagraha of 1917 was organised for:", [("peasants against the oppressive plantation system", ""), ("cotton mill workers", "That was Ahmedabad, 1918."), ("peasants who could not pay revenue after crop failure", "That was Kheda, 1917."), ("tea plantation workers of Assam", "That was during Non-Cooperation.")], "Champaran, Bihar: indigo plantation peasants.")
M("mcq05", WAR, "The Kheda satyagraha took place in which state?", [("Gujarat", ""), ("Bihar", "Champaran is in Bihar."), ("Punjab", "Jallianwala Bagh is in Punjab."), ("Uttar Pradesh", "Awadh is in Uttar Pradesh.")], "Kheda district, Gujarat.")
M("mcq06", WAR, "On which date did the Jallianwala Bagh massacre take place?", [("13 April 1919", ""), ("6 April 1919", "6 April 1919 was the hartal day."), ("6 April 1930", "That was the Salt March at Dandi."), ("26 January 1930", "That was Independence Day.")], "13 April 1919, Baisakhi day.")
M("mcq07", WAR, "Why had many people gathered at Jallianwala Bagh on 13 April 1919?", [("Some to protest against repression, others for the Baisakhi fair", ""), ("To welcome General Dyer", "Dyer was the officer who opened fire."), ("To attend a Congress session", "There was no Congress session there."), ("To start the Salt March", "The Salt March was in 1930.")], "Many did not know martial law had been imposed.")
M("mcq08", WAR, "The Khilafat Committee was formed in Bombay in:", [("March 1919", ""), ("September 1920", "That was the Calcutta session."), ("December 1929", "That was the Lahore Congress."), ("March 1931", "That was the Gandhi–Irwin Pact.")], "March 1919.", "medium")
M("mcq09", NCM, "In which book did Gandhiji say that British rule survived only because of Indian cooperation?", [("Hind Swaraj", ""), ("Anandamath", "Anandamath was written by Bankim Chandra Chattopadhyay."), ("The Folklore of Southern India", "That was by Natesa Sastri."), ("Gitanjali", "Gitanjali is Rabindranath Tagore's poetry.")], "Hind Swaraj (1909).")
M("mcq10", NCM, "The Non-Cooperation programme was adopted at which Congress session?", [("Nagpur, December 1920", ""), ("Calcutta, September 1920", "At Calcutta, Gandhiji convinced the leaders; the programme was adopted at Nagpur."), ("Lahore, December 1929", "Lahore demanded Purna Swaraj."), ("Madras, 1927", "Madras 1927 is on the map list, but Non-Cooperation was adopted at Nagpur.")], "Nagpur, December 1920.", "medium")
M("mcq11", NCM, "In which province did the Justice Party not boycott the council elections?", [("Madras", ""), ("Bengal", "The boycott was effective in most provinces."), ("Punjab", "The boycott was effective there."), ("Bombay", "The boycott was effective there.")], "The Justice Party, the party of the non-Brahmans, contested in Madras.")
M("mcq12", NCM, "Between 1921 and 1922 the value of imported foreign cloth fell from:", [("Rs 102 crore to Rs 57 crore", ""), ("Rs 57 crore to Rs 102 crore", "Imports fell, not rose."), ("Rs 200 crore to Rs 100 crore", "The figures were Rs 102 crore and Rs 57 crore."), ("Rs 10 crore to Rs 5 crore", "The figures were Rs 102 crore and Rs 57 crore.")], "Imports were halved.", "medium")
M("mcq13", NCM, "What was 'begar'?", [("Labour that villagers were forced to give without payment", ""), ("A tax on salt", "Salt tax is different."), ("A type of khadi cloth", "Begar has nothing to do with cloth."), ("A Congress session", "Begar was forced labour.")], "Forced unpaid labour.")
M("mcq14", NCM, "Who led the militant guerrilla movement in the Gudem Hills of Andhra Pradesh?", [("Alluri Sitarama Raju", ""), ("Baba Ramchandra", "He led the Awadh peasants."), ("C. R. Das", "He formed the Swaraj Party."), ("Abdul Ghaffar Khan", "He led the movement in the North-West Frontier.")], "Alluri Sitarama Raju, executed in 1924.")
M("mcq15", NCM, "Under which Act were Assam plantation workers not allowed to leave the tea gardens without permission?", [("Inland Emigration Act, 1859", ""), ("Rowlatt Act, 1919", "The Rowlatt Act allowed detention without trial."), ("Government of India Act, 1919", "That set up the provincial councils."), ("Vernacular Press Act, 1878", "That was a press law.")], "The Inland Emigration Act of 1859.", "medium")
M("mcq16", NCM, "The Oudh Kisan Sabha was headed by:", [("Jawaharlal Nehru, Baba Ramchandra and others", ""), ("Gandhiji and Irwin", "Irwin was the Viceroy."), ("C. R. Das and Motilal Nehru", "They formed the Swaraj Party."), ("Ambedkar and Jinnah", "They were not leaders of the Kisan Sabha.")], "Set up by October 1920.", "medium")
M("mcq17", CDM, "Which incident led Gandhiji to withdraw the Non-Cooperation Movement in February 1922?", [("Chauri Chaura", ""), ("Jallianwala Bagh", "That was in 1919, before Non-Cooperation began."), ("Dandi March", "That started Civil Disobedience."), ("Sholapur riots", "Sholapur was in 1930.")], "A violent clash with the police at Chauri Chaura, Gorakhpur.")
M("mcq18", CDM, "The Simon Commission was boycotted because:", [("it did not have a single Indian member", ""), ("it was headed by Gandhiji", "It was headed by Sir John Simon."), ("it abolished the salt tax", "It had nothing to do with salt."), ("it came during the Khilafat movement", "It came in 1928.")], "An all-British commission to decide India's future was seen as an insult.")
M("mcq19", CDM, "The Lahore session of December 1929, which demanded Purna Swaraj, was presided over by:", [("Jawaharlal Nehru", ""), ("Subhas Chandra Bose", "Bose was a younger radical leader, but did not preside at Lahore."), ("Motilal Nehru", "Motilal Nehru co-founded the Swaraj Party."), ("C. R. Das", "C. R. Das died in 1925.")], "Jawaharlal Nehru.")
M("mcq20", CDM, "Which date was declared Independence Day by the Congress in 1930?", [("26 January", ""), ("15 August", "15 August 1947 was the day of actual independence."), ("6 April", "6 April 1930 was the day at Dandi."), ("13 April", "13 April 1919 was Jallianwala Bagh.")], "26 January 1930.")
M("mcq21", CDM, "How many volunteers started the Salt March with Gandhiji?", [("78", ""), ("240", "240 miles was the distance."), ("24", "24 days was the time taken."), ("11", "11 was the number of demands in his letter.")], "78 trusted volunteers.", "medium")
M("mcq22", CDM, "How was Civil Disobedience different from Non-Cooperation?", [("People were asked to break colonial laws, not only refuse cooperation", ""), ("It was led by Ambedkar", "It was led by Gandhiji."), ("It supported the Khilafat", "Non-Cooperation supported the Khilafat."), ("It allowed violence", "Both were meant to be non-violent.")], "Civil Disobedience meant breaking unjust laws, such as the salt law.")
M("mcq23", CDM, "Whose arrest in April 1930 led to angry demonstrations in Peshawar?", [("Abdul Ghaffar Khan", ""), ("Jawaharlal Nehru", "Nehru was arrested, but the Peshawar protests followed Ghaffar Khan's arrest."), ("Alluri Sitarama Raju", "Raju was executed in 1924."), ("Baba Ramchandra", "He led the Awadh peasants in 1920–21.")], "Abdul Ghaffar Khan, a devout disciple of Gandhiji.", "medium")
M("mcq24", CDM, "The Gandhi–Irwin Pact was signed on:", [("5 March 1931", ""), ("6 April 1930", "That was the end of the Salt March."), ("September 1932", "That was the Poona Pact."), ("31 January 1930", "That was Gandhiji's letter to Irwin.")], "5 March 1931.", "medium")
M("mcq25", PART, "Which rich peasant communities actively supported Civil Disobedience?", [("Patidars of Gujarat and Jats of Uttar Pradesh", ""), ("Talukdars of Awadh", "Talukdars were the landlords the Awadh peasants opposed."), ("Junkers of Prussia", "That is European history."), ("Tea planters of Assam", "Planters were mostly British.")], "They were hit by falling prices and wanted revenue reduced.")
M("mcq26", PART, "FICCI was formed in 1927 under the leadership of:", [("Purshottamdas Thakurdas and G. D. Birla", ""), ("C. R. Das and Motilal Nehru", "They formed the Swaraj Party."), ("Ambedkar and Jayakar", "They were political leaders."), ("Muhammad Ali and Shaukat Ali", "They led the Khilafat movement.")], "Prominent industrialists led FICCI.")
M("mcq27", PART, "Who organised the dalits into the Depressed Classes Association in 1930?", [("Dr B. R. Ambedkar", ""), ("Gandhiji", "Gandhiji called them harijans but opposed separate electorates."), ("M. R. Jayakar", "He was a Hindu Mahasabha leader."), ("Jinnah", "He was a leader of the Muslim League.")], "Dr B. R. Ambedkar.")
M("mcq28", PART, "In the region of which city did industrial workers participate actively in Civil Disobedience?", [("Nagpur", ""), ("Madras", "Workers did not participate in large numbers there."), ("Lahore", "Workers did not participate in large numbers there."), ("Calcutta", "Workers did not participate in large numbers there.")], "Except in the Nagpur region, workers did not join in large numbers.", "medium")
M("mcq29", BEL, "Who wrote 'Vande Mataram'?", [("Bankim Chandra Chattopadhyay", ""), ("Rabindranath Tagore", "Tagore wrote India's national anthem, not Vande Mataram."), ("Abanindranath Tagore", "He painted Bharat Mata."), ("Natesa Sastri", "He collected Tamil folk tales.")], "Written in the 1870s, later included in Anandamath.")
M("mcq30", BEL, "Gandhiji's Swaraj flag of 1921 had which colours and symbol?", [("Red, green and white, with a spinning wheel", ""), ("Red, green and yellow, with eight lotuses", "That was the Swadeshi flag of Bengal."), ("Saffron, white and green, with the Ashoka Chakra", "That is today's national flag."), ("Black, red and gold", "That was the German liberal flag of 1848.")], "A tricolour with the charkha at the centre.", "medium")
M("mcq31", BEL, "The eight lotuses on the Swadeshi movement flag represented:", [("the eight provinces of British India", ""), ("eight religions", "The crescent moon represented Hindus and Muslims; the lotuses stood for provinces."), ("eight demands of Gandhiji", "Gandhiji sent eleven demands in 1930."), ("eight Congress sessions", "They represented provinces.")], "Eight provinces of British India.", "medium")
M("mcq32", BEL, "Who published the four-volume collection 'The Folklore of Southern India'?", [("Natesa Sastri", ""), ("Rabindranath Tagore", "Tagore collected Bengali ballads and rhymes."), ("Bankim Chandra Chattopadhyay", "He wrote Vande Mataram."), ("Abanindranath Tagore", "He was a painter.")], "Natesa Sastri, in Madras.", "medium")
# ---------------- Map work (text) ----------------
M("map01", MAP, "Map work: which place is associated with the satyagraha of indigo plantation peasants in 1917?", [("Champaran (Bihar)", ""), ("Kheda (Gujarat)", "Kheda was for peasants unable to pay revenue."), ("Ahmedabad (Gujarat)", "Ahmedabad was for mill workers, 1918."), ("Dandi (Gujarat)", "Dandi is the Salt March, 1930.")], "Champaran, Bihar.")
M("map02", MAP, "Map work: in which city was the Congress session of December 1920 held, where the Non-Cooperation programme was adopted?", [("Nagpur", ""), ("Calcutta", "Calcutta was the September 1920 session."), ("Madras", "Madras hosted the 1927 session."), ("Lahore", "Lahore hosted the 1929 session.")], "Nagpur, December 1920.", "medium")
M("map03", MAP, "Map work: the Indian National Congress session of 1927 on the CBSE map list was held at:", [("Madras", ""), ("Nagpur", "Nagpur was December 1920."), ("Calcutta", "Calcutta was September 1920."), ("Amritsar", "Amritsar is Jallianwala Bagh.")], "Madras, 1927.", "medium")
M("map04", MAP, "Map work: Jallianwala Bagh is located in:", [("Amritsar, Punjab", ""), ("Lahore, Punjab", "Jallianwala Bagh is in Amritsar."), ("Gorakhpur, Uttar Pradesh", "Gorakhpur is linked to Chauri Chaura."), ("Peshawar", "Peshawar saw protests in 1930.")], "Amritsar, Punjab.")
W("map05", "very_short_answer", MAP, "Map work: name the places in Gujarat on the CBSE map list for this chapter and state why each is famous.",
  ["Kheda (1917): satyagraha for peasants who could not pay revenue after crop failure and plague; Ahmedabad (1918): satyagraha of cotton mill workers.",
   "Dandi (6 April 1930): Gandhiji broke the salt law at the end of the Salt March, starting the Civil Disobedience Movement."], difficulty="easy")
# ---------------- Assertion-reason ----------------
C.arq("ar1", WAR, "Indians were outraged by the Rowlatt Act.", "It allowed the detention of political prisoners without trial for two years.", 0,
      "Detention without trial denied basic civil rights; that explains the outrage.", "it was passed despite united Indian opposition.", "detention without trial explains the anger.")
C.arq("ar2", NCM, "Gandhiji supported the Khilafat movement.", "He saw it as an opportunity to bring Muslims under the umbrella of a unified national movement.", 0,
      "R explains A.", "he joined it with Non-Cooperation in 1920.", "uniting Hindus and Muslims explains his support.")
C.arq("ar3", NCM, "The Non-Cooperation Movement slowed down in the cities.", "Khadi was cheaper than mill cloth.", 2,
      "A is true; R is false: khadi was more expensive than mill cloth.", "students and lawyers drifted back.", "khadi was costlier, not cheaper.")
C.arq("ar4", CDM, "The Simon Commission was greeted with the slogan 'Go back Simon'.", "It did not have a single Indian member.", 0,
      "R explains A.", "Indians boycotted it in 1928.", "an all-British commission was seen as an insult.")
C.arq("ar5", PART, "Gandhiji opposed separate electorates for dalits.", "He believed separate electorates would speed up their integration into society.", 2,
      "A is true; R is false: he believed they would slow down integration.", "he went on a fast unto death in 1932.", "he thought they would slow integration.")
C.arq("ar6", PART, "Rich peasants were disappointed when Civil Disobedience was called off in 1931.", "The revenue rates had not been revised.", 0,
      "R explains A.", "the Patidars and Jats felt let down.", "no revenue reduction explains their disappointment.")
# ---------------- True / false ----------------
C.tf("tf1", WAR, "The Jallianwala Bagh massacre took place in Lahore.", False, "It took place in Amritsar, on 13 April 1919.")
C.tf("tf2", CDM, "The Salt March covered over 240 miles from Sabarmati to Dandi in 24 days.", True, "About 10 miles a day, with 78 volunteers.")
C.tf("tf3", PART, "The Poona Pact gave the Depressed Classes separate electorates.", False, "It gave reserved seats, but they were elected by the general electorate.")
C.tf("tf4", CDM, "The Swaraj Party was formed outside the Congress.", False, "C. R. Das and Motilal Nehru formed it within the Congress.")
# ---------------- Shine written ----------------
W("vsa1", "very_short_answer", WAR, "What were the effects of the First World War on the Indian economy? Give two.",
  ["Defence expenditure rose, financed by war loans, higher customs duties and the introduction of income tax.", "Prices doubled between 1913 and 1918, causing extreme hardship for the common people."])
W("vsa2", "very_short_answer", NCM, "What did swaraj mean to the plantation workers of Assam?",
  ["The right to move freely in and out of the confined space of the tea gardens, which the Inland Emigration Act of 1859 denied them.", "Retaining a link with the villages they had come from."])
W("vsa3", "very_short_answer", BEL, "Describe the two flags designed during the national movement.",
  ["Swadeshi movement (Bengal): a tricolour of red, green and yellow, with eight lotuses for the eight provinces and a crescent moon for Hindus and Muslims.",
   "Gandhiji's Swaraj flag (1921): a tricolour of red, green and white with a spinning wheel at the centre, representing self-help."])
W("sa1", "short_answer", NCM, "How did the Non-Cooperation Movement spread in the countryside of Awadh?",
  ["Peasants led by Baba Ramchandra rose against talukdars and landlords who demanded high rents, cesses and begar.",
   "They demanded reduction of revenue and abolition of begar, and organised nai–dhobi bandhs to boycott oppressive landlords; the Oudh Kisan Sabha was set up by October 1920 with Nehru and Baba Ramchandra.",
   "In 1921 houses of talukdars and merchants were attacked and grain hoards taken over, as local leaders claimed Gandhiji had said no taxes would be paid."])
W("sa2", "short_answer", PART, "Why did the industrial working class not participate in large numbers in the Civil Disobedience Movement?",
  ["The industrialists, who were close to the Congress, did not want workers' demands to be part of the movement.",
   "The Congress was reluctant to include workers' demands in its programme, fearing it would alienate industrialists and divide the anti-imperial forces.",
   "So workers joined mainly in the Nagpur region; elsewhere only some adopted the boycott, and railway, dock and Chotanagpur mine workers took part in strikes and rallies."])
W("sa3", "short_answer", PART, "Describe the role of women in the Civil Disobedience Movement.",
  ["Women participated in large numbers in protest marches, manufactured salt and picketed foreign-cloth and liquor shops; many went to jail.",
   "In urban areas they were mostly from high-caste families; in rural areas from rich peasant households, moved by Gandhiji's call to serve the nation.",
   "Yet their position did not change much: Gandhiji believed women's duty was home and hearth, and the Congress was reluctant to give women positions of authority."])
W("la1", "long_answer", CDM, "Describe the events from the Simon Commission to the Gandhi–Irwin Pact.",
  ["1928: the Simon Commission, with no Indian member, arrived and was greeted with 'Go back Simon'; in October 1929 Irwin offered a vague dominion status and a Round Table Conference.",
   "December 1929: the Lahore Congress under Nehru demanded Purna Swaraj; 26 January 1930 was celebrated as Independence Day.",
   "31 January 1930: Gandhiji sent Irwin eleven demands, including abolition of the salt tax; on 12 March he began the Salt March and broke the salt law at Dandi on 6 April.",
   "Civil Disobedience spread: people broke laws and refused taxes; Abdul Ghaffar Khan and Gandhiji were arrested; about 100,000 people were jailed.",
   "5 March 1931: in the Gandhi–Irwin Pact, Gandhiji agreed to attend the Round Table Conference, and the government agreed to release political prisoners."])
# ---------------- Case and source based ----------------
W("cb1", "case_based", NCM, "Read the source and answer the questions.\n\n*\"The movement started with middle-class participation in the cities. Thousands of students left government-controlled schools and colleges, headmasters and teachers resigned, and lawyers gave up their legal practices. The council elections were boycotted in most provinces except Madras... The effects of non-cooperation on the economic front were more dramatic. Foreign goods were boycotted, liquor shops picketed, and foreign cloth burnt in huge bonfires.\"* (NCERT)\n\n"
  "(i) Why did the Justice Party not boycott the council elections in Madras? (1)\n\n(ii) By how much did the import of foreign cloth fall between 1921 and 1922? (1)\n\n(iii) Give two reasons why the movement slowed down in the cities. (2)",
  ["(i) It was the party of the non-Brahmans, and it felt that entering the council was one way of gaining power.", "(ii) It halved: its value dropped from Rs 102 crore to Rs 57 crore.",
   "(iii) Khadi was more expensive than mill cloth, so the poor could not afford it; alternative Indian institutions were slow to come up, so students, teachers and lawyers went back."])
W("cb2", "case_based", CDM, "Read the source and answer the questions.\n\n*\"Mahatma Gandhi found in salt a powerful symbol that could unite the nation. On 31 January 1930, he sent a letter to Viceroy Irwin stating eleven demands... The most stirring of all was the demand to abolish the salt tax. Salt was something consumed by the rich and the poor alike, and it was one of the most essential items of food.\"* (NCERT)\n\n"
  "(i) Why was salt a powerful symbol? (1)\n\n(ii) What would the Congress do if the demands were not met by 11 March? (1)\n\n(iii) Describe the Salt March in brief. (2)",
  ["(i) It was consumed by rich and poor alike and was one of the most essential items of food.", "(ii) It would launch a civil disobedience campaign.",
   "(iii) Gandhiji walked over 240 miles with 78 volunteers from Sabarmati to Dandi in 24 days, and on 6 April 1930 broke the salt law by making salt from sea water, starting Civil Disobedience."])
W("cb3", "case_based", PART, "Read the source and answer the questions.\n\n*\"Dr B.R. Ambedkar, who organised the dalits into the Depressed Classes Association in 1930, clashed with Mahatma Gandhi at the second Round Table Conference by demanding separate electorates for dalits. When the British government conceded Ambedkar's demand, Gandhiji began a fast unto death.\"* (NCERT)\n\n"
  "(i) What did Ambedkar demand at the Second Round Table Conference? (1)\n\n(ii) Why did Gandhiji go on a fast unto death? (1)\n\n(iii) What was the outcome of this conflict? (2)",
  ["(i) Separate electorates for the dalits.", "(ii) He believed separate electorates would slow down the integration of dalits into society.",
   "(iii) The Poona Pact of September 1932: the Depressed Classes (later Scheduled Castes) got reserved seats in provincial and central legislative councils, but they were to be voted in by the general electorate."])

chapter = header(SUBJ, N, "Nationalism in India", ["war_and_satyagraha", "non_cooperation", "civil_disobedience", "participants_and_limits", "collective_belonging", "map_work"],
  "Follows the CBSE 2025-26 Social Science (087) syllabus: this chapter is fully in the board examination and carries the History map items (Congress sessions of 1920 Calcutta, 1920 Nagpur and 1927 Madras; Kheda, Champaran and Ahmedabad mill workers; Jallianwala Bagh; Dandi).")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
