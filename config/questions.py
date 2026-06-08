'''
Author:     Sai Vignesh Golla
LinkedIn:   https://www.linkedin.com/in/saivigneshgolla/

Copyright (C) 2024 Sai Vignesh Golla

License:    GNU Affero General Public License
            https://www.gnu.org/licenses/agpl-3.0.en.html
            
GitHub:     https://github.com/GodsScion/Auto_job_applier_linkedIn

version:    26.01.20.5.08
'''


###################################################### APPLICATION INPUTS ######################################################


# >>>>>>>>>>> Easy Apply Questions & Inputs <<<<<<<<<<<

# Resume path — update with your actual resume filename
default_resume_path = "all resumes/default/resume.pdf"

# Years of experience as a physician
years_of_experience = "2"          # 1-3 years post-residency

# Visa sponsorship
require_visa = "No"

# Portfolio / website
website = "https://www.linkedin.com/in/yawnkrumahmd/"

# LinkedIn profile
linkedIn = "https://www.linkedin.com/in/yawnkrumahmd/"

# Citizenship status
us_citizenship = "U.S. Citizen/Permanent Resident"


## COMPENSATION ##

# Annual salary for permanent/telehealth roles ($250k target)
desired_salary = 250000

# Current CTC — update if employed; 0 if between positions
current_ctc = 0

# Notice period — 0 = available immediately (ideal for locums)
notice_period = 0


# LinkedIn headline
linkedin_headline = "Family Medicine Physician | Telehealth & Virtual Care | Locum Tenens | Washington State"

# LinkedIn summary
linkedin_summary = """
Board-eligible Family Medicine physician with experience in primary care, preventive medicine, and chronic disease management. 
Passionate about expanding access to care through telehealth and virtual medicine. 
Currently seeking telehealth/virtual positions and locum tenens opportunities in Washington State, 
with openness to short-term and contract engagements while pursuing longer-term roles.
Committed to delivering high-quality, patient-centered care across diverse populations.
"""

# Cover letter
cover_letter = """
Dear Hiring Team,

I am a Family Medicine physician seeking telehealth, virtual care, and locum tenens opportunities in Washington State. 
I bring strong clinical training, adaptability across care settings, and a genuine commitment to accessible, high-quality patient care.

I am available for immediate start and am open to full-time, part-time, contract, and short-term engagements. 
I am particularly drawn to virtual and telehealth models that expand reach to underserved communities.

I look forward to the opportunity to contribute to your team.

Sincerely,
Dr. Yaw A. Nkrumah
"""

# Full background info used by AI to answer application questions
user_information_all = """
Name: Dr. Yaw A. Nkrumah, MD
Specialty: Family Medicine
Experience: 1-3 years post-residency
Location: Washington State
Interest: Telehealth/virtual care (primary), locum tenens (secondary), short-term/contract positions
LinkedIn: https://www.linkedin.com/in/yawnkrumahmd/
Citizenship: U.S. Citizen/Permanent Resident
Visa: No sponsorship needed
Board Status: Board-eligible/certified Family Medicine
Salary: $250,000 annual for permanent roles; $120-150/hr for locum tenens
Availability: Immediate
Languages: English
"""

# Most recent employer — update with your actual employer
recent_employer = "Update with your most recent employer"

# Confidence level (clinical competence)
confidence_level = "9"


# >>>>>>>>>>> RELATED SETTINGS <<<<<<<<<<<

# Pause before submitting each application to review
pause_before_submit = True

# Pause if a question can't be auto-answered
pause_at_failed_question = True

# Overwrite previously saved answers
overwrite_previous_answers = False


############################################################################################################
