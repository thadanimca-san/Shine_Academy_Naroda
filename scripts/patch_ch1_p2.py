import json

file_path = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class11_spcc_part2_ch1.json'

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

new_blocks = [
    {
        "type": "numerical",
        "question": "Who appoints a personal / private secretary?",
        "question_hi": "निजी सचिव (Private Secretary) की नियुक्ति कौन करता है?",
        "question_gu": "ખાનગી સેક્રેટરી (Private Secretary) ની નિમણૂક કોણ કરે છે?",
        "solution": "A personal or private secretary is appointed by busy professionals or high-ranking individuals who do not have time to handle all their daily tasks. \nFor example: Doctors, lawyers, chartered accountants, political leaders, actors, business tycoons, and ministers appoint a private secretary to manage their schedules, appointments, and correspondence.",
        "solution_hi": "एक निजी सचिव की नियुक्ति व्यस्त पेशेवरों या उच्च पदस्थ व्यक्तियों द्वारा की जाती है जिनके पास अपने सभी दैनिक कार्यों को संभालने का समय नहीं होता है।\nउदाहरण के लिए: डॉक्टर, वकील, चार्टर्ड एकाउंटेंट, राजनीतिक नेता, अभिनेता, बड़े व्यापारी और मंत्री अपने कार्यक्रमों, नियुक्तियों और पत्राचार (correspondence) को प्रबंधित करने के लिए एक निजी सचिव की नियुक्ति करते हैं।",
        "solution_gu": "ખાનગી સેક્રેટરીની નિમણૂક વ્યસ્ત વ્યાવસાયિકો અથવા ઉચ્ચ કક્ષાના વ્યક્તિઓ દ્વારા કરવામાં આવે છે જેમને તેમના તમામ દૈનિક કાર્યોને સંભાળવાનો સમય હોતો નથી.\nઉદાહરણ તરીકે: ડૉક્ટરો, વકીલો, ચાર્ટર્ડ એકાઉન્ટન્ટ્સ, રાજકીય નેતાઓ, અભિનેતાઓ, મોટા ઉદ્યોગપતિઓ અને પ્રધાનો તેમના સમયપત્રક, નિમણૂંકો અને પત્રવ્યવહારનું સંચાલન કરવા માટે ખાનગી સેક્રેટરીની નિમણૂક કરે છે.",
        "id": "KOBJ_GSEB_11SPCC_P2C1_NUME_005"
    },
    {
        "type": "numerical",
        "question": "Who is called Ministerial secretary and Secretary of Embassy?",
        "question_hi": "विभागीय सचिव (Ministerial Secretary) और दूतावास सचिव (Secretary of Embassy) किसे कहा जाता है?",
        "question_gu": "વિભાગીય સેક્રેટરી (Ministerial Secretary) અને દૂતાવાસના સેક્રેટરી (Secretary of Embassy) કોને કહેવામાં આવે છે?",
        "solution": "1. **Ministerial Secretary (Departmental Secretary):** In a democratic government, elected ministers head various departments (like Education, Defense, Finance). The senior administrative officer appointed by the government to manage the day-to-day operations of that specific department on behalf of the minister is called a Ministerial or Departmental Secretary (usually an IAS officer).\n2. **Secretary of Embassy:** Every country appoints its representatives in other countries to protect its interests and citizens abroad. These representatives or ambassadors work from an embassy. The chief administrative officer who manages the embassy is known as the Secretary of Embassy.",
        "solution_hi": "1. **विभागीय सचिव:** एक लोकतांत्रिक सरकार में, निर्वाचित मंत्री विभिन्न विभागों (जैसे शिक्षा, रक्षा, वित्त) के प्रमुख होते हैं। मंत्री की ओर से उस विशिष्ट विभाग के दिन-प्रतिदिन के कार्यों का प्रबंधन करने के लिए सरकार द्वारा नियुक्त वरिष्ठ प्रशासनिक अधिकारी को विभागीय सचिव कहा जाता है (आमतौर पर एक आईएएस अधिकारी)।\n2. **दूतावास सचिव:** प्रत्येक देश विदेशों में अपने हितों और नागरिकों की रक्षा के लिए अन्य देशों में अपने प्रतिनिधि नियुक्त करता है। ये प्रतिनिधि दूतावास (Embassy) से काम करते हैं। दूतावास का प्रबंधन करने वाले मुख्य प्रशासनिक अधिकारी को दूतावास सचिव कहा जाता है।",
        "solution_gu": "1. **વિભાગીય સેક્રેટરી:** લોકશાહી સરકારમાં, ચૂંટાયેલા પ્રધાનો વિવિધ વિભાગો (જેમ કે શિક્ષણ, સંરક્ષણ, નાણાં) ના વડા હોય છે. પ્રધાન વતી તે ચોક્કસ વિભાગની રોજબરોજની કામગીરીનું સંચાલન કરવા માટે સરકાર દ્વારા નિયુક્ત વરિષ્ઠ વહીવટી અધિકારીને વિભાગીય સેક્રેટરી કહેવામાં આવે છે (સામાન્ય રીતે IAS અધિકારી).\n2. **દૂતાવાસના સેક્રેટરી:** દરેક દેશ વિદેશમાં પોતાના હિતો અને નાગરિકોના રક્ષણ માટે અન્ય દેશોમાં પોતાના પ્રતિનિધિઓની નિમણૂક કરે છે. આ પ્રતિનિધિઓ દૂતાવાસ (Embassy) માંથી કામ કરે છે. દૂતાવાસનું સંચાલન કરતા મુખ્ય વહીવટી અધિકારીને દૂતાવાસના સેક્રેટરી તરીકે ઓળખવામાં આવે છે.",
        "id": "KOBJ_GSEB_11SPCC_P2C1_NUME_006"
    },
    {
        "type": "numerical",
        "question": "Who used to keep Mantri (Secretary) in olden days? Explain with examples.",
        "question_hi": "पुराने जमाने में मंत्री (सचिव) कौन रखता था? उदाहरण सहित स्पष्ट करें।",
        "question_gu": "જૂના જમાનામાં મંત્રી (સેક્રેટરી) કોણ રાખતું હતું? ઉદાહરણ આપી સમજાવો.",
        "solution": "In olden days, Kings, Emperors, and prominent merchants used to appoint a 'Mantri' or 'Amatya' to handle correspondence and confidential state matters.\n**Examples:**\n1. King Dasharatha (from Ramayana) had 'Sumantra' as his Mantri.\n2. King Dhritarashtra (from Mahabharata) had 'Vidur' as his Mantri.\n3. Emperor Chandragupta Maurya had 'Chanakya' as his Amatya (Chief Minister/Secretary).\nEven in the Mughal empire, the person handling correspondence was known as 'Wazir' or 'Munshi'.",
        "solution_hi": "पुराने समय में, राजा, सम्राट और प्रमुख व्यापारी पत्राचार और गोपनीय राज्य के मामलों को संभालने के लिए 'मंत्री' या 'अमात्य' नियुक्त करते थे।\n**उदाहरण:**\n1. राजा दशरथ (रामायण से) के मंत्री 'सुमंत' थे।\n2. राजा धृतराष्ट्र (महाभारत से) के मंत्री 'विदुर' थे।\n3. सम्राट चंद्रगुप्त मौर्य के अमात्य 'चाणक्य' थे।\nमुगल साम्राज्य में भी, पत्राचार संभालने वाले व्यक्ति को 'वज़ीर' या 'मुंशी' कहा जाता था।",
        "solution_gu": "જૂના જમાનામાં, રાજાઓ, સમ્રાટો અને અગ્રણી વેપારીઓ પત્રવ્યવહાર અને રાજ્યની ગોપનીય બાબતોને સંભાળવા માટે 'મંત્રી' અથવા 'અમાત્ય' ની નિમણૂક કરતા હતા.\n**ઉદાહરણો:**\n1. રાજા દશરથ (રામાયણમાંથી) ના મંત્રી 'સુમંત' હતા.\n2. રાજા ધૃતરાષ્ટ્ર (મહાભારતમાંથી) ના મંત્રી 'વિદુર' હતા.\n3. સમ્રાટ ચંદ્રગુપ્ત મૌર્યના અમાત્ય 'ચાણક્ય' હતા.\nમુઘલ સામ્રાજ્યમાં પણ, પત્રવ્યવહાર સંભાળનાર વ્યક્તિને 'વઝીર' અથવા 'મુનશી' તરીકે ઓળખવામાં આવતા હતા.",
        "id": "KOBJ_GSEB_11SPCC_P2C1_NUME_007"
    },
    {
        "type": "numerical",
        "question": "How many types of company secretary can be considered based on the authority delegated by the Board of Directors? Which are they?",
        "question_hi": "निदेशक मंडल (Board of Directors) द्वारा सौंपे गए अधिकार के आधार पर कंपनी सचिव के कितने प्रकार माने जा सकते हैं? वे कौन से हैं?",
        "question_gu": "બોર્ડ ઓફ ડિરેક્ટર્સ દ્વારા સોંપવામાં આવેલી સત્તાના આધારે કંપની સેક્રેટરીના કેટલા પ્રકાર ગણી શકાય? કયા કયા?",
        "solution": "Based on the authority delegated by the Board of Directors, a Company Secretary can be broadly divided into two types:\n1. **General Secretary:** This secretary handles routine and regular administrative tasks. Examples include drafting correspondence, keeping records of shares, sending notices for meetings, and preparing minutes.\n2. **Administrative Secretary:** This secretary acts as a key executive officer. They are responsible for implementing the policies framed by the Board of Directors, managing different departments, and ensuring that the company functions according to the Companies Act.",
        "solution_hi": "निदेशक मंडल द्वारा सौंपे गए अधिकार के आधार पर, कंपनी सचिव को मोटे तौर पर दो प्रकारों में विभाजित किया जा सकता है:\n1. **सामान्य सचिव (General Secretary):** यह सचिव नियमित और सामान्य प्रशासनिक कार्यों को संभालता है। उदाहरणों में पत्राचार का मसौदा तैयार करना, शेयरों का रिकॉर्ड रखना, बैठकों के लिए नोटिस भेजना और कार्यवृत्त (minutes) तैयार करना शामिल है।\n2. **प्रशासनिक सचिव (Administrative Secretary):** यह सचिव एक प्रमुख कार्यकारी अधिकारी के रूप में कार्य करता है। वे निदेशक मंडल द्वारा बनाई गई नीतियों को लागू करने, विभिन्न विभागों के प्रबंधन और यह सुनिश्चित करने के लिए जिम्मेदार हैं कि कंपनी, कंपनी अधिनियम के अनुसार कार्य करे।",
        "solution_gu": "બોર્ડ ઓફ ડિરેક્ટર્સ દ્વારા સોંપવામાં આવેલી સત્તાના આધારે, કંપની સેક્રેટરીને વ્યાપક રીતે બે પ્રકારમાં વહેંચી શકાય છે:\n1. **સામાન્ય સેક્રેટરી (General Secretary):** આ સેક્રેટરી નિયમિત અને સામાન્ય વહીવટી કાર્યો સંભાળે છે. ઉદાહરણોમાં પત્રવ્યવહારનો ડ્રાફ્ટ તૈયાર કરવો, શેરનો રેકોર્ડ રાખવો, મીટિંગ માટે નોટિસ મોકલવી અને મિનિટ્સ (minutes) તૈયાર કરવી સામેલ છે.\n2. **વહીવટી સેક્રેટરી (Administrative Secretary):** આ સેક્રેટરી મુખ્ય કારોબારી અધિકારી તરીકે કાર્ય કરે છે. તેઓ બોર્ડ ઓફ ડિરેક્ટર્સ દ્વારા ઘડવામાં આવેલી નીતિઓનો અમલ કરવા, વિવિધ વિભાગોનું સંચાલન કરવા અને કંપની કંપની ધારા મુજબ કાર્ય કરે છે તેની ખાતરી કરવા માટે જવાબદાર છે.",
        "id": "KOBJ_GSEB_11SPCC_P2C1_NUME_008"
    },
    {
        "type": "numerical",
        "question": "\"Company Secretary works under the control of the Board of Directors.\" Explain.",
        "question_hi": "\"कंपनी सचिव निदेशक मंडल (Board of Directors) के नियंत्रण में कार्य करता है।\" स्पष्ट करें।",
        "question_gu": "\"કંપની સેક્રેટરી બોર્ડ ઓફ ડિરેક્ટર્સના નિયંત્રણ હેઠળ કામ કરે છે.\" સમજાવો.",
        "solution": "A company is an artificial legal person. It is owned by shareholders, but managed by the elected representatives known as the Board of Directors. \nThe Company Secretary is appointed by the Board of Directors. The Secretary does not have inherent powers to take major policy decisions independently. They only have the authority that is explicitly delegated to them by the Board. \nThe Secretary executes the decisions taken by the Board, issues notices as directed by them, and ensures legal compliance under their supervision. Thus, the Secretary works entirely under the control and guidance of the Board of Directors.",
        "solution_hi": "कंपनी एक कृत्रिम कानूनी व्यक्ति है। इसका स्वामित्व शेयरधारकों के पास है, लेकिन इसका प्रबंधन निदेशक मंडल नामक निर्वाचित प्रतिनिधियों द्वारा किया जाता है।\nकंपनी सचिव की नियुक्ति निदेशक मंडल द्वारा की जाती है। सचिव के पास स्वतंत्र रूप से प्रमुख नीतिगत निर्णय लेने की अंतर्निहित शक्ति नहीं होती है। उनके पास केवल वही अधिकार होता है जो बोर्ड द्वारा स्पष्ट रूप से उन्हें सौंपा जाता है।\nसचिव बोर्ड द्वारा लिए गए निर्णयों को क्रियान्वित करता है, उनके निर्देशानुसार नोटिस जारी करता है, और उनकी देखरेख में कानूनी अनुपालन सुनिश्चित करता है। इस प्रकार, सचिव पूरी तरह से निदेशक मंडल के नियंत्रण और मार्गदर्शन में कार्य करता है।",
        "solution_gu": "કંપની એક કૃત્રિમ કાનૂની વ્યક્તિ છે. તેની માલિકી શેરધારકો પાસે છે, પરંતુ તેનું સંચાલન બોર્ડ ઓફ ડિરેક્ટર્સ તરીકે ઓળખાતા ચૂંટાયેલા પ્રતિનિધિઓ દ્વારા કરવામાં આવે છે.\nકંપની સેક્રેટરીની નિમણૂક બોર્ડ ઓફ ડિરેક્ટર્સ દ્વારા કરવામાં આવે છે. સેક્રેટરી પાસે સ્વતંત્ર રીતે મોટા નીતિગત નિર્ણયો લેવાની આંતરિક સત્તા હોતી નથી. તેમની પાસે માત્ર એટલી જ સત્તા છે જે તેમને બોર્ડ દ્વારા સ્પષ્ટપણે સોંપવામાં આવે છે.\nસેક્રેટરી બોર્ડ દ્વારા લેવામાં આવેલા નિર્ણયોનો અમલ કરે છે, તેમના નિર્દેશ મુજબ નોટિસ જારી કરે છે અને તેમની દેખરેખ હેઠળ કાનૂની પાલનની ખાતરી કરે છે. આમ, સેક્રેટરી સંપૂર્ણપણે બોર્ડ ઓફ ડિરેક્ટર્સના નિયંત્રણ અને માર્ગદર્શન હેઠળ કામ કરે છે.",
        "id": "KOBJ_GSEB_11SPCC_P2C1_NUME_009"
    },
    {
        "type": "numerical",
        "question": "\"Administrative Secretary is a link between Board of Directors and Company.\" Explain.",
        "question_hi": "\"प्रशासनिक सचिव निदेशक मंडल और कंपनी के बीच एक कड़ी है।\" स्पष्ट करें।",
        "question_gu": "\"વહીવટી સેક્રેટરી એ બોર્ડ ઓફ ડિરેક્ટર્સ અને કંપની વચ્ચેની કડી છે.\" સમજાવો.",
        "solution": "The Board of Directors frames the policies and makes the major decisions for the company. However, the Board does not run the day-to-day operations. \nIt is the Administrative Secretary who takes these policies from the Board and ensures they are implemented across all departments of the company. The Secretary communicates the Board's decisions to the managers and staff. Conversely, the Secretary reports the progress, problems, and daily functioning of the company back to the Board.\nBecause information flows in both directions through the Administrative Secretary, they are rightly considered the vital linking pin between the Board of Directors and the Company.",
        "solution_hi": "निदेशक मंडल कंपनी के लिए नीतियां बनाता है और प्रमुख निर्णय लेता है। हालांकि, बोर्ड दिन-प्रतिदिन के संचालन नहीं चलाता है।\nयह प्रशासनिक सचिव है जो बोर्ड से इन नीतियों को लेता है और यह सुनिश्चित करता है कि उन्हें कंपनी के सभी विभागों में लागू किया जाए। सचिव बोर्ड के निर्णयों से प्रबंधकों और कर्मचारियों को अवगत कराता है। इसके विपरीत, सचिव कंपनी की प्रगति, समस्याओं और दैनिक कामकाज की रिपोर्ट बोर्ड को देता है।\nचूंकि सूचना प्रशासनिक सचिव के माध्यम से दोनों दिशाओं में बहती है, इसलिए उन्हें निदेशक मंडल और कंपनी के बीच महत्वपूर्ण कड़ी माना जाता है।",
        "solution_gu": "બોર્ડ ઓફ ડિરેક્ટર્સ કંપની માટે નીતિઓ ઘડે છે અને મોટા નિર્ણયો લે છે. જોકે, બોર્ડ રોજિંદી કામગીરી ચલાવતું નથી.\nતે વહીવટી સેક્રેટરી છે જે આ નીતિઓને બોર્ડ પાસેથી લે છે અને ખાતરી કરે છે કે તે કંપનીના તમામ વિભાગોમાં લાગુ થાય. સેક્રેટરી મેનેજરો અને કર્મચારીઓને બોર્ડના નિર્ણયો વિશે માહિતગાર કરે છે. તેનાથી વિપરિત, સેક્રેટરી કંપનીની પ્રગતિ, સમસ્યાઓ અને રોજિંદી કામગીરીનો અહેવાલ બોર્ડને આપે છે.\nમાહિતી વહીવટી સેક્રેટરી દ્વારા બંને દિશામાં વહેતી હોવાથી, તેમને બોર્ડ ઓફ ડિરેક્ટર્સ અને કંપની વચ્ચેની મહત્વપૂર્ણ કડી માનવામાં આવે છે.",
        "id": "KOBJ_GSEB_11SPCC_P2C1_NUME_010"
    }
]

data['blocks'].extend(new_blocks)

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Part 2 Chapter 1 updated with user questions!")
