import os
import streamlit as st

from utils.path_utils import get_first_pdf_file_paths
from utils.pdf_to_text import pdf_to_text


def setup_tab():
    st.title("Setup")

    st.subheader("Search Parameters")
    search_term = st.text_input("Search Term", "Software Engineer Java")
    results_wanted = st.number_input("Number of jobs to filter", 10, 1000, 100)
    hours_old = st.number_input("Hours Old", 0, 100, 24)
    offset = st.number_input("Offset", 0, 1000, 0)

    st.sidebar.subheader("Filters and Resume Selection (Optional)")
    highlight_keywords_file = st.sidebar.file_uploader("Upload Highlight Keywords for Descriptions- (Give one keyword per line)", type="txt")
    exclude_keywords_file = st.sidebar.file_uploader("Upload Excluded Keywords for Descriptions ----(Give one keyword per line)", type="txt")
    exclude_titles_file = st.sidebar.file_uploader("Upload Excluded Keywords for Titles ------------(Give one keyword per line)", type="txt")
    exclude_companies_file = st.sidebar.file_uploader("Upload Exclude Keywords for Companies -------(Give one keyword per line)", type="txt")

    resume_names = []
    resume_data = {}
    x = 1
    while True:
        uploaded_file = st.sidebar.file_uploader("Choose your resume file -------------------------------", type=["pdf"], key=x)
        x = x + 1
        if uploaded_file is not None:
            resume_names.append(uploaded_file.name)
            resume_data[uploaded_file.name] = pdf_to_text(uploaded_file)
        else:
            break

    if st.button("Proceed to Scraper", disabled=not st.session_state["setup_tab"]):
        st.session_state["setup_tab"] = False
        st.session_state["scraper"] = True

        if highlight_keywords_file:
            st.session_state["highlight_keywords"] = highlight_keywords_file.read().decode("utf-8").splitlines()
        if exclude_keywords_file:
            st.session_state["exclude_keywords"] = exclude_keywords_file.read().decode("utf-8").splitlines()
        if exclude_titles_file:
            st.session_state["exclude_titles"] = exclude_titles_file.read().decode("utf-8").splitlines()
        if exclude_companies_file:
            st.session_state["exclude_companies"] = exclude_companies_file.read().decode("utf-8").splitlines()
        if len(resume_names) > 0:
            st.session_state["resume_data"] = resume_data
            st.session_state["resume_names"] = resume_names

        # setting up search
        st.session_state["search_term"] = search_term
        st.session_state["results_wanted"] = results_wanted
        st.session_state["hours_old"] = hours_old
        st.session_state["offset"] = offset

        st.rerun()

#         data = [
#             {"description.txt": """Cover Letter
# **Stefanini Group is hiring!****Stefanini is looking for Java Developer for Richardson, TX location (Onsite Role)****For quick Apply, please reach out to Akash Gupta- call: (248) 728-2603/ email:** **akash.kumar@stefanini.com****Open to W2 Candidates only!****Duties:*** Across Asset & Wealth Management, client helps empower clients and customers around the world to reach their financial goals.
# * Our advisor-led wealth management businesses provide financial planning, investment management, banking, and comprehensive advice to a wide range of clients, including ultra-high net worth and high net worth individuals, as well as family offices, foundations and endowments, and corporations and their employees.
# * Our direct-to-consumer business provides digital solutions that help customers save and invest.
# * Across Wealth Management, our growth is driven by a relentless focus on our people, our clients and customers, and leading-edge technology, data, and design.
#
#
#
#
#
#
#
# **Must haves Skill Set:****4+ years in the following:*** Java Development experience
# * Java 11+
# * Spring
# * Experience working with microservices architecture
# * Kafka for messaging
# * Strong understanding of SDLC
# * Gitlab
# * MongoDB
# * Test automation (JUnit, Mocking, Gherkin)
#
# **Education:*** Bachelor's Degree in Computer Science or related field, or equivalent work experience
#
# **Listed salary ranges may vary based on experience, qualifications, and local market. Also, some positions may include bonuses or other incentives.**
#
# Stefanini takes pride in hiring top talent and developing relationships with our future employees. Our talent acquisition teams will never make an offer of employment without having a phone conversation with you. Those face-to-face conversations will involve a description.txt of the job for which you have applied. We also speak with you about the process including interviews and job offers.
# **About Stefanini Group:**
# The Stefanini Group is a global provider of offshore, onshore and near shore outsourcing, IT digital consulting, systems integration, application, and strategic staffing services to Fortune 1000 enterprises around the world. Our presence is in countries like the Americas, Europe, Africa, and Asia, and more than four hundred clients across a broad spectrum of markets, including financial services, manufacturing, telecommunications, chemical services, technology, public sector, and utilities. Stefanini is a CMM level 5, IT consulting company.txt with a global presence. We are CMM Level 5 company.txt.
# """, "title.txt": "Job Title", "company.txt": "Company Name", "location": "Location",
#              "min_amount": 1000, "max_amount": 2000, "interval": "year", "job_url": "Job URL"}]
