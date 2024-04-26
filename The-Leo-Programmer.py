import streamlit as st
import time
import difflib

st.set_page_config(
    page_title="The Leo Programmer",
    page_icon="🦁",
)

def get_response(user_input):
    user_input = user_input.lower()
    responses = {
        "1": """
**Here is AF's educational background:**

1. **Bachelors Degree in B.Sc Artificial Intelligence and Machine Learning**
   - **Institution:** P. B. Siddhartha College of Arts & Science, Vijayawada, AP
   - **Duration:** 2021 - 2024
   - **GPA:** 7.8

2. **Intermediate in M.P.C**
   - **Institution:** Sri Gayatri Jr. College, Vijayawada, AP
   - **Passed Year:** 2021
   - **GPA:** 9.1

3. **SSC**
   - **Institution:** Swarna Bharathi Smart School, Vijayawada, AP
   - **Passed Year:** 2019
   - **GPA:** 9.2
""",

        "2": """ Here’s a snapshot of AF's technical expertise crafted through years of experience:

- **Programming Languages Known:** C, Python, and R
- **Frontend:** HTML, CSS
- **Backend:** PHP
- **Databases:** Oracle SQL, MySQL, MongoDB
        """,
"3": """
**AF's Certifications and Professional Development:**

1. **AICTE - EDUSKILLS Virtual Internship**
   - **Title:** Data Analytic Process Automation
   - **Duration:** May - July 2023
   - **Supported by:** Alteryx SparkED, Inc.

2. **Python Programming for Every Beginner**
   - **Issued by:** Udemy
   - **Date:** April 2022
""",

        "4": """
**Research Contributions by AF:**

- **Supervised Learning Study on K-NN Classification**
  - **Publication:** International Journal of Food and Nutritional Sciences
  - **Details:** Volume 11, Issue 12, Pages 6885-6894
  - **Co-authorship:** Investigated the k-Nearest Neighbors (kNN) Algorithm, focusing on classification and predictive analytics in supervised learning.
  - **Access:** [View the Journal](https://www.ijfans.org/uploads/paper/bdd0e15b055a9b79495130c7787d2d42.pdf)

- **AI Resonance: Predictive Analytics for Customer Churn**
  - **Publication:** International Journal for Innovative Engineering & Management Research, Vol. 13, No. 4, 2024
  - **Overview:** Authored a paper on using artificial intelligence to forecast customer churn, emphasizing future business stability.
  - **Access:** [View the Journal](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4792480)

- **Class Imbalance in Machine Learning: A Comparative Analysis**
  - **Contribution:** Chapter in the book 'Sustainable AI and IOT Based Sensor Data Analytics'
  - **Focus:** Addressed the challenges of class imbalance in machine learning and deep learning.
  - **ISBN:** 978-93-340-1496-9
  - **Pages:** 99-133
  - **Publisher:** Immortal Publications
""",

"5": """
**Prominent Conference Presentations by AF:**

- **Title:** "Predicting Sleep Disorders for Improved Healthcare: A Comprehensive Study"
  - **Event:** 7th International Conference on Innovative Computing and Communication (ICICC 2024)
  - **Details:** This paper has been accepted into the Springer Scopus Indexed LNNS series and focuses on the application of advanced computational techniques to predict sleep disorders, aiming to enhance healthcare outcomes.
  - **Location:** New Delhi, India
  - **Date:** February 16, 2024  
""",
        
"6": """
**AF's Project Showcase**

These project lists showcase my abilities in skills like Machine Learning, Natural Language Processing, Deep Learning, Data Analysis, and more, reflecting a broad spectrum of applications and technologies.

1. **Text Summarizer Application**
   - **Description:** Developed a text summarizer using TF-IDF Vectorizer, integrating Django Framework for the backend and applying principles of Machine Learning and Natural Language Processing (NLP).
   - **Link:** [Text Summarizer on GitHub](https://github.com/AF011/Text_Summarizer)
   - **Additional NLP Projects:** [NLP Projects on GitHub](https://github.com/AF011/NLP_Projects)

2. **Future Foundations - Projecting Real Estate Values in Bangalore**
   - **Description:** Crafted an application to predict real estate values using data analysis and machine learning techniques, deployed via Streamlit.
   - **Link:** [Bangalore House Prediction](https://banglore-house-pred-af011.streamlit.app/)

3. **Diverse Machine Learning Applications**
   - **Description:** Engaged in various projects employing classification and regression algorithms focused on practical applications such as diabetes detection, employability predictions for students, and insurance risk analysis.
   - **Link:** [Machine Learning Projects on GitHub](https://github.com/AF011/Machine-Learning-Projects-Academic)

4. **Advanced Deep Learning Initiatives**
   - **Description:** Undertook multiple projects leveraging Artificial Neural Networks (ANNs) and Convolutional Neural Networks (CNNs) for tasks including complex challenges like leaf disease detection.
   - **Link:** [Deep Learning Projects on GitHub](https://github.com/AF011/Deep-Learning-Projects)

**Explore More**
   - Dive deeper into my full range of projects by visiting my GitHub repositories.
   - **Link:** [AF011 GitHub Repositories](https://github.com/AF011?tab=repositories)
""",

"7": """
**Here are the AF's Key Achievements:**

1. **National-wide Datathon - 4th Place**
   - Organized by Alteryx SparkED, Inc. during a virtual internship, competing against 37 teams from prestigious colleges.

2. **2nd Place in Coding and Decoding Competition**
   - Attained during an inter-college competition in my 2nd year, with a 1st place victory in the decoding category.
""",


"8": """
**Explore AF's Resume**

Take a closer look at AF's comprehensive resume to understand the depth of his experience and the breadth of his skills.

**View AF's Resume:** [AF011 Resume PDF](https://drive.google.com/file/d/1mylhIpJotOrJvrKu3k-KrRFKt2882TD-/view?usp=sharing)
""",

"9": """
**Meet Abdul Faheem - The Leo Programmer**

**Born:** February 11, 2004  
**Location:** Vijayawada, Andhra Pradesh, 520007

I have a strong passion for technology, especially in areas like AI & ML, NLP, and Deep Learning. My expertise extends across various programming languages, including C and Python, but I identify more broadly as a software engineer who is eager to acquire new skills and address challenges in Software Development, AI & ML, Data Analysis, and Data Science.

My approach is not limited to programming in specific languages; rather, I thrive on solving complex problems wherever they arise. This flexibility and willingness to adapt are central to my ongoing professional development and my enthusiasm for taking on new opportunities in the tech field.

The nickname 'The Leo Programmer' is inspired by my zodiac sign, representing my dedication and proactive approach to Programming and technology. It underscores my commitment to leading in my field and striving for excellence.


**Let's Connect!**  
- **Mobile:** +91 9391122345  
- **GitHub:** [LeoProgrammer - AF011](https://github.com/AF011)  
- **LinkedIn:** [Abdul Faheem](https://www.linkedin.com/in/abdulfaheem011/)
"""


    }
    
    synonym_map = {
        "education": "1",
        "skills": "2",
        "certifications": "3",
        "research activities": "4",
        "research": "4",
        "publications": "4",
        "conference publications": "5",
        "conference": "5",
        "projects": "6",
        "achievements": "7",
        "resume": "8",
        "about": "9",
        "af011": "9",
        "abdul faheem": "9"
    }

    
    if not user_input.isdigit():
        #user_input = synonym_map.get(user_input, "default")  # Map synonyms to keys or default
        matches = difflib.get_close_matches(user_input, synonym_map.keys(), n=1, cutoff=0.7)
        user_input = synonym_map[matches[0]] if matches else "default"
            
    return responses.get(user_input, "I'm not sure how to respond to that. Can you try asking about a specific area like Skills, Education, etc.?")


