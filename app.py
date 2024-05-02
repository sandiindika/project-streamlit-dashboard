# Configuration

import streamlit as st

from PIL import Image

st.set_page_config(
    page_title= "Sans",
    layout= "centered",
    page_icon= Image.open("./assets/favicon.ico"),
    initial_sidebar_state= "expanded"
)

st.markdown(
    """<style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .st-emotion-cache-gh2jqd {padding-top: 2rem; padding-bottom: 2rem;}
    </style>""",
    unsafe_allow_html= True
)

def ms_1():
    st.markdown("<div class= \"ms-1\"></div>", unsafe_allow_html= True)

def ms_2():
    st.markdown("<div class= \"ms-2\"></div>", unsafe_allow_html= True)

def ms_3():
    st.markdown("<div class= \"ms-3\"></div>", unsafe_allow_html= True)

def card_project(lt_img , lt_text, lt_link, rg_img, rg_text, rg_link):
    cols = st.columns([1, .02, 1])
    with cols[0]:
        st.image(lt_img)
        st.markdown(f'<p class="project-detail"><a id="project-link" href="{lt_link}">{lt_text}</a></p>', unsafe_allow_html= True)
    with cols[2]:
        st.image(rg_img)
        st.markdown(f'<p class="project-detail"><a id="project-link" href="{rg_link}">{rg_text}</a></p>', unsafe_allow_html= True)
    ms_1()

with open("./css/style.css") as file:
    st.markdown("<style>{}</style>".format(file.read()), unsafe_allow_html= True)

# Sidebar
    
