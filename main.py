import requests
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from flask_bootstrap import Bootstrap
from flask import Flask, render_template, request, session
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
Bootstrap(app)

#* Creating the routes for HTML report.
@app.route("/", methods=["GET", "POST"])
def home():
    
    # username = ""
        
    if request.method == "POST":
        username = request.form.get("username")
    elif request.method == "GET":
        username = request.args.get("username")
    
    if username:

        #* Creating CSV
        try:
            with open (f"csv/{username}.csv", "r") as file:
                file.read()
        
        except FileNotFoundError:
            with open (f"csv/{username}.csv", "w") as file:
                file.write("repo_name,description,url,forks,stars,language,creation_date,last_update")
        
        def get_repos(username):
            
            url = f"https://api.github.com/users/{username}/repos"
            params = {"per_page": 100,
                    "rel": "next"}
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()

        df = pd.read_csv(f"csv/{username}.csv")

        #* Receiving the repos
        for repos in get_repos(username):
            repo_name = repos["name"]
            description = repos["description"]
            url = repos["html_url"]
            forks = repos["forks"]
            stars = repos["stargazers_count"]
            language = repos["language"]
            start_date = repos["created_at"]
            updates = []
            updates.append(repos["updated_at"])
            previous = updates[-1]
            
            first = dt.datetime.strptime(start_date, "%Y-%m-%dT%H:%M:%SZ")
            creation_date = first.strftime("%B %d, %Y")
            last = dt.datetime.strptime(previous, "%Y-%m-%dT%H:%M:%SZ")
            last_update = last.strftime("%B %d, %Y")
            
            if repo_name in df["repo_name"].values:
                continue
            else:
                df.loc[len(df)] = [repo_name, 
                                description, 
                                url, forks, 
                                stars, language, 
                                creation_date, 
                                last_update]
                
        #* Creating the directories
        df.to_csv(f"csv/{username}.csv", index=False)
        
        return render_template("index.html", username=username)
    

    return render_template("index.html")

@app.route("/charts/<username>", methods=["GET", "POST"])
def charts(username):
    
    username = username
        
    df = pd.read_csv(f"csv/{username}.csv")
    #* Pie chart of number of repositories per language
    fig = px.pie(labels=df["language"].value_counts().index, 
                values=df["language"].value_counts(), 
                title="Percentages of Languages Used",
                names=df["language"].value_counts().index,)

    fig.update_traces(textinfo='label+percent', textposition='outside')
    pie_html = fig.to_html(full_html=False, include_plotlyjs="cdn")

    #* Bar chart of number of repositories per year
    for col in df.columns:
        if col == "creation_date":
            df[col] = pd.to_datetime(df[col])
            df[col] = df[col].dt.strftime("%Y")
            
        if col == "language":
            df[col] = df[col].fillna("Unknown")
            

    plt.figure(figsize=(10, 8))
    plt.barh(df["creation_date"].value_counts().index, df["creation_date"].value_counts())
    plt.xlabel("Number of repositories")
    plt.ylabel("Year")
    plt.title("Number of repositories per year")
    plt.savefig(f"static/{username}_bar_chart.png")
    bar_chart = f"{username}_bar_chart.png"
    return render_template("charts.html", pie_html=pie_html, bar_chart=bar_chart, username=username)

@app.route("/table/<username>", methods=["GET", "POST"])
def table(username):
    
    username = username
    
    df = pd.read_csv(f"csv/{username}.csv")
    df.to_html(f"templates/{username}.html")
    table = f"{username}.html"
    return render_template("table.html", table=table, username=username)


#* Running the app
if __name__ == "__main__":
    app.run(debug=True)