def footer():
    # Footer Section
    st.markdown('<style>div.block-container{padding-bottom: 100px;}</style>', unsafe_allow_html=True)
    st.markdown("""---""")
    st.markdown("""
        An AF's Endeavour, developed with 💡 and 🥤: The Leo Programmer AF011's Portfolio ✨. <br>
                
        -AF011
    """, unsafe_allow_html=True)


def main():
    st.title("Abdul Faheem")
    st.caption("The Leo Programmer - AF011 🦁")
    
    st.write("""
    I am interested in AI & ML, NLP, and Deep Learning, and I am proficient in C and Python languages. I'm also 
    interested in Data Analysis and Data Science. I am not limited to only one area or to saying I only know 
    specific languages; I am a problem solver with versatility. I am always ready to learn new things if required 
    at any time.
    """)
    st.divider()
    st.markdown("You can ask my friend Leo about my:")
    st.write("""
    1. Education
    2. Skills
    3. Certifications
    4. Research Activities
    5. Conference Publications
    6. Projects 
    7. Achievements
    8. Resume
    9. About
    """)

    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    for author, text in st.session_state['chat_history']:
        if author == 'bot':
            st.success(f"🦁: {text}")
        elif author == 'user':
            st.info(f"You: {text}")

    user_input = st.text_input("🦁: Hello! I'm Leo, a friend of AF. If you'd like to know more about AF, please specify a keyword you're interested in from the list above or use the serial number associated with it.", key="user_input")

    send_button = st.button("Send")

    if send_button and user_input:
        with st.status("Sending the Message..."):
            st.write("Sending the Message...")
            time.sleep(0.5)
            st.write("Message Sent...")
            time.sleep(0.2)
            st.write("Message Seen...")
            time.sleep(0.2)
        
        st.session_state['chat_history'].append(('user', user_input))
        response = get_response(user_input)
        st.session_state['chat_history'].append(('bot', response))

        st.experimental_rerun()
        
    footer()

    
if __name__ == '__main__':
    main()
