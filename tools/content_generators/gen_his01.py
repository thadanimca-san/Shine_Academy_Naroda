"""CBSE Class 10 History Ch 1: The Rise of Nationalism in Europe (fully in the 2025-26 board syllabus)."""
import sys
from ss_common import make, header, path, SQP, SHINE, MS2, MS3, MS5, CB

ROOT = sys.argv[1]
SUBJ, N = "history", 1
PATH = path(SUBJ, "ch01_rise_of_nationalism_in_europe")
C = make(SUBJ, N, "his10ch01")
blk, kc, M, W = C.blk, C.kc, C.m, C.w
FR, LIB, REV, UNI, VIS = ["french_revolution_napoleon"], ["liberalism_conservatism"], ["age_of_revolutions"], ["unification"], ["visualising_balkans"]
def ex(n): return {"kind": "ncert_exercise", "exercise": "Chapter 1 exercises", "question": n}

TIMELINE = ("| Year | Event |\n|---|---|\n| 1789 | French Revolution |\n| 1804 | Napoleonic Code (Civil Code) |\n| 1814–1815 | Fall of Napoleon; Congress and Treaty of Vienna |\n"
            "| 1821 | Greek struggle for independence begins |\n| 1830 | July Revolution in France; Belgium breaks away from the Netherlands |\n| 1832 | Treaty of Constantinople recognises Greece as independent |\n"
            "| 1834 | Zollverein (customs union) formed under Prussia |\n| 1848 | Revolutions across Europe; Frankfurt Parliament (18 May) |\n| 1859–1870 | Unification of Italy (Victor Emmanuel II proclaimed king in 1861) |\n"
            "| 1866–1871 | Unification of Germany (William I proclaimed Emperor at Versailles, January 1871) |\n| 1914 | First World War begins |")
LIBCON = ("| | Liberalism | Conservatism |\n|---|---|---|\n| Root idea | *liber* (Latin) = free: freedom for the individual, equality before law | preserve traditional institutions: monarchy, Church, social hierarchy, property, family |\n"
          "| Government | by consent; constitution and representative (elected) parliament | strong monarchy; change only gradually |\n"
          "| Economy | freedom of markets; abolition of state-imposed restrictions on movement of goods and capital | accepted modernisation (army, bureaucracy, economy) to strengthen monarchy |\n"
          "| After 1815 | wanted to unite German/Italian states into nation-states | Congress of Vienna (1815) tried to undo Napoleon's changes |")
VIENNA = ("| Provision of the Treaty of Vienna (1815) | Purpose |\n|---|---|\n| The Bourbon dynasty restored to power in France | bring back the old monarchy |\n"
          "| France lost the territories it had annexed under Napoleon | weaken France |\n| States set up on France's borders: Kingdom of the Netherlands (with Belgium) in the north; Genoa added to Piedmont in the south | prevent French expansion |\n"
          "| Prussia given important new territories on its western frontier; Austria given control of northern Italy | strengthen the conservative powers |\n"
          "| German Confederation of 39 states (set up by Napoleon) left untouched | |\n| In the east, Russia given part of Poland; Prussia a portion of Saxony | |")
GERMANIA = ("| Symbol (Germania, painted by Philip Veit, 1848) | Meaning |\n|---|---|\n| Broken chains | being freed |\n| Breastplate with eagle | symbol of the German empire: strength |\n"
            "| Crown of oak leaves | heroism |\n| Sword | readiness to fight |\n| Olive branch around the sword | willingness to make peace |\n"
            "| Black, red and gold tricolour | flag of the liberal-nationalists in 1848, banned by the dukes of the German states |\n| Rays of the rising sun | beginning of a new era |")
UNIFY = ("| | Germany | Italy |\n|---|---|---|\n| Before unity | 39 states in the German Confederation | 7 states; only Sardinia-Piedmont ruled by an Italian princely house |\n"
         "| Leader state | Prussia | Sardinia-Piedmont |\n| Key people | Otto von Bismarck (chief minister), William I | Mazzini, Cavour (chief minister), Garibaldi, Victor Emmanuel II |\n"
         "| Method | three wars over seven years, with Denmark, Austria and France; army and bureaucracy | diplomacy (alliance with France), war with Austria (1859), Garibaldi's volunteers in the south (1860) |\n"
         "| Result | January 1871: William I proclaimed German Emperor in the Hall of Mirrors, Versailles | 1861: Victor Emmanuel II proclaimed king of united Italy |")

