import pandas as pd


def filter_jobs(data, keywords, keywords_to_filter_title, keywords_to_filter_company):
    df = pd.DataFrame(data)

    filtered_df = df[
        ~df['description'].apply(lambda x: isinstance(x, str) and any(keyword.lower() in x.lower() for keyword in keywords)) &
        ~df['title'].apply(lambda x: isinstance(x, str) and any(keyword.lower() in x.lower() for keyword in keywords_to_filter_title)) &
        ~df['company'].apply(lambda x: isinstance(x, str) and any(keyword.lower() in x.lower() for keyword in keywords_to_filter_company))
        ]
    return filtered_df.to_dict('records')


# data = {
#     'job_url': ['url1', 'url2', 'url3', 'url4'],
#     'title.txt': ['Lead Java Developer', 'React Developer', 'Backend Developer', 'Backend C++ Engineer'],
#     'description.txt': [
#         'Java Developer with 5 years of experience and Java skills',
#         'React Developer with 6+ years of experience and JavaScript skills',
#         'F Developer with Java and Python and Google Cloud Platform experienced in scalable',
#         'F Developer with Java and Python requesting API GATEWAY information and OOP and GCP scala and requires sponsorship'
#     ],
#     'min_amount': [24, 24, 24, 24],
#     'max_amount': [28, 28, 28, 24],
#     'interval': ["hour", "hour", "hour", "hour"],
#     'location': ['IA', 'IA', 'IA', 'IA'],
#     'company.txt': ["C1", "C1", "C1", "C1"]
# }
# keywords = ['5 years of experience', '5+years', '5+ years', 'Minimum of 5 years', '6 years of experience', '6+years', '6+ years', 'Minimum of 6 years', '7 years of experience', '7+years', '7+ years', 'Minimum of 7 years', '8 years of experience', '8+years', '8+ years', 'Minimum of 8 years', '9 years of experience', '9+years', '9+ years', 'Minimum of 9 years', '10 years of experience', '10+years', '10+ years', 'Minimum of 10 years', '11 years of experience', '11+years', '11+ years', 'Minimum of 11 years', '12 years of experience', '12+years', '12+ years', 'Minimum of 12 years', '13 years of experience', '13+years', '13+ years', 'Minimum of 13 years', '14 years of experience', '14+years', '14+ years', 'Minimum of 14 years', '15 years of experience', '15+years', '15+ years', 'Minimum of 15 years', 'clearance', 'React', 'angular', 'US citizen', 'GC Holder', 'full stack', 'QA Engineer', 'Cascading Style Sheets', 'Sr. Software Engineer', 'internship', 'without sponsorship', 'Seven (7) years experience', 'Korean fluently', 'embedded', 'speak Korean', 'PHP', 'part time', 'U.S. citizen', 'TS/SCI']
#
# filter_jobs(data, keywords, [], [] )