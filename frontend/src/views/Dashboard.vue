<script setup lang="ts">
    import { ref, onMounted, computed } from 'vue';
    import { useAuthStore } from '@/stores/auth';
    import {
        AcademicCapIcon,
        CodeBracketIcon,
        ChatBubbleLeftRightIcon,
        TrophyIcon,
        ChartBarSquareIcon,
        FireIcon,
    } from '@heroicons/vue/24/outline';

    const authStore = useAuthStore();

    const stats = ref([
        {
            name: 'Quizzes Completed',
            value: '12',
            change: '+2',
            icon: AcademicCapIcon,
            color: 'bg-blue-500',
        },
        {
            name: 'Challenges Solved',
            value: '8',
            change: '+1',
            icon: CodeBracketIcon,
            color: 'bg-green-500',
        },
        {
            name: 'Mock Interviews',
            value: '3',
            change: '+1',
            icon: ChatBubbleLeftRightIcon,
            color: 'bg-purple-500',
        },
        {
            name: 'Badges Earned',
            value: '5',
            change: '+1',
            icon: TrophyIcon,
            color: 'bg-yellow-500',
        },
    ]);

    const recentActivities = ref([
        { type: 'quiz', title: 'JavaScript Fundamentals Quiz', score: '85%', time: '2 hours ago' },
        { type: 'challenge', title: 'Two Sum Problem', status: 'Completed', time: '1 day ago' },
        {
            type: 'interview',
            title: 'Frontend Interview Practice',
            score: '90%',
            time: '2 days ago',
        },
        { type: 'badge', title: 'Earned "Problem Solver" badge', time: '3 days ago' },
    ]);

    const upcomingTasks = ref([
        { title: 'Complete React Advanced Quiz', due: 'Today', priority: 'high' },
        { title: 'Practice System Design Interview', due: 'Tomorrow', priority: 'medium' },
        { title: 'Update Resume with New Skills', due: 'This Week', priority: 'low' },
    ]);

    const currentLevel = computed(() => {
        return authStore.user?.progress.level || 1;
    });

    const totalPoints = computed(() => {
        return authStore.user?.progress.total_points || 0;
    });

    const progressToNextLevel = computed(() => {
        const currentPoints = totalPoints.value;
        const pointsForNextLevel = currentLevel.value * 1000; // Example: 1000 points per level
        const pointsNeeded = pointsForNextLevel - (currentPoints % pointsForNextLevel);
        return {
            current: currentPoints % pointsForNextLevel,
            needed: pointsForNextLevel,
            percentage: ((currentPoints % pointsForNextLevel) / pointsForNextLevel) * 100,
        };
    });

    onMounted(() => {
        // Load dashboard data
        console.log('Dashboard mounted, user:', authStore.user);
    });
</script>