sections = [
 {"id": "s1", "title": "A dream of nations", "blocks": [
  blk("s1.hook", "hook", title="A painting that imagined the future",
    body="In 1848 a French artist, **Frédéric Sorrieu**, made a set of four prints showing his dream of a world of **\"democratic and social republics\"**. "
         "In the first print, the peoples of Europe and America, men and women of all ages, march in a long line and offer homage to the **Statue of Liberty**, who holds the torch of Enlightenment in one hand and the Charter of the Rights of Man in the other. "
         "In the foreground lie the shattered remains of the symbols of **absolutist institutions**. Above them, Christ, saints and angels watch: a sign of fraternity among the nations.\n\n"
         "In 1848 this was only a dream: Europe was ruled by kings and emperors over many small states and huge mixed empires. By 1871 Germany and Italy had become nation-states. How did this happen? That is the story of this chapter."),
  blk("s1.inspiration", "inspiration", title="The general with the red shirts", person="Giuseppe Garibaldi", years="1807–1882",
    body="Garibaldi was a sailor from Nice who joined Mazzini's Young Italy movement and was sentenced to death after a failed rising in 1834. He escaped to South America and returned to fight for Italy.\n\n"
         "In 1860 he led his famous **Expedition of the Thousand**, armed volunteers in red shirts, into South Italy and the Kingdom of the Two Sicilies, drove out the Spanish Bourbon rulers and handed the south over to King Victor Emmanuel II. "
         "Ordinary people with courage and a shared idea helped create a nation.",
    future="History builds the skills of reading sources, weighing evidence and arguing a case: useful in civil services, law, journalism, teaching, archives and museums."),
  C.socratic("s1.socratic", "Before 1800, people in Europe mostly saw themselves as subjects of a king or members of a local community. What new idea made them feel they belonged to one **nation**?",
    ["A shared identity: common language, history, culture and equal rights as citizens", "Paying taxes to the same king", "Living near the same river"], 0,
    "A nation is held together by a sense of shared identity and history. The French Revolution turned subjects into citizens, and this idea spread across Europe."),
 ]},
 {"id": "s2", "title": "The French Revolution and the idea of the nation", "blocks": [
  blk("s2.thm", "theory", title="From subjects to citizens", revision=True,
    body="The first clear expression of nationalism came with the **French Revolution of 1789**. Political and constitutional changes transferred sovereignty from the monarchy to a body of French citizens: **the people** would now form the nation and shape its destiny.\n\n"
         "**Measures to create a collective identity among the French people:**\n- The ideas of ***la patrie*** (the fatherland) and ***le citoyen*** (the citizen) stressed a united community with equal rights under a constitution.\n"
         "- A new French flag, the **tricolour**, replaced the royal standard.\n- The Estates General was elected by active citizens and renamed the **National Assembly**.\n"
         "- New hymns were composed, oaths taken and martyrs commemorated, all in the name of the nation.\n- A **centralised administrative system** made uniform laws for all citizens.\n"
         "- Internal customs duties and dues were abolished, and a **uniform system of weights and measures** was adopted.\n- Regional dialects were discouraged; **French**, as spoken and written in Paris, became the common language.\n\n"
         "The revolutionaries declared it their mission to liberate the peoples of Europe from despotism. Students and members of the educated middle classes set up **Jacobin clubs** in other countries, and the French armies carried the idea of nationalism abroad."),
  blk("s2.napoleon", "theory", title="Napoleon: reforms and resentment", revision=True,
    body="Napoleon destroyed democracy in France, but he made administration more rational and efficient. His **Civil Code of 1804**, known as the **Napoleonic Code**:\n"
         "- did away with all privileges based on birth;\n- established equality before the law;\n- secured the right to property.\n\n"
         "He carried these reforms into the regions he conquered (Dutch Republic, Switzerland, Italy, Germany):\n- simplified administrative divisions;\n- abolished the feudal system and freed peasants from serfdom and manorial dues;\n"
         "- removed guild restrictions in towns;\n- improved transport and communication;\n- standardised weights and measures and a common national currency helped businessmen and small producers.\n\n"
         "**Why enthusiasm turned to hostility:** increased taxation, censorship, and forced conscription into the French armies to conquer the rest of Europe outweighed the advantages of the reforms."),
  C.kc("s2.check", "Which of these was NOT a feature of the Napoleonic Code of 1804?",
    [("It gave the vote to all adult men and women", ""), ("It did away with privileges based on birth", "This *was* a feature of the Code."),
     ("It established equality before the law", "This *was* a feature of the Code."), ("It secured the right to property", "This *was* a feature of the Code.")],
    "The Napoleonic Code did not give universal suffrage; it denied women rights and made them subject to the authority of fathers and husbands."),
 ]},
 {"id": "s3", "title": "Europe after Napoleon: liberals and conservatives", "blocks": [
  blk("s3.thm", "theory", title="A Europe of empires and classes", revision=True,
    body="In the mid-18th century there were no 'nation-states' as we know them. Germany, Italy and Switzerland were divided into kingdoms, duchies and cantons. Eastern and Central Europe were under autocratic monarchies with many peoples. "
         "The **Habsburg Empire** (Austria-Hungary) was a patchwork: German-speaking regions like the Alpine Tyrol, Austria and the Sudetenland, and Bohemia; Italian-speaking Lombardy and Venetia; half of Hungary spoke Magyar; Galicia spoke Polish; and there were many Slav peasants (Bohemians, Slovaks, Slovenes, Croats, Roumans).\n\n"
         "**Social classes:** a small, landed **aristocracy** (who spoke French and were united by lifestyle and marriage across Europe) dominated a majority of **peasants**. "
         "With industrialisation (England from the late 18th century; France and the German states in the 19th) a **new middle class** of industrialists, businessmen and professionals grew. Among the educated middle class, ideas of national unity following the abolition of aristocratic privileges gained popularity.\n\n"
         "**Economic liberalism:** in the German states there were 39 states with their own currencies, weights and measures; a merchant travelling from Hamburg to Nuremberg had to pass 11 customs barriers. "
         "In **1834** a customs union, the **Zollverein**, was formed at the initiative of **Prussia** and joined by most German states. It abolished tariff barriers and reduced the number of currencies from over thirty to two. A network of railways improved mobility. Economic nationalism strengthened the wider nationalist feeling."),
  blk("s3.libcon", "markdown_table", title="Liberalism vs conservatism", revision=True, body=LIBCON),
  blk("s3.vienna", "theory", title="The Congress of Vienna (1815)", revision=True,
    body="After Napoleon's defeat in 1815, representatives of the European powers **Britain, Russia, Prussia and Austria** met at Vienna. The Congress was hosted by the Austrian Chancellor **Duke Metternich**. "
         "The **Treaty of Vienna** aimed to undo most of the changes made during the Napoleonic wars.\n\n"
         "The conservative regimes set up after 1815 were **autocratic**: they did not tolerate criticism, imposed censorship on newspapers, books, plays and songs, and suppressed liberal ideas. Even so, the memory of the French Revolution inspired liberals.\n\n"
         "**Revolutionaries:** many liberal-nationalists went underground and formed secret societies. **Giuseppe Mazzini**, an Italian revolutionary from Genoa, became a member of the secret society of the **Carbonari**. "
         "After a failed revolution in Liguria he was sent into exile in **1831**. He founded **Young Italy** in Marseilles and **Young Europe** in Berne. He believed God intended nations to be the natural units of mankind, so Italy could not remain a patchwork of small states. "
         "Metternich described him as *\"the most dangerous enemy of our social order\"*."),
  blk("s3.table", "markdown_table", title="What the Treaty of Vienna did", revision=True, body=VIENNA),
  C.kc("s3.check", "Who hosted the Congress of Vienna in 1815?",
    [("Duke Metternich", ""), ("Otto von Bismarck", "Bismarck led German unification in the 1860s."), ("Giuseppe Mazzini", "Mazzini was a revolutionary whom Metternich called a dangerous enemy."), ("Napoleon", "The Congress met after Napoleon's defeat.")],
    "The Austrian Chancellor, Duke Metternich, hosted the Congress of Vienna."),
  C.kc("s3.check2", "What was the Zollverein?",
    [("A customs union of German states formed in 1834 under Prussia", ""), ("A secret society of Italian revolutionaries", "That was the Carbonari."),
     ("A parliament that met in Frankfurt in 1848", "That was the Frankfurt Parliament."), ("A treaty that recognised Greece as independent", "That was the Treaty of Constantinople (1832).")],
    "The Zollverein (1834) abolished tariff barriers among German states and reduced currencies from over thirty to two."),
 ]},
 {"id": "s4", "title": "The age of revolutions: 1830–1848", "blocks": [
  blk("s4.thm", "theory", title="Revolutions, culture and hunger", revision=True,
    body="**1830, France:** the **July Revolution** overthrew the Bourbon kings who had been restored in 1815; a constitutional monarchy was set up with **Louis Philippe** at its head. Metternich remarked, *\"When France sneezes, the rest of Europe catches cold.\"* "
         "The July Revolution sparked an uprising in Brussels, and **Belgium broke away** from the United Kingdom of the Netherlands.\n\n"
         "**Greece:** Greece had been part of the Ottoman Empire since the 15th century. The struggle for independence began in **1821**. Nationalists got support from Greeks living in exile and from many West Europeans who admired ancient Greek culture. "
         "Poets and artists praised Greece as the cradle of European civilisation; the English poet **Lord Byron** organised funds and went to fight, dying of fever in 1824. The **Treaty of Constantinople (1832)** recognised Greece as an independent nation.\n\n"
         "**Culture and the nation (Romanticism):** Romantic artists and poets criticised the glorification of reason and focused instead on emotions, intuition and mystical feelings, to create a sense of a shared collective heritage. "
         "The German philosopher **Johann Gottfried Herder** claimed that true German culture was to be discovered among the common people, ***das volk***, through folk songs, folk poetry and folk dances.\n"
         "- **Poland**, partitioned at the end of the 18th century by Russia, Prussia and Austria, kept nationalism alive through music and language. **Karol Kurpinski** celebrated the national struggle through his operas and music, turning folk dances like the *polonaise* and *mazurka* into national symbols. "
         "After the Russian occupation, Russian was imposed everywhere; after a failed armed rebellion against Russian rule in **1831**, the clergy used Polish as a weapon of resistance, and using Polish came to be seen as a symbol of the struggle.\n"
         "- In Germany, the **Grimm brothers** collected folktales, seeing them as an expression of the national spirit.\n\n"
         "**Hunger and hardship:** the 1830s were years of great economic hardship: population rise, unemployment, competition from cheap machine-made goods from England, food shortages. In **1845** weavers in **Silesia** revolted against contractors who had drastically reduced payments.\n\n"
         "**1848:** food shortages and widespread unemployment brought the people of Paris onto the roads. **Louis Philippe was forced to flee**; a National Assembly proclaimed a **Republic**, granted suffrage to all adult males above 21, and guaranteed the right to work. National workshops were set up to provide employment."),
  blk("s4.liberals", "theory", title="The 1848 revolution of the liberals", revision=True,
    body="Alongside the revolts of the poor, educated middle classes in Germany, Italy, Poland and the Austro-Hungarian Empire demanded constitutionalism with national unification: a nation-state based on parliamentary principles, a constitution, freedom of the press and freedom of association.\n\n"
         "**Frankfurt Parliament:** in the German regions, middle-class professionals, businessmen and artisans elected an all-German National Assembly. On **18 May 1848**, **831 elected representatives** took their places in the **Church of St Paul** in Frankfurt. "
         "They drafted a constitution for a German nation to be headed by a monarchy subject to a parliament. When the deputies offered the crown to **Friedrich Wilhelm IV, King of Prussia**, he **rejected it** and joined other monarchs to oppose the elected assembly. "
         "The Parliament was dominated by the middle classes, who resisted the demands of workers and artisans and so lost their support. In the end, troops were called in and the assembly was forced to disband.\n\n"
         "**Women:** the issue of political rights for women was controversial. Women had formed their own associations and newspapers, but they were **denied suffrage** in the Assembly and could attend only as observers in the visitors' gallery.\n\n"
         "**Results:** the 1848 uprisings were suppressed, but the autocratic monarchs realised that revolution could be avoided only by concessions. **Serfdom and bonded labour were abolished** in the Habsburg dominions and in Russia, and the Habsburg rulers granted more autonomy to the Hungarians in **1867**."),
  C.kc("s4.check", "Which treaty recognised Greece as an independent nation?",
    [("Treaty of Constantinople, 1832", ""), ("Treaty of Vienna, 1815", "The Treaty of Vienna restored conservative rule after Napoleon."),
     ("Treaty of Versailles, 1919", "That ended the First World War."), ("Act of Union, 1707", "That united England and Scotland.")],
    "The Treaty of Constantinople (1832) recognised Greece as an independent nation."),
  C.kc("s4.check2", "Why did the Frankfurt Parliament fail?",
    [("The King of Prussia rejected the crown and the middle-class deputies lost the support of workers and artisans", ""),
     ("Napoleon's army attacked Frankfurt", "Napoleon had been defeated by 1815."), ("Women won the right to vote and opposed the monarchy", "Women were denied suffrage."),
     ("Britain refused to recognise it", "Britain was not involved.")],
    "Friedrich Wilhelm IV rejected the crown and opposed the assembly, and the middle classes resisted workers' demands, so the parliament lost support and was disbanded by troops."),
 ]},
 {"id": "s5", "title": "The making of Germany, Italy and Britain", "blocks": [
  blk("s5.thm", "theory", title="Nationalism from above", revision=True,
    body="After 1848, nationalism moved away from democracy and revolution. Conservatives used nationalist feelings to strengthen state power and gain political control.\n\n"
         "**Germany: can the army be the architect of a nation?** Nationalist feelings were widespread among middle-class Germans, who tried to unite the German Confederation in 1848 but were crushed by the monarchy and the military, supported by the large landowners of Prussia (the **Junkers**). "
         "**Prussia** then took the lead. Its chief minister, **Otto von Bismarck**, was the architect of this process, carried out with the help of the Prussian army and bureaucracy. **Three wars over seven years**, with **Austria, Denmark and France**, ended in Prussian victory. "
         "In **January 1871**, the Prussian king **William I** was proclaimed **German Emperor** in a ceremony at **Versailles**. The new state placed a strong emphasis on modernising the currency, banking, legal and judicial systems.\n\n"
         "**Italy unified:** Italy was divided into **seven states**; only **Sardinia-Piedmont** was ruled by an Italian princely house. The north was under the Austrian Habsburgs, the centre under the Pope, and the south under the Bourbon kings of Spain. Even the Italian language had many regional variations. "
         "Mazzini's revolutionary uprisings of 1831 and 1848 failed. Then **King Victor Emmanuel II** of Sardinia-Piedmont took up the task through war. His chief minister **Count Camillo de Cavour** was neither a revolutionary nor a democrat; like many educated Italians he spoke French much better than Italian. "
         "Through a tactful diplomatic alliance with **France**, Sardinia-Piedmont defeated the Austrian forces in **1859**. A large number of armed volunteers under **Giuseppe Garibaldi** joined. In **1860** they marched into South Italy and the Kingdom of the Two Sicilies and drove out the Spanish rulers. "
         "In **1861** Victor Emmanuel II was proclaimed **king of united Italy**. Most of the people, many of them illiterate peasants, were not aware of the liberal-nationalist ideology.\n\n"
         "**The strange case of Britain:** in Britain the nation-state was **not the result of a sudden upheaval or revolution, but of a long-drawn-out process**. Before the 18th century there was no British nation; the English, Welsh, Scots and Irish had their own cultures. "
         "The **English** grew in wealth and power and extended their influence. The English **Parliament**, which had seized power from the monarchy in **1688**, was the instrument of nation-building. The **Act of Union (1707)** between England and Scotland created the **United Kingdom of Great Britain**, which in effect meant England imposed its influence on Scotland; Scottish culture and the Gaelic language were suppressed. "
         "In **Ireland**, Catholics and Protestants were divided; after a failed revolt led by **Wolfe Tone** and his United Irishmen (1798), Ireland was **forcibly incorporated in 1801**. A new British nation was forged through an English culture: the **British flag (Union Jack)**, the national anthem (**God Save Our Noble King**) and the **English language** were actively promoted."),
  blk("s5.table", "markdown_table", title="Germany and Italy compared", revision=True, body=UNIFY),
  C.kc("s5.check", "Who was the chief minister of Sardinia-Piedmont who led the movement to unify Italy through diplomacy?",
    [("Count Camillo de Cavour", ""), ("Giuseppe Garibaldi", "Garibaldi led armed volunteers; he was not chief minister."), ("Otto von Bismarck", "Bismarck was the chief minister of Prussia."), ("Giuseppe Mazzini", "Mazzini was a revolutionary in exile.")],
    "Cavour, chief minister of Sardinia-Piedmont, made the alliance with France that defeated Austria in 1859."),
  C.kc("s5.check2", "Which statement about the British nation-state is correct?",
    [("It developed through a long-drawn-out process, not a sudden revolution", ""), ("It was created by Bismarck's three wars", "That was Germany."),
     ("Scotland's culture was given equal importance", "Scottish culture and Gaelic were suppressed."), ("Ireland joined voluntarily in 1707", "Ireland was forcibly incorporated in 1801.")],
    "Britain's nation-state grew gradually, through the English Parliament, the Act of Union (1707) and the incorporation of Ireland (1801)."),
 ]},
 {"id": "s6", "title": "Visualising the nation, and the road to war", "blocks": [
  blk("s6.thm", "theory", title="Nations as women: allegory", revision=True,
    body="Artists in the 18th and 19th centuries personified nations, showing a country as if it were a person. Nations were portrayed as **female figures**. The female form did not stand for any real woman; it gave the abstract idea of the nation a concrete form. "
         "Such a figure is an **allegory**: an abstract idea (greed, envy, freedom, liberty) expressed through a person or a thing.\n\n"
         "- **Marianne (France):** a popular Christian name, chosen to underline the idea of a people's nation. Her characteristics were drawn from those of Liberty and the Republic: **the red cap, the tricolour, the cockade**. Statues of Marianne were put up in public squares, and her image was marked on coins and stamps.\n"
         "- **Germania (Germany):** she wears a **crown of oak leaves**, because the German oak stands for heroism. The painter **Philip Veit** painted Germania in 1848; it hung from the ceiling of St Paul's Church, where the Frankfurt Parliament met."),
  blk("s6.germania", "markdown_table", title="The symbols around Germania", revision=True, body=GERMANIA),
  blk("s6.balkans", "theory", title="Nationalism and imperialism: the Balkans", revision=True,
    body="By the last quarter of the 19th century, nationalism no longer kept its idealistic, liberal-democratic spirit. It became a narrow creed with limited ends, and nationalist groups became intolerant of each other and ready to go to war.\n\n"
         "The most serious source of tension after 1871 was the **Balkans**, a region of geographical and ethnic variation: modern-day Romania, Bulgaria, Albania, Greece, Macedonia, Croatia, Bosnia-Herzegovina, Slovenia, Serbia and Montenegro. Its inhabitants were broadly known as the **Slavs**. "
         "A large part of the Balkans was under the control of the **Ottoman Empire**. The spread of romantic nationalism together with the disintegration of the Ottoman Empire made the region very explosive.\n\n"
         "- Balkan peoples claimed independence on the basis of nationality, using history to prove they had once been free.\n- The Balkan states were jealous of each other and each wanted more territory at the others' expense.\n"
         "- The great European powers, **Russia, Germany, England and Austro-Hungary**, competed for trade, colonies and naval and military might, and each tried to counter the others' hold over the Balkans.\n\n"
         "This led to a series of wars in the region and finally the **First World War (1914)**. Many countries colonised by the Europeans later opposed imperial domination; their anti-imperial movements were nationalist too, but they built their own forms of nationalism."),
  blk("s6.timeline", "markdown_table", title="Timeline of the chapter", revision=True, body=TIMELINE),
  C.kc("s6.check", "In the allegory of Germania, what does the crown of oak leaves stand for?",
    [("Heroism", ""), ("Readiness to fight", "That is the sword."), ("Being freed", "That is the broken chains."), ("Willingness to make peace", "That is the olive branch.")],
    "The German oak stands for heroism."),
  C.kc("s6.check2", "Why was the Balkan region called a source of tension after 1871?",
    [("Rising nationalism, the breakup of the Ottoman Empire and rivalry among the big European powers", ""), ("It was the home of the Frankfurt Parliament", "The Frankfurt Parliament met in Germany."),
     ("It had already united peacefully under one king", "The Balkan states were rivals, not united."), ("Britain ruled the whole region", "Most of it was under the Ottoman Empire.")],
    "Slav nationalism, Ottoman decline and great-power rivalry made the Balkans explosive and led to the First World War."),
 ]},
 {"id": "s7", "title": "Remember, avoid, practise", "blocks": [
  blk("s7.memory", "memory_trick", title="Memory tricks",
    body="- **French collective identity, \"P-C-T-N-H-C-W-L\":** **P**atrie, **C**itoyen, **T**ricolour, **N**ational Assembly, **H**ymns/oaths, **C**entralised laws, **W**eights and measures, **L**anguage (French).\n"
         "- **Germany = B-P-W-3-71:** **B**ismarck, **P**russia, **W**illiam I, **3** wars (Denmark, Austria, France: *DAF*), **1871**.\n"
         "- **Italy = M-C-G-V:** **M**azzini (heart), **C**avour (brain), **G**aribaldi (sword), **V**ictor Emmanuel II (crown). 1859 → 1860 → 1861.\n"
         "- **Treaty of Vienna = undo Napoleon:** Bourbons back, buffer states round France, gifts to Prussia, Austria and Russia.\n- **Germania's symbols:** \"Chains broken, Eagle strong, Oak brave, Sword ready, Olive peaceful, Sun new.\""),
  blk("s7.mistakes", "common_mistakes", title="Common mistakes",
    body="1. Saying the Napoleonic Code gave women equal rights: it did not.\n2. Mixing up Metternich (Austria, Congress of Vienna) and Bismarck (Prussia, German unification).\n"
         "3. Writing that the Frankfurt Parliament made Friedrich Wilhelm IV emperor: he **rejected** the crown.\n4. Saying Garibaldi was king of Italy: Victor Emmanuel II became king in 1861.\n"
         "5. Saying Britain was formed by revolution: it was a long process.\n6. Confusing the Treaty of Vienna (1815) with the Treaty of Constantinople (1832).\n7. Writing *Zollverein* as a political party: it was a customs union."),
  blk("s7.tip", "teacher_tip", title="Try this in class",
    body="Show Sorrieu's print and Veit's Germania and let students find the symbols themselves before revealing the meanings. Then split the class into three groups (Germany, Italy, Britain); each group explains its nation's making in two minutes, and the class votes on which path was most democratic."),
  blk("s7.reflection", "reflection", title="Think and explain",
    body="Was the unification of Germany a victory for the people's nationalism of 1848 or for the Prussian state? Give one reason for your view."),
  blk("s7.connection", "connection", title="Where this leads",
    body="- **Chapter 2, Nationalism in India:** Indian nationalism grew through anti-colonial struggle; compare it with the European paths.\n- **Political Science, Power Sharing and Federalism:** how modern nations hold diverse peoples together.\n"
         "- **Bharat Mata** (painted by Abanindranath Tagore) is India's allegory, like Marianne and Germania."),
  blk("s7.mastery", "mastery", title="Mastery challenge",
    body="In 120 words, compare the unification of Italy with the unification of Germany under: leaders, method and result.\n\n"
         "**Model answer:** Both were divided into many states and unified under the leadership of one kingdom. In Germany, Prussia's chief minister Otto von Bismarck used the army and bureaucracy in three wars (with Denmark, Austria and France); in January 1871 William I was proclaimed German Emperor at Versailles. "
         "In Italy, Sardinia-Piedmont under Victor Emmanuel II and his chief minister Cavour used diplomacy and an alliance with France to defeat Austria (1859), while Garibaldi's volunteers freed the south (1860); Victor Emmanuel II became king of united Italy in 1861. "
         "Germany's unification was mainly by military power from above; Italy's combined diplomacy, war and popular volunteers."),
  blk("s7.summary", "summary", title="Chapter summary",
    body="- The French Revolution (1789) made the people the nation; collective identity was built through symbols, laws, language and uniform measures.\n"
         "- Napoleon's Civil Code (1804) ended birth privileges and gave equality before law, but taxes, censorship and conscription caused resentment.\n"
         "- The new middle class supported liberal nationalism; economic unity came through the Zollverein (1834).\n- The Congress of Vienna (1815, Metternich) restored conservative rule; secret societies and Mazzini kept the idea of nation alive.\n"
         "- 1830–1848: July Revolution, Belgian and Greek independence, Romanticism (Herder, Polish music and language), hunger revolts, the 1848 revolution and the failed Frankfurt Parliament.\n"
         "- Germany was unified by Bismarck and Prussia (1871), Italy by Cavour, Garibaldi and Victor Emmanuel II (1861); Britain grew by a long process.\n"
         "- Nations were shown as women (Marianne, Germania). Narrow nationalism and imperial rivalry in the Balkans led to the First World War."),
  blk("s7.examtips", "exam_tips", title="Board exam tips",
    body="- 5-mark questions often ask: Treaty of Vienna provisions, Britain's long process, German unification, steps of the French revolutionaries, Napoleon's reforms, the 1848 liberals.\n"
         "- Write points with names and dates (1804, 1815, 1832, 1834, 1848, 1861, 1871).\n- In MCQs on pictures (Sorrieu, Germania), learn the symbol table.\n- Assertion-reason questions test cause and effect: check both statements separately first."),
  blk("s7.flash1", "flashcard", front="What did the Zollverein (1834) do?", back="Abolished tariff barriers among German states and reduced currencies from over 30 to 2."),
  blk("s7.flash2", "flashcard", front="Who said \"When France sneezes, the rest of Europe catches cold\"?", back="Duke Metternich, the Austrian Chancellor."),
  blk("s7.flash3", "flashcard", front="When and where was William I proclaimed German Emperor?", back="January 1871, in the Hall of Mirrors at Versailles."),
  blk("s7.flash4", "flashcard", front="What is an allegory?", back="An abstract idea expressed through a person or thing, e.g. Marianne for the French Republic."),
 ]},
]