with st.sidebar:
    st.image("./assets/profile-image.png")
    st.title("Hi! I am Sandi")
    st.caption("A Web Developer and Data Analyst. I work during the day and am busy at night.")
    ms_1()

    st.caption("**Social links**")
    cols = st.columns([1]*7)
    with cols[0]:
        st.markdown('''<a href="https://www.linkedin.com/in/ndisan">
                    <svg fill="#a3a8b8" viewBox="0 0 25 25" width="26" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"><path d="m5.706 7.798v16.202h-5.395v-16.202zm.343-5.002c.001.029.002.063.002.098 0 .749-.318 1.423-.826 1.895l-.002.001c-.545.498-1.274.803-2.075.803-.049 0-.099-.001-.148-.003h.007-.033c-.041.002-.089.003-.137.003-.784 0-1.496-.306-2.025-.804l.001.001c-.504-.488-.816-1.17-.816-1.925 0-.024 0-.048.001-.073v.004c-.001-.021-.001-.045-.001-.069 0-.762.324-1.448.841-1.929l.002-.001c.544-.495 1.271-.799 2.068-.799.046 0 .091.001.137.003h-.006c.043-.002.092-.003.143-.003.785 0 1.5.303 2.034.798l-.002-.002c.515.497.835 1.193.835 1.964v.042-.002zm19.062 11.92v9.284h-5.378v-8.665c.005-.079.007-.171.007-.263 0-.896-.249-1.733-.682-2.447l.012.021c-.427-.596-1.117-.979-1.896-.979-.06 0-.12.002-.18.007h.008c-.027-.001-.058-.002-.089-.002-.62 0-1.19.213-1.641.57l.006-.004c-.453.367-.808.836-1.032 1.375l-.008.023c-.116.355-.182.763-.182 1.187 0 .048.001.096.003.144v-.007 9.042h-5.378q.033-6.523.033-10.578t-.016-4.839l-.016-.785h5.378v2.354h-.033c.214-.345.435-.644.678-.924l-.008.009c.281-.309.583-.588.908-.838l.016-.012c.404-.311.878-.555 1.392-.704l.03-.007c.538-.161 1.157-.254 1.797-.254h.079-.004c.071-.003.154-.005.237-.005 1.681 0 3.195.714 4.256 1.856l.003.004q1.702 1.856 1.702 5.436z"></path></g></svg>
                    </a>''',
                    unsafe_allow_html= True)
    with cols[1]:
        st.markdown('''<a href="https://www.instagram.com/ndisans__/">
                    <svg viewBox="0 0 20 20" width="26" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" fill="#a3a8b8"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <title>instagram [#167]</title> <desc>Created with Sketch.</desc> <defs> </defs> <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"> <g id="Dribbble-Light-Preview" transform="translate(-340.000000, -7439.000000)" fill="#a3a8b8"> <g id="icons" transform="translate(56.000000, 160.000000)"> <path d="M289.869652,7279.12273 C288.241769,7279.19618 286.830805,7279.5942 285.691486,7280.72871 C284.548187,7281.86918 284.155147,7283.28558 284.081514,7284.89653 C284.035742,7285.90201 283.768077,7293.49818 284.544207,7295.49028 C285.067597,7296.83422 286.098457,7297.86749 287.454694,7298.39256 C288.087538,7298.63872 288.809936,7298.80547 289.869652,7298.85411 C298.730467,7299.25511 302.015089,7299.03674 303.400182,7295.49028 C303.645956,7294.859 303.815113,7294.1374 303.86188,7293.08031 C304.26686,7284.19677 303.796207,7282.27117 302.251908,7280.72871 C301.027016,7279.50685 299.5862,7278.67508 289.869652,7279.12273 M289.951245,7297.06748 C288.981083,7297.0238 288.454707,7296.86201 288.103459,7296.72603 C287.219865,7296.3826 286.556174,7295.72155 286.214876,7294.84312 C285.623823,7293.32944 285.819846,7286.14023 285.872583,7284.97693 C285.924325,7283.83745 286.155174,7282.79624 286.959165,7281.99226 C287.954203,7280.99968 289.239792,7280.51332 297.993144,7280.90837 C299.135448,7280.95998 300.179243,7281.19026 300.985224,7281.99226 C301.980262,7282.98483 302.473801,7284.28014 302.071806,7292.99991 C302.028024,7293.96767 301.865833,7294.49274 301.729513,7294.84312 C300.829003,7297.15085 298.757333,7297.47145 289.951245,7297.06748 M298.089663,7283.68956 C298.089663,7284.34665 298.623998,7284.88065 299.283709,7284.88065 C299.943419,7284.88065 300.47875,7284.34665 300.47875,7283.68956 C300.47875,7283.03248 299.943419,7282.49847 299.283709,7282.49847 C298.623998,7282.49847 298.089663,7283.03248 298.089663,7283.68956 M288.862673,7288.98792 C288.862673,7291.80286 291.150266,7294.08479 293.972194,7294.08479 C296.794123,7294.08479 299.081716,7291.80286 299.081716,7288.98792 C299.081716,7286.17298 296.794123,7283.89205 293.972194,7283.89205 C291.150266,7283.89205 288.862673,7286.17298 288.862673,7288.98792 M290.655732,7288.98792 C290.655732,7287.16159 292.140329,7285.67967 293.972194,7285.67967 C295.80406,7285.67967 297.288657,7287.16159 297.288657,7288.98792 C297.288657,7290.81525 295.80406,7292.29716 293.972194,7292.29716 C292.140329,7292.29716 290.655732,7290.81525 290.655732,7288.98792" id="instagram-[#167]"> </path> </g> </g> </g> </g></svg>
                    </a>''',
                    unsafe_allow_html= True)
    with cols[2]:
        st.markdown('''<a href="https://github.com/sandiindika/">
                    <svg viewBox="0 0 20 20" width="26" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" fill="#a3a8b8"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <title>github [#142]</title> <desc>Created with Sketch.</desc> <defs> </defs> <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"> <g id="Dribbble-Light-Preview" transform="translate(-140.000000, -7559.000000)" fill="#a3a8b8"> <g id="icons" transform="translate(56.000000, 160.000000)"> <path d="M94,7399 C99.523,7399 104,7403.59 104,7409.253 C104,7413.782 101.138,7417.624 97.167,7418.981 C96.66,7419.082 96.48,7418.762 96.48,7418.489 C96.48,7418.151 96.492,7417.047 96.492,7415.675 C96.492,7414.719 96.172,7414.095 95.813,7413.777 C98.04,7413.523 100.38,7412.656 100.38,7408.718 C100.38,7407.598 99.992,7406.684 99.35,7405.966 C99.454,7405.707 99.797,7404.664 99.252,7403.252 C99.252,7403.252 98.414,7402.977 96.505,7404.303 C95.706,7404.076 94.85,7403.962 94,7403.958 C93.15,7403.962 92.295,7404.076 91.497,7404.303 C89.586,7402.977 88.746,7403.252 88.746,7403.252 C88.203,7404.664 88.546,7405.707 88.649,7405.966 C88.01,7406.684 87.619,7407.598 87.619,7408.718 C87.619,7412.646 89.954,7413.526 92.175,7413.785 C91.889,7414.041 91.63,7414.493 91.54,7415.156 C90.97,7415.418 89.522,7415.871 88.63,7414.304 C88.63,7414.304 88.101,7413.319 87.097,7413.247 C87.097,7413.247 86.122,7413.234 87.029,7413.87 C87.029,7413.87 87.684,7414.185 88.139,7415.37 C88.139,7415.37 88.726,7417.2 91.508,7416.58 C91.513,7417.437 91.522,7418.245 91.522,7418.489 C91.522,7418.76 91.338,7419.077 90.839,7418.982 C86.865,7417.627 84,7413.783 84,7409.253 C84,7403.59 88.478,7399 94,7399" id="github-[#142]"> </path> </g> </g> </g> </g></svg>
                    </a>''',
                    unsafe_allow_html= True)
    with cols[3]:
        st.markdown('''<a href="https://hashnode.com/@suryaeceran">
                    <svg fill="#a3a8b8" viewBox="0 0 24 24" width="26" role="img" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"><path d="m22.351 8.019-6.37-6.37a5.63 5.63 0 0 0-7.962 0l-6.37 6.37a5.63 5.63 0 0 0 0 7.962l6.37 6.37a5.63 5.63 0 0 0 7.962 0l6.37-6.37a5.63 5.63 0 0 0 0-7.962zM12 15.953a3.953 3.953 0 1 1 0-7.906 3.953 3.953 0 0 1 0 7.906z"></path></g></svg>
                    </a>''',
                    unsafe_allow_html= True)
    with cols[4]:
        st.markdown('''<a href="https://www.kaggle.com/ndisan">
                    <svg fill="#a3a8b8" viewBox="0 0 32 32" width="26" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M25.099 31.812c-0.025 0.12-0.156 0.188-0.375 0.188h-4.183c-0.249 0-0.468-0.109-0.656-0.328l-6.907-8.787-1.932 1.828v6.817c0 0.313-0.151 0.469-0.463 0.469h-3.245c-0.312 0-0.469-0.156-0.469-0.469v-31.061c0-0.308 0.157-0.469 0.469-0.469h3.245c0.312 0 0.463 0.161 0.463 0.469v19.124l8.271-8.359c0.224-0.224 0.443-0.328 0.661-0.328h4.319c0.192 0 0.317 0.077 0.38 0.239 0.063 0.199 0.047 0.339-0.047 0.417l-8.74 8.459 9.115 11.343c0.125 0.141 0.156 0.276 0.093 0.48z"></path> </g></svg>
                    </a>''',
                    unsafe_allow_html= True)

