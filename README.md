Basic User Authentication Backend Template   


This project provides a simple backend template for implementing user authentication in a website. It allows storing and managing user details securely using a basic Flask-based web framework. This can serve as a foundation for any project requiring login/signup functionality.

🔧 Tech Stack


1.Flask – Python micro web framework
2.Bootstrap (CSS) – For styling the frontend
3.SQLAlchemy – ORM for database operations

🚀 Getting Started

📁 Project Setup

1.Download the ZIP of the project and extract it while maintaining the original folder structure.
2.Open a terminal in the project directory.

Install Dependencies


pip install -r requirements.txt


Features


1.User Registration
2.User Login
3.Secure Password Storage (via hashing)
4.Session Management
5.Bootstrap-based UI for basic styling

Folder Structure


website/                        
│   ├── static/                     
│   ├── templates/                  
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── login.html
│   │   └── signup.html
│   ├── __init__.py                 
│   ├── auth.py                     
│   ├── models.py                  
│   └── views.py                    
│
├── main.py                         
├── requirements.txt                
└── README.md 