# ---------------- Sample paper ----------------
M("sqp1", VIS, "Match the following and choose the correct option:\n\n| Column I | Column II |\n|---|---|\n| A. Frederic Sorrieu | 1. Torch of enlightenment |\n| B. Statue of Liberty | 2. Shattered remains of absolutist institutions |\n"
  "| C. Foreground in front of the Statue of Liberty | 3. Democratic and social republics |\n| D. Sorrieu's utopian vision | 4. French artist |",
  [("A-4, B-1, C-2, D-3", ""), ("A-2, B-4, C-4, D-1", "Sorrieu was the French artist (A-4), and the Statue holds the torch (B-1)."),
   ("A-1, B-2, C-4, D-3", "Sorrieu (A) was an artist, not a torch."), ("A-4, B-1, C-3, D-4", "The foreground (C) shows the shattered remains of absolutist institutions.")],
  "Sorrieu was a French artist; Liberty holds the torch of Enlightenment; the foreground shows the remains of absolutism; his vision was a world of democratic and social republics.", "medium", SQP(1))
W("sqp7a", "long_answer", UNI, "'In Britain the formation of the nation-state was not the result of a sudden upheaval or revolution but was the result of a long-drawn-out process.' Analyse this statement with suitable reasons.",
  ["Before the 18th century there was no British nation; the English, Welsh, Scots and Irish had their own ethnic identities, cultures and political traditions.",
   "The English nation steadily grew in wealth, importance and power, and extended its influence over the other nations of the islands.",
   "The English Parliament, which seized power from the monarchy in 1688, was the instrument through which a nation-state with England at its centre was forged.",
   "The Act of Union (1707) between England and Scotland formed the United Kingdom of Great Britain; Scottish culture and the Gaelic language were suppressed.",
   "Ireland was forcibly incorporated in 1801 after the failed revolt of Wolfe Tone and the United Irishmen; a British identity was promoted through the Union Jack, the anthem God Save Our Noble King and the English language."],
  source=SQP("7A"))
