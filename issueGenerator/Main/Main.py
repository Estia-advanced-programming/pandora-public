'''
Created on 6 Mar 2020

@author: w.delamare
'''


import re
import os
import sys
import getopt

# https://pygithub.readthedocs.io/en/latest/introduction.html
from github import Github
from github.Milestone import Milestone
from github.Label import Label

from dotenv import load_dotenv

'''
To run the script outside Eclipse
(otherwise import pbms)
'''
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
os.chdir(SCRIPT_DIR)

from Resources import Data as d

#load_dotenv("../Resources/.env")


file_feature = None
dico_to_log = {}
output_json = "../TestFilesJSON/"
output_md = "../MDFiles/"



def DisplayMDMilestones(dico_to_log):

#     dico_nb = {}
#     for issue in d.issues:
#         if issue['milestone'] not in dico_nb:
#             dico_nb[issue['milestone']] = 0
#         dico_nb[issue['milestone']] += 1
#
#     s = ""
#     i = 0
#     for m in d.milestones:
#         s +=  "* " +m['title'] + "\n    * Description: " + m['description'] + "\n"
#         s += "    * Number of issues: " + str(dico_nb[i]) + "\n"
#         i += 1
#     print(s)
#
#
    s = ""

    for k,v in dico_to_log.items():
        m = d.milestones[d.mapping_milestones[str(k)]]
        s += "\n* **" + m['title'] + "**\n"
        s += "    * Description: " + m['description'] + "\n"
        s += "    * Number of features: " + str(len(v)) + "\n"
        s += "    * List:\n"
        for cur in v:
            s += "        * " + cur['name'] + " >> CLI option: " + cur['optionLine']
            s += " \n"
    f = open(output_md + "milestones.md", "a+")
    f.write(s)
    f.close()


def PrintHelp():
    print('python Main.py -t <git_token> -r <git_repo> [-v]')
    print("-t --token: mandatory (default: env variable)")
    print("-r --repo: mandatory (default: 'Estia-advanced-programming/weekendtest-team3'")
    print("v: verbose - optional (print Milestones in md format + test files json)")


# make sure we have the correct links between d.milestones and milestones from github
def GetMilestone(m_nb, milestones):
    m_title = d.milestones[m_nb]['title']
    for m in milestones:
        if m.title.find(m_title) != -1:
            return m
    # nothing found?
    print("A problem occured: could not find milestone " + m_nb)
    sys.exit(1)






# python Main.py -t <git_token> -r <git_repo> [-v]
def main(argv):
    git_token = ""
    git_repo = ""
    verbose = False

    try:
        opts, args = getopt.getopt(argv,"ht:r:v",["token=","repo="])
    except getopt.GetoptError:
        PrintHelp()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            PrintHelp()
            sys.exit()
        elif opt in ("-t", "--token"):
            git_token = arg
        elif opt in ("-r", "--repo"):
            git_repo = arg
        elif opt in ("-v",):
            verbose = True

    if len(git_repo) == 0:
        # this is running on a machine
        print("running on a machine")
        load_dotenv("../Resources/.env")
        git_token = os.getenv("GITHUB_TOKEN")
        git_repo = os.getenv("GITHUB_REPOSITORY")
        verbose = True

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

    gmilestones = repo.get_milestones(state='all')

    g_issues = repo.get_issues(state='all')

    i_names = []
    for gi in g_issues:
        i_names.append(gi.title)
        # TODO: manage to update issues (and re-open them if needed)

    for issue in d.issues:
        if issue['title'] not in i_names:
            val = repo.create_issue(title = issue['title'], body = issue['body'], milestone=GetMilestone(issue['milestone'], gmilestones), labels=issue['labels'])
            print("creating " + val.title)
        else:
            # update issue if the body has changed, and add the label 'modified'
            for gi in g_issues:
                if gi.title == issue['title'] and gi.body != issue['body']:
                    gi.edit(title = issue['title'], body = issue['body'], milestone=GetMilestone(issue['milestone'], gmilestones), labels=issue['labels'] + ['modified'], state='open')

        if verbose:
            optionLine = ""
            # "**CLI Output Name**: -o flightDuration\n\n"
            print(issue)
            tab = re.findall(re.compile("CLI Output Name.*?(\: .*?)\n", re.DOTALL), issue['body'])
            if len(tab) > 0:
                optionLine = tab[0]
            m_title = GetMilestone(issue['milestone'], gmilestones).title
            pos = int(m_title[m_title.find(' ')+1:m_title.find(":")])
            if pos not in dico_to_log:
                dico_to_log[pos] = []

            dico_to_log[pos].append({"name" : issue['title'], "optionLine":optionLine, "testFile": d.milestones[issue['milestone']]['file']})

    if verbose:
        for k,v in dico_to_log.items():
            print("create file for milestone " + str(k))
            f = open(output_json + "milestone_" + str(k), "w+")
            f.write(str(v))
            f.close()


    if verbose:
        DisplayMDMilestones(dico_to_log)


if __name__ == '__main__':
    main(sys.argv[1:])
