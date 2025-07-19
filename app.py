from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# Personal information
personal_info = {
    "name": "Janon DUKUZUMUREMYI",
    "email": "janon3030@gmail.com",
    "phone": "0733695764 / 0786003139",
    "address": "Nyamata-Bugesera",
    "dob": "1999/12/20",
    "nationality": "Rwandan",
    "marital_status": "Single",
    "gender": "Male",
    "profile": "Looking for an exciting and dynamic role where I can utilize my skills and experience to drive tangible results. Passionate about joining an organization that fosters a culture of innovation, continuous learning, and personal growth."
}

# Professional experience
experiences = [
    {
        "period": "2023 – 2023",
        "position": "Academic Intern",
        "company": "Nyamata Level Teaching Hospital",
        "description": "I have done internship at Nyamata L2 Teaching Hospital in department of Data Management and have highly Trained About HMIS, CVRS and MCH."
    },
    {
        "period": "2023 – 2024",
        "position": "Data Analysis Graduate",
        "company": "ICT CHAMBER And HANGA Hub Rwanda",
        "description": "I have gained a lot of skills in data analysis in Theoretical and Practical with high performance."
    },
    {
        "period": "2020 – 2024",
        "location": "Kigali, Rwanda",
        "position": "Enumerator",
        "company": "NISR and MINALOC Rwanda",
        "description": "I worked as Enumerator in Data collection in charge of NISR and MINALOC, and Currently working as Enumerator in NISR (Temporary)."
    },
    {
        "period": "2023 – present",
        "location": "Nyamata-Bugesera",
        "position": "Commissioner of Media and Public Relations in NYC (Nyamata sector)",
        "company": "Nyamata Sector",
        "description": "I am Youth volunteer at position of Commissioner of Media and Public Relations in NYC (Nyamata sector)"
    },
    {
        "period": "2023 – present",
        "position": "Chairperson of Youth in RPF",
        "company": "Kayumba cell",
        "description": ""
    }
]

# Education
education = [
    {
        "period": "2021 – 2023",
        "location": "Kigali, Rwanda",
        "degree": "Bachelor degree A0",
        "institution": "University of Rwanda",
        "description": "I have acquired bachelor degree in Applied statistics in Demography from University of Rwanda."
    },
    {
        "period": "2017 – 2019",
        "location": "Kigali, Rwanda",
        "degree": "Secondary Diploma",
        "institution": "Es: Kanombe/EFOTEC",
        "description": "I have acquired Secondary Diploma in option of Mathematics Physics and computer science."
    },
    {
        "period": "2014 – 2016",
        "degree": "Ordinary Level",
        "institution": "Gs.Saint Joseph de Kabgayi",
        "description": ""
    }
]

# Skills
skills = {
    "left": [
        "HMIS, MRS, OPEN-MRS CRVs",
        "QuickBooks",
        "Data Collection tools (Google form, Kobotool box, Microsoft form)"
    ],
    "right": [
        "Data Analysis",
        "Microsoft Office",
        "Statistical Softwares (Python, Power Bi, Stata, SPSS, R-Programming)"
    ]
}

# Languages
languages = [
    {"name": "English", "level": "Proficient (EF Set C2)"},
    {"name": "Kinyarwanda", "level": "Native"}
]

# Interests
interests = [
    "Volunteering",
    "Playing Football",
    "Learning Languages"
]

# References
references = [
    {
        "name": "NGARAMBE Jean Paul",
        "position": "Chief of Accountant",
        "company": "Nyamata L2 Teaching Hospital",
        "contact": "0785200012"
    },
    {
        "name": "Didier NDABANA",
        "position": "Data Manager",
        "company": "Nyamata Level 2 Teaching Hospital",
        "contact": "0788615463"
    },
    {
        "name": "Callixte NGIRUWONSANGA",
        "position": "System Admin Specialist",
        "company": "MINEDUC",
        "contact": "callixten@gmail.com, 0788626580"
    }
]

@app.route('/')
def index():
    return render_template('index.html', 
                          personal_info=personal_info,
                          skills=skills,
                          languages=languages,
                          interests=interests)

@app.route('/experience')
def experience():
    return render_template('experience.html', 
                          personal_info=personal_info,
                          experiences=experiences)

@app.route('/education')
def education_page():
    return render_template('education.html', 
                          personal_info=personal_info,
                          education=education,
                          references=references)

@app.route('/contact')
def contact():
    return render_template('contact.html', personal_info=personal_info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)


@app.context_processor
def inject_now():
    return {'now': datetime.now()}