W("sqp7b", "long_answer", LIB, "'The Treaty of Vienna was drawn up in 1815 with the object of undoing most of the changes that had come about in Europe during the Napoleonic wars.' Highlight the significant provisions of this treaty.",
  ["The Bourbon dynasty, which had been deposed during the French Revolution, was restored to power.", "France lost the territories it had annexed under Napoleon.",
   "A series of states was set up on the boundaries of France to prevent French expansion: the Kingdom of the Netherlands (including Belgium) in the north and Genoa added to Piedmont in the south.",
   "Prussia was given important new territories on its western frontiers, and Austria was given control of northern Italy.",
   "The German Confederation of 39 states was left untouched; in the east, Russia was given part of Poland and Prussia a portion of Saxony."],
  source=SQP("7B"))

# ---------------- NCERT exercises ----------------
W("ex1a", "short_answer", LIB, "Write a note on Giuseppe Mazzini.", ["Mazzini was an Italian revolutionary from Genoa and a member of the secret society of the Carbonari.",
  "After a failed revolution in Liguria he was exiled in 1831; he founded Young Italy in Marseilles and Young Europe in Berne.",
  "He believed nations were the natural units of mankind and that Italy must be one unified republic; Metternich called him 'the most dangerous enemy of our social order'."], source=ex("1(a)"))
