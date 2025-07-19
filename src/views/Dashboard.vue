<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { 
  AcademicCapIcon, 
  CodeBracketIcon, 
  ChatBubbleLeftRightIcon,
  TrophyIcon,
  ChartBarSquareIcon,
  FireIcon
} from '@heroicons/vue/24/outline'

const authStore = useAuthStore()

const stats = ref([
  { name: 'Quizzes Completed', value: '12', change: '+2', icon: AcademicCapIcon, color: 'bg-blue-500' },
  { name: 'Challenges Solved', value: '8', change: '+1', icon: CodeBracketIcon, color: 'bg-green-500' },
  { name: 'Mock Interviews', value: '3', change: '+1', icon: ChatBubbleLeftRightIcon, color: 'bg-purple-500' },
  { name: 'Badges Earned', value: '5', change: '+1', icon: TrophyIcon, color: 'bg-yellow-500' },
])

const recentActivities = ref([
  { type: 'quiz', title: 'JavaScript Fundamentals Quiz', score: '85%', time: '2 hours ago' },
  { type: 'challenge', title: 'Two Sum Problem', status: 'Completed', time: '1 day ago' },
  { type: 'interview', title: 'Frontend Interview Practice', score: '90%', time: '2 days ago' },
  { type: 'badge', title: 'Earned "Problem Solver" badge', time: '3 days ago' },
])

const upcomingTasks = ref([
  { title: 'Complete React Advanced Quiz', due: 'Today', priority: 'high' },
  { title: 'Practice System Design Interview', due: 'Tomorrow', priority: 'medium' },
  { title: 'Update Resume with New Skills', due: 'This Week', priority: 'low' },
])

const currentLevel = computed(() => {
  return authStore.user?.progress.level || 1
})

const totalPoints = computed(() => {
  return authStore.user?.progress.total_points || 0
})

const progressToNextLevel = computed(() => {
  const currentPoints = totalPoints.value
  const pointsForNextLevel = currentLevel.value * 1000 // Example: 1000 points per level
  const pointsNeeded = pointsForNextLevel - (currentPoints % pointsForNextLevel)
  return {
    current: currentPoints % pointsForNextLevel,
    needed: pointsForNextLevel,
    percentage: ((currentPoints % pointsForNextLevel) / pointsForNextLevel) * 100
  }
})

onMounted(() => {
  // Load dashboard data
  console.log('Dashboard mounted, user:', authStore.user)
})
</script>

