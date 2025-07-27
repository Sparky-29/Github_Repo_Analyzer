# GitHub Repository Analyzer

A clean and lightweight Flask application that allows users to visualize and explore the repositories of any public GitHub profile. Simply enter a username, and get a fully interactive dashboard with charts, tables, and trends—no browser extensions or authentication needed.

---

##  What It Does

The app fetches public repository data from GitHub’s REST API and presents it in a digestible, visual format:
- **Pie charts** showing language distribution across repositories
- **Bar charts** illustrating yearly repository creation trends
- **Data tables** showing repo names, descriptions, stars, forks, and timestamps

It also generates and stores data locally in CSV format for fast reloads and optional analysis.

---

## Why I Built It

This was my very first project done completely on my own, and I am super happy with it. I'm wanting to start looking for work so I wanted to create something for my Portfolio that I gravitated towards. Something that could be useful and simple to use for anybody from beginner programmers to professionals, and even for recruiters. A way to view either your own Github activity or somebody of interest, or the recruiters to view a candidate's project history at a quick glance.

This is also a project I’ve used to demonstrate:
- API integration with authentication-free public endpoints
- Data wrangling and cleaning
- Building interactive and polished visuals with **Plotly** and **Matplotlib**
- Web app deployment with **Flask** and **Bootstrap**

---

## Technologies Used

| Area               | Stack                            |
|--------------------|-----------------------------------|
| Backend            | Python, Flask                     |
| Frontend Styling   | Bootstrap (via Flask-Bootstrap)   |
| Charts & Graphs    | Plotly, Matplotlib                |
| Data Management    | Pandas, CSV                       |
| GitHub Integration | GitHub REST API                   |

---

## How It Works

### Step 1: Run the App

Make sure you have the necessary dependencies:

```bash
pip install requirements.txt
```

Start the development server:

```bash
python main.py
```

The app runs on `http://127.0.0.1:5000/`.

---

### Step 2: Enter a GitHub Username

Once on the homepage:
- Input any valid public GitHub username
- Hit submit
- The app fetches, processes, and stores repo data into `csv/username.csv`

---

### Step 3: Explore the Visuals

After submission, navigate to:
- `/charts/<username>` — for interactive charts
- `/table/<username>` — for an HTML table of repos

---

## Example Output

- **Pie Chart:** % of repositories by language
- **Bar Chart:** Number of repositories created per year
- **CSV File:** Saved locally for reuse and backup
- **HTML Table:** Interactive table of all repository metadata

---

## Design Decisions

- CSV files are used to avoid unnecessary re-fetching of data
- Missing fields like `language` are handled gracefully (`"Unknown"`)
- GitHub rate limits are respected with minimal API calls
- Static bar charts are saved to disk for fast rendering

---

## Future Enhancements

- OAuth login for private repo analysis
- Deployable via Docker or Render
- Add repository filtering by forks, stars, or language
- Extend visualization with timelines and contribution heatmaps

---

## License

This project is open-source and available under the [MIT License](LICENSE). Built for learning, experimenting, and showcasing development skills.

---

## Final Notes

This project reflects my approach to building tools that are both useful and elegant. It’s simple but robust, and easy to expand as needs evolve. If you’re a hiring manager, a fellow developer, or just curious—thanks for checking it out!

**Author:** Clark Allan  
**Contact:** [https://github.com/Sparky-29](https://github.com/Sparky-29)