W("ex1b", "short_answer", UNI, "Write a note on Count Camillo de Cavour.", ["Cavour was the chief minister of Sardinia-Piedmont who led the movement to unify the regions of Italy.",
  "He was neither a revolutionary nor a democrat; like many wealthy and educated Italians he spoke French better than Italian.",
  "Through a tactful diplomatic alliance with France, Sardinia-Piedmont defeated the Austrian forces in 1859, a key step towards unification."], source=ex("1(b)"))
W("ex1c", "short_answer", REV, "Write a note on the Greek war of independence.", ["Greece had been part of the Ottoman Empire since the 15th century; the struggle for independence began in 1821.",
  "Nationalists got support from Greeks in exile and from West Europeans who admired ancient Greek culture; poets and artists praised Greece as the cradle of European civilisation, and Lord Byron organised funds and fought (dying in 1824).",
  "The Treaty of Constantinople (1832) recognised Greece as an independent nation."], source=ex("1(c)"))
W("ex1d", "short_answer", REV, "Write a note on the Frankfurt Parliament.", ["On 18 May 1848, 831 elected representatives of the German regions met in the Church of St Paul, Frankfurt, as an all-German National Assembly.",
  "They drafted a constitution for a German nation headed by a monarchy subject to a parliament, and offered the crown to Friedrich Wilhelm IV of Prussia, who rejected it.",
  "Dominated by the middle classes, it resisted the demands of workers and artisans, lost their support, and was finally disbanded by troops."], source=ex("1(d)"))
W("ex1e", "short_answer", REV, "Write a note on the role of women in nationalist struggles.", ["Women actively took part in the revolutions of 1830 and 1848, formed their own political associations, started newspapers and joined political meetings and demonstrations.",
  "Yet they were denied suffrage; the Napoleonic Code made women subordinate to fathers and husbands.",
  "At the Frankfurt Parliament women were admitted only as observers in the visitors' gallery, showing that liberal nationalism excluded them from political rights."], source=ex("1(e)"))
W("ex2", "short_answer", FR, "What steps did the French revolutionaries take to create a sense of collective identity among the French people?",
  ["The ideas of la patrie (fatherland) and le citoyen (citizen) stressed a united community with equal rights; a new tricolour flag replaced the royal standard.",
   "The Estates General was renamed the National Assembly; new hymns, oaths and commemorations were introduced; a centralised administration made uniform laws.",
   "Internal customs duties were abolished, uniform weights and measures adopted, and French as spoken in Paris became the common language."], source=ex(2))
W("ex3", "short_answer", VIS, "Who were Marianne and Germania? What was the importance of the way in which they were portrayed?",
  ["Marianne was the female allegory of France and Germania the female allegory of Germany.",
   "Marianne had the red cap, tricolour and cockade of Liberty and the Republic; her statues stood in public squares and her image was on coins and stamps. Germania wore a crown of oak leaves, symbolising heroism.",
   "The portrayal gave the abstract idea of the nation a concrete, recognisable form and reminded people of national symbols, building unity and patriotism."], source=ex(3))
W("ex4", "short_answer", UNI, "Briefly trace the process of German unification.",
  ["After the failure of the 1848 Frankfurt Parliament, Prussia took the lead in German unification, with chief minister Otto von Bismarck as its architect.",
   "With the help of the Prussian army and bureaucracy, three wars were fought over seven years with Austria, Denmark and France, all won by Prussia.",
   "In January 1871 the Prussian king William I was proclaimed German Emperor at Versailles; the new state modernised its currency, banking, legal and judicial systems."], source=ex(4))
W("ex5", "short_answer", FR, "What changes did Napoleon introduce to make the administrative system more efficient in the territories ruled by him?",
  ["The Civil Code of 1804 did away with privileges based on birth, established equality before the law and secured the right to property.",
   "He simplified administrative divisions, abolished the feudal system and freed peasants from serfdom and manorial dues.",
   "Guild restrictions in towns were removed, transport and communication improved, and uniform laws, weights, measures and currency helped trade."], source=ex(5))
W("ex6", "long_answer", REV, "Explain what is meant by the 1848 revolution of the liberals. What were the political, social and economic ideas supported by the liberals?",
  ["Along with the revolts of the poor, educated middle classes in Germany, Italy, Poland and Austria-Hungary rose in 1848 demanding constitutionalism with national unification: this is the revolution of the liberals.",
   "Political ideas: a nation-state based on parliamentary principles, a written constitution, freedom of the press and freedom of association; government by consent.",
   "Social ideas: an end to autocracy and clerical privileges, and equality of all before the law; abolition of serfdom.",
   "Economic ideas: freedom of markets, abolition of state restrictions on the movement of goods and capital, and the inviolability of private property.",
   "Though suppressed, it led monarchs to abolish serfdom and bonded labour in the Habsburg dominions and Russia, and to give Hungary more autonomy in 1867."], source=ex("discuss 1"))
W("ex7", "long_answer", REV, "Choose three examples to show the contribution of culture to the growth of nationalism in Europe.",
  ["Romanticism: Romantic artists and poets stressed emotions and a shared collective heritage; Herder said true German culture lay among the common people (das volk), so folk songs, poetry and dances became national treasures.",
   "Music: in partitioned Poland, Karol Kurpinski's operas and music turned folk dances like the polonaise and mazurka into national symbols.",
   "Language: after Russia imposed Russian in Poland, the clergy used Polish as a weapon of resistance; using Polish became a symbol of the struggle against Russian dominance.",
   "Folktales: the Grimm brothers collected German folktales as an expression of the national spirit.",
   "Art: allegories like Marianne and Germania gave the nation a visible form that people could identify with."], source=ex("discuss 2"))
