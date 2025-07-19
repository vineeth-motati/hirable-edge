<script setup lang="ts">
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { 
  AcademicCapIcon, 
  CodeBracketIcon, 
  ChatBubbleLeftRightIcon,
  DocumentTextIcon,
  SparklesIcon,
  TrophyIcon
} from '@heroicons/vue/24/outline'

const router = useRouter()
const authStore = useAuthStore()

const features = [
  {
    name: 'Skill Assessment Quizzes',
    description: 'Take timed quizzes to assess your technical and soft skills across various domains.',
    icon: AcademicCapIcon,
  },
  {
    name: 'Coding Challenges',
    description: 'Solve coding problems with different difficulty levels and get instant feedback.',
    icon: CodeBracketIcon,
  },
  {
    name: 'Mock Interviews',
    description: 'Practice mock interviews with AI-driven feedback to improve your performance.',
    icon: ChatBubbleLeftRightIcon,
  },
  {
    name: 'Resume Builder',
    description: 'Create and optimize your resume based on job descriptions and industry standards.',
    icon: DocumentTextIcon,
  },
  {
    name: 'AI Career Tutor',
    description: 'Get personalized career guidance and learning recommendations from our AI tutor.',
    icon: SparklesIcon,
  },
  {
    name: 'Achievements & Badges',
    description: 'Earn badges and track your progress as you complete challenges and assessments.',
    icon: TrophyIcon,
  },
]

const stats = [
  { id: 1, name: 'Students Helped', value: '10,000+' },
  { id: 2, name: 'Success Rate', value: '85%' },
  { id: 3, name: 'Practice Questions', value: '1,000+' },
  { id: 4, name: 'Partner Companies', value: '50+' },
]

const navigateToAuth = (type: 'login' | 'register') => {
  router.push(`/${type}`)
}

// Redirect to dashboard if already authenticated
if (authStore.isAuthenticated) {
  router.push('/dashboard')
}
</script>

