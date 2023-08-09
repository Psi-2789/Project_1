#Installation

Clone this repository to your local machine using:
git clone https://github.com/your-username/netflix-automation.git

Install the required Python packages using:
pip install -r requirements.txt

#Usage

Replace the placeholders in the script with your own Netflix login credentials:
mail.send_keys("your-email@example.com")
password.send_keys("your-password")


#Run the script using the following command:
python netflix_ui_automation.py

The script will open the Netflix website, search for the term "netflix," log into the account, and print the duration of a movie.


#Script Details:
The script uses the Selenium library to automate web interactions. It utilizes Chrome as the browser and the ChromeDriverManager to manage the WebDriver.

#It performs the following steps:

1. Opens the Google website and searches for "netflix."
2. Clicks on the Netflix link.
3. Logs into the Netflix account using the provided email and password.
4. Navigates to a movie's page and extracts its duration.


