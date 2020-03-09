'''
Created on 6 Mar 2020

@author: w.delamare
'''



# https://pygithub.readthedocs.io/en/latest/github_objects/Label.html
labels = [
    {"name": 'reporting', "color": "f6fc1b"}
    , {"name": 'computing', "color": "eb44db"}
    , {"name": 'analysis', "color": "eba444"}
    , {"name":'input', "color": "1b61fc"}
    , {"name": 'output', "color": "17c462"}
    , {"name": 'error', "color": "ed1758"}
    ]


mapping_milestones = {
    "1" : 0
    , "2" : 1
    , "3": 2
    , "4": 3
    , "5": 4
    , "6": 5
    , "7": 6
    , "8": 7
    , "0": 8
    }


milestones = [
    {
        "title": "Milestone 1: Mono RU Flight Description",
        "state":'open',
        "description":"Provide basic descriptive summary data of a Russian fighter jet flight",
        "file": "mono"
    }
    ,
    {
        "title": "Milestone 2: Mono RU Cockpit Description",
        "state":'open',
        "description":"Provide basic descriptive summary data of a Russian cockpit during a flight",
        "file": "mono"
    }
    ,
    {
        "title": "Milestone 3: Mono RU Flight Computation",
        "state":'open',
        "description":"Provide simple computed data about a Russian jet flight",
        "file": "mono"
    }
    ,
    {
        "title": "Milestone 4: Mono RU Flight Analysis",
        "state":'open',
        "description":"Extract high-level information from data",
        "file": "mono"
    }
    ,
    {
        "title": "Milestone 5: File Handling",
        "state":'open',
        "description":"Handle batch option and US fighter jet files",
        "file": "mono"
    }
    ,
    {
        "title": "Milestone 6: Error Management",
        "state":'open',
        "description":"Handle Errors",
        "file": "all"
    }
    ,
    {
        "title": "Milestone 7: Multiple Flights Computations",
        "state":'open',
        "description":"Perform computations using multiple flights data",
        "file": "multi"
    }
    ,
    {
        "title": "Milestone 8: Multiple Flights Analysis",
        "state":'open',
        "description":"Extract high-level information about multiple flights",
        "file": "multi"
    }
    ,
    {
        "title": "Milestone 0: Initiation to Git",
        "state":'open',
        "description":"Learn about Git and the Pandora project",
        "file": "none"
    }
    ]

