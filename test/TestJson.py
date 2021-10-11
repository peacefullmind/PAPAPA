import pandas as pd

df='''
{
  "expand": "schema,names",
  "issues": [
    {
      "fields": {
        "issuetype": {
          "avatarId": 10300,
          "description": "",
          "id": "10005",
          "name": "New Feature",
          "subtask": False
        },
        "status": {
          "description": "A resolution has been taken, and it is awaiting verification by reporter. From here issues are either reopened, or are closed.",
          "id": "5",
          "name": "Resolved",
          "statusCategory": {
            "colorName": "green",
            "id": 3,
            "key": "done",
            "name": "Done",
          }
        },
        "summary": "Recovered data collection Defraglar $MFT problem"
      },
      "id": "11861",
      "key": "CAE-160",
    },
    {
      "fields": { 
... more issues],
  "maxResults": 5,
  "startAt": 0,
  "total": 160
}
'''
df = (
    df["fields"]
    .apply(pd.Series)
    .merge(df, left_index=True, right_index = True)
)