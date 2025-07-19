<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

# HirableEdge - Full-Stack Career Development Platform

## Project Overview
HirableEdge is a comprehensive full-stack web application that helps students and professionals improve their job hirability through various features including quizzes, coding challenges, mock interviews, and personalized career roadmaps.

## Tech Stack
- **Frontend**: Vue.js 3 with TypeScript, Vite, TailwindCSS, Headless UI, Heroicons, Pinia (state management)
- **Backend**: FastAPI with Python, async/await patterns
- **Database**: MongoDB with Motor (async driver)
- **Authentication**: JWT-based authentication
- **AI Integration**: OpenAI API for career guidance and feedback
- **Styling**: TailwindCSS with custom design system

## Code Style Guidelines

### Vue.js Components
- Use Composition API with `<script setup lang="ts">`
- Implement proper TypeScript interfaces for all data structures
- Use Pinia stores for state management
- Follow Vue 3 best practices for reactivity and lifecycle
- Use Heroicons for consistent iconography
- Implement proper loading states and error handling

### API Development
- Use FastAPI with async/await patterns
- Implement proper Pydantic models for request/response validation
- Use dependency injection for database connections and authentication
- Follow RESTful API conventions
- Implement proper error handling with HTTP status codes
- Use MongoDB with Motor for async database operations

### Styling
- Use TailwindCSS utility classes
- Follow the established design system (primary colors, spacing, etc.)
- Implement responsive design patterns
- Use Headless UI components for complex interactions
- Maintain consistent component patterns

### Authentication & Security
- Implement JWT-based authentication
- Use proper password hashing with bcrypt
- Validate all inputs on both client and server
- Implement proper CORS configuration
- Use environment variables for sensitive configuration

## Key Features to Implement
1. User authentication and profile management
2. Skill assessment quizzes with timed questions
3. Coding challenges with multiple languages support
4. Mock interview simulation with AI feedback
5. Resume builder with job description analysis
6. Personalized career roadmap generation
7. AI-powered career tutor chatbot
8. Achievement and badge system
9. Progress tracking and analytics
10. Responsive design for mobile and desktop

## File Organization
- Frontend components in `/src/components/` organized by feature
- Views in `/src/views/` with nested folders for related pages
- Stores in `/src/stores/` for state management
- Services in `/src/services/` for API interactions
- Backend models in `/app/models/` with Pydantic schemas
- API routes in `/app/api/routes/` organized by feature
- Core functionality in `/app/core/` (auth, database, config)

## Development Guidelines
- Write comprehensive error handling for all API calls
- Implement loading states for better UX
- Use TypeScript strictly with proper type definitions
- Write reusable components and utilities
- Follow accessibility best practices
- Implement proper form validation on both client and server
- Use environment variables for configuration
- Write clean, documented code with meaningful variable names
