import numpy as np
import streamlit as st

from utils.filter import filter_jobs
from utils.highlight import highlight_words


class JobScraperApp:
    def __init__(self, data):
        self.filtered_df = filter_jobs(
            data,
            st.session_state.get("exclude_keywords", []),
            st.session_state.get("exclude_titles", []),
            st.session_state.get("exclude_companies", [])
        )
        self.current_job_index = st.session_state.get("current_job_index", 0)
        self.selected_jobs = st.session_state.get("selected_jobs", [])
        self.resumes = st.session_state.get("resume_names", ['Default Resume'])

    def show_jobs(self):
        if self.current_job_index < len(self.filtered_df):
            job = self.filtered_df[self.current_job_index]
            description, counts = highlight_words(job['description'], st.session_state.get("highlight_keywords", []))
            col1, col2 = st.columns([4, 1])
            with col1:
                st.subheader(job['title'])
                st.markdown(description, unsafe_allow_html=True)
            with col2:
                if job['location']:
                    st.write(job['location'])
                if job['min_amount'] and not np.isnan(job['min_amount']) and job['max_amount'] and not np.isnan(job['max_amount']):
                    st.write(f"{job['min_amount']} - ${job['max_amount']}")
                if job['company']:
                    st.write(job['company'])
                if job["job_url"]:
                    st.write(job["job_url"])
            st.sidebar.write(f"Remaining Jobs: {len(self.filtered_df) - self.current_job_index}")
            st.sidebar.write(f"Date Posted:{job['date_posted']}")
            st.sidebar.write(counts)
            if st.sidebar.button("Reject"):
                self.current_job_index += 1
                st.session_state["current_job_index"] = self.current_job_index
                st.rerun()
            for resume in self.resumes:
                if st.sidebar.button(resume):
                    self.current_job_index += 1
                    st.session_state["current_job_index"] = self.current_job_index
                    job["resume_type"] = resume
                    self.selected_jobs.append(job)
                    st.session_state["selected_jobs"] = self.selected_jobs
                    st.rerun()
        else:
            st.session_state["scraper_tab"] = False
            st.session_state["result_tab"] = True
            st.rerun()

def scraper_tab():
    data = st.session_state.get("data", {})
    if data is not None and len(data) > 0:
        app = JobScraperApp(data)
        app.show_jobs()
    else:
        st.write("No data available")

# def execute():
#     st.session_state["scraper_tab"] = True
#     st.session_state["result_tab"] = False
#     scraper_tab(data)
#
# if __name__ == '__main__':
#     data = {
#         'job_url': ['url1', 'url2', 'url3', 'url4'],
#         'title.txt': ['Lead Java Developer', 'React Developer', 'Backend Developer', 'Backend C++ Engineer'],
#         'description.txt': [
#             'Java Developer with 5 years of experience and Java skills',
#             'React Developer with 6+ years of experience and JavaScript skills',
#             'Backend Developer with Java and Python and Google Cloud Platform experience in scalable systems',
#             'Backend Engineer with Java and Python requesting API GATEWAY information and OOP and GCP skills and requires sponsorship'
#         ],
#         'min_amount': [24, 24, 24, 24],
#         'max_amount': [28, 28, 28, 24],
#         'interval': ["hour", "hour", "hour", "hour"],
#         'location': ['IA', 'IA', 'IA', 'IA'],
#         'company.txt': ["C2", "C2", "C3", "C4"]
#     }
#
#     if "result_tab" not in st.session_state:
#         st.session_state["result_tab"] = False
#
#     if st.session_state["result_tab"]:
#         result_tab(st.session_state["selected_jobs"])
#     else:
#         st.session_state["button_clicked"] = False
#         st.session_state["include_keywords_content"] = ["Java", "Kafka", "GCP"]
#         st.session_state["exclude_keywords_content"] = ["ing", "streaming"]
#         st.session_state["keywords_to_filter_title"] = ["Senior"]
#         st.session_state["keywords_to_filter_company"] = ["C1"]
#         st.session_state["resume_names"] = ["test"]
#         execute()
