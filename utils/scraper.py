from jobspy import scrape_jobs


def scrape(search_term, results_wanted, hours_old, offset):
    jobs = scrape_jobs(
        site_name=["indeed","glassdoor"],
        search_term=search_term,
        location="United States",
        results_wanted=results_wanted,
        hours_old=hours_old, # (only Linkedin/Indeed is hour specific, others round up to days old)
        country_indeed='USA',  # only needed for indeed / glassdoor,
        linkedin_fetch_description=True,
        job_type="fulltime",
        offset=offset
    )
    print(f"Found {len(jobs)} jobs")
    print(jobs.head())
    if len(jobs) > results_wanted:
        return jobs[0:results_wanted]
