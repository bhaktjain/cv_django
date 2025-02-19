from django.shortcuts import render

def cv_view(request):
    context = {
        "name": "Bhaktram Jain",
        "email": "bj2411@nyu.edu",
        "phone": "+1 (929) 210-2651",
        "location": "New York, NY, USA",
        "education": [
            {
                "institution": "New York University",
                "degree": "M.S. Computer Science",
                "duration": "September 2024 – May 2026",
                "location": "New York City, United States",
                "coursework": "Machine Learning, Big Data, Principles of Database Systems"
            },
            {
                "institution": "SRM Institute of Science and Technology",
                "degree": "B.Tech in Computer Science",
                "duration": "July 2019 – May 2023",
                "location": "Chennai, India",
                "details": "CGPA: 9.65/10, Merit-based Scholarship: 2019-2020, 2021-2022",
                "coursework": "Data Structures and Algorithms, Software Engineering, Data Science"
            }
        ],
        "technical_skills": {
            "Languages": ["Scala", "Python", "C/C++", "SQL", "R", "JavaScript", "Java", "Shell Scripting", "Statistical Analysis"],
            "Libraries": ["Pandas", "Numpy", "TensorFlow", "PyTorch", "Keras", "Matplotlib", "Seaborn", "Flask", "AWSCloud", "Git"],
            "Tools": ["MS Excel", "MS Office 365", "Power Bi", "Tableau", "Jupyter Notebook", "MS Visual Studio", "Microsoft Azure"],
            "Certifications": [
                "Machine Learning by Stanford University",
                "Full Stack Web Development Node.js mastery",
                "Linux Administration",
                "PSE SASE by Palo Alto",
                "ZCSE, ZIA and ZPA Administrator by Zcaler"
            ]
        },
        "work_experience": [
            {
                "role": "Data Analyst",
                "company": "Computacenter",
                "duration": "January 2023 – August 2024",
                "location": "Bengaluru, India",
                "details": [
                    "Partnered with 10+ clients and internal teams to analyze business needs, utilizing advanced SQL and KPI reporting, resulting in 15% revenue growth through Tableau and Power BI dashboards.",
                    "Orchestrated the seamless migration of LANs and software-defined access for Cisco SAP, ensuring a 100% successful project launch within the projected timeline.",
                    "Streamlined SQL by creating 50+ procedures and views, cutting query time by 40% and boosting data analytics.",
                    "Trained in technologies like Office 365, PowerShell scripting, Microsoft Intune, virtualization, and ITIL; came in 2nd place out of 70 interns in the overall internship assessments."
                ]
            },
            {
                "role": "Machine Learning Research Intern",
                "company": "National University of Singapore",
                "duration": "June 2022 – July 2022",
                "location": "Singapore",
                "details": [
                    "Engineered a stock market movement predictor using NLP to analyze 10,000+ news headlines.",
                    "Incorporated 5 years of historical data, achieving a 22% increase in prediction accuracy.",
                    "Designed a model that analyzes news headlines for polarity, predicting stock movements with 85% accuracy."
                ]
            },
            {
                "role": "Machine Learning Intern",
                "company": "HighRadius",
                "duration": "January 2022 – April 2022",
                "location": "Chennai, India",
                "details": [
                    "Developed and deployed an AI-enabled Fintech B2B cloud application, improving processing speed by 30%.",
                    "Conducted predictive analysis on a dataset of over 1 million transactions, devising ensemble strategies and troubleshooting feature engineering techniques.",
                    "Garnered a 20% increase in forecasting accuracy for customer delays and estimated payment dates."
                ]
            },
            {
                "role": "Web Developer Intern",
                "company": "Artistry Agency",
                "duration": "October 2021 – December 2021",
                "location": "Kolkata, India",
                "details": [
                    "Engineered a robust online application using HTML, CSS, JavaScript, Node.js, and MongoDB, integrating 5+ libraries like Socket.io, Bulma, and ORM Sequelize.",
                    "Managed a database of 1,000+ products with MongoDB, ensuring efficient data solutions and ETL."
                ]
            }
        ],
        "projects": [
            {
                "title": "A Novel Framework for Potato Leaf Disease Detection",
                "duration": "January 2023 – May 2023",
                "details": [
                    "Innovated a deep learning model using VGG19 to detect potato leaf diseases with 95.2% accuracy, enhancing agricultural disease management.",
                    "Implemented transfer learning for fine-tuning a VGG19 model on a dataset of 4,000 potato leaf images."
                ]
            },
            {
                "title": "Violence Detection in Real Life Videos using Deep Learning",
                "duration": "August 2022 – December 2022",
                "details": [
                    "Fabricated a violence detection system using U-Net and MobileNetV2, achieving a 95% precision and 94% accuracy across 2,000 real-world video datasets.",
                    "Automated surveillance across 50+ CCTV feeds by deploying a real-time detection model, reducing manual monitoring efforts by 60%."
                ]
            }
        ],
        "links": {
            "linkedin": "https://linkedin.com/in/bhaktjain",
            "github": "https://github.com/bhaktjain"
        }
    }
    return render(request, 'cv/cv.html', context)
