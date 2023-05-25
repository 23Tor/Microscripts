from simple_salesforce import Salesforce
import requests
import pandas as pd
import datetime
from io import StringIO
import openpyxl

# Date the report is created
now = datetime.datetime.now()
date_string = now.strftime("%Y_%m_%d")

# Salesforce instance
sf = Salesforce(
    username="user",
    password="pass",
    security_token="secret",
)
sf_instance = "https://yourdomain.my.salesforce.com/"

export = "?isdtp=p1&export=1&enc=UTF-8&xf=csv"  # export report csv

# Get the report
reportId = "the report id"
sfUrl = sf_instance + reportId + export
response = requests.get(sfUrl, headers=sf.headers, cookies={"sid": sf.session_id})

# Download report and save to folder
report_download = response.content.decode("utf-8")
report = pd.read_csv(StringIO(report_download))
report.to_excel(
    f"a/folder/or/shared/drive/path/reportname-{date_string}.xlsx",
    index=False,
)
