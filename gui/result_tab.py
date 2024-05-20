import string
import random
import pandas as pd
import streamlit as st

from genai.cover_letter_generator import generate_cover_letter
from style.custom_button import get_custom_button
from utils.date_utils import get_current_date


def get_cover_letter(title, company, description, resume, tokens, api_key):
    with st.spinner("Generating Cover Letter..."):
        return generate_cover_letter(title, company, description, resume, tokens, api_key)


def result_tab():
    if st.session_state.get("cover_letter") is None:
        st.session_state["cover_letter"] = {}
    data = st.session_state.get("selected_jobs", [])
    st.title("Result")
    data_table = pd.DataFrame(data)

    col1, col2, col3 = st.columns([8, 12, 12])

    columns_to_keep = [
        'company', 'location', 'job_type', 'date_posted',
        'min_amount', 'max_amount', 'is_remote', 'emails', 'description', 'resume_type'
    ]

    # Filter the DataFrame to only include the specified columns
    if data_table is not None and len(data_table) > 0:
        filtered_df = data_table[columns_to_keep]
    else:
        return st.write("No data to show")

    with col2:
        upload_merge_download(filtered_df)
    with col3:
        st.download_button('Download As CSV File', filtered_df.to_csv(), str(get_current_date()) + "_result.csv",
                           'text/csv', key='download-csv')

    st.sidebar.header("Cover letter generator parameters")
    api_key = st.sidebar.text_input("Open AI API key", type="password", key="openai_api_key")
    tokens = st.sidebar.number_input("Number of tokens to generate", min_value=10, max_value=1000, value=400, step=10,
                                     key="num_tokens")

    # Create a DataFrame for the user table

    # Display user table with interactive buttons
    colms = st.columns((20, 100, 50, 90, 90, 90))
    fields = ["№", 'Company', 'Resume Type', 'Link', 'Cover Letter']
    for col, field_name in zip(colms, fields):
        col.write(field_name)

    for x in range(len(data_table)):
        col1, col2, col3, col4, col5, col6 = st.columns((1, 100, 50, 90, 90, 90))
        col1.write(x + 1)  # index
        col2.write(data_table['company'][x])
        col3.write(data_table['resume_type'][x])
        col4.write(data_table['job_url'][x])
        cover_letter_phold = col5.empty()
        cover_letter_download_phold = col6.empty()
        cover_letter_phold.markdown(get_custom_button(), unsafe_allow_html=True)
        cover_letter_download_phold.markdown(get_custom_button(), unsafe_allow_html=True)
        if cover_letter_phold.button("Generate", key=x):
            resume_data = st.session_state["resume_data"][data_table['resume_type'][x]] \
                if st.session_state.get("resume_data") is not None else ''
            st.session_state["cover_letter"][x] = get_cover_letter(data_table['title'][x], data_table['company'][x],
                                                                   data_table['description'][x],
                                                                   resume_data,
                                                                   api_key, tokens)
        if x in st.session_state["cover_letter"]:
            cover_letter_download_phold.download_button(key=str(x) + "_download", label="Download",
                                                        file_name=f"{data_table['company'][x]}.txt",
                                                        data=st.session_state["cover_letter"][x])


def upload_merge_download(data_table):
    # Step 1: File uploader
    uploaded_file = st.file_uploader("Merge With Another CSV file", type="csv")

    if uploaded_file is not None:
        # Step 2: Read the uploaded CSV file
        df = pd.read_csv(uploaded_file)

        merged_df = pd.concat([df, data_table], ignore_index=True)

        # Step 5: Convert the merged DataFrame to CSV
        @st.cache_data
        def convert_df_to_csv(dataframe):
            return dataframe.to_csv(index=False).encode('utf-8')

        csv = convert_df_to_csv(merged_df)

        # Step 6: Provide download button for the merged CSV file
        st.download_button(
            label="Download merged CSV",
            data=csv,
            file_name='merged_file.csv',
            mime='text/csv',
        )


if __name__ == '__main__':
    def generate_random_address():
        random_string = ''.join(random.choices(string.ascii_lowercase, k=5))
        return f"{random_string}@example.com"


    data = {
        "company": ''.join(random.choices(string.ascii_letters + string.digits, k=10)),
        "id": [random.randint(100, 9999) for _ in range(20)],
        "location": [random.choice([True, False]) for _ in range(20)],
        "price": [random.choice([True, False]) for _ in range(20)],
        "title": ''.join(random.choices(string.ascii_letters + string.digits, k=10)),
        "min_amount": [random.choice([True, False]) for _ in range(20)],
        "max_amount": [random.choice([True, False]) for _ in range(20)],
        "resume_type": [random.choice([True, False]) for _ in range(20)],
        "job_url": [generate_random_address() for _ in range(20)],
        "description": ''.join(random.choices(string.ascii_letters + string.digits, k=10)),
        "job_type": [random.choice(["Full-time", "Part-time", "Internship"]) for _ in range(20)],
        "date_posted": [random.choice(["Today", "Yesterday", "Last Week"]) for _ in range(20)],
        "is_remote": [random.choice([True, False]) for _ in range(20)],
        "emails": [generate_random_address() for _ in range(20)]
    }
    st.session_state["selected_jobs"] = data
    st.session_state["resumes_data"] = {True: "resume1.txt", False: "resume2.txt"}
    result_tab()