# Introduction

st.write("## *Introduction*")
st.write("---")
st.write("#### I like working with new tools and technologies.")
ms_2()

st.write("My name is Sandi, currently a freelance web developer while teaching programming via the Superprof platform and writing web projects. You can see some of my projects below. Having coding experience since 2017, I have worked on small and large projects. I usually use PHP + Bootstrap for small projects, and Node framework for large projects.")
ms_1()

with open("CV.pdf", "rb") as file:
    btn = st.download_button(
        label= "Download Resume",
        data= file,
        file_name= "CV.pdf",
        mime= "application/pdf"
    )
ms_3()

# Experience

st.write("## *Experience*")
st.write("---")
ms_1()

# exp 1
st.markdown('''
            ### *Freelance Tutor*
            <p class="work-place">Superprof Indonesia (Sep 2021 - Present)</p>
            <p>
                Aims to create a learning environment that supports, motivates, and builds students' confidence in exploring the world of programming.
                Is committed to providing instruction that is structured, interactive, and tailored to individual student needs.
                Through experience in the IT industry and formal education in the computer field, I want to guide students to achieve success in learning various programming languages,
                algorithm concepts, and the latest technology.
            </p>
            ''', unsafe_allow_html= True)
ms_1()

# exp 2
st.markdown('''
            ### *Intern Data Scientist*
            <p class="work-place">Project-Based Virtual Intern : Data Scientist ID/X Partners x Rakamin Academy (Feb 2024 - Mar 2024)</p>
            <p>
                Implement various skills and tools such as Big Data Fundamentals, Statistics & Data Analytics, SQL Querying, R Programming,
                Python Programming, Machine Learning, etc. As well as end-to-end Machine Learning modeling to create data science solutions for clients.
            </p>
            ''', unsafe_allow_html= True)