W("ex8", "long_answer", UNI, "Through a focus on any two countries, explain how nations developed over the nineteenth century.",
  ["Germany: the liberal attempt of 1848 (Frankfurt Parliament) failed; Prussia took the lead under Bismarck.",
   "Bismarck fought three wars (Denmark, Austria, France) with the Prussian army and bureaucracy; in January 1871 William I was proclaimed German Emperor at Versailles.",
   "Italy: divided into seven states; Mazzini's uprisings of 1831 and 1848 failed, and Sardinia-Piedmont under Victor Emmanuel II took the lead.",
   "Cavour's alliance with France defeated Austria in 1859; Garibaldi's volunteers freed South Italy and the Kingdom of the Two Sicilies in 1860.",
   "In 1861 Victor Emmanuel II was proclaimed king of united Italy. In both, nationalism was led from above by a strong state."], source=ex("discuss 3"))
W("ex9", "long_answer", UNI, "How was the history of nationalism in Britain unlike the rest of Europe?",
  ["In most of Europe nation-states came from revolutions or wars; in Britain the nation-state was the result of a long-drawn-out process.",
   "There was no British nation before the 18th century; the English, Welsh, Scots and Irish had separate identities; the English grew in power and extended their influence.",
   "The English Parliament, which seized power from the monarchy in 1688, was the instrument of nation-building.",
   "The Act of Union (1707) created the United Kingdom of Great Britain; Scottish culture and Gaelic were suppressed; Ireland was forcibly incorporated in 1801 after Wolfe Tone's failed revolt.",
   "A new British identity was spread through English culture: the Union Jack, the anthem God Save Our Noble King and the English language."], source=ex("discuss 4"))
W("ex10", "long_answer", VIS, "Why did nationalist tensions emerge in the Balkans?",
  ["The Balkans was a region of great geographical and ethnic variation (Romania, Bulgaria, Albania, Greece, Macedonia, Croatia, Bosnia-Herzegovina, Slovenia, Serbia, Montenegro) whose people were broadly known as Slavs.",
   "A large part was under the Ottoman Empire; the spread of romantic nationalism with the Ottoman Empire's disintegration made the region explosive.",
   "Each Balkan nationality claimed independence using history, and the states were jealous of each other, each wanting more territory.",
   "The great powers, Russia, Germany, England and Austro-Hungary, competed for trade, colonies and military might, and each tried to counter the others in the Balkans.",
   "This led to a series of wars in the region and finally to the First World War in 1914."], source=ex("discuss 5"))

