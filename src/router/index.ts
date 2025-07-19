import { createRouter, createWebHistory } from 'vue-router';

const routes = [
    {
        path: '/',
        name: 'Home',
        component: () => import('@/views/Home.vue'),
    },
    {
        path: '/login',
        name: 'Login',
        component: () => import('@/views/auth/Login.vue'),
    },
    {
        path: '/register',
        name: 'Register',
        component: () => import('@/views/auth/Register.vue'),
    },
    {
        path: '/dashboard',
        name: 'Dashboard',
        component: () => import('@/views/Dashboard.vue'),
    },
    {
        path: '/profile',
        name: 'Profile',
        component: () => import('@/views/Profile.vue'),
    },
    {
        path: '/quizzes',
        name: 'QuizList',
        component: () => import('@/views/quizzes/QuizList.vue'),
    },
    {
        path: '/quizzes/:id',
        name: 'QuizDetail',
        component: () => import('@/views/quizzes/QuizDetail.vue'),
        props: true,
    },
    {
        path: '/quizzes/:id/attempt',
        name: 'QuizAttempt',
        component: () => import('@/views/quizzes/QuizAttempt.vue'),
        props: true,
    },
    {
        path: '/challenges',
        name: 'ChallengeList',
        component: () => import('@/views/challenges/ChallengeList.vue'),
    },
    {
        path: '/challenges/:id',
        name: 'ChallengeDetail',
        component: () => import('@/views/challenges/ChallengeDetail.vue'),
        props: true,
    },
    {
        path: '/challenges/:id/attempt',
        name: 'ChallengeAttempt',
        component: () => import('@/views/challenges/ChallengeAttempt.vue'),
        props: true,
    },
    {
        path: '/interviews',
        name: 'InterviewList',
        component: () => import('@/views/interviews/InterviewList.vue'),
    },
    {
        path: '/interviews/:id',
        name: 'InterviewDetail',
        component: () => import('@/views/interviews/InterviewDetail.vue'),
        props: true,
    },
    {
        path: '/resume',
        name: 'ResumeBuilder',
        component: () => import('@/views/resume/ResumeBuilder.vue'),
    },
    {
        path: '/roadmap',
        name: 'CareerRoadmap',
        component: () => import('@/views/roadmap/CareerRoadmap.vue'),
    },
    {
        path: '/ai-tutor',
        name: 'AITutor',
        component: () => import('@/views/tutor/AITutor.vue'),
    },
    {
        path: '/achievements',
        name: 'Achievements',
        component: () => import('@/views/achievements/Achievements.vue'),
    },
    {
        path: '/leaderboard',
        name: 'Leaderboard',
        component: () => import('@/views/Leaderboard.vue'),
    },
    {
        path: '/:catchAll(.*)',
        redirect: '/',
    },
];

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes,
});

export default router;