# https://pygithub.readthedocs.io/en/latest/github_objects/Issue.html
issues = [
	#region Initiation
    {
        "title": "Exercice 1: Project set up"
        , "body" : "" +
                   "# Description \n" +
                   "\n" +
                   "See the [wiki][wiki_Exercice1] to read more about this first exercice. \n" +
                   "\n" +
                   "# tasks : \n" +
                   "- [ ] Updated the readme to list your team members\n" +
                   "- [ ] Created a automated kanban project on github \n" +
                   "- [ ] Moved all issues from the Milestone Initiation to Git into todo\n" +
                   "- [ ] this Issue has been closed\n" +
                   "\n" +
                   "[wiki_Exercice1]: https://github.com/Estia-advanced-programming/pandora-public/wiki/Assignements»-Ex1\n"
        , "labels" : ['good first issue']
        , "milestone" : 8
    }
    ,{
        "title": "Exercice 2: Update team member information"
        , "body" :  "" +
                    "# Description \n" +
                    "\n" +
                    "In this exercice all member will edit the same file on their local repository to learn about conflict resolution. \n" +
                    "See the [wiki][wiki_Exercice2] to read more about this first exercice. \n" +
                    "\n" +
                    "# Tasks\n" +
                    "\n" +
                    "- [ ] Member1 has modified `README.md` and created a commit locally\n" +
                    "- [ ] Member2 has modified `README.md` and created a commit locally\n" +
                    "- [ ] Member3 has modified `README.md` and created a commit locally\n" +
                    "- [ ] Member1 has **push**ed their commit to the remote repository\n" +
                    "- [ ] Member2 and 3 \n" +
                    "      - have **Pull**ed the commit from member1\n" +
                    "      - have **Merg**ed the modification into their local repository\n" +
                    "      - have **Commit** the change locally \n" +
                    "- [ ] Member2  *push* their commit to the remote repository\n" +
                    "- [ ] Memberd3 \n" +
                    "      - has **Pull**ed the commit from member2\n" +
                    "      - has **Merg**ed the modification into their local repository\n" +
                    "      - has **Commit** the change locally \n" +
                    "- [ ] this Issue has been closed\n" +
                    "[wiki_Exercice2]: https://github.com/Estia-advanced-programming/pandora-public/wiki/Assignements»-Ex2\n"
        , "labels" : ['good first issue']
        , "milestone" : 8
    }
    ,{
        "title": "Exercice 3: Branch"
        , "body" :  "" +
                    "# Description \n" +
                    "\n" +
                    "In this exercice you learn to create a branch for commiting your change before integrating it with the other. \n" +
                    "\n" +
                    "# Tasks \n" +
                    "\n" +
                    "- [ ] Member 1 has created a `dev_member1` branch locally and commited some change to it \n" +
                    "- [ ] Member 2 has created a `dev_member2` branch locally and commited some change to it \n" +
                    "- [ ] Member 3 has created a `dev_member3` branch locally and commited some change to it \n" +
                    "* [ ] Member 1 has pushed its branch to the remote repository \n" +
                    "* [ ] Member 2 has pushed its branch to the remote repository \n" +
                    "* [ ] Member 3 has pushed its branch to the remote repository \n" +
                    "- [ ] Member 1 has created a pull request and linked this issue to the pull request\n" +
                    "- [ ] Member 2 has created a pull request and linked this issue to the pull request\n" +
                    "- [ ] Member 3 has created a pull request and linked this issue to the pull request\n" +
                    "* [ ] Member 2 and 3 comment on Member 1 pull request, \n" +
                    "    - if the change is accepted, Merge the branch into master.  \n" +
                    "* [ ] Member 2 pull request has been discussed\n" +
                    "    - If there are conflicts, resolve them online, \n" +
                    "    - if the change is accepted, Merge the branch into master.  \n" +
                    "* [ ] Member 3 pull request has been discussed\n" +
                    "    - If there are conflicts pull the change locally, merge them into `dev_member3`, push the new commit, and continue commenting and modifying until the pull request is accepted. \n" +
                    "    - if the change is accepted, Merge the branch into master.  \n" +
                    "- [ ] The issue have been closed\n" +
                    "[wiki_Exercice3]: https://github.com/Estia-advanced-programming/pandora-public/wiki/Assignements»-Ex3\n"
        , "labels" : ['good first issue']
        , "milestone" : 8
    }
    #endregion
	#region milestone 0 Mono RU Flight Description

    ,{
        "title": "Average Altitude"
        , "body" : "" +
                "**CLI Output Name**: -o avgAlt\n\n" +
                "**Input**: a flight record file\n\n" +
                "**Print**: the average altitude (m) during the flight\n"
        , "labels" : ['reporting']
        , "milestone" : 0
    }
    ,{
        "title": "Max Altitude"
        , "body" : ""+
                "**CLI Output Name**: -o maxAlt\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the maximum altitude (m) during the flight\n"
        , "labels" : ['reporting']
        , "milestone" : 0
    }
    ,{
        "title": "Average Air Speed"
        , "body" : ""+
                "**CLI Output Name**: -o avgAirSpeed\n\n"
                "**Input**: a flight record file\n\n"
                "**Print**: the average air speed (m/s) during the flight\n"
        , "labels" : ['reporting']
        , "milestone" : 0
    }
    ,{
        "title": "Max Air Speed"
        , "body" : ""+
                "**CLI Output Name**: -o maxAirSpeed\n\n"
                "**Input**: a flight record file\n\n"+
                "**Print**: the maximum air speed (m/s) during the flight\n\n"
        , "labels" : ['reporting']
        , "milestone" : 0
    }
    ,{
        "title": "Average Engine Power"
        , "body" : ""+
                "**CLI Output Name**: -o avgEnginePower\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the average total engine power (W) during the flight\n"
        , "labels" : ['reporting']
        , "milestone" : 0
    }
    ,{
        "title": "Max Engine Power"
        , "body" : ""+
                "**CLI Output Name**: -o maxEnginePower\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the maximum total engine power (W) during the flight\n"
        , "labels" : ['reporting']
        , "milestone" : 0
    }
    ,{
        "title": "Milestone 0 Full Report"
        , "body" : ""+
                "**Description**: Without any option, the program outputs every milestone 0's issues at once.\n"+
                "feature_cli_name:value\n"+
                "One feature per line (ordered alphabetically)\n"
        , "labels" : ['output']
        , "milestone" : 0
    }

    #endregion



    #region milestone 1 Mono RU Cockpit Description

    ,{
        "title": "Average Temperature"
        , "body" : ""+
                "**CLI Output Name**: -o avgTemp\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the average temperature in the cockpit (℃) during the flight\n"
        , "labels" : ['reporting']
        , "milestone" : 1
    }
    ,{
        "title": "Min Temperature"
        , "body" : ""
                "**CLI Output Name**: -o minTemp\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the minimum temperature in the cockpit (℃) during the flight\n"
        , "labels" : ['reporting']
        , "milestone" : 1
    }
    ,{
        "title": "Max Temperature"
        , "body" : ""+
                "**CLI Output Name**: -o avgTemp\n\n"
                "**Input**: a flight record file\n\n"
                "**Print**: the maximum temperature in the cockpit (℃) during the flight\n"
        , "labels" : ['reporting']
        , "milestone" : 1
    }
    ,{
        "title": "Average Pressure"
        , "body" : ""+
                "**CLI Output Name**: -o avgPressure\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the average pressure in the cockpit (Pa) during the flight\n"
        , "labels" : ['reporting']
        , "milestone" : 1
    }
    ,{
        "title": "Max Pressure"
        , "body" : ""+
                "**CLI Output Name**: -o maxPressure\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the maximum pressure in the cockpit (Pa) during the flight\n"
        , "labels" : ['reporting']
        , "milestone" : 1
    }
    ,{
        "title": "Minimum Pressure"
        , "body" : ""+
                "**CLI Output Name**: -o minPressure\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the minimum pressure in the cockpit (Pa) during the flight\n"
        , "labels" : ['reporting']
        , "milestone" : 1
    }
    ,{
        "title": "Average Relative Humidity"
        , "body" : ""+
                "**CLI Output Name**: -o avgHumidity\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the average relative humidity in the cockpit (%) during the flight\n"
        , "labels" : ['reporting']
        , "milestone" : 1
    }
    ,{
        "title": "Max Relative Humidity"
        , "body" : ""+
                "**CLI Output Name**: -o maxHumidity\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the maximum relative humidity in the cockpit (%) during the flight\n"
        , "labels" : ['reporting']
        , "milestone" : 1
    }
    ,{
        "title": "Min Relative Humidity"
        , "body" : ""+
                "**CLI Output Name**: -o minHumidity\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the minimum relative humidity in the cockpit (%) during the flight\n"
        , "labels" : ['reporting']
        , "milestone" : 1
    }
    ,{
        "title": "Average Heart Rate"
        , "body" : ""+
                "**CLI Output Name**: -o avgHeartRate\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the average pilot's heart rate (bpm) during the flight\n"
        , "labels" : ['reporting']
        , "milestone" : 1
    }
    ,{
        "title": "Max Heart Rate"
        , "body" : ""+
                "**CLI Output Name**: -o maxHeartRate\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the maximum pilot's heart rate (bpm) during the flight\n"
        , "labels" : ['reporting']
        , "milestone" : 1
    }
    ,{
        "title": "Min Heart Rate"
        , "body" : ""+
                "**CLI Output Name**: -o minHeartRate\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the minimum pilot's heart rate (bpm) during the flight\n"
        , "labels" : ['reporting']
        , "milestone" : 1
    }
    ,{
        "title": "Average Oxygen Concentration"
        , "body" : ""+
                "**CLI Output Name**: -o avgOxygen\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the average oxygen concentration (%) delivered by the pilot's mask during the flight\n"
        , "labels" : ['reporting']
        , "milestone" : 1
    }
    ,{
        "title": "Min Oxygen Concentration"
        , "body" : ""+
                "**CLI Output Name**: -o minOxygen\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the minimum oxygen concentration (%) delivered by the pilot's mask during the flight\n"
        , "labels" : ['reporting']
        , "milestone" : 1
    }
    ,{
        "title": "Max Oxygen Concentration"
        , "body" : ""+
                "**CLI Output Name**: -o maxOxygen\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the maximum oxygen concentration (%) delivered by the pilot's mask during the flight\n"
        , "labels" : ['reporting']
        , "milestone" : 1
    }
    ,{
        "title": "Milestone 1 Full Report"
        , "body" : ""+
                "**Description**: Without any option, the program outputs every milestone 1's issues at once.\n"+
                "feature_cli_name:value\n"+
                "One feature per line (ordered alphabetically)\n"
        , "labels" : ['output']
        , "milestone" : 1
    }

    #endregion


    #region milestone 2 Mono RU Flight Computation
    ,{
        "title": "Flight Duration"
        , "body" : ""+
                "**CLI Output Name**: -o flightDuration\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the flight duration (HH:mm:ss)\n"
        , "labels" : ['computing']
        , "milestone" : 2
    }
    ,{
        "title": "Flight Distance"
        , "body" : ""+
                "**CLI Output Name**: -o flightDistance\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the total flight distance (km)\n"
        , "labels" : ['computing']
        , "milestone" : 2
    }
    ,{
        "title": "Average Acceleration"
        , "body" : ""+
                "**CLI Output Name**: -o avgAcceleration\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the average acceleration (m/s^2) during the flight\n"
        , "labels" : ['computing']
        , "milestone" : 2
    }
    ,{
        "title": "Max Acceleration"
        , "body" : ""+
                "**CLI Output Name**: -o maxAcceleration\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the maximum acceleration (m/s^2) during the flight\n"
        , "labels" : ['computing']
        , "milestone" : 2
    }
    ,{
        "title": "Wind Speed"
        , "body" : ""+
                "**CLI Output Name**: -o windSpeed\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the average wind speed (m/s) during the flight\n"
        , "labels" : ['computing']
        , "milestone" : 2
    }
    ,{
        "title": "Average Mach Speed"
        , "body" : ""+
                "**CLI Output Name**: -o avgMachSpeed\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the average speed in Mach during the flight\n"
        , "labels" : ['computing']
        , "milestone" : 2
    }
    ,{
        "title": "Max Mach Speed"
        , "body" : ""+
                "**CLI Output Name**: -o maxMachSpeed\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the maximum speed in Mach during the flight\n"
        , "labels" : ['computing']
        , "milestone" : 2
    }
    ,{
        "title": "Max Acceleration in G"
        , "body" : ""+
                "**CLI Output Name**: -o maxAccelG\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the maximum acceleration in G during the flight\n"
        , "labels" : ['computing']
        , "milestone" : 2
    }
    ,{
        "title": "Milestone 2 Full Report"
        , "body" : ""+
                "**Description**: Without any option, the program outputs every milestone 2's issues at once.\n"+
                "feature_cli_name:value\n"+
                "One feature per line (ordered alphabetically)\n"
        , "labels" : ['output']
        , "milestone" : 2
    }

    #endregion


    #region milestone 3 Mono RU Flight Analysis
    ,{
        "title": "Take Off Phase Detection"
        , "body" : ""+
                "**CLI Output Name**: -o takeOff\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the start and end time of the take off phase: start=HH:mm:ss / end=HH:mm:ss\n"
        , "labels" : ['analysis']
        , "milestone" : 3
    }
    ,{
        "title": "Cruise Phase Detection"
        , "body" : ""+
                "**CLI Output Name**: -o cruise\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the start and end time of the cruise phase: start=HH:mm:ss / end=HH:mm:ss\n"
        , "labels" : ['analysis']
        , "milestone" : 3
    }
    ,{
        "title": "Landing Phase Detection"
        , "body" : ""+
                "**CLI Output Name**: -o landing\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the start and end time of the landing phase: start=HH:mm:ss / end=HH:mm:ss\n"
        , "labels" : ['analysis']
        , "milestone" : 3
    }
    ,{
        "title": "Ratio Distance"
        , "body" : ""+
                "**CLI Output Name**: -o ratioDistance\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the ratio between the distance actually done and the point-to-point distance between the take off and landing\n"
        , "labels" : ['analysis']
        , "milestone" : 3
    }



    ,{
        "title": "Average Air Speed (Take Off)"
        , "body" : ""+
                "**CLI Output Name**: -o avgAirSpeedTakeOff\n\n"
                "**Input**: a flight record file\n\n"
                "**Print**: the average air speed (m/s) during the take off phase\n"
        , "labels" : ['analysis']
        , "milestone" : 3
    }
    ,{
        "title": "Max Air Speed (Take Off)"
        , "body" : ""+
                "**CLI Output Name**: -o maxAirSpeedTakeOff\n\n"
                "**Input**: a flight record file\n\n"+
                "**Print**: the maximum air speed (m/s) during the take off phase\n\n"
        , "labels" : ['analysis']
        , "milestone" : 3
    }
    ,{
        "title": "Average Engine Power (Take Off)"
        , "body" : ""+
                "**CLI Output Name**: -o avgEnginePowerTakeOff\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the average total engine power (W) during the take off phase\n"
        , "labels" : ['analysis']
        , "milestone" : 3
    }
    ,{
        "title": "Max Engine Power (Take Off)"
        , "body" : ""+
                "**CLI Output Name**: -o maxEnginePowerTakeOff\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the maximum total engine power (W) during the take off phase\n"
        , "labels" : ['analysis']
        , "milestone" : 3
    }

    ,{
        "title": "Average Air Speed (Cruise)"
        , "body" : ""+
                "**CLI Output Name**: -o avgAirSpeedCruise\n\n"
                "**Input**: a flight record file\n\n"
                "**Print**: the average air speed (m/s) during the cruise phase\n"
        , "labels" : ['analysis']
        , "milestone" : 3
    }
    ,{
        "title": "Max Air Speed (Cruise)"
        , "body" : ""+
                "**CLI Output Name**: -o maxAirSpeedCruise\n\n"
                "**Input**: a flight record file\n\n"+
                "**Print**: the maximum air speed (m/s) during the cruise phase\n\n"
        , "labels" : ['analysis']
        , "milestone" : 3
    }
    ,{
        "title": "Average Engine Power (Cruise)"
        , "body" : ""+
                "**CLI Output Name**: -o avgEnginePowerCruise\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the average total engine power (W) during the cruise phase\n"
        , "labels" : ['analysis']
        , "milestone" : 3
    }
    ,{
        "title": "Max Engine Power (Cruise)"
        , "body" : ""+
                "**CLI Output Name**: -o maxEnginePowerCruise\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the maximum total engine power (W) during the cruise phase\n"
        , "labels" : ['analysis']
        , "milestone" : 3
    }


    ,{
        "title": "Average Air Speed (Landing)"
        , "body" : ""+
                "**CLI Output Name**: -o avgAirSpeedLanding\n\n"
                "**Input**: a flight record file\n\n"
                "**Print**: the average air speed (m/s) during the landing phase\n"
        , "labels" : ['analysis']
        , "milestone" : 3
    }
    ,{
        "title": "Max Air Speed (Landing)"
        , "body" : ""+
                "**CLI Output Name**: -o maxAirSpeedLanding\n\n"
                "**Input**: a flight record file\n\n"+
                "**Print**: the maximum air speed (m/s) during the landing phase\n\n"
        , "labels" : ['analysis']
        , "milestone" : 3
    }
    ,{
        "title": "Average Engine Power (Landing)"
        , "body" : ""+
                "**CLI Output Name**: -o avgEnginePowerLanding\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the average total engine power (W) during the landing phase\n"
        , "labels" : ['analysis']
        , "milestone" : 3
    }
    ,{
        "title": "Max Engine Power (Landing)"
        , "body" : ""+
                "**CLI Output Name**: -o maxEnginePowerLanding\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the maximum total engine power (W) during the landing phase\n"
        , "labels" : ['analysis']
        , "milestone" : 3
    }




    ,{
        "title": "Flight Distance (Take Off)"
        , "body" : ""+
                "**CLI Output Name**: -o flightDistanceTakeOff\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the total flight distance (km) during the take off phase\n"
        , "labels" : ['analysis']
        , "milestone" : 3
    }
    ,{
        "title": "Average Acceleration (Take Off)"
        , "body" : ""+
                "**CLI Output Name**: -o avgAccelerationTakeOff\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the average acceleration (m/s^2) during the take off phase\n"
        , "labels" : ['analysis']
        , "milestone" : 3
    }
    ,{
        "title": "Max Acceleration (Take Off)"
        , "body" : ""+
                "**CLI Output Name**: -o maxAccelerationTakeOff\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the maximum acceleration (m/s^2) during the take off phase\n"
        , "labels" : ['analysis']
        , "milestone" : 3
    }
    ,{
        "title": "Wind Speed (Take Off)"
        , "body" : ""+
                "**CLI Output Name**: -o windSpeedTakeOff\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the average wind speed (m/s) during the take off phase\n"
        , "labels" : ['analysis']
        , "milestone" : 3
    }


    ,{
        "title": "Flight Distance (Cruise)"
        , "body" : ""+
                "**CLI Output Name**: -o flightDistanceCruise\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the total flight distance (km) during the cruise phase\n"
        , "labels" : ['analysis']
        , "milestone" : 3
    }
    ,{
        "title": "Average Acceleration (Cruise)"
        , "body" : ""+
                "**CLI Output Name**: -o avgAccelerationCruise\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the average acceleration (m/s^2) during the cruise phase\n"
        , "labels" : ['analysis']
        , "milestone" : 3
    }
    ,{
        "title": "Max Acceleration (Cruise)"
        , "body" : ""+
                "**CLI Output Name**: -o maxAccelerationCruise\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the maximum acceleration (m/s^2) during the cruise phase\n"
        , "labels" : ['analysis']
        , "milestone" : 3
    }
    ,{
        "title": "Wind Speed (Cruise)"
        , "body" : ""+
                "**CLI Output Name**: -o windSpeedCruise\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the average wind speed (m/s) during the cruise phase\n"
        , "labels" : ['analysis']
        , "milestone" : 3
    }


    ,{
        "title": "Flight Distance (Landing)"
        , "body" : ""+
                "**CLI Output Name**: -o flightDistanceLanding\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the total flight distance (km) during the landing phase\n"
        , "labels" : ['analysis']
        , "milestone" : 3
    }
    ,{
        "title": "Average Acceleration (Landing)"
        , "body" : ""+
                "**CLI Output Name**: -o avgAccelerationLanding\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the average acceleration (m/s^2) during the landing phase\n"
        , "labels" : ['analysis']
        , "milestone" : 3
    }
    ,{
        "title": "Max Acceleration (Landing)"
        , "body" : ""+
                "**CLI Output Name**: -o maxAccelerationLanding\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the maximum acceleration (m/s^2) during the landing phase\n"
        , "labels" : ['analysis']
        , "milestone" : 3
    }
    ,{
        "title": "Wind Speed (Landing)"
        , "body" : ""+
                "**CLI Output Name**: -o windSpeedLanding\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the average wind speed (m/s) during the landing phase\n"
        , "labels" : ['analysis']
        , "milestone" : 3
    }


    ,{
        "title": "Most Demanding Phase - Engine Power"
        , "body" : ""+
                "**CLI Output Name**: -o mostPowerPhase\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the name of the phase which required the most average engine power: phase_name:Power (W)\n"
        , "labels" : ['analysis']
        , "milestone" : 3
    }

    ,{
        "title": "Most Demanding Phase - Stress"
        , "body" : ""+
                "**CLI Output Name**: -o mostStressPhase\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the name of the phase which provoked the highest average heart rate: phase_name:heart_beat (bpm)\n"
        , "labels" : ['analysis']
        , "milestone" : 3
    }

    ,{
        "title": "Most Demanding Phase - Horizontal Acceleration"
        , "body" : ""+
                "**CLI Output Name**: -o mostAccelPhase\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the name of the phase with the highest average horizontal acceleration: phase_name:acceleration (m/s^2)\n"
        , "labels" : ['analysis']
        , "milestone" : 3
    }

    ,{
        "title": "Reaching 80% Max Altitude"
        , "body" : ""+
                "**CLI Output Name**: -o reachAlt\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the time it took the jet to reach 80% of its maximum altitude during the flight: time (min) / max_altitude (m)\n"
        , "labels" : ['analysis']
        , "milestone" : 3
    }

    ,{
        "title": "Reaching 80% Total Distance"
        , "body" : ""+
                "**CLI Output Name**: -o reachDist\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the time it took the jet to arrive at 80% of its total flight distance: time (min) / total_distance (km)\n"
        , "labels" : ['analysis']
        , "milestone" : 3
    }

    ,{
        "title": "Altitude with Fastest Wind"
        , "body" : ""+
                "**CLI Output Name**: -o fastWindAlt\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the altitude with the fastest wind outside the aircraft over a period of 5min: altitude (m): avg_5min_wind_speed (m/s)\n"
        , "labels" : ['analysis']
        , "milestone" : 3
    }

    ,{
        "title": "Altitude with Highest Aircraft Speed"
        , "body" : ""+
                "**CLI Output Name**: -o fastJetAlt\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: the altitude at which the jet had its fastest speed over a time window of 5min: altitude (m): avg_5min_jet_speed (m/s)\n"
        , "labels" : ['analysis']
        , "milestone" : 3
    }

    ,{
        "title": "Noise of Temperature Sensors"
        , "body" : ""+
                "**CLI Output Name**: -o noiseTemp\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: Assuming an average temperature set to 25℃, get the average noise in the temperature data: noise_value (℃)\n"
        , "labels" : ['analysis']
        , "milestone" : 3
    }

    ,{
        "title": "Stressed Pilot"
        , "body" : ""+
                "**CLI Output Name**: -o stressedPilot\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: Did the pilot had a stress attack: y/n\n"
        , "labels" : ['analysis']
        , "milestone" : 3
    }

    ,{
        "title": "50% Oxygen Phase"
        , "body" : ""+
                "**CLI Output Name**: -o oxygenPhase\n\n"+
                "**Input**: a flight record file\n\n"+
                "**Print**: Which phase required more than 50% oxygen concentration in the mask: phase_name\n"
        , "labels" : ['analysis']
        , "milestone" : 3
    }
    ,{
        "title": "Milestone 3 Full Report"
        , "body" : ""+
                "**Description**: Without any option, the program outputs every milestone 3's issues at once.\n"+
                "feature_cli_name:value\n"+
                "One feature per line (ordered alphabetically)\n"
        , "labels" : ['output']
        , "milestone" : 3
    }

    #endregion

    #region milestone 4 File Handling
    ,{
        "title": "US files Parser"
        , "body" : "**Description**: The program needs to handle both Russian and American files\n\n"
        , "labels" : ['input']
        , "milestone" : 4
    }
    ,{
        "title": "Mono US Flight Description"
        , "body" : "**Description**: Make sure your functionalities from the milestone 0 'Mono RU Flight Description' are working on US files and still working with RU files.\n\n"
        , "labels" : ['input']
        , "milestone" : 4
    }
    ,{
        "title": "Mono US Cockpit Description"
        , "body" : "**Description**: Make sure your functionalities from the milestone 1 'Mono RU Cockpit Description' are working on US files and still working with RU files.\n\n"
        , "labels" : ['input']
        , "milestone" : 4
    }
    ,{
        "title": "Mono US Flight Computation"
        , "body" : "**Description**: Make sure your functionalities from the milestone 2 'Mono RU Flight Computation' are working on US files and still working with RU files.\n\n"
        , "labels" : ['input']
        , "milestone" : 4
    }
    ,{
        "title": "Mono US Flight Analysis"
        , "body" : "**Description**: Make sure your functionalities from the milestone 3 'Mono RU Flight Analysis' are working on US files and still working with RU files.\n\n"
        , "labels" : ['input']
        , "milestone" : 4
    }
    ,{
        "title": "Batch  Option"
        , "body" : ''+
            "**Description**: Instead of giving multiple file names in the parameter of the program, manage the **--batch** (or **-b**) option to give a folder (e.g., --batch testFilesMilestone1/)."+
            "The program will then run on each files individually in **alphabetical order**.\n\n"
            "**Example**: The test/ folder contains 4 files. When running the program with '-o avgALT -b test', the output will be\n"+
            "value1\n"+
            "value2\n"+
            "value3\n"+
            "value4\n"
        , "labels" : ['input']
        , "milestone" : 4
    }
    #endregion

    #region milestone 5 Error Management
    ,{
        "title": "Invalid Command Line Options"
        , "body" : ""+
            "**Description**: An option (-x or --xxxx) is not recognized\n\n"+
            "**Output**: ERROR: Invalid Options -x (or --xxxx) is not recognized"
        , "labels" : ['error']
        , "milestone" : 5
    }
    ,{
        "title": "Missing Command Line Parameters"
        , "body" : ""+
            "**Description**: An option requires missing parameters (e.g., -o missing the feature identifier)\n\n"+
            "**Output**: ERROR: Invalid Options -x (or --xxxx) is missing a parameter"
        , "labels" : ['error']
        , "milestone" : 5
    }
    ,{
        "title": "Not Implemented Handling"
        , "body" : ""+
            "**Description**: If an output is not implemented by the program\n\n"+
            "**Output**: ERROR: Invalid Options -x (or --xxxx) has not been implemented yet"
        , "labels" : ['error']
        , "milestone" : 5
    }
    ,{
        "title": "Missing Files"
        , "body" : ""+
            "**Description**: File(s) given as input are not found\n\n"+
            "**Output**: ERROR: MISSING_FILE - file1 file2 file3 (in alphabetical order)"
        , "labels" : ['error']
        , "milestone" : 5
    }
    ,{
        "title": "Encoding Problems"
        , "body" : ""+
            "**Description**: File(s) given as input are not correctly encoded\n\n"+
            "**Output**: ERROR: ENCODING - file1 file2 file3 (in alphabetical order)"
        , "labels" : ['error']
        , "milestone" : 5
    }
    ,{
        "title": "Corrupted Files"
        , "body" : ""+
            "**Description**: Files cannot be open because of incorrect binary data\n\n"+
            "**Output**: ERROR: CORRUPTED - file1 file2 file3 (in alphabetical order)"
        , "labels" : ['error']
        , "milestone" : 5
    }
    ,{
        "title": "Missing Header"
        , "body" : ""+
            "**Description**: Files have no header information\n\n"+
            "**Output**: ERROR: MISSING_HEADER - file1 file2 file3 (in alphabetical order)"
        , "labels" : ['error']
        , "milestone" : 5
    }
    ,{
        "title": "Incomplete Header"
        , "body" : ""+
            "**Description**: The header is missing some information\n\n"+
            "**Output**: ERROR: INCOMPLETE_HEADER - file1=[info1,info2] file2=[info3] file3=[info4] (in alphabetical order)"
        , "labels" : ['error']
        , "milestone" : 5
    }
    ,{
        "title": "Missing Columns"
        , "body" : ""+
            "**Description**: Some required columns are not in the file\n\n"+
            "**Output**: ERROR: MISSING_COLUMNS - file1=[col_name1,col_name2] file2=[col_name3] (in alphabetical order)"
        , "labels" : ['error']
        , "milestone" : 5
    }
    ,{
        "title": "Missing Column Names"
        , "body" : ""+
            "**Description**: The file does not contain the column names\n\n"+
            "**Output**: ERROR: MISSING_COLNAMES - file1 file2 (in alphabetical order)"
        , "labels" : ['error']
        , "milestone" : 5
    }
    ,{
        "title": "Incorrect Timestamp Ordering"
        , "body" : ""+
            "**Description**: The log file is not presenting data lines in a timely ordered way\n\n"+
            "**Output**: ERROR: ORDERING - file1 file2 file3 (in alphabetical order)"
        , "labels" : ['error']
        , "milestone" : 5
    }
    ,{
        "title": "Incorrect Input"
        , "body" : ""+
            "**Description**: The input (file(s) or folder(s)) is not the one expected\n\n"+
            "**Output**: ERROR: INPUT_ERROR - input_name1 input_name2 (in alphabetical order)"
        , "labels" : ['error']
        , "milestone" : 5
    }
    ,{
        "title": "Milestone 5 Full Report"
        , "body" : ""+
                "**Description**: Without any option, the program outputs every milestone 5's issues at once.\n"+
                "feature_cli_name:value\n"+
                "One feature per line (ordered alphabetically)\n"
        , "labels" : ['output']
        , "milestone" : 5
    }
    #endregion

    #region milestone 6 Multiple Flights Computations
    ,{
        "title": "Total Cumulative Flight Duration"
        , "body" : ""+
                "**CLI Output Name**: -o cumulDuration\n\n"+
                "**Input**: a folder name containing flight record file(s)\n\n"+
                "**Print**: the cumulative flight duration (HH:mm:ss)\n"
        , "labels" : ['computing']
        , "milestone" : 6
    }
    ,{
        "title": "Total Cumulative Flight Distance"
        , "body" : ""+
                "**CLI Output Name**: -o cumulDistance\n\n"+
                "**Input**: a folder name containing flight record file(s)\n\n"+
                "**Print**: the cumulative flight distance (km)\n"
        , "labels" : ['computing']
        , "milestone" : 6
    }
    ,{
        "title": "Most Used Airport (Take Off)"
        , "body" : ""+
                "**CLI Output Name**: -o airportTakeOff\n\n"+
                "**Input**: a folder name containing flight record file(s)\n\n"+
                "**Print**: the name of the airport most often used for take off\n"
        , "labels" : ['computing']
        , "milestone" : 6
    }
    ,{
        "title": "Most Used Airport (Landing)"
        , "body" : ""+
                "**CLI Output Name**: -o airportLanding\n\n"+
                "**Input**: a folder name containing flight record file(s)\n\n"+
                "**Print**: the name of the airport most often used for Landing\n"
        , "labels" : ['computing']
        , "milestone" : 6
    }
    ,{
        "title": "Highest Drag Coef"
        , "body" : ""+
                "**CLI Output Name**: -o highestDrag\n\n"+
                "**Input**: a folder name containing flight record file(s)\n\n"+
                "**Print**: the id of the fighter jet with the highest drag coefficient: jet_id:drag_coef\n"
        , "labels" : ['computing']
        , "milestone" : 6
    }
    ,{
        "title": "Smallest Drag Coef"
        , "body" : ""+
                "**CLI Output Name**: -o smallestDrag\n\n"+
                "**Input**: a folder name containing flight record file(s)\n\n"+
                "**Print**: the id of the fighter jet with the smallest drag coefficient: jet_id:drag_coef\n"
        , "labels" : ['computing']
        , "milestone" : 6
    }
    ,{
        "title": "Highest Lift Coef"
        , "body" : ""+
                "**CLI Output Name**: -o highestLift\n\n"+
                "**Input**: a folder name containing flight record file(s)\n\n"+
                "**Print**: the id of the fighter jet with the highest lift coefficient: jet_id:drag_coef\n"
        , "labels" : ['computing']
        , "milestone" : 6
    }
    ,{
        "title": "Smallest Lift Coef"
        , "body" : ""+
                "**CLI Output Name**: -o smallestLift\n\n"+
                "**Input**: a folder name containing flight record file(s)\n\n"+
                "**Print**: the id of the fighter jet with the smallest lift coefficient: jet_id:drag_coef\n"
        , "labels" : ['computing']
        , "milestone" : 6
    }
    ,{
        "title": "Highest Average Speed"
        , "body" : ""+
                "**CLI Output Name**: -o highestSpeed\n\n"+
                "**Input**: a folder name containing flight record file(s)\n\n"+
                "**Print**: the id of the fighter jet which had the fastest average speed during its flight: jet_id:speed (km/h)\n"
        , "labels" : ['computing']
        , "milestone" : 6
    }
    ,{
        "title": "Slowest Average Speed"
        , "body" : ""+
                "**CLI Output Name**: -o slowestSpeed\n\n"+
                "**Input**: a folder name containing flight record file(s)\n\n"+
                "**Print**: the id of the fighter jet which had the slowest average speed during its flight: jet_id:speed (km/h)\n"
        , "labels" : ['computing']
        , "milestone" : 6
    }
    ,{
        "title": "Highest Altitude"
        , "body" : ""+
                "**CLI Output Name**: -o highestAltitude\n\n"+
                "**Input**: a folder name containing flight record file(s)\n\n"+
                "**Print**: the id of the fighter jet which flew the highest: jet_id:max_altitude (m)\n"
        , "labels" : ['computing']
        , "milestone" : 6
    }
    ,{
        "title": "Longest Flight Duration"
        , "body" : ""+
                "**CLI Output Name**: -o longestDuration\n\n"+
                "**Input**: a folder name containing flight record file(s)\n\n"+
                "**Print**: the id of the fighter jet which flew the longest: jet_id:duration (HH:mm:ss)\n"
        , "labels" : ['computing']
        , "milestone" : 6
    }
    ,{
        "title": "First Landing"
        , "body" : ""+
                "**CLI Output Name**: -o firstLanding\n\n"+
                "**Input**: a folder name containing flight record file(s)\n\n"+
                "**Print**: the id of the fighter jet which landed first: jet_id:airport_name:landing_time(HH:mm:ss)\n"
        , "labels" : ['computing']
        , "milestone" : 6
    }
    ,{
        "title": "Last Landing"
        , "body" : ""+
                "**CLI Output Name**: -o lastLanding\n\n"+
                "**Input**: a folder name containing flight record file(s)\n\n"+
                "**Print**: the id of the fighter jet which landed last: jet_id:airport_name:landing_time(HH:mm:ss)\n"
        , "labels" : ['computing']
        , "milestone" : 6
    }
    ,{
        "title": "Highest Average Engine Power"
        , "body" : ""+
                "**CLI Output Name**: -o highestPower\n\n"+
                "**Input**: a folder name containing flight record file(s)\n\n"+
                "**Print**: the id of the fighter jet which used the highest engine power: jet_id:power (w)\n"
        , "labels" : ['computing']
        , "milestone" : 6
    }
    ,{
        "title": "Highest Average Oxygen"
        , "body" : ""+
                "**CLI Output Name**: -o highestOxygen\n\n"+
                "**Input**: a folder name containing flight record file(s)\n\n"+
                "**Print**: the id of the fighter jet which used the highest average oxygen concentration: jet_id:oxygen (%)\n"
        , "labels" : ['computing']
        , "milestone" : 6
    }
    ,{
        "title": "Highest Average Heart Beat"
        , "body" : ""+
                "**CLI Output Name**: -o highestHeartBeat\n\n"+
                "**Input**: a folder name containing flight record file(s)\n\n"+
                "**Print**: the id of the fighter jet whose pilot had the highest average heart beat: jet_id:beat (bpm)\n"
        , "labels" : ['computing']
        , "milestone" : 6
    }
    ,{
        "title": "Lowest Average Heart Beat"
        , "body" : ""+
                "**CLI Output Name**: -o lowestHeartBeat\n\n"+
                "**Input**: a folder name containing flight record file(s)\n\n"+
                "**Print**: the id of the fighter jet whose pilot had the lowest average heart beat: jet_id:beat (bpm)\n"
        , "labels" : ['computing']
        , "milestone" : 6
    }
    ,{
        "title": "Milestone 6 Full Report"
        , "body" : ""+
                "**Description**: Without any option, the program outputs every milestone 6's issues at once.\n"+
                "feature_cli_name:value\n"+
                "One feature per line (ordered alphabetically)\n"
        , "labels" : ['output']
        , "milestone" : 6
    }

    #endregion

    #region milestone 7 Multiple Flights Analysis
    ,{
        "title": "Flight Closeness "
        , "body" : ""+
                "**CLI Output Name**: -o closeFlight\n\n"+
                "**Input**: a folder name containing flight record file(s)\n\n"+
                "**Print**: A list of jet id who flew less than 50km from each others: "+
                "\n[jet_id1, jet_id2]:min_distance (km)\n"+
                "[jet_id1, jet_id3]:min_distance (km)\netc (alphabetical order)"
        , "labels" : ['analysis']
        , "milestone" : 7
    }
    ,{
        "title": "Flight Closeness (Same origin)"
        , "body" : ""+
                "**CLI Output Name**: -o closeFlightSameOri\n\n"+
                "**Input**: a folder name containing flight record file(s)\n\n"+
                "**Print**: A list of jet id who flew less than 50km from each others and are from the same origin (US/RU): "+
                "\n[jet_id1, jet_id2]:min_distance (km)\n"+
                "[jet_id1, jet_id3]:min_distance (km)\netc (alphabetical order)"
        , "labels" : ['analysis']
        , "milestone" : 7
    }
    ,{
        "title": "Flight Closeness (Different origin)"
        , "body" : ""+
                "**CLI Output Name**: -o closeFlightDiffOri\n\n"+
                "**Input**: a folder name containing flight record file(s)\n\n"+
                "**Print**: A list of jet id who flew less than 50km from each others and are from different origins (US/RU): "+
                "\n[jet_id1, jet_id2]:min_distance (km)\n"+
                "[jet_id1, jet_id3]:min_distance (km)\netc (alphabetical order)"
        , "labels" : ['analysis']
        , "milestone" : 7
    }
    ,{
        "title": "Milestone 7 Full Report"
        , "body" : ""+
                "**Description**: Without any option, the program outputs every milestone 7's issues at once.\n"+
                "feature_cli_name:value\n"+
                "One feature per line (ordered alphabetically)\n"
        , "labels" : ['output']
        , "milestone" : 7
    }
    #endregion
    ]
