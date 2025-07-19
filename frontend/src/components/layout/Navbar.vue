<script setup lang="ts">
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import {
  Disclosure,
  DisclosureButton,
  DisclosurePanel,
  Menu,
  MenuButton,
  MenuItem,
  MenuItems
} from '@headlessui/vue'
import {
  Bars3Icon,
  XMarkIcon,
  UserCircleIcon,
  ChevronDownIcon
} from '@heroicons/vue/24/outline'
import {
  HomeIcon,
  AcademicCapIcon,
  CodeBracketIcon,
  ChatBubbleLeftRightIcon,
  DocumentTextIcon,
  MapIcon,
  SparklesIcon,
  TrophyIcon,
  ChartBarIcon
} from '@heroicons/vue/24/solid'

const router = useRouter()
const authStore = useAuthStore()

const navigation = [
  { name: 'Dashboard', to: '/dashboard', icon: HomeIcon, current: false },
  { name: 'Quizzes', to: '/quizzes', icon: AcademicCapIcon, current: false },
  { name: 'Challenges', to: '/challenges', icon: CodeBracketIcon, current: false },
  { name: 'Mock Interviews', to: '/interviews', icon: ChatBubbleLeftRightIcon, current: false },
  { name: 'Resume Builder', to: '/resume-builder', icon: DocumentTextIcon, current: false },
  { name: 'Career Roadmap', to: '/career-roadmap', icon: MapIcon, current: false },
  { name: 'AI Tutor', to: '/ai-tutor', icon: SparklesIcon, current: false },
  { name: 'Achievements', to: '/achievements', icon: TrophyIcon, current: false },
  { name: 'Leaderboard', to: '/leaderboard', icon: ChartBarIcon, current: false }
]

const currentRoute = computed(() => router.currentRoute.value.path)

const isCurrentRoute = (path: string) => {
  return currentRoute.value === path || currentRoute.value.startsWith(path + '/')
}

const handleLogout = () => {
  authStore.logout()
  router.push('/login')
}
</script>

<template>
  <Disclosure as="nav" class="bg-white shadow-sm border-b fixed w-full top-0 z-50" v-slot="{ open }">
    <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
      <div class="flex h-16 justify-between">
        <div class="flex">
          <!-- Logo -->
          <div class="flex flex-shrink-0 items-center">
            <router-link to="/dashboard" class="flex items-center">
              <span class="text-2xl font-bold text-primary-600">HirableEdge</span>
            </router-link>
          </div>
          
          <!-- Desktop Navigation -->
          <div class="hidden sm:ml-6 sm:flex sm:space-x-8">
            <router-link
              v-for="item in navigation"
              :key="item.name"
              :to="item.to"
              class="inline-flex items-center px-1 pt-1 text-sm font-medium transition-colors duration-200"
              :class="isCurrentRoute(item.to)
                ? 'border-b-2 border-primary-500 text-gray-900'
                : 'border-b-2 border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700'"
            >
              <component :is="item.icon" class="mr-2 h-4 w-4" />
              {{ item.name }}
            </router-link>
          </div>
        </div>

        <!-- User Menu -->
        <div class="hidden sm:ml-6 sm:flex sm:items-center">
          <Menu as="div" class="relative ml-3">
            <div>
              <MenuButton class="flex max-w-xs items-center rounded-full bg-white text-sm focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2">
                <span class="sr-only">Open user menu</span>
                <div class="flex items-center space-x-2">
                  <UserCircleIcon class="h-8 w-8 text-gray-400" />
                  <span class="text-gray-700">{{ authStore.fullName || 'User' }}</span>
                  <ChevronDownIcon class="h-4 w-4 text-gray-400" />
                </div>
              </MenuButton>
            </div>
            <transition
              enter-active-class="transition ease-out duration-200"
              enter-from-class="transform opacity-0 scale-95"
              enter-to-class="transform opacity-100 scale-100"
              leave-active-class="transition ease-in duration-75"
              leave-from-class="transform opacity-100 scale-100"
              leave-to-class="transform opacity-0 scale-95"
            >
              <MenuItems class="absolute right-0 z-10 mt-2 w-48 origin-top-right rounded-md bg-white py-1 shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none">
                <MenuItem v-slot="{ active }">
                  <router-link
                    to="/profile"
                    :class="[active ? 'bg-gray-100' : '', 'block px-4 py-2 text-sm text-gray-700']"
                  >
                    Your Profile
                  </router-link>
                </MenuItem>
                <MenuItem v-slot="{ active }">
                  <button
                    @click="handleLogout"
                    :class="[active ? 'bg-gray-100' : '', 'block w-full text-left px-4 py-2 text-sm text-gray-700']"
                  >
                    Sign out
                  </button>
                </MenuItem>
              </MenuItems>
            </transition>
          </Menu>
        </div>

        <!-- Mobile menu button -->
        <div class="-mr-2 flex items-center sm:hidden">
          <DisclosureButton class="inline-flex items-center justify-center rounded-md bg-white p-2 text-gray-400 hover:bg-gray-100 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2">
            <span class="sr-only">Open main menu</span>
            <Bars3Icon v-if="!open" class="block h-6 w-6" aria-hidden="true" />
            <XMarkIcon v-else class="block h-6 w-6" aria-hidden="true" />
          </DisclosureButton>
        </div>
      </div>
    </div>

    <!-- Mobile Navigation -->
    <DisclosurePanel class="sm:hidden">
      <div class="space-y-1 pb-3 pt-2">
        <router-link
          v-for="item in navigation"
          :key="item.name"
          :to="item.to"
          class="flex items-center border-l-4 py-2 pl-3 pr-4 text-base font-medium transition-colors duration-200"
          :class="isCurrentRoute(item.to)
            ? 'border-primary-500 bg-primary-50 text-primary-700'
            : 'border-transparent text-gray-600 hover:border-gray-300 hover:bg-gray-50 hover:text-gray-800'"
        >
          <component :is="item.icon" class="mr-3 h-5 w-5" />
          {{ item.name }}
        </router-link>
      </div>
      <div class="border-t border-gray-200 pb-3 pt-4">
        <div class="flex items-center px-4">
          <div class="flex-shrink-0">
            <UserCircleIcon class="h-10 w-10 text-gray-400" />
          </div>
          <div class="ml-3">
            <div class="text-base font-medium text-gray-800">{{ authStore.fullName || 'User' }}</div>
            <div class="text-sm font-medium text-gray-500">{{ authStore.user?.email }}</div>
          </div>
        </div>
        <div class="mt-3 space-y-1">
          <router-link
            to="/profile"
            class="block px-4 py-2 text-base font-medium text-gray-500 hover:bg-gray-100 hover:text-gray-800"
          >
            Your Profile
          </router-link>
          <button
            @click="handleLogout"
            class="block w-full text-left px-4 py-2 text-base font-medium text-gray-500 hover:bg-gray-100 hover:text-gray-800"
          >
            Sign out
          </button>
        </div>
      </div>
    </DisclosurePanel>
  </Disclosure>
</template>
