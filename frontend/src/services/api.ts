import axios from 'axios';
import type { AxiosInstance, AxiosResponse } from 'axios';

// Base API configuration
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/api';

export const apiClient: AxiosInstance = axios.create({
    baseURL: API_BASE_URL,
    timeout: 10000,
    headers: {
        'Content-Type': 'application/json',
    },
});

// Request interceptor to add auth token
apiClient.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem('access_token');
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
    },
    (error) => Promise.reject(error),
);

// Response interceptor for error handling
apiClient.interceptors.response.use(
    (response: AxiosResponse) => response,
    (error) => {
        if (error.response?.status === 401) {
            localStorage.removeItem('access_token');
            window.location.href = '/login';
        }
        return Promise.reject(error);
    },
);

// Authentication API
export const authAPI = {
    login: (email: string, password: string) => apiClient.post('/auth/login', { email, password }),

    register: (userData: {
        email: string;
        password: string;
        first_name: string;
        last_name: string;
        university?: string;
        major?: string;
    }) => apiClient.post('/auth/register', userData),

    getToken: (username: string, password: string) =>
        apiClient.post('/auth/token', new URLSearchParams({ username, password }), {
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        }),
};

// Users API
export const usersAPI = {
    getCurrentUser: () => apiClient.get('/users/me'),
    updateCurrentUser: (userData: any) => apiClient.put('/users/me', userData),
    getLeaderboard: (limit: number = 10) => apiClient.get(`/users/leaderboard?limit=${limit}`),
    getUserStats: () => apiClient.get('/users/stats'),
};

// Quizzes API
export const quizzesAPI = {
    getQuizzes: (category?: string, difficulty?: string) =>
        apiClient.get('/quizzes', { params: { category, difficulty } }),
    getQuiz: (id: string) => apiClient.get(`/quizzes/${id}`),
    createQuiz: (quizData: any) => apiClient.post('/quizzes', quizData),
    updateQuiz: (id: string, quizData: any) => apiClient.put(`/quizzes/${id}`, quizData),
    deleteQuiz: (id: string) => apiClient.delete(`/quizzes/${id}`),
    startQuiz: (id: string) => apiClient.post(`/quizzes/${id}/start`),
    submitQuiz: (id: string, answers: Record<string, string>) =>
        apiClient.post(`/quizzes/${id}/submit`, { answers }),
    getQuizAttempts: (userId?: string) =>
        apiClient.get('/quizzes/attempts', { params: { userId } }),
    getQuizResults: (attemptId: string) => apiClient.get(`/quizzes/attempts/${attemptId}`),
};

// Challenges API
export const challengesAPI = {
    getChallenges: (category?: string, difficulty?: string) =>
        apiClient.get('/challenges', { params: { category, difficulty } }),
    getChallenge: (id: string) => apiClient.get(`/challenges/${id}`),
    createChallenge: (challengeData: any) => apiClient.post('/challenges', challengeData),
    updateChallenge: (id: string, challengeData: any) =>
        apiClient.put(`/challenges/${id}`, challengeData),
    deleteChallenge: (id: string) => apiClient.delete(`/challenges/${id}`),
    submitSolution: (id: string, code: string, language: string) =>
        apiClient.post(`/challenges/${id}/submit`, { code, language }),
    getChallengeAttempts: (userId?: string) =>
        apiClient.get('/challenges/attempts', { params: { userId } }),
    getSubmission: (submissionId: string) =>
        apiClient.get(`/challenges/submissions/${submissionId}`),
};

// Interviews API
export const interviewsAPI = {
    getInterviews: () => apiClient.get('/interviews'),
    getInterview: (id: string) => apiClient.get(`/interviews/${id}`),
    startInterview: (type: string, difficulty: string) =>
        apiClient.post('/interviews/start', { type, difficulty }),
    submitAnswer: (id: string, questionId: string, answer: string) =>
        apiClient.post(`/interviews/${id}/answer`, { questionId, answer }),
    completeInterview: (id: string) => apiClient.post(`/interviews/${id}/complete`),
    getInterviewResults: (id: string) => apiClient.get(`/interviews/${id}/results`),
};

// Resume API
export const resumeAPI = {
    getResumes: () => apiClient.get('/resume'),
    getResume: (id: string) => apiClient.get(`/resume/${id}`),
    createResume: (resumeData: any) => apiClient.post('/resume', resumeData),
    updateResume: (id: string, resumeData: any) => apiClient.put(`/resume/${id}`, resumeData),
    deleteResume: (id: string) => apiClient.delete(`/resume/${id}`),
    analyzeJobDescription: (jobDescription: string) =>
        apiClient.post('/resume/analyze', { jobDescription }),
    generateResume: (profileData: any) => apiClient.post('/resume/generate', profileData),
};

// Roadmap API
export const roadmapAPI = {
    getRoadmap: (userId?: string) => apiClient.get('/roadmap', { params: { userId } }),
    generateRoadmap: (goals: any, skills: any) =>
        apiClient.post('/roadmap/generate', { goals, skills }),
    updateProgress: (stepId: string, completed: boolean) =>
        apiClient.put(`/roadmap/progress/${stepId}`, { completed }),
    getRoadmapTemplates: () => apiClient.get('/roadmap/templates'),
};

// AI Tutor API
export const tutorAPI = {
    startChat: () => apiClient.post('/tutor/chat/start'),
    sendMessage: (chatId: string, message: string) =>
        apiClient.post(`/tutor/chat/${chatId}/message`, { message }),
    getChatHistory: (chatId: string) => apiClient.get(`/tutor/chat/${chatId}/history`),
    getCareerAdvice: (userProfile: any) => apiClient.post('/tutor/advice', userProfile),
    getSkillRecommendations: (currentSkills: string[], targetRole: string) =>
        apiClient.post('/tutor/recommendations', { currentSkills, targetRole }),
};

// Achievements API
export const achievementsAPI = {
    getAchievements: (userId?: string) => apiClient.get('/achievements', { params: { userId } }),
    getUserBadges: (userId?: string) =>
        apiClient.get('/achievements/badges', { params: { userId } }),
    claimAchievement: (achievementId: string) =>
        apiClient.post(`/achievements/${achievementId}/claim`),
    getLeaderboard: (category?: string) =>
        apiClient.get('/achievements/leaderboard', { params: { category } }),
};

// Generic API helper functions
export const apiHelpers = {
    handleApiError: (error: any) => {
        if (error.response?.data?.detail) {
            return error.response.data.detail;
        }
        return error.message || 'An unexpected error occurred';
    },

    uploadFile: (endpoint: string, file: File, additionalData?: any) => {
        const formData = new FormData();
        formData.append('file', file);

        if (additionalData) {
            Object.keys(additionalData).forEach((key) => {
                formData.append(key, additionalData[key]);
            });
        }

        return apiClient.post(endpoint, formData, {
            headers: { 'Content-Type': 'multipart/form-data' },
        });
    },

    downloadFile: (endpoint: string, filename?: string) => {
        return apiClient
            .get(endpoint, {
                responseType: 'blob',
            })
            .then((response) => {
                const url = window.URL.createObjectURL(new Blob([response.data]));
                const link = document.createElement('a');
                link.href = url;
                link.setAttribute('download', filename || 'download');
                document.body.appendChild(link);
                link.click();
                link.remove();
            });
    },
};

export default apiClient;