<template>
  <div class="min-h-screen bg-gray-50 py-8">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
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
      <div class="bg-gradient-to-r from-primary-600 to-primary-700 rounded-lg shadow-lg p-6 mb-8 text-white">
        <div class="flex items-center justify-between">
          <div>
            <h2 class="text-lg font-medium">Level {{ currentLevel }}</h2>
            <p class="text-primary-100">{{ totalPoints }} total points earned</p>
          </div>
          <FireIcon class="h-12 w-12 text-primary-200" />
        </div>
        <div class="mt-4">
          <div class="flex justify-between text-sm text-primary-100 mb-2">
            <span>Progress to Level {{ currentLevel + 1 }}</span>
            <span>{{ progressToNextLevel.current }}/{{ progressToNextLevel.needed }} points</span>
          </div>
          <div class="w-full bg-primary-800 rounded-full h-2">
            <div 
              class="bg-white h-2 rounded-full transition-all duration-300"
              :style="{ width: `${progressToNextLevel.percentage}%` }"
            ></div>
          </div>
        </div>
      </div>

      <!-- Stats Grid -->
      <div class="grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-4 mb-8">
        <div
          v-for="stat in stats"
          :key="stat.name"
          class="relative bg-white pt-5 px-4 pb-12 sm:pt-6 sm:px-6 shadow rounded-lg overflow-hidden"
        >
          <div class="flex items-center">
            <div class="flex-shrink-0">
              <div :class="[stat.color, 'rounded-md p-3']">
                <component :is="stat.icon" class="h-6 w-6 text-white" />
              </div>
            </div>
            <div class="ml-5 w-0 flex-1">
              <dl>
                <dt class="text-sm font-medium text-gray-500 truncate">{{ stat.name }}</dt>
                <dd>
                  <div class="flex items-baseline">
                    <div class="text-2xl font-semibold text-gray-900">{{ stat.value }}</div>
                    <div class="ml-2 flex items-baseline text-sm font-semibold text-green-600">
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
        <div class="bg-white shadow rounded-lg">
          <div class="px-4 py-5 sm:p-6">
            <h3 class="text-lg leading-6 font-medium text-gray-900 mb-4">Recent Activity</h3>
            <div class="flow-root">
              <ul class="-mb-8">
                <li v-for="(activity, index) in recentActivities" :key="index">
                  <div class="relative pb-8" :class="{ 'pb-0': index === recentActivities.length - 1 }">
                    <span
                      v-if="index !== recentActivities.length - 1"
                      class="absolute top-4 left-4 -ml-px h-full w-0.5 bg-gray-200"
                    ></span>
                    <div class="relative flex space-x-3">
                      <div>
                        <span 
                          class="h-8 w-8 rounded-full flex items-center justify-center ring-8 ring-white"
                          :class="{
                            'bg-blue-500': activity.type === 'quiz',
                            'bg-green-500': activity.type === 'challenge',
                            'bg-purple-500': activity.type === 'interview',
                            'bg-yellow-500': activity.type === 'badge'
                          }"
                        >
                          <AcademicCapIcon v-if="activity.type === 'quiz'" class="h-4 w-4 text-white" />
                          <CodeBracketIcon v-else-if="activity.type === 'challenge'" class="h-4 w-4 text-white" />
                          <ChatBubbleLeftRightIcon v-else-if="activity.type === 'interview'" class="h-4 w-4 text-white" />
                          <TrophyIcon v-else class="h-4 w-4 text-white" />
                        </span>
                      </div>
                      <div class="min-w-0 flex-1 pt-1.5 flex justify-between space-x-4">
                        <div>
                          <p class="text-sm text-gray-900">{{ activity.title }}</p>
                          <p v-if="activity.score" class="text-sm text-gray-500">Score: {{ activity.score }}</p>
                          <p v-if="activity.status" class="text-sm text-gray-500">{{ activity.status }}</p>
                        </div>
                        <div class="text-right text-sm whitespace-nowrap text-gray-500">
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
        <div class="bg-white shadow rounded-lg">
          <div class="px-4 py-5 sm:p-6">
            <h3 class="text-lg leading-6 font-medium text-gray-900 mb-4">Upcoming Tasks</h3>
            <div class="space-y-4">
              <div
                v-for="task in upcomingTasks"
                :key="task.title"
                class="flex items-center justify-between p-4 bg-gray-50 rounded-lg"
              >
                <div>
                  <p class="text-sm font-medium text-gray-900">{{ task.title }}</p>
                  <p class="text-sm text-gray-500">Due: {{ task.due }}</p>
                </div>
                <span
                  class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium"
                  :class="{
                    'bg-red-100 text-red-800': task.priority === 'high',
                    'bg-yellow-100 text-yellow-800': task.priority === 'medium',
                    'bg-green-100 text-green-800': task.priority === 'low'
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
      <div class="mt-8 bg-white shadow rounded-lg">
        <div class="px-4 py-5 sm:p-6">
          <h3 class="text-lg leading-6 font-medium text-gray-900 mb-4">Quick Actions</h3>
          <div class="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-4">
            <router-link
              to="/quizzes"
              class="relative group bg-white p-6 focus-within:ring-2 focus-within:ring-inset focus-within:ring-primary-500 rounded-lg border border-gray-200 hover:border-primary-300 transition-colors"
            >
              <div>
                <span class="rounded-lg inline-flex p-3 bg-blue-50 text-blue-700 ring-4 ring-white">
                  <AcademicCapIcon class="h-6 w-6" />
                </span>
              </div>
              <div class="mt-8">
                <h4 class="text-lg font-medium">Take a Quiz</h4>
                <p class="mt-2 text-sm text-gray-500">Test your knowledge with our skill assessments</p>
              </div>
            </router-link>

            <router-link
              to="/challenges"
              class="relative group bg-white p-6 focus-within:ring-2 focus-within:ring-inset focus-within:ring-primary-500 rounded-lg border border-gray-200 hover:border-primary-300 transition-colors"
            >
              <div>
                <span class="rounded-lg inline-flex p-3 bg-green-50 text-green-700 ring-4 ring-white">
                  <CodeBracketIcon class="h-6 w-6" />
                </span>
              </div>
              <div class="mt-8">
                <h4 class="text-lg font-medium">Solve Challenge</h4>
                <p class="mt-2 text-sm text-gray-500">Practice with coding problems</p>
              </div>
            </router-link>

            <router-link
              to="/interviews"
              class="relative group bg-white p-6 focus-within:ring-2 focus-within:ring-inset focus-within:ring-primary-500 rounded-lg border border-gray-200 hover:border-primary-300 transition-colors"
            >
              <div>
                <span class="rounded-lg inline-flex p-3 bg-purple-50 text-purple-700 ring-4 ring-white">
                  <ChatBubbleLeftRightIcon class="h-6 w-6" />
                </span>
              </div>
              <div class="mt-8">
                <h4 class="text-lg font-medium">Mock Interview</h4>
                <p class="mt-2 text-sm text-gray-500">Practice your interview skills</p>
              </div>
            </router-link>

            <router-link
              to="/ai-tutor"
              class="relative group bg-white p-6 focus-within:ring-2 focus-within:ring-inset focus-within:ring-primary-500 rounded-lg border border-gray-200 hover:border-primary-300 transition-colors"
            >
              <div>
                <span class="rounded-lg inline-flex p-3 bg-yellow-50 text-yellow-700 ring-4 ring-white">
                  <ChartBarSquareIcon class="h-6 w-6" />
                </span>
              </div>
              <div class="mt-8">
                <h4 class="text-lg font-medium">AI Tutor</h4>
                <p class="mt-2 text-sm text-gray-500">Get personalized career guidance</p>
              </div>
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
