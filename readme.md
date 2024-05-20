# JobSculptor

JobSculptor is a Streamlit application designed to assist job seekers in efficiently managing their job applications by scraping and filtering job descriptions. It provides a readable interface for reviewing these descriptions, enabling users to select the right resume for each job. Additionally, it allows users to generate personalized cover letters using OpenAI's API and save them for further reference.

## Features

- **Job Description Analysis**: Scrapes job descriptions from Glassdoor and Indeed to identify key requirements.
- **Resume Selection**: Allows users to select the best-fitting resume for each job description.
- **Cover Letter Generation**: Uses OpenAI's API to generate personalized cover letters based on the selected resume and job description.
- **Job Tracking**: Tracks the jobs users have applied for and allows exporting the data as a CSV file.

## Installation

To install JobSculptor, clone the repository and install the required dependencies.

```bash
git clone https://github.com/utkuaysev/JobSculptor.git
cd JobSculptor
pip install -r requirements.txt
```

## Usage

To run the JobSculptor Streamlit application, follow these steps:

**Run the Application**:
    ```bash
    streamlit run main.py
    ```

### Scraping Phase


1. **Setup Scraper and Filters**:
    - Configure the scraper and filter parameters.


2.  **Scrape Job Descriptions**:
    - Use the application to scrape job descriptions from Glassdoor and Indeed based on your preferences.
    - Review the scraped jobs and either select the best-fitting resume or reject them.

### Results Phase

1. **Review Accepted Jobs**:
    - View the list of jobs you have accepted.
    - Generate personalized cover letters for each job using the OpenAI API.
    - Download the results as a CSV file for further tracking.

## Project Structure

- `data/`: Contains data files used by the application.
- `genai/`: Contains the scripts used for generating ai-written cover letter.
- `gui/`: Contains the Streamlit GUI components.
- `style/`: Contains styling files.
- `utils/`: Contains utility scripts.
- `main.py`: The main entry point for the Streamlit application.
- `requirements.txt`: Lists the dependencies required to run the application.

## Contributing

We welcome contributions! Please follow these steps to contribute:

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or further assistance, please contact utkuaysev@gmail.com.

---