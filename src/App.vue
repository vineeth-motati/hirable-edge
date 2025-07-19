<script setup lang="ts">
    import { useAuthStore } from '@/stores/auth';
    import Navbar from '@/components/layout/Navbar.vue';
    import NotificationContainer from '@/components/ui/NotificationContainer.vue';

    const authStore = useAuthStore();
</script>

<template>
    <div class="min-h-screen bg-gray-50">
        <!-- Navigation -->
        <Navbar v-if="authStore.isAuthenticated" />

        <!-- Main Content -->
        <main class="transition-all duration-300" :class="authStore.isAuthenticated ? 'pt-16' : ''">
            <RouterView />
        </main>

        <!-- Global Notifications -->
        <NotificationContainer />
    </div>
</template>

<style>
    /* Global styles are handled in style.css with TailwindCSS */
</style>