# ---------------- Shine: MCQs ----------------
M("mcq01", FR, "The term *la patrie* means:", [("the fatherland", ""), ("the citizen", "*le citoyen* means the citizen."), ("the king", "The revolution moved power away from the king."), ("the church", "*la patrie* has nothing to do with the Church.")], "*la patrie* = the fatherland; *le citoyen* = the citizen.")
M("mcq02", FR, "Which of the following was NOT done by the French revolutionaries to create a collective identity?", [("Encouraging regional dialects", ""), ("Introducing the tricolour flag", "This was done."), ("Adopting uniform weights and measures", "This was done."), ("Renaming the Estates General as the National Assembly", "This was done.")], "Regional dialects were *discouraged*; French became the common language.")
M("mcq03", FR, "Why did people in the conquered areas turn against Napoleon's rule?", [("Increased taxation, censorship and forced conscription", ""), ("He abolished the feudal system", "That was a popular reform."), ("He improved transport", "That helped people."), ("He removed guild restrictions", "That helped businessmen.")], "The burdens of taxes, censorship and conscription outweighed the benefits.")
M("mcq04", LIB, "The word *liberalism* comes from the Latin root *liber*, which means:", [("free", ""), ("equal", "*liber* means free."), ("nation", "*liber* means free."), ("king", "*liber* means free.")], "*liber* = free.")
M("mcq05", LIB, "A merchant travelling from Hamburg to Nuremberg in the 1830s had to pass how many customs barriers?", [("11", ""), ("5", "The figure was 11."), ("39", "39 was the number of German states."), ("30", "Over 30 was the number of currencies.")], "Eleven customs barriers, each with about 5% duty: a strong argument for the Zollverein.", "medium")
M("mcq06", LIB, "Which of the following countries did NOT take part in the Congress of Vienna's settlement as a victor over Napoleon?", [("France", ""), ("Britain", "Britain was one of the victors."), ("Russia", "Russia was one of the victors."), ("Prussia", "Prussia was one of the victors.")], "Britain, Russia, Prussia and Austria defeated Napoleon; France was the defeated power.")
M("mcq07", LIB, "Giuseppe Mazzini founded which two underground societies?", [("Young Italy and Young Europe", ""), ("Carbonari and Jacobin clubs", "Mazzini was a member of the Carbonari; Jacobin clubs were French."), ("Zollverein and Young Italy", "The Zollverein was a customs union."), ("Red Shirts and Young Europe", "The Red Shirts were Garibaldi's volunteers.")], "Young Italy (Marseilles) and Young Europe (Berne).")
M("mcq08", REV, "Who said \"When France sneezes, the rest of Europe catches cold\"?", [("Metternich", ""), ("Mazzini", "Mazzini was a revolutionary."), ("Bismarck", "Bismarck was Prussian chief minister later."), ("Napoleon", "Napoleon had fallen by then.")], "Metternich, after the July Revolution of 1830.")
M("mcq09", REV, "After the July Revolution of 1830, which country broke away from the United Kingdom of the Netherlands?", [("Belgium", ""), ("Greece", "Greece broke away from the Ottoman Empire."), ("Poland", "Poland was partitioned among Russia, Prussia and Austria."), ("Italy", "Italy was not part of the Netherlands.")], "An uprising in Brussels led Belgium to break away.")
M("mcq10", REV, "Johann Gottfried Herder believed that true German culture was to be found among:", [("the common people (das volk)", ""), ("the aristocracy", "The aristocracy spoke French and followed a European lifestyle."), ("the Church", "Herder looked to folk culture."), ("the army", "Herder looked to folk songs, poetry and dances.")], "Folk songs, folk poetry and folk dances expressed the true spirit of the nation.")
M("mcq11", REV, "Karol Kurpinski is remembered for:", [("turning Polish folk dances into national symbols through operas and music", ""), ("collecting German folktales", "That was the Grimm brothers."), ("founding Young Italy", "That was Mazzini."), ("painting Germania", "That was Philip Veit.")], "His music made the polonaise and mazurka symbols of Polish nationalism.", "medium")
M("mcq12", REV, "The weavers of Silesia revolted in 1845 because:", [("contractors drastically reduced their payments", ""), ("they wanted voting rights for women", "Their revolt was about wages."), ("they opposed the Zollverein", "Their revolt was about payment for cloth."), ("Napoleon raised taxes", "Napoleon had fallen in 1815.")], "Contractors supplied raw material and cut payments for finished cloth.", "medium")
M("mcq13", REV, "In 1848 in France, the new Republic granted suffrage to:", [("all adult males above 21", ""), ("all adults, men and women", "Women were not given the vote."), ("only property-owning men", "The 1848 Republic widened it to all adult males above 21."), ("only nobles", "The Republic opposed privilege.")], "Universal adult male suffrage above the age of 21.", "medium")
M("mcq14", REV, "Who rejected the crown offered by the Frankfurt Parliament?", [("Friedrich Wilhelm IV, King of Prussia", ""), ("William I", "William I became emperor in 1871."), ("Victor Emmanuel II", "He became king of Italy."), ("Louis Philippe", "He fled France in 1848.")], "Friedrich Wilhelm IV rejected the crown and opposed the assembly.")
M("mcq15", UNI, "The architect of German unification was:", [("Otto von Bismarck", ""), ("Duke Metternich", "Metternich was the conservative Austrian chancellor."), ("Cavour", "Cavour worked for Italy."), ("Friedrich Wilhelm IV", "He rejected the crown in 1848.")], "Bismarck, the Prussian chief minister.")
M("mcq16", UNI, "Prussia fought wars with which three countries to unify Germany?", [("Austria, Denmark and France", ""), ("Britain, Russia and Austria", "Prussia did not fight Britain or Russia for unification."), ("Italy, Spain and France", "Italy and Spain were not involved."), ("Poland, Greece and Belgium", "These were not involved.")], "Three wars over seven years: Denmark, Austria and France.")
M("mcq17", UNI, "In 1861, who was proclaimed king of united Italy?", [("Victor Emmanuel II", ""), ("Giuseppe Garibaldi", "Garibaldi led volunteers but did not become king."), ("Count Cavour", "Cavour was chief minister."), ("Giuseppe Mazzini", "Mazzini wanted a republic.")], "Victor Emmanuel II of Sardinia-Piedmont.")
M("mcq18", UNI, "Before unification, which part of Italy was ruled by the Pope?", [("The centre", ""), ("The north", "The north was under the Austrian Habsburgs."), ("The south", "The south was under the Bourbon kings of Spain."), ("Sardinia-Piedmont", "It was ruled by an Italian princely house.")], "The north: Austria; the centre: the Pope; the south: Spanish Bourbons.", "medium")
M("mcq19", UNI, "The Act of Union of 1707 was between:", [("England and Scotland", ""), ("England and Ireland", "Ireland was incorporated in 1801."), ("England and Wales", "The Act of 1707 united England and Scotland."), ("Scotland and Ireland", "England was a party to the Act.")], "It created the United Kingdom of Great Britain.")
M("mcq20", UNI, "Which of these was NOT a symbol promoted to build a British nation?", [("The Gaelic language", ""), ("The Union Jack", "This was promoted."), ("God Save Our Noble King", "This was promoted."), ("The English language", "This was promoted.")], "Gaelic, the Scottish language, was suppressed.")
M("mcq21", VIS, "Marianne was the allegory of:", [("France", ""), ("Germany", "Germany's allegory was Germania."), ("Italy", "Marianne represented the French Republic."), ("Britain", "Marianne represented the French Republic.")], "Marianne, with the red cap, tricolour and cockade.")
M("mcq22", VIS, "In the image of Germania, the olive branch around the sword stands for:", [("willingness to make peace", ""), ("heroism", "Heroism is the oak crown."), ("strength", "Strength is the eagle breastplate."), ("being freed", "Being freed is the broken chains.")], "Olive branch = peace.")
M("mcq23", VIS, "Which of these regions was NOT part of the Balkans?", [("Belgium", ""), ("Bulgaria", "Bulgaria is in the Balkans."), ("Serbia", "Serbia is in the Balkans."), ("Montenegro", "Montenegro is in the Balkans.")], "Belgium is in western Europe.")
M("mcq24", VIS, "The inhabitants of the Balkans were broadly known as:", [("Slavs", ""), ("Magyars", "Magyars were in Hungary."), ("Junkers", "Junkers were Prussian landowners."), ("Bourbons", "The Bourbons were a royal dynasty.")], "The Slavs.")
M("mcq25", LIB, "Which group in Prussia supported the monarchy and the military in crushing the liberals?", [("The Junkers (large landowners)", ""), ("The Carbonari", "The Carbonari were Italian revolutionaries."), ("The weavers of Silesia", "The weavers revolted against contractors."), ("The Jacobins", "Jacobin clubs supported revolutionary ideas.")], "The large landowners of Prussia, the Junkers.", "medium")
M("mcq26", REV, "The Treaty of Constantinople (1832) recognised the independence of:", [("Greece", ""), ("Belgium", "Belgium broke away from the Netherlands in 1830."), ("Poland", "Poland stayed partitioned."), ("Italy", "Italy was unified in 1861.")], "Greece, after the war of independence that began in 1821.")
M("mcq27", REV, "After 1848, what change did the Habsburg rulers introduce in 1867?", [("More autonomy for the Hungarians", ""), ("Independence for Greece", "That came in 1832 from the Ottomans."), ("Universal suffrage for all", "This did not happen."), ("Unification of Italy", "Italy was unified separately.")], "The Habsburgs granted the Hungarians more autonomy in 1867.", "medium")
M("mcq28", FR, "Students and members of the educated middle class in other European countries set up which clubs to support the French Revolution's ideas?", [("Jacobin clubs", ""), ("Carbonari", "The Carbonari were an Italian secret society."), ("Young Europe", "Young Europe was founded later by Mazzini."), ("Zollverein", "The Zollverein was a customs union.")], "Jacobin clubs spread revolutionary ideas.")
M("mcq29", VIS, "Who painted the image of Germania that hung in the Church of St Paul in 1848?", [("Philip Veit", ""), ("Frédéric Sorrieu", "Sorrieu made the 1848 prints of democratic republics."), ("Karol Kurpinski", "Kurpinski was a composer."), ("Lord Byron", "Byron was a poet.")], "Philip Veit painted Germania.", "medium")
M("mcq30", UNI, "In which year did Sardinia-Piedmont, with French help, defeat the Austrian forces?", [("1859", ""), ("1848", "1848 saw failed revolutions."), ("1861", "1861 is when Victor Emmanuel II became king of Italy."), ("1871", "1871 is the German Empire.")], "1859.")
# ---------------- Assertion-reason ----------------
C.arq("ar1", FR, "The French Revolution laid the foundation of nationalism in Europe.", "It transferred sovereignty from the monarch to the body of French citizens.", 0,
      "Making the people sovereign created the idea of a nation of citizens.", "it made the people the nation.", "sovereignty passed to the citizens, which explains A.")
C.arq("ar2", FR, "Napoleon was welcomed everywhere throughout his rule.", "His Civil Code of 1804 abolished privileges based on birth.", 3,
      "A is false: enthusiasm turned to hostility because of taxes, censorship and conscription. R is true.", "people turned against him because of taxes, censorship and conscription.", "the Civil Code did abolish privileges of birth.")
C.arq("ar3", LIB, "The Zollverein helped economic unity in the German states.", "It abolished tariff barriers and reduced the number of currencies from over thirty to two.", 0,
      "R explains A.", "it promoted economic unity.", "removing tariffs and currencies explains the unity.")
C.arq("ar4", REV, "The Frankfurt Parliament failed to unify Germany.", "The middle-class deputies supported the demands of workers and artisans.", 2,
      "A is true; R is false: they resisted the demands of workers and artisans and lost their support.", "troops disbanded it after the Prussian king rejected the crown.", "the deputies resisted, not supported, workers' demands.")
C.arq("ar5", UNI, "In Britain the nation-state was formed through a long-drawn-out process.", "England imposed its influence on Scotland and Ireland over a long period.", 0,
      "R explains A: a gradual English dominance, not a revolution, made the British nation.", "it was not a sudden revolution.", "gradual English dominance explains it.")
C.arq("ar6", VIS, "The Balkans became a source of tension after 1871.", "The Balkan states were united and supported each other against the Ottoman Empire.", 2,
      "A is true; R is false: the Balkan states were jealous of each other.", "nationalism, Ottoman decline and great-power rivalry made it explosive.", "the Balkan states were rivals.")
