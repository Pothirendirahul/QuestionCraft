in txt format5:40 PM# 🎯 QuestionCraft

**AI-Powered Interview Question Generator for Technical Hiring**

## 📋 Overview

QuestionCraft is an intelligent interview question generator that creates personalized, unique coding challenges based on:

- Candidate's Resume: Analyzes skills, experience, and domain expertise
- Company Tech Stack: Matches questions to your technologies
- Role Requirements: Adjusts difficulty and focus areas
- Real-Time Assistance: AI helps interviewers during live sessions

### The Problem We Solve

Traditional technical interviews have major issues:
- Candidates memorize LeetCode solutions
- Same questions repeated across interviews
- Generic problems don't test real job skills
- Inconsistent evaluation across interviewers

### Our Solution

QuestionCraft generates unique questions every time, personalized to each candidate's background, ensuring fair and relevant assessments.

---

## 🏗️ Architecture

### Tech Stack

**Backend:**
- Framework: FastAPI (Python 3.11)
- Database: PostgreSQL 15
- AI/ML: OpenAI GPT-4, LangChain
- Task Queue: Celery + Redis
- ORM: SQLAlchemy + Alembic

**AI Agents:**
- Resume Analyzer (extracts skills, experience)
- Question Generator (creates personalized problems)
- Solution Validator (ensures solvability)
- Interview Assistant (real-time insights)
- Report Generator (post-interview evaluation)

**Frontend (Coming in Week 4):**
- React + TypeScript
- Monaco Editor (code editor)
- WebSocket (real-time updates)

---

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- PostgreSQL 15+
- OpenAI API Key
- Git

### Installation

#### 1. Clone the Repository

git clone https://github.com/YOUR_USERNAME/QuestionCraft.git
cd QuestionCraft

#### 2. Setup Backend

cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Download spaCy English model
python -m spacy download en_core_web_sm

#### 3. Configure Environment

# Copy environment template
copy .env.example .env    # Windows
# cp .env.example .env    # Mac/Linux

# Edit .env and add your API keys
notepad .env              # Windows
# nano .env               # Mac/Linux

Required Environment Variables:
OPENAI_API_KEY=sk-your-actual-api-key-here
DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/questioncraft

#### 4. Setup Database

# Make sure PostgreSQL is running
# Create database
psql -U postgres -c "CREATE DATABASE questioncraft;"

# Run migrations (after Week 1 setup)
alembic upgrade head

#### 5. Start the Server

uvicorn src.api.main:app --reload

Visit: http://localhost:8000/docs

---

## 🐳 Docker Setup (Alternative)

# Start all services
docker-compose up -d

# View logs
docker-compose logs -f api

# Stop services
docker-compose down

---

## 📚 Project Structure

QuestionCraft/
├── backend/
│   ├── src/
│   │   ├── api/              # FastAPI routes
│   │   ├── agents/           # AI agent system
│   │   ├── parsers/          # Resume parsing
│   │   ├── models/           # Pydantic schemas
│   │   ├── services/         # Business logic
│   │   ├── db/               # Database models
│   │   ├── core/             # Config & utilities
│   │   └── utils/            # Helper functions
│   ├── tests/                # Test suite
│   ├── requirements.txt
│   └── .env.example
├── frontend/                 # React app (Week 4+)
├── docs/                     # Documentation
├── docker-compose.yml
└── README.md

---

## 🔑 Key Features

### Phase 1: Question Generation (Week 1-2)
- [x] Upload candidate resume (PDF/DOCX)
- [x] AI-powered resume parsing
- [x] Extract skills, experience, domain expertise
- [x] Generate personalized interview questions
- [x] Create test cases and reference solutions

### Phase 2: Live Interview (Week 3-4)
- [ ] Browser-based code editor
- [ ] Real-time code execution
- [ ] AI interviewer assistant
- [ ] Automatic evaluation

### Phase 3: Advanced Features (Week 5-6)
- [ ] Real-time code analysis
- [ ] Follow-up question suggestions
- [ ] Comprehensive interview reports
- [ ] Question effectiveness tracking

---

## 🎯 API Endpoints

POST   /api/candidates/upload      # Upload resume
GET    /api/candidates/{id}         # Get candidate profile
GET    /api/candidates              # List all candidates

POST   /api/questions/generate      # Generate question
GET    /api/questions/{id}          # Get question details
GET    /api/questions               # List questions

GET    /health                      # Health check

Full API documentation: http://localhost:8000/docs

---

## 🧪 Testing

# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# Run specific test
pytest tests/unit/test_resume_analyzer.py

---

## 🗓️ Development Timeline