ms_1()

# exp 3
st.markdown('''
            ### *Data Analyst*
            <p class="work-place">Bimbingin.id (Feb 2023 - Feb 2024)</p>
            <p>
                Designed and executed an optimized data gathering methodology to enhance the efficiency of data collection processes, resulting in a
                20% reduction in project turnaround time. Implemented a standardized data reporting structure, enhancing the accessibility and clarity of
                key performance indicators (KPIs) across all organizational tiers. This initiative facilitated data-centric decision-making, empowering
                stakeholders with actionable insights for strategic planning and operational improvements.
            </p>
            ''', unsafe_allow_html= True)
ms_1()

# exp 4
st.markdown('''
            ### *Software Engineer*
            <p class="work-place">Bimbingin.id (Jan 2021 - Jan 2023)</p>
            <p>
                Building IT Startup through practical, proprietary framework. We Incubate, Advise,
                and Grow, any size business & enterprise by solving holistic problems through research, strategy, and applicable management.
            </p>
            ''', unsafe_allow_html= True)
ms_3()

# Projects

st.write("## *Projects*")
st.write("---")
ms_1()

st.caption("Check out some of my data science projects.")
ms_1()

# row project 1
card_project(
    "./assets/projects/ai-chatbot.png",
    "Intelligent ChatBot built with Microsoft's DialoGPT transformer to interact with human users!",
    "https://www.kaggle.com/code/ndisan/ai-chatbot",
    "./assets/projects/forecasting.png",
    "Analysis based on time series, focusing primarily on hourly energy use, with the PJME_hourly data set given by PJM, a regional transmission organization in the United States.",
    "https://www.kaggle.com/code/ndisan/time-series-analysis-comparison"
)

# row project 2
card_project(
    "./assets/projects/retail-campaign.png",
    "Performe unsupervised clustering on customer log data from the wholesale company database. Customers will be separated into divisions to maximize the value of each customer to the business.",
    "https://www.kaggle.com/code/ndisan/retail-campaign-kmedoids",
    "./assets/projects/music-classification.png",
    "Explore music genre classification using Random Forest and MFCC feature extraction. Uncover intricate audio patterns for accurate genre categorization.",
    "https://github.com/sandiindika/4fun-abdul-aziz"
)

# row project 3
card_project(
    "./assets/projects/steganography.png",
    "Embark on a journey into the realm of covert communication with our Image-Based Steganography solution fortified with cryptographic protection.",
    "https://github.com/sandiindika/4fun-muhammad-rifqy",
    "./assets/projects/titanic.jpg",
    'Create a prediction model to answer the question, "What types of people are more likely to survive?" by employing passenger information (e.g., name, age, gender, socioeconomic status, etc.).',
    "https://www.kaggle.com/code/ndisan/titanic-survival-prediction-xgboost"
)

# row project 4
card_project(
    "./assets/projects/expert-system.png",
    "Expert System for Diagnosing Pregnant Women's Diseases Using the Forward Chaining and Certainty Factor Method",
    "https://github.com/sandiindika/4fun-AA2",
    "./assets/projects/rule-based.png",
    "Integration of a Rule-Based Expert System for Diagnosis of Diseases in Pregnant Women",
    "https://github.com/sandiindika/4fun-ACU"
)

# Footer
st.write("---")
col_footer = st.columns([1, 1])

with col_footer[0]:
    st.write("#### Links")
    st.markdown('''
        - [Blog](https://suryaeceran.hashnode.dev/)
        - [Datasets](https://www.kaggle.com/ndisan/datasets)
        - [Personal Site](https://sandidika.vercel.app/)
    ''')

with col_footer[1]:
    st.write("#### Contact Info")
    st.caption("Email: sandidikaputra@gmail.com")
ms_3()

st.markdown('<p class="label-footer">Made with <svg fill="#fff" viewBox="0 0 30 30" width="22" xmlns="http://www.w3.org/2000/svg" stroke="#fff"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"><path d="M20.808,11.079C19.829,16.132,12,20.5,12,20.5s-7.829-4.368-8.808-9.421C2.227,6.1,5.066,3.5,8,3.5a4.444,4.444,0,0,1,4,2,4.444,4.444,0,0,1,4-2C18.934,3.5,21.773,6.1,20.808,11.079Z"></path></g></svg></p>',
            unsafe_allow_html= True)