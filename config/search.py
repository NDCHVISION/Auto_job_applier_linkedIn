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

# Priority order: telehealth/virtual > locums > short-term/contract > clinical AI (bonus track)
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
    "Contract Family Medicine Physician",
    "Primary Care Physician Remote",
    "Urgent Care Physician Washington",
    "Physician Clinical AI",
    "Medical Director Telehealth"
]

search_location = "Washington, United States"

switch_number = 20

randomize_search_order = False     # False = priority order above

sort_by = "Most recent"
date_posted = "Past week"
salary = "$200,000+"               # Highest LinkedIn bracket; locums hourly not captured here

easy_apply_only = True

experience_level = ["Associate", "Mid-Senior level"]
job_type = ["Full-time", "Contract", "Temporary"]
on_site = ["Remote", "On-site", "Hybrid"]  # Remote=telehealth, On-site=locums

companies = []
location = []
industry = []
job_function = []
job_titles = []
benefits = []
commitments = []

under_10_applicants = False
in_your_network = False
fair_chance_employer = False

pause_after_filters = True

about_company_bad_words = []
about_company_good_words = []

# Filter out non-physician roles and irrelevant positions
bad_words = [
    "Nurse Practitioner", "NP only", "Physician Assistant", "PA only",
    "CRNA", "Registered Nurse", "RN required", "LCSW", "Therapist only",
    "Veterinarian", "Dentist", "Pharmacist", "Optometrist",
    "Software Engineer", "Data Scientist", "Developer",
    "Security Clearance required", "Must be US Citizen"
]

security_clearance = False

did_masters = True                 # MD counts; helps bot pass experience gates

# Residency July 2022–June 2025 + Sankofa Sept 2025–present = ~4 years clinical
current_experience = 4

############################################################################################################
