import requests
from dotenv import load_dotenv
import os

load_dotenv()

# Your GitHub access token
headers = {"Authorization": os.getenv("AUTH_TOKEN")}


def run_query(q):
    """
    Run the graphql query to fetch contribution data from GitHub API
    :param q: The query to be run
    :return: The contribution data in JSON format
    """
    request = requests.post('https://api.github.com/graphql',
                            json={'query': q.format(
                                username=os.getenv("GIT_USER"))},
                            headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run...")


# The graphql query
query = """
{{ 
  user(login: "{username}"){{
    contributionsCollection {{
      contributionCalendar {{
        totalContributions
        weeks {{
          contributionDays {{
            contributionCount
            date
          }}
        }}
      }}
    }}
  }}
}}
"""


def find_last_contribution():
    """
    Find the date of the last contribution
    :return: The date in string format
    """
    result = run_query(query)
    weeks = \
        result["data"]["user"]["contributionsCollection"][
            "contributionCalendar"]["weeks"]
    contributions = weeks[len(weeks) - 1]["contributionDays"]

    for contribution in list(reversed(contributions)):
        if contribution["contributionCount"] > 0:
            return contribution["date"]
