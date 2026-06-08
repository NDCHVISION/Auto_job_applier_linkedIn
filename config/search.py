'''
Author:     Sai Vignesh Golla
LinkedIn:   https://www.linkedin.com/in/saivigneshgolla/

Copyright (C) 2024 Sai Vignesh Golla

License:    GNU Affero General Public License
            https://www.gnu.org/licenses/agpl-3.0.en.html
            
GitHub:     https://github.com/GodsScion/Auto_job_applier_linkedIn

version:    26.01.20.5.08
'''


###################################################### LINKEDIN SEARCH PREFERENCES ######################################################

# Search terms ordered by priority: telehealth first, then locums, then short-term/contract
search_terms = [
    "Telehealth Family Medicine Physician",
    "Telemedicine Physician",
    "Virtual Care Physician",
    "Remote Family Medicine Physician",
    "Telehealth Primary Care Physician",
    "Locum Tenens Family Medicine",
    "Locum Tenens Physician Washington",
    "Locum Family Physician",
    "Family Medicine Physician Washington",
    "Primary Care Physician Remote",
    "Contract Family Medicine Physician",
    "Urgent Care Physician Washington"
]

# Washington state — covers telehealth based in WA and locum positions in WA
search_location = "Washington, United States"

# After how many applications per search term should the bot switch to next?
switch_number = 20                 # Keep lower so all search terms get coverage

# Randomize search order?
randomize_search_order = False     # False = priority order above


# >>>>>>>>>>> Job Search Filters <<<<<<<<<<<

sort_by = "Most recent"            # "Most recent", "Most relevant" or ""
date_posted = "Past week"          # "Any time", "Past month", "Past week", "Past 24 hours"
salary = "$200,000+"               # Closest LinkedIn bracket to physician compensation

easy_apply_only = True             # True or False

experience_level = ["Associate", "Mid-Senior level"]   # 1-3 years post-residency
job_type = ["Full-time", "Contract", "Temporary"]       # Covers perm, locums, and short-term
on_site = ["Remote", "On-site", "Hybrid"]               # Remote for telehealth, on-site for locums

companies = []                     # Leave open — don't restrict to specific employers
location = []                      # Covered by search_location above
industry = []
job_function = []
job_titles = []
benefits = []
commitments = []

under_10_applicants = False
in_your_network = False
fair_chance_employer = False


## >>>>>>>>>>> RELATED SETTING <<<<<<<<<<<
pause_after_filters = True         # Pause to review results before applying


## >>>>>>>>>>> SKIP IRRELEVANT JOBS <<<<<<<<<<<

# Skip staffing companies that post generic listings without real jobs
about_company_bad_words = []

about_company_good_words = []

# Skip jobs clearly not for physicians
bad_words = [
    "Nurse Practitioner", "NP only", "Physician Assistant", "PA only",
    "CRNA", "Registered Nurse", "RN required",
    "Veterinarian", "Dentist", "Pharmacist",
    "Software Engineer", "Developer", "Data Scientist",
    "Security Clearance", "US Citizen required"
]

security_clearance = False

# MD = doctorate level; did_masters = True helps with experience-gating logic
did_masters = True

# 1-3 years post-residency; set to 2 as midpoint. Bot skips jobs requiring > current_experience + 2
current_experience = 2


############################################################################################################