<template>
    <div class="min-h-screen py-8 bg-gray-50">
        <div class="px-4 mx-auto max-w-7xl sm:px-6 lg:px-8">
            <!-- Welcome Section -->
            <div class="mb-8">
                <h1 class="text-3xl font-bold text-gray-900">
                    Welcome back, {{ authStore.user?.profile.first_name }}! 👋
                </h1>
                <p class="mt-2 text-gray-600">
                    Here's your learning progress and what's coming up next.
                </p>
            </div>

            <!-- Level Progress Card -->
            <div
                class="p-6 mb-8 text-white rounded-lg shadow-lg bg-gradient-to-r from-primary-600 via-purple-600 to-success-700"
            >
                <div class="flex items-center justify-between">
                    <div>
                        <h2 class="text-lg font-medium">Level {{ currentLevel }}</h2>
                        <p class="text-primary-100">{{ totalPoints }} total points earned</p>
                    </div>
                    <FireIcon class="w-12 h-12 text-primary-200" />
                </div>
                <div class="mt-4">
                    <div class="flex justify-between mb-2 text-sm text-primary-100">
                        <span>Progress to Level {{ currentLevel + 1 }}</span>
                        <span
                            >{{ progressToNextLevel.current }}/{{
                                progressToNextLevel.needed
                            }}
                            points</span
                        >
                    </div>
                    <div class="w-full h-2 rounded-full bg-primary-800">
                        <div
                            class="h-2 transition-all duration-300 bg-white rounded-full"
                            :style="{ width: `${progressToNextLevel.percentage}%` }"
                        ></div>
                    </div>
                </div>
            </div>

            <!-- Stats Grid -->
            <div class="grid grid-cols-1 gap-5 mb-8 sm:grid-cols-2 lg:grid-cols-4">
                <div
                    v-for="stat in stats"
                    :key="stat.name"
                    class="relative px-4 pt-5 pb-12 overflow-hidden bg-white rounded-lg shadow sm:pt-6 sm:px-6"
                >
                    <div class="flex items-center">
                        <div class="flex-shrink-0">
                            <div :class="[stat.color, 'rounded-md p-3']">
                                <component :is="stat.icon" class="w-6 h-6 text-white" />
                            </div>
                        </div>
                        <div class="flex-1 w-0 ml-5">
                            <dl>
                                <dt class="text-sm font-medium text-gray-500 truncate">
                                    {{ stat.name }}
                                </dt>
                                <dd>
                                    <div class="flex items-baseline">
                                        <div class="text-2xl font-semibold text-gray-900">
                                            {{ stat.value }}
                                        </div>
                                        <div
                                            class="flex items-baseline ml-2 text-sm font-semibold text-green-600"
                                        >
                                            {{ stat.change }}
                                        </div>
                                    </div>
                                </dd>
                            </dl>
                        </div>
                    </div>
                </div>
            </div>

            <div class="grid grid-cols-1 gap-8 lg:grid-cols-2">
                <!-- Recent Activity -->
                <div class="bg-white rounded-lg shadow">
                    <div class="px-4 py-5 sm:p-6">
                        <h3 class="mb-4 text-lg font-medium leading-6 text-gray-900">
                            Recent Activity
                        </h3>
                        <div class="flow-root">
                            <ul class="-mb-8">
                                <li v-for="(activity, index) in recentActivities" :key="index">
                                    <div
                                        class="relative pb-8"
                                        :class="{ 'pb-0': index === recentActivities.length - 1 }"
                                    >
                                        <span
                                            v-if="index !== recentActivities.length - 1"
                                            class="absolute top-4 left-4 -ml-px h-full w-0.5 bg-gray-200"
                                        ></span>
                                        <div class="relative flex space-x-3">
                                            <div>
                                                <span
                                                    class="flex items-center justify-center w-8 h-8 rounded-full ring-8 ring-white"
                                                    :class="{
                                                        'bg-blue-500': activity.type === 'quiz',
                                                        'bg-green-500':
                                                            activity.type === 'challenge',
                                                        'bg-purple-500':
                                                            activity.type === 'interview',
                                                        'bg-yellow-500': activity.type === 'badge',
                                                    }"
                                                >
                                                    <AcademicCapIcon
                                                        v-if="activity.type === 'quiz'"
                                                        class="w-4 h-4 text-white"
                                                    />
                                                    <CodeBracketIcon
                                                        v-else-if="activity.type === 'challenge'"
                                                        class="w-4 h-4 text-white"
                                                    />
                                                    <ChatBubbleLeftRightIcon
                                                        v-else-if="activity.type === 'interview'"
                                                        class="w-4 h-4 text-white"
                                                    />
                                                    <TrophyIcon v-else class="w-4 h-4 text-white" />
                                                </span>
                                            </div>
                                            <div
                                                class="min-w-0 flex-1 pt-1.5 flex justify-between space-x-4"
                                            >
                                                <div>
                                                    <p class="text-sm text-gray-900">
                                                        {{ activity.title }}
                                                    </p>
                                                    <p
                                                        v-if="activity.score"
                                                        class="text-sm text-gray-500"
                                                    >
                                                        Score: {{ activity.score }}
                                                    </p>
                                                    <p
                                                        v-if="activity.status"
                                                        class="text-sm text-gray-500"
                                                    >
                                                        {{ activity.status }}
                                                    </p>
                                                </div>
                                                <div
                                                    class="text-sm text-right text-gray-500 whitespace-nowrap"
                                                >
                                                    {{ activity.time }}
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>

                <!-- Upcoming Tasks -->
                <div class="bg-white rounded-lg shadow">
                    <div class="px-4 py-5 sm:p-6">
                        <h3 class="mb-4 text-lg font-medium leading-6 text-gray-900">
                            Upcoming Tasks
                        </h3>
                        <div class="space-y-4">
                            <div
                                v-for="task in upcomingTasks"
                                :key="task.title"
                                class="flex items-center justify-between p-4 rounded-lg bg-gray-50"
                            >
                                <div>
                                    <p class="text-sm font-medium text-gray-900">
                                        {{ task.title }}
                                    </p>
                                    <p class="text-sm text-gray-500">Due: {{ task.due }}</p>
                                </div>
                                <span
                                    class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium"
                                    :class="{
                                        'bg-red-100 text-red-800': task.priority === 'high',
                                        'bg-yellow-100 text-yellow-800': task.priority === 'medium',
                                        'bg-green-100 text-green-800': task.priority === 'low',
                                    }"
                                >
                                    {{ task.priority }}
                                </span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Quick Actions -->
            <div class="mt-8 bg-white rounded-lg shadow">
                <div class="px-4 py-5 sm:p-6">
                    <h3 class="mb-4 text-lg font-medium leading-6 text-gray-900">Quick Actions</h3>
                    <div class="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-4">
                        <router-link
                            to="/quizzes"
                            class="relative p-6 transition-colors bg-white border border-gray-200 rounded-lg group focus-within:ring-2 focus-within:ring-inset focus-within:ring-primary-500 hover:border-primary-300"
                        >
                            <div>
                                <span
                                    class="inline-flex p-3 text-blue-700 rounded-lg bg-blue-50 ring-4 ring-white"
                                >
                                    <AcademicCapIcon class="w-6 h-6" />
                                </span>
                            </div>
                            <div class="mt-8">
                                <h4 class="text-lg font-medium">Take a Quiz</h4>
                                <p class="mt-2 text-sm text-gray-500">
                                    Test your knowledge with our skill assessments
                                </p>
                            </div>
                        </router-link>

                        <router-link
                            to="/challenges"
                            class="relative p-6 transition-colors bg-white border border-gray-200 rounded-lg group focus-within:ring-2 focus-within:ring-inset focus-within:ring-primary-500 hover:border-primary-300"
                        >
                            <div>
                                <span
                                    class="inline-flex p-3 text-green-700 rounded-lg bg-green-50 ring-4 ring-white"
                                >
                                    <CodeBracketIcon class="w-6 h-6" />
                                </span>
                            </div>
                            <div class="mt-8">
                                <h4 class="text-lg font-medium">Solve Challenge</h4>
                                <p class="mt-2 text-sm text-gray-500">
                                    Practice with coding problems
                                </p>
                            </div>
                        </router-link>

                        <router-link
                            to="/interviews"
                            class="relative p-6 transition-colors bg-white border border-gray-200 rounded-lg group focus-within:ring-2 focus-within:ring-inset focus-within:ring-primary-500 hover:border-primary-300"
                        >
                            <div>
                                <span
                                    class="inline-flex p-3 text-purple-700 rounded-lg bg-purple-50 ring-4 ring-white"
                                >
                                    <ChatBubbleLeftRightIcon class="w-6 h-6" />
                                </span>
                            </div>
                            <div class="mt-8">
                                <h4 class="text-lg font-medium">Mock Interview</h4>
                                <p class="mt-2 text-sm text-gray-500">
                                    Practice your interview skills
                                </p>
                            </div>
                        </router-link>

                        <router-link
                            to="/ai-tutor"
                            class="relative p-6 transition-colors bg-white border border-gray-200 rounded-lg group focus-within:ring-2 focus-within:ring-inset focus-within:ring-primary-500 hover:border-primary-300"
                        >
                            <div>
                                <span
                                    class="inline-flex p-3 text-yellow-700 rounded-lg bg-yellow-50 ring-4 ring-white"
                                >
                                    <ChartBarSquareIcon class="w-6 h-6" />
                                </span>
                            </div>
                            <div class="mt-8">
                                <h4 class="text-lg font-medium">AI Tutor</h4>
                                <p class="mt-2 text-sm text-gray-500">
                                    Get personalized career guidance
                                </p>
                            </div>
                        </router-link>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