# ---------------- True / false ----------------
C.tf("tf1", FR, "The Napoleonic Code gave women the right to vote.", False, "It denied women rights and made them subordinate to fathers and husbands.")
C.tf("tf2", UNI, "Cavour spoke French better than Italian.", True, "Like many educated Italians of his time, he spoke French much better than Italian.")
C.tf("tf3", REV, "Lord Byron died fighting for Greek independence in 1824.", True, "He organised funds and went to fight, but died of fever in 1824.")
C.tf("tf4", UNI, "William I was proclaimed German Emperor in Berlin.", False, "He was proclaimed in the Hall of Mirrors at Versailles in January 1871.")
# ---------------- Shine written ----------------
W("vsa1", "very_short_answer", LIB, "What is meant by a plebiscite? Give one example of its use in the nineteenth century.", ["A plebiscite is a direct vote by which all the people of a region are asked to accept or reject a proposal.",
  "In the unification of Italy, plebiscites in the conquered regions approved their joining the Kingdom of Sardinia-Piedmont, making the union appear to be the people's choice."], difficulty="medium")
W("vsa2", "very_short_answer", LIB, "State any two features of conservatism after 1815.", ["Conservatives believed that established, traditional institutions of state and society, like the monarchy, the Church, social hierarchies, property and the family, should be preserved.",
  "They did not want a return to pre-revolutionary society, but accepted modernisation (a modern army, efficient bureaucracy, dynamic economy, end of feudalism) to strengthen autocratic monarchies."])
W("vsa3", "very_short_answer", REV, "Why is the period 1830–1848 called the age of revolutions? Give two examples.", ["Liberal-nationalist uprisings broke out across Europe in this period, led by the educated middle classes.",
  "Examples: the July Revolution of 1830 in France and Belgium's break from the Netherlands; the 1848 revolutions in France and the German states (Frankfurt Parliament)."])
W("vsa4", "very_short_answer", VIS, "What is an allegory? Name the allegory of France.", ["An allegory is an abstract idea (such as freedom or the nation) expressed through a person or thing.",
  "France was represented by Marianne, with the red cap, tricolour and cockade of Liberty and the Republic."])
W("sa1", "short_answer", LIB, "Describe the economic hardships faced by Europe in the 1830s.", ["Population rose enormously, and there were more seekers of jobs than jobs; people migrated from rural areas to crowded urban slums.",
  "Small producers in towns faced stiff competition from cheap machine-made goods from England, where industrialisation was more advanced.",
  "In regions where aristocracy still had power, peasants bore feudal dues; a rise in food prices or a bad harvest led to widespread pauperism, as in Paris in 1848."])
W("sa2", "short_answer", LIB, "Explain the role of the new middle class in spreading liberal nationalism in Europe.", ["Industrialisation created a new middle class of industrialists, businessmen and professionals.",
  "Among them, ideas of national unity following the abolition of aristocratic privileges became popular; they demanded freedom for the individual and equality before law.",
  "They wanted a constitution, a representative government and freedom of markets; economically they backed unified territory with common currency and no internal customs (e.g. the Zollverein)."])
W("sa3", "short_answer", UNI, "How did Garibaldi contribute to the unification of Italy?", ["Giuseppe Garibaldi was a revolutionary who had joined Young Italy; after the defeat of Austria in 1859, large numbers of armed volunteers joined him.",
  "In 1860 his volunteers (the Red Shirts) marched into South Italy and the Kingdom of the Two Sicilies and drove out the Spanish Bourbon rulers.",
  "He handed over the conquered south to Victor Emmanuel II, which led to Victor Emmanuel II being proclaimed king of united Italy in 1861."])
W("la1", "long_answer", VIS, "'Nationalism, aligned with imperialism, led Europe to disaster in 1914.' Explain.", ["By the late 19th century nationalism lost its liberal-democratic idealism and became a narrow creed; nationalist groups grew intolerant and ready for war.",
  "The Balkans, home of the Slavs, was the main area of tension; much of it was under the disintegrating Ottoman Empire.",
  "Balkan nationalities claimed independence on historical grounds, and the Balkan states were jealous of each other, each wanting more territory.",
  "The great powers, Russia, Germany, England and Austro-Hungary, competed for trade, colonies and naval and military might, and each tried to counter the others in the Balkans.",
  "This led to a series of wars and finally the First World War in 1914."], difficulty="hard")
W("la2", "long_answer", REV, "How did Romanticism and culture help create a sense of nationalism in Europe? Explain with examples.", ["Romanticism criticised the glorification of reason and science and focused on emotion, intuition and mystical feelings, creating a sense of a shared collective heritage.",
  "Herder taught that true German culture was found among das volk, in folk songs, poetry and dances, so collecting folk culture became a national project (the Grimm brothers collected folktales).",
  "Language was used as a weapon: in Poland, after Russian was imposed, the clergy used Polish in church gatherings and religious instruction.",
  "Music: Karol Kurpinski's operas made the polonaise and mazurka national symbols.",
  "Art: images such as Marianne and Germania gave the nation a visible form."])
# ---------------- Case and source based ----------------
W("cb1", "case_based", UNI, "Read the source and answer the questions.\n\n*\"Nationalist feelings were widespread among middle-class Germans, who in 1848 tried to unite the different regions of the German confederation into a nation-state governed by an elected parliament. This liberal initiative to nation-building was, however, repressed by the combined forces of the monarchy and the military, supported by the large landowners (called Junkers) of Prussia. From then on, Prussia took on the leadership of the movement for national unification. Its chief minister, Otto von Bismarck, was the architect of this process carried out with the help of the Prussian army and bureaucracy.\"* (NCERT)\n\n"
  "(i) Who were the Junkers? (1)\n\n(ii) Who was the architect of German unification? (1)\n\n(iii) Explain how German unification was completed. (2)",
  ["(i) The large landowners of Prussia, who supported the monarchy and the military.", "(ii) Otto von Bismarck, chief minister of Prussia.",
   "(iii) Prussia fought three wars over seven years with Austria, Denmark and France and won them all; in January 1871 the Prussian king William I was proclaimed German Emperor at Versailles."])
W("cb2", "case_based", REV, "Read the source and answer the questions.\n\n*\"The 1830s were years of great economic hardship in Europe. The first half of the nineteenth century saw an enormous increase in population all over Europe. In most countries there were more seekers of jobs than employment. Population from rural areas migrated to the cities to live in overcrowded slums. Small producers in towns were often faced with stiff competition from imports of cheap machine-made goods from England.\"* (NCERT)\n\n"
  "(i) Why did people migrate from rural areas to cities? (1)\n\n(ii) Which country's cheap machine-made goods hurt small producers? (1)\n\n(iii) How did hardship lead to the events of 1848 in France? (2)",
  ["(i) Population rose enormously and there were more job-seekers than jobs in the countryside.", "(ii) England.",
   "(iii) Food shortages and widespread unemployment brought the people of Paris onto the roads; barricades were put up and Louis Philippe was forced to flee; a National Assembly proclaimed a Republic, gave the vote to all adult males above 21 and guaranteed the right to work."])
W("cb3", "case_based", VIS, "Read the source and answer the questions.\n\n*\"Artists in the eighteenth and nineteenth centuries found a way out by personifying a nation. In other words they represented a country as if it were a person. Nations were then portrayed as female figures. The female form that was chosen to personify the nation did not stand for any particular woman in real life; rather it sought to give the abstract idea of the nation a concrete form.\"* (NCERT)\n\n"
  "(i) What does it mean to personify a nation? (1)\n\n(ii) Name the female allegory of Germany. (1)\n\n(iii) Explain the meaning of any two symbols in the image of Germania. (2)",
  ["(i) To represent the nation as if it were a person, here a female figure.", "(ii) Germania.",
   "(iii) Any two: crown of oak leaves = heroism; broken chains = being freed; breastplate with eagle = strength of the German empire; sword = readiness to fight; olive branch = willingness to make peace; rays of the rising sun = beginning of a new era."])

chapter = header(SUBJ, N, "The Rise of Nationalism in Europe", ["french_revolution_napoleon", "liberalism_conservatism", "age_of_revolutions", "unification", "visualising_balkans"],
  "Follows the CBSE 2025-26 Social Science (087) syllabus: this chapter is fully in the board examination (History: 18 marks + 2 map marks; there is no map item from this chapter).")
chapter["sections"] = sections
C.write(ROOT, PATH, chapter)
