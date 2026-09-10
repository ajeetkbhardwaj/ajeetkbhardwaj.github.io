import urllib.request
import json
import os
import re
import glob
import argparse
from datetime import datetime

PROJECT_DIR = "_portfolio"

# Create _portfolio directory if it doesn't exist
os.makedirs(PROJECT_DIR, exist_ok=True)

MARKER_START = "<!-- AUTO-TEAM-START -->"
MARKER_END = "<!-- AUTO-TEAM-END -->"

def main():
    parser = argparse.ArgumentParser(description="Auto-update team from a GitHub repository")
    parser.add_argument("--repo", default="ajeetkbhardwaj/automlresearch", help="GitHub repo URL or owner/repo")
    args = parser.parse_args()

    # Extract owner/repo from URL if needed
    repo = args.repo.replace("https://github.com/", "").replace("http://github.com/", "").strip("/")
    api_url = f"https://api.github.com/repos/{repo}/contributors"
    safe_repo = repo.replace("/", "-")
    
    today = datetime.now().strftime("%Y-%m-%d")

    # Find existing project file to avoid creating a new one every time the date changes
    existing_project_files = [f for f in glob.glob(f"{PROJECT_DIR}/*{safe_repo}.md") if "-auto-" not in f]
    if existing_project_files:
        team_file_path = existing_project_files[0]
    else:
        team_file_path = os.path.join(PROJECT_DIR, f"{today}-{safe_repo}.md")

    try:
        # Fetch contributors from GitHub API
        headers = {'User-Agent': 'Mozilla/5.0'}
        if "GITHUB_TOKEN" in os.environ:
            headers['Authorization'] = f"Bearer {os.environ['GITHUB_TOKEN']}"
        req = urllib.request.Request(api_url, headers=headers)
        with urllib.request.urlopen(req) as response:
            contributors = json.loads(response.read().decode())
            
        # Clean up old individual files so they don't duplicate
        for f in glob.glob(f"{PROJECT_DIR}/*-auto-{safe_repo}-*.md"):
            try:
                os.remove(f)
            except:
                pass

        # Build the team list markdown
        team_snippet = f"{MARKER_START}\n## 👥 Team Roster for `{repo}`\n\n"
        leader_snippet = ""
        members_snippet = ""

        for user in contributors:
            username = user.get("login")
            profile_url = user.get("html_url")
            contributions = user.get("contributions")
            avatar_url = user.get("avatar_url")
            
            list_item = f"<img src='{avatar_url}?s=50' width='25' style='border-radius:50%; vertical-align:middle'/> **{username}** ({contributions} commits)\n"
            
            if username.lower() == repo.split('/')[0].lower():
                leader_snippet += f"* **👑 Team Leader:**\n  * {list_item}"
            else:
                members_snippet += f"  * {list_item}"

        if members_snippet:
            members_snippet = f"* **👨‍💻 Team Members:**\n{members_snippet}"
            
        team_snippet += leader_snippet + members_snippet + f"\n{MARKER_END}"

        # Check if the project file already exists
        if os.path.exists(team_file_path):
            with open(team_file_path, "r") as f:
                content = f.read()
                
            # If markers exist, replace everything between them
            if MARKER_START in content and MARKER_END in content:
                content = re.sub(f"{MARKER_START}.*?{MARKER_END}", team_snippet, content, flags=re.DOTALL)
            else:
                # Otherwise, append to the end
                content += f"\n\n{team_snippet}\n"
                
            with open(team_file_path, "w") as f:
                f.write(content)
            print(f"Updated existing project file: {team_file_path}")
            
        else:
            # Create a brand new project file with the weekly update template
            new_content = f"""---
title: "{repo} Project"
collection: portfolio
date: {today}
excerpt: "Team updates and project details for {repo}"
---

## 🎯 Project Overview
**Project Aim:** [Briefly describe the goal of the project]  
**Project Span:** [Start Date] — [End Date]

{team_snippet}

---
## 📅 Weekly Plan & Updates
*Write your weekly plan, problems tackled, and achievements here. The automated script will never overwrite this text!*

### 👑 Team Leader Update
* **Solved:** [What did you solve?]

### 👨‍💻 Team Member Updates
* **Solved:** [What did the team solve?]
"""
            with open(team_file_path, "w") as f:
                f.write(new_content)
            print(f"Created new project file: {team_file_path}")
                
        print(f"Successfully generated team profiles for {len(contributors)} contributors from {repo}.")
        
    except Exception as e:
        print(f"Error fetching contributors for {repo}: {e}")

if __name__ == "__main__":
    main()