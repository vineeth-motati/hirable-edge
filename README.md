# HirableEdge - Career Development Platform

HirableEdge is a comprehensive full-stack web application designed to help students and professionals improve their job hirability through various interactive features including skill assessment quizzes, coding challenges, mock interviews, and personalized career roadmaps.

## 🚀 Features

### Core Functionality
- **User Authentication**: Secure JWT-based authentication system with registration and login
- **Interactive Dashboard**: Personalized dashboard showing progress, achievements, and upcoming tasks
- **Skill Assessment Quizzes**: Timed quizzes across various technical and soft skills domains
- **Coding Challenges**: Programming challenges with multiple difficulty levels and instant feedback
- **Mock Interviews**: AI-driven mock interview simulations with personalized feedback
- **Resume Builder**: Intelligent resume creation tool that analyzes job descriptions
- **Career Roadmap**: Personalized career guidance based on user goals and current skills
- **AI Tutor**: Personal AI assistant for career advice and learning recommendations
- **Achievement System**: Badges, points, and level progression to gamify learning
- **Leaderboards**: Competitive element with user rankings and achievements

### Technical Features
- **Responsive Design**: Mobile-first design that works seamlessly across all devices
- **Real-time Updates**: Live progress tracking and instant feedback
- **Advanced Analytics**: Detailed progress reports and performance insights
- **Multi-language Support**: Coding challenges support multiple programming languages

## 🛠 Tech Stack

### Frontend
- **Vue.js 3** - Progressive JavaScript framework with Composition API
- **TypeScript** - Type-safe JavaScript development
- **Vite** - Next-generation frontend build tool
- **TailwindCSS** - Utility-first CSS framework
- **Headless UI** - Unstyled, accessible UI components
- **Heroicons** - Beautiful hand-crafted SVG icons
- **Pinia** - Vue.js state management library
- **Vue Router** - Official router for Vue.js
- **Axios** - Promise-based HTTP client

### Backend
- **FastAPI** - Modern, fast Python web framework
- **Python 3.8+** - Programming language
- **MongoDB** - NoSQL document database
- **Motor** - Async MongoDB driver for Python
- **Pydantic** - Data validation using Python type hints
- **JWT** - JSON Web Token for authentication
- **bcrypt** - Password hashing library
- **OpenAI API** - AI-powered features integration

## 🔧 Quick Start

### Prerequisites
- Node.js (v18 or higher)
- Python (3.8 or higher)
- MongoDB (v4.4 or higher)

### 1. Frontend Setup
```bash
# Install dependencies
npm install

# Start development server
npm run dev
```

### 2. Backend Setup
```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate

# Install dependencies
pip install -r requirements.txt

# Start backend server
python main.py
```

### 3. Environment Configuration
Create `.env` files in both root and backend directories with appropriate configuration values.

## 🌐 Access Points

- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

## 📁 Project Structure

```
hirableedge/
├── src/                    # Frontend source code
│   ├── components/         # Vue components
│   ├── views/             # Page components
│   ├── stores/            # Pinia stores
│   ├── services/          # API services
│   └── router/            # Vue Router config
├── backend/               # Backend source code
│   ├── app/
│   │   ├── api/          # API routes
│   │   ├── core/         # Core functionality
│   │   ├── models/       # Data models
│   │   └── services/     # Business logic
│   └── main.py           # FastAPI app entry
└── README.md
```

## 🎯 Current Status

✅ **Completed**:
- Project structure setup
- Vue.js + TypeScript frontend configuration
- FastAPI backend with MongoDB integration
- User authentication system (JWT)
- Basic UI components and routing
- Dashboard with user progress tracking

🔄 **In Progress**:
- Quiz system implementation
- Coding challenge platform
- Mock interview features

📋 **Planned**:
- Resume builder
- AI-powered career roadmap
- Achievement and badge system
- Advanced analytics and reporting

## 🤝 Contributing

This project follows Vue 3 Composition API patterns and FastAPI best practices. Check the `.github/copilot-instructions.md` file for detailed development guidelines.

---

Made with ❤️ for helping students achieve their career goals
