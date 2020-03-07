'''
Created on 6 Mar 2020

@author: w.delamare
'''


import re
import os


from github import Github
from github.Milestone import Milestone
from github.Label import Label

from dotenv import load_dotenv

from Resources import Data as d

load_dotenv("../Resources/.env")

git_token = os.getenv("GIT_TOKEN")
git_repo = "Estia-advanced-programming/pandora-template"

file_feature = None
dico_to_log = {}
output_json = "../TestFilesJSON/"



def DisplayMDMilestones():
    
    dico_nb = {}
    for issue in d.issues:
        if issue['milestone'] not in dico_nb:
            dico_nb[issue['milestone']] = 0
        dico_nb[issue['milestone']] += 1
        
    s = ""
    i = 0
    for m in d.milestones:
        s += "* **Milestone "+ str(i) + "** : " + m['title'] + "\n    * Description: " + m['description'] + "\n"
        s += "    * Number of issues: " + str(dico_nb[i]) + "\n"
        i += 1
    print(s)
    
    
if __name__ == '__main__':
    
    DisplayMDMilestones()
    exit(0)
    
    g = Github(git_token)
    repo = g.get_repo(git_repo)
    
    for label in d.labels:
        try:
            repo.create_label(name = label["name"], color=label['color'], description="")
        except:
            pass
    labels = repo.get_labels()
    
    for milestone in d.milestones:
        try:
            repo.create_milestone(title = milestone['title'], state = milestone['state'], description = milestone['description'])   
        except:
            pass
    milestones = repo.get_milestones(state='open')
    
    g_issues = repo.get_issues()
    i_names = []
    for gi in g_issues:
        i_names.append(gi.title)

    for issue in d.issues:
        if issue['title'] not in i_names:
            val = repo.create_issue(title = issue['title'], body = issue['body'], milestone=milestones[issue['milestone']], labels=issue['labels'])
            print("creating " + val.title)
        
        optionLine = ""
        # "**CLI Output Name**: -o flightDuration\n\n"
        tab = re.findall(re.compile("CLI Output Name.*(\-o .*?)\s\s", re.DOTALL), issue['body'])
        if len(tab) > 0:
            optionLine = tab[0]
            if issue['milestone'] not in dico_to_log:
                dico_to_log[issue['milestone']] = []
            dico_to_log[issue['milestone']].append({"name" : issue['title'], "optionLine":optionLine, "testFile": d.milestones[issue['milestone']]['file']})
            
    for k,v in dico_to_log.items():
        print("create file for milestone " + str(k))
        f = open(output_json + "milestone_" + str(k), "w+")
        f.write(str(v))
        f.close()
        
        
    DisplayMDMilestones()