Week 1: Backend setup + Resume parsing - In Progress
Week 2: Question generation engine - Planned
Week 3: Code execution integration - Upcoming
Week 4: Frontend development - Upcoming
Week 5: Real-time features - Upcoming
Week 6: Testing & deployment - Upcoming

---

## 💡 Example Usage

# Upload resume
candidate = await create_candidate("resume.pdf")

# Generate personalized question
question = await generate_question(
    candidate_id=candidate.id,
    difficulty="medium",
    category="system-design"
)

print(question.title)
# "Design a Rate Limiter for Video Streaming API"

---

## 🐛 Troubleshooting

Database Connection Error:
- Check PostgreSQL is running
- Windows: Check Services
- Mac: brew services list

Module Not Found:
pip install -r requirements.txt

OpenAI API Error:
- Check .env has valid OPENAI_API_KEY
- Verify API key at platform.openai.com

---

## 📊 Tech Stack Details

Language: Python 3.11
Framework: FastAPI
Database: PostgreSQL
ORM: SQLAlchemy
AI/ML: OpenAI GPT-4
NLP: spaCy
Task Queue: Celery
Cache: Redis

---

## 📈 Roadmap

- Support more languages (Java, C++, Go)
- Video interview integration
- Collaborative interviewing
- Analytics dashboard
- Mobile app
- ATS integrations

---

## 📄 License

MIT License

---

## 👨‍💻 Author

Your Name
GitHub: @yourusername
LinkedIn: Your Profile

---

Built with love for better technical hiring

================================================================================
================================================================================
================================================================================

requirements.txt

================================================================================

# Web Framework
fastapi==0.109.2
uvicorn[standard]==0.27.1
python-multipart==0.0.9

# Database
sqlalchemy==2.0.25
alembic==1.13.1
psycopg2-binary==2.9.9
asyncpg==0.29.0

# AI/ML
langchain==0.1.6
langchain-openai==0.0.5
openai==1.12.0

# Document Processing
pypdf2==3.0.1
python-docx==1.1.0
pdfplumber==0.10.3

# NLP
spacy==3.7.2

# Data Validation
pydantic==2.6.1
pydantic-settings==2.1.0
email-validator==2.1.0

# Utilities
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-dotenv==1.0.1
structlog==24.1.0
httpx==0.26.0

# Task Queue
celery[redis]==5.3.6
redis==5.0.1

================================================================================
================================================================================
================================================================================

requirements-dev.txt

================================================================================

# Testing
pytest==8.0.0
pytest-asyncio==0.23.4
pytest-cov==4.1.0
pytest-mock==3.12.0
httpx==0.26.0

# Code Quality
black==24.1.1
ruff==0.2.1
mypy==1.8.0
pre-commit==3.6.0

# Development
ipython==8.21.0
ipdb==0.13.13
watchdog==4.0.0

================================================================================
================================================================================
================================================================================

.gitignore

================================================================================

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
.venv
pip-log.txt
.pytest_cache/
.coverage
htmlcov/
*.egg-info/
dist/
build/

# Environment variables
.env
.env.local
*.env
!.env.example

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Logs
*.log
logs/

# Database
*.db
*.sqlite3

# Uploaded files
uploads/
temp/

# Node
node_modules/
npm-debug.log
.next/
out/

# Docker
docker-compose.override.yml

# Misc
.mypy_cache/
.ruff_cache/

================================================================================
================================================================================
================================================================================

.env.example

================================================================================

# Application
APP_ENV=development
DEBUG=True
SECRET_KEY=your-secret-key-change-this-in-production
API_HOST=0.0.0.0
API_PORT=8000

# Database
DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/questioncraft
DATABASE_POOL_SIZE=5
DATABASE_MAX_OVERFLOW=10

# OpenAI
OPENAI_API_KEY=sk-your-api-key-here
OPENAI_MODEL=gpt-4o
OPENAI_TEMPERATURE=0.7
OPENAI_MAX_TOKENS=2000

# Redis
REDIS_URL=redis://localhost:6379/0

# Celery
CELERY_BROKER_URL=redis://localhost:6379/1
CELERY_RESULT_BACKEND=redis://localhost:6379/2

# File Upload
MAX_UPLOAD_SIZE_MB=10
ALLOWED_EXTENSIONS=pdf,docx,doc
UPLOAD_DIR=./uploads

# Logging
LOG_LEVEL=INFO
LOG_FORMAT=json

# CORS
CORS_ORIGINS=http://localhost:3000,http://localhost:5173

# JWT
JWT_SECRET_KEY=another-secret-key-change-this
JWT_ALGORITHM=HS256
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=30

================================================================================