<template>
  <div class="bg-white">
    <!-- Hero section -->
    <div class="relative isolate px-6 pt-14 lg:px-8">
      <div class="absolute inset-x-0 -top-40 -z-10 transform-gpu overflow-hidden blur-3xl sm:-top-80" aria-hidden="true">
        <div class="relative left-[calc(50%-11rem)] aspect-[1155/678] w-[36.125rem] -translate-x-1/2 rotate-[30deg] bg-gradient-to-tr from-[#ff80b5] to-[#9089fc] opacity-30 sm:left-[calc(50%-30rem)] sm:w-[72.1875rem]"></div>
      </div>
      
      <div class="mx-auto max-w-2xl py-32 sm:py-48 lg:py-56">
        <div class="hidden sm:mb-8 sm:flex sm:justify-center">
          <div class="relative rounded-full px-3 py-1 text-sm leading-6 text-gray-600 ring-1 ring-gray-900/10 hover:ring-gray-900/20">
            Boost your job readiness with AI-powered tools. 
            <a href="#features" class="font-semibold text-primary-600">
              <span class="absolute inset-0" aria-hidden="true"></span>
              Learn more <span aria-hidden="true">&rarr;</span>
            </a>
          </div>
        </div>
        
        <div class="text-center">
          <h1 class="text-4xl font-bold tracking-tight text-gray-900 sm:text-6xl">
            Master Your <span class="text-primary-600">Career Journey</span>
          </h1>
          <p class="mt-6 text-lg leading-8 text-gray-600">
            HirableEdge helps students and professionals improve their job hirability through 
            quizzes, coding challenges, mock interviews, and personalized career roadmaps powered by AI.
          </p>
          <div class="mt-10 flex items-center justify-center gap-x-6">
            <button 
              @click="navigateToAuth('register')"
              class="rounded-md bg-primary-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-primary-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-600"
            >
              Get started
            </button>
            <button 
              @click="navigateToAuth('login')"
              class="text-sm font-semibold leading-6 text-gray-900 hover:text-primary-600"
            >
              Sign in <span aria-hidden="true">→</span>
            </button>
          </div>
        </div>
      </div>
      
      <div class="absolute inset-x-0 top-[calc(100%-13rem)] -z-10 transform-gpu overflow-hidden blur-3xl sm:top-[calc(100%-30rem)]" aria-hidden="true">
        <div class="relative left-[calc(50%+3rem)] aspect-[1155/678] w-[36.125rem] -translate-x-1/2 bg-gradient-to-tr from-[#ff80b5] to-[#9089fc] opacity-30 sm:left-[calc(50%+36rem)] sm:w-[72.1875rem]"></div>
      </div>
    </div>

    <!-- Feature section -->
    <div id="features" class="mx-auto max-w-7xl px-6 lg:px-8 py-24 sm:py-32">
      <div class="mx-auto max-w-2xl lg:text-center">
        <h2 class="text-base font-semibold leading-7 text-primary-600">Level Up Your Skills</h2>
        <p class="mt-2 text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">
          Everything you need to land your dream job
        </p>
        <p class="mt-6 text-lg leading-8 text-gray-600">
          Our comprehensive platform provides all the tools and resources you need to assess, 
          improve, and showcase your skills to potential employers.
        </p>
      </div>
      
      <div class="mx-auto mt-16 max-w-2xl sm:mt-20 lg:mt-24 lg:max-w-4xl">
        <dl class="grid max-w-xl grid-cols-1 gap-x-8 gap-y-10 lg:max-w-none lg:grid-cols-2 lg:gap-y-16">
          <div v-for="feature in features" :key="feature.name" class="relative pl-16">
            <dt class="text-base font-semibold leading-7 text-gray-900">
              <div class="absolute left-0 top-0 flex h-10 w-10 items-center justify-center rounded-lg bg-primary-600">
                <component :is="feature.icon" class="h-6 w-6 text-white" aria-hidden="true" />
              </div>
              {{ feature.name }}
            </dt>
            <dd class="mt-2 text-base leading-7 text-gray-600">{{ feature.description }}</dd>
          </div>
        </dl>
      </div>
    </div>

    <!-- Stats section -->
    <div class="bg-gray-50 py-24 sm:py-32">
      <div class="mx-auto max-w-7xl px-6 lg:px-8">
        <div class="mx-auto max-w-2xl lg:max-w-none">
          <div class="text-center">
            <h2 class="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">
              Trusted by thousands of students
            </h2>
            <p class="mt-4 text-lg leading-8 text-gray-600">
              Join the community of successful job seekers who have used HirableEdge to advance their careers.
            </p>
          </div>
          <dl class="mt-16 grid grid-cols-1 gap-0.5 overflow-hidden rounded-2xl text-center sm:grid-cols-2 lg:grid-cols-4">
            <div v-for="stat in stats" :key="stat.id" class="flex flex-col bg-white px-8 py-10">
              <dt class="text-sm font-semibold leading-6 text-gray-600">{{ stat.name }}</dt>
              <dd class="order-first text-3xl font-bold tracking-tight text-primary-600">{{ stat.value }}</dd>
            </div>
          </dl>
        </div>
      </div>
    </div>

    <!-- CTA section -->
    <div class="bg-primary-600">
      <div class="px-6 py-24 sm:px-6 sm:py-32 lg:px-8">
        <div class="mx-auto max-w-2xl text-center">
          <h2 class="text-3xl font-bold tracking-tight text-white sm:text-4xl">
            Ready to boost your career?<br />Start your journey today.
          </h2>
          <p class="mx-auto mt-6 max-w-xl text-lg leading-8 text-primary-200">
            Join thousands of students who have already improved their job prospects with HirableEdge.
          </p>
          <div class="mt-10 flex items-center justify-center gap-x-6">
            <button 
              @click="navigateToAuth('register')"
              class="rounded-md bg-white px-3.5 py-2.5 text-sm font-semibold text-primary-600 shadow-sm hover:bg-primary-50 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-white"
            >
              Get started
            </button>
            <button 
              @click="navigateToAuth('login')"
              class="text-sm font-semibold leading-6 text-white hover:text-primary-100"
            >
              Sign in <span aria-hidden="true">→</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
