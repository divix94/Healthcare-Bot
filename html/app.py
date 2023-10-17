from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Your chatbot logic with patterns and responses
def healthcare_chatbot(input_text):
     chatbot_responses = [
    (r'(.*)(Hello|Hi|hi|hello|hey)',['Hello, If you are in pain or have any questions regarding your health you can ask me. I hope to be of assistance.']),
    (r'(.*)(bye|quit|thank you)', ['Goodbye!', 'See you later!']),
    (r'(.*)(help|problem)', ['I can help you with general health and medical queries.']),
    (r'(.*) (symptoms)', ["It could be a variety of conditions. Please consult a healthcare professional."]),
    (r'(.*) (treatment|cure)', ["The treatment may vary depending on the condition. Consult a doctor for advice."]),
    (r'(.*)(headache|head pain|head hurts)', ["A headache can be caused by various factors, such as stress, dehydration, or underlying health issues. Try drinking water and resting. If it persists, consult a doctor."]),
    (r'(.*)fever', ["Fever is a symptom of various illnesses. Monitor your temperature and consult a doctor if it's high or persistent."]),
    (r'(.*)(cough|coughing)', ["Coughs can be caused by infections or allergies. Get plenty of rest, drink fluids, and consider over-the-counter cough remedies. If it continues, see a healthcare professional."]),
    (r'(.*)(flu)', ["The flu is caused by influenza viruses. Rest, stay hydrated, and consult a doctor if you suspect you have the flu."]),
    (r'(.*)(cold)', ["Colds are viral infections. Rest, drink fluids, and use over-the-counter cold remedies to alleviate symptoms."]),
    (r'(.*)(COVID-19|coronavirus|covid)', ["If you suspect you have COVID-19, self-isolate and get tested. Follow local health guidelines and consult a healthcare provider."]),
    (r'(.*)(heart attack|heart pain)', ["If you believe you or someone else is having a heart attack, call 911 immediately. Do not wait."]),
    (r'(.*)(diabetes)', ["Diabetes is a chronic condition. Maintain a healthy lifestyle, monitor your blood sugar, and follow your doctor's advice."]),
    (r'(.*)(asthma|breathing difficulty)', ["Asthma is a respiratory condition. Use prescribed inhalers and avoid triggers. Consult your doctor for a personalized plan."]),
    (r'(.*)(allergies|allergy|allergic reaction)', ["Allergies can be managed with antihistamines and by avoiding allergens. Consult an allergist for testing and advice."]),
    (r'(.*)skin rash', ["Skin rashes can have many causes, including allergies, infections, or autoimmune conditions. Consult a dermatologist for diagnosis and treatment."]),
    (r'(.*)depression', ["Depression is a serious mental health condition. Seek help from a mental health professional or therapist."]),
    (r'(.*)anxiety', ["Anxiety can be managed through therapy and, in some cases, medication. Speak to a mental health professional for support."]),
    (r'(.*)insomnia', ["If you have trouble sleeping, practice good sleep hygiene and consider talking to a sleep specialist for advice."]),
    (r'(.*)weight loss', ["Unexplained weight loss can be a sign of underlying health issues. Consult a doctor to rule out any serious conditions."]),
    (r'(.*)weight gain', ["Unexplained weight gain can have various causes. Consult a healthcare provider to determine the underlying issue."]),
    (r'(.*)(diet|nutrition)', ["Maintaining a balanced diet is essential for good health. Consult a nutritionist for personalized dietary advice."]),
    (r'(.*)(exercise|workout)', ["Regular exercise is crucial for physical and mental health. Start with a fitness plan that suits your fitness level and goals."]),
    (r'(.*)(stress management|stress|stressed)', ["Stress can impact your health. Practice stress-reduction techniques like mindfulness, yoga, or meditation."]),
    (r'(.*)blood pressure', ["High blood pressure can lead to serious health issues. Monitor your blood pressure regularly and consult a doctor for guidance."]),
    (r'(.*)cholesterol', ["High cholesterol levels can increase the risk of heart disease. Consult a healthcare provider for dietary and medical management."]),
    (r'(.*)pregnancy', ["If you suspect you're pregnant, take a home pregnancy test and consult an obstetrician for prenatal care."]),
    (r'(.*)birth control', ["There are various birth control methods available. Consult a gynecologist to discuss options and find the best fit for you."]),
    (r'(.*)nutrition during pregnancy', ["A healthy diet during pregnancy is essential. Consult with a nutritionist or healthcare provider for guidance."]),
    (r'(.*)childhood vaccinations', ["Vaccinations are crucial to protect children from diseases. Follow the recommended vaccination schedule for your child."]),
    (r'(.*)elderly care', ["Elderly individuals may have unique healthcare needs. Consult a geriatrician for specialized care and advice."]),
    (r'(.*)arthritis', ["Arthritis can cause joint pain and stiffness. Consult a rheumatologist for diagnosis and management."]),
    (r'(.*)dental care', ["Regular dental check-ups and oral hygiene are essential for maintaining healthy teeth and gums."]),
    (r'(.*)vision problems', ["If you experience vision problems, consult an eye specialist (ophthalmologist) for an eye examination."]),
    (r'(.*)ear infection', ["Ear infections can be painful. Consult an ENT specialist for diagnosis and treatment."]),
    (r'(.*)stroke', ["If you suspect someone is having a stroke, call 911 immediately. Recognize the FAST signs: Face drooping, Arm weakness, Speech difficulty, Time to call 911."]),
    (r'(.*)asthma attack', ["During an asthma attack, use your inhaler as prescribed and seek immediate medical attention if your symptoms worsen."]),
    (r'(.*)food poisoning', ["If you suspect food poisoning, stay hydrated and rest. If symptoms persist or worsen, consult a doctor."]),
    (r'(.*)sunburn', ["Treat sunburn by applying aloe vera or a cool compress. Stay out of the sun until the burn heals."]),
    (r'(.*)poisoning', ["If you or someone is exposed to a toxic substance, call poison control and seek medical attention immediately."]),
    (r'(.*)concussion', ["A concussion is a type of brain injury. Rest, avoid physical activity, and consult a healthcare provider for evaluation."]),
    (r'(.*)(sleep apnea|insomnia)', ["Sleep apnea can disrupt your sleep and health. Consult a sleep specialist for evaluation and treatment options."]),
    (r'(.*)strep throat', ["Strep throat is a bacterial infection. Consult a doctor for diagnosis and antibiotic treatment."]),
    (r'(.*)ear (ache|pain|hurts)', ["Earaches can have various causes. Consult an ENT specialist for diagnosis and treatment."]),
    (r'(.*)stomach (ache|pain|hurts)', ["Stomach aches can be caused by various factors. Avoid irritating foods and consult a doctor if pain persists."]),
    (r'(.*)diarrhea', ["Diarrhea can have many causes, including infections and dietary issues. Stay hydrated and consult a doctor if it continues."]),
    (r'(.*)constipation', ["Constipation can result from dietary choices or underlying conditions. Increase fiber intake and consult a doctor if it persists."]),
    (r'(.*)acne', ["Acne is a common skin condition. Consult a dermatologist for skincare recommendations and treatment options."]),
    (r'(.*)hair (loss|breakage)', ["Hair loss can have multiple causes. Consult a dermatologist for a proper diagnosis and potential treatments."]),
    (r'(.*)migraine', ["Migraines can be debilitating. Identify triggers and consult a healthcare provider for management strategies."]),
    (r'(.*)joint pain', ["Joint pain can be due to arthritis or other conditions. Consult a rheumatologist for diagnosis and pain management."]),
    (r'(.*)(sinusitis|sinus)', ["Sinusitis is an inflammation of the sinuses. Consult a doctor for diagnosis and treatment, which may include antibiotics."]),
    (r'(.*)common cold', ["The common cold is a viral infection. Get plenty of rest, stay hydrated, and use over-the-counter cold remedies to alleviate symptoms."]),
    (r'(.*)(pink eye|conjunctivitis)', ["Pink eye can be caused by viruses or bacteria. Consult an eye specialist (ophthalmologist) for diagnosis and treatment."]),
    (r'(.*)sore throat', ["A sore throat can result from infections or irritation. Gargle with warm salt water and consult a doctor if it persists."]),
    (r'(.*)swollen glands', ["Swollen glands can be a sign of infection or other health issues. Consult a doctor for a proper evaluation."]),
    (r'(.*)(sinus congestion|nose congestion|nasal block)', ["Sinus congestion can lead to discomfort. Use saline nasal sprays and consider decongestants if advised by a healthcare provider."]),
    (r'(.*)gastroenteritis', ["Gastroenteritis, often caused by viruses, results in stomach and intestinal symptoms. Stay hydrated and consult a doctor if it persists."]),
    (r'(.*)indigestion', ["Indigestion can occur after eating. Avoid trigger foods and try antacids. Consult a doctor if it continues."]),
    (r'(.*)heartburn', ["Heartburn can result from acid reflux. Avoid trigger foods, elevate your head while sleeping, and consult a doctor if it persists."]),
    (r'(.*)ulcer', ["Ulcers can lead to stomach pain. Consult a gastroenterologist for diagnosis and treatment options."]),
    (r'(.*)gallstones', ["Gallstones can cause abdominal pain. Consult a gastroenterologist for diagnosis and potential treatment options."]),
    (r'(.*)kidney stones', ["Kidney stones can be painful. Stay hydrated and consult a urologist for diagnosis and treatment."]),
    (r'(.*)inflammatory bowel disease', ["Inflammatory bowel diseases like Crohn's or ulcerative colitis require specialized care from a gastroenterologist."]),
    (r'(.*)appendicitis', ["Appendicitis is a medical emergency. If you suspect appendicitis, seek immediate medical attention."]),
    (r'(.*)pneumonia', ["Pneumonia is a serious lung infection. Consult a doctor for diagnosis and treatment, which may include antibiotics."]),
    (r'(.*)tuberculosis', ["Tuberculosis is a bacterial infection. Consult a healthcare provider for diagnosis and a treatment plan."]),
    (r'(.*)hepatitis', ["Hepatitis can have various forms and causes. Consult a hepatologist for diagnosis and treatment options."]),
    (r'(.*)cancer', ["Cancer can manifest in many forms. Consult an oncologist for diagnosis, staging, and treatment options."]),
    (r'(.*)dental cavity', ["Cavities require dental care. Consult a dentist for filling or other treatment options."]),
    (r'(.*)gingivitis', ["Gingivitis is an early stage of gum disease. Maintain good oral hygiene and consult a dentist for treatment."]),
    (r'(.*)gum disease', ["Advanced gum disease may require specialized care from a periodontist."]),
    (r'(.*)arthritis treatment', ["Arthritis treatment options include medications, physical therapy, and lifestyle changes. Consult a rheumatologist for personalized advice."]),
    (r'(.*)(osteoporosis|weak bones)', ["Osteoporosis weakens bones. Consult a healthcare provider for diagnosis and treatment options."]),
    (r'(.*)allergic reaction', ["For severe allergic reactions (anaphylaxis), use an epinephrine auto-injector if prescribed and seek immediate medical attention."]),
    (r'(.*)strep infection', ["Strep infections can lead to various health issues. Consult a doctor for diagnosis and antibiotic treatment."]),
    (r'(.*)burns', ["Treat burns with cool, running water and clean dressings. Seek medical attention for severe burns."]),
    (r'(.*)(pneumothorax|lung collapse)', ["Pneumothorax is a collapsed lung. Seek immediate medical attention if you suspect this condition."]),
    (r'(.*)asthma prevention', ["Asthma prevention involves avoiding triggers, using prescribed inhalers, and following an asthma action plan."]),
    (r'(.*)sun safety', ["Protect your skin from the sun by wearing sunscreen, protective clothing, and sunglasses."]),
    (r'(.*)blood sugar control', ["Managing blood sugar is crucial for diabetics. Follow a personalized plan provided by your doctor."]),
    (r'(.*)cholesterol management', ["Control high cholesterol with dietary changes, exercise, and, in some cases, medications. Consult a healthcare provider."]),
    (r'(.*)heart health', ["Maintain heart health by eating a heart-healthy diet, exercising, and avoiding smoking and excessive alcohol consumption."]),
    (r'(.*)respiratory infections', ["Respiratory infections can be caused by viruses or bacteria. Consult a doctor for diagnosis and treatment."]),
    (r'(.*)earwax removal', ["Excessive earwax can affect hearing. Consult an ENT specialist for safe earwax removal."]),
    (r'(.*)back (pain|hurt|ache)', ["Back pain can have various causes. Consult a healthcare provider or a physiotherapist for diagnosis and treatment."]),
    (r'(.*)high blood sugar', ["High blood sugar can be a sign of uncontrolled diabetes. Consult your healthcare provider for management strategies."]),
    (r'(.*)low blood sugar', ["Low blood sugar can be dangerous for diabetics. Consume glucose or follow your doctor's advice to raise your blood sugar."]),
    (r'(.*)concussion symptoms', ["Recognize concussion symptoms such as headache, dizziness, and confusion. Rest and seek medical attention if needed."]),
    (r'(.*)heatstroke', ["Heatstroke is a medical emergency. Move to a cooler place, hydrate, and seek immediate medical attention."]),
    (r'(.*)heat exhaustion', ["If you experience heat exhaustion, move to a cooler place, hydrate, and rest."]),
    (r'(.*)hypertension', ["Hypertension is high blood pressure. Follow a healthcare provider's recommendations to manage it."]),
    (r'(.*)eczema', ["Eczema is a skin condition that may require specialized care from a dermatologist. Follow a skincare plan for relief."]),
    (r'(.*)flu vaccination', ["Get a flu vaccine annually to reduce the risk of influenza infection."]),
    (r'(.*)measles', ["Measles is a highly contagious viral infection. Vaccination is the best prevention."]),
    (r'(.*)dengue', ["Dengue is a viral illness transmitted by mosquitoes. Stay hydrated, rest, and seek medical attention if symptoms worsen."]),
(r'(.*)reproductive health', ["Reproductive health covers various aspects of sexual and reproductive well-being. Consult a gynecologist or reproductive health specialist for guidance."]),
(r'(.*)contraception', ["Contraception methods vary, including birth control pills, condoms, and IUDs. Consult a healthcare provider to choose the most suitable option."]),
(r'(.*)oral hygiene', ["Maintaining good oral hygiene is essential for healthy teeth and gums. Regular dental check-ups and proper brushing and flossing are crucial."]),
(r'(.*)aneurysm', ["An aneurysm is a bulge in a blood vessel. Seek immediate medical attention if you suspect an aneurysm."]),
(r'(.*)addiction', ["Addiction can affect various substances or behaviors. Seek help from addiction specialists and support groups for recovery."]),
(r'(.*)addison disease', ["Addison's disease is a rare condition affecting the adrenal glands. Treatment involves hormone replacement therapy."]),
(r'(.*)alzheimer', ["Alzheimer's disease is a progressive neurological condition. Consult a neurologist for diagnosis and caregiving support."]),
(r'(.*)eczema', ["Eczema is a common skin condition. Follow a skincare plan and use topical treatments as prescribed."]),
(r'(.*)ADHD', ["ADHD is a neurodevelopmental disorder. Consult a psychiatrist or specialist for diagnosis and treatment options."]),
(r'(.*)bipolar', ["Bipolar disorder involves mood swings. Consult a psychiatrist for diagnosis and management."]),
(r'(.*)bpd disorder', ["Borderline Personality Disorder (BPD) is a mental health condition. Treatment may include therapy and medications."]),
(r'(.*)blood poisoning', ["Blood poisoning, or sepsis, is a life-threatening condition. Seek immediate medical attention if you suspect sepsis."]),
(r'(.*)chest pain', ["Chest pain can have numerous causes, including heart-related issues. Seek immediate medical attention for chest pain."]),
(r'(.*)chicken pox', ["Chickenpox is a contagious viral infection. Rest and antiviral medications can help manage symptoms."]),
(r'(.*)smallpox', ["Smallpox has been eradicated, and vaccination is no longer necessary."]),
(r'(.*)polio', ["Polio is a viral disease. Vaccination has nearly eradicated polio worldwide."]),
(r'(.*)chronic pain', ["Chronic pain can result from various conditions. Consult a pain specialist for diagnosis and pain management strategies."]),
(r'(.*)coma', ["Coma is a state of unconsciousness. Medical care is essential for coma patients."]),
(r'(.*)cysts', ["Cysts can occur in various parts of the body. Consult a healthcare provider for evaluation and treatment."]),
(r'(.*)warts', ["Warts are skin growths caused by viruses. Various treatments, including freezing or topical medications, can remove warts."]),
(r'(.*)dehydration', ["Dehydration can lead to health problems. Stay hydrated with water and, in some cases, oral rehydration solutions."]),
(r'(.*)Downs syndrome', ["Down's syndrome is a genetic condition. Early intervention programs and support are essential for individuals with Down's syndrome."]),
(r'(.*)ebola', ["Ebola is a highly infectious and often deadly viral disease. Isolation and supportive care are necessary during outbreaks."]),
(r'(.*)(HIV|AIDS)', ["HIV is a virus that can lead to AIDS. Antiretroviral therapy can manage HIV, and prevention is crucial."]),
(r'(.*)hypertension', ["Hypertension is high blood pressure. Follow a healthcare provider's recommendations to manage it."]),
(r'(.*)stroke', ["Stroke is a medical emergency. Recognize the signs and seek immediate medical attention if you suspect a stroke."]),
(r'(.*)epilepsy', ["Epilepsy is a neurological condition characterized by seizures. Consult a neurologist for diagnosis and treatment."]),
(r'(.*)endometriosis', ["Endometriosis can cause pelvic pain and fertility issues. Consult a gynecologist for diagnosis and treatment."]),
(r'(.*)fibroids', ["Fibroids are noncancerous uterine growths. Treatment options include medication, noninvasive procedures, and surgery."]),
(r'(.*)fungal infection', ["Fungal infections can affect the skin, nails, and other body parts. Antifungal medications and proper hygiene can help."]),
(r'(.*)gallstones', ["Gallstones can cause abdominal pain. Consult a gastroenterologist for diagnosis and potential treatment options."]),
(r'(.*)herpes', ["Herpes infections can be oral or genital. Antiviral medications can help manage outbreaks and reduce transmission."]),
(r'(.*)gonorrhea', ["Gonorrhea is a sexually transmitted infection. Antibiotics are used for treatment."]),
(r'(.*)hay fever', ["Hay fever, or allergic rhinitis, can cause allergy symptoms. Over-the-counter antihistamines and allergen avoidance can provide relief."]),
(r'(.*)hepatitis', ["Hepatitis can have various forms and causes. Consult a hepatologist for diagnosis and treatment options."]),
(r'(.*)glaucoma', ["Glaucoma is an eye condition that can lead to vision loss. Consult an ophthalmologist for diagnosis and treatment."]),
(r'(.*)cataract', ["Cataracts are a clouding of the eye's lens. Surgery is typically required to remove cataracts."]),
(r'(.*)indigestion', ["Indigestion can occur after eating. Avoid trigger foods and try antacids. Consult a doctor if it continues."]),
(r'(.*)itching', ["Itching can result from various causes. Consult a dermatologist for diagnosis and treatment."]),
(r'(.*)cramps', ["Muscle cramps can be caused by dehydration, overuse, or underlying conditions. Stretching and hydration can help."]),
(r'(.*)lupus', ["Lupus is an autoimmune disease. Treatment varies and may include medications to manage symptoms."]),
(r'(.*)malaria', ["Malaria is a parasitic infection transmitted by mosquitoes. Antimalarial medications and preventive measures are crucial."]),
(r'(.*)malnutrition', ["Malnutrition can have serious health consequences. Consult a healthcare provider for evaluation and dietary guidance."]),
(r'(.*)menopause', ["Menopause can lead to various symptoms. Hormone therapy or lifestyle adjustments may help manage them."]),
(r'(.*)mumps', ["Mumps is a viral infection that can cause swollen salivary glands. Vaccination can prevent mumps."]),
(r'(.*)sinusitis', ["Sinusitis is an inflammation of the sinuses. Consult a doctor for diagnosis and treatment, which may include antibiotics."]),
(r'(.*)nosebleed', ["Nosebleeds can result from dry air, trauma, or underlying conditions. Pinch the nostrils and lean forward to stop bleeding."]),


]



    
    
   
     for pattern, response in chatbot_responses.items():
        if pattern in input_text.lower():
            return response

# If no specific pattern is matched, respond with a default message
     return "I'm sorry, I couldn't understand that. Please ask another question."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/image_click', methods=['POST'])
def handle_image_click():
    user_input = request.json['userInput']
    bot_response = healthcare_chatbot(user_input)
    return jsonify({'bot_response': bot_response})

if __name__ == '__main__':
    app.run(debug=True, port=5001)

