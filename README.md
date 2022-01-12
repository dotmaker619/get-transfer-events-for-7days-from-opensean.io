# Scrapping data from Google Sheets & etherscan.io to csv


## How To Use
1. Make sure you've already installed python and pip on your workspace.<br />
2. Install necessary modules with command 'pip install xxx'.

   For example:
   ```shell script
   pip install pandas
   ```
3. You will need chromedriver to run this script. Download [chromedriver](https://chromedriver.chromium.org/downloads) and place it with main.py.
4. Next, you need <b>client_secret.JSON</b> file to access to Google Sheets api.<br />
   You can download <b>client_secret.JSON</b> from the API Console, and authorize with the credential like this.
   ```shell script
     def getGSData() :
          scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
          creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
          client = gspread.authorize(creds)

          spreadsheets = client.open_by_url("Place google sheets url you want to access here")

          sheet1 = spreadsheets.sheet1
   ```
5. Finally, you can run this script with this command.
   ```shell script
   python main.py
   ```
   
Done! it will generate 'result.csv' file, and paste scrapping result to csv file. 😉
