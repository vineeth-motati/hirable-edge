<script setup lang="ts">
    import { ref, reactive } from 'vue';
    import { useRouter } from 'vue-router';
    import { useAuthStore } from '@/stores/auth';
    import { EyeIcon, EyeSlashIcon } from '@heroicons/vue/24/outline';

    const router = useRouter();
    const authStore = useAuthStore();

    const showPassword = ref(false);
    const showConfirmPassword = ref(false);
    const isLoading = ref(false);

    const form = reactive({
        first_name: '',
        last_name: '',
        email: '',
        password: '',
        confirmPassword: '',
        university: '',
        major: '',
    });

    const errors = ref<Record<string, string>>({});

    const validateForm = () => {
        errors.value = {};

        if (!form.first_name) {
            errors.value.first_name = 'First name is required';
        }

        if (!form.last_name) {
            errors.value.last_name = 'Last name is required';
        }

        if (!form.email) {
            errors.value.email = 'Email is required';
        } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(form.email)) {
            errors.value.email = 'Please enter a valid email address';
        }

        if (!form.password) {
            errors.value.password = 'Password is required';
        } else if (form.password.length < 6) {
            errors.value.password = 'Password must be at least 6 characters';
        }

        if (!form.confirmPassword) {
            errors.value.confirmPassword = 'Please confirm your password';
        } else if (form.password !== form.confirmPassword) {
            errors.value.confirmPassword = 'Passwords do not match';
        }

        return Object.keys(errors.value).length === 0;
    };

    const handleSubmit = async () => {
        if (!validateForm()) return;

        isLoading.value = true;

        try {
            const success = await authStore.register({
                email: form.email,
                password: form.password,
                first_name: form.first_name,
                last_name: form.last_name,
                university: form.university || undefined,
                major: form.major || undefined,
            });

            if (success) {
                router.push('/dashboard');
            }
        } finally {
            isLoading.value = false;
        }
    };

    const togglePasswordVisibility = () => {
        showPassword.value = !showPassword.value;
    };

    const toggleConfirmPasswordVisibility = () => {
        showConfirmPassword.value = !showConfirmPassword.value;
    };
</script>

<template>
    <div
        class="flex items-center justify-center min-h-screen px-4 py-12 bg-gray-50 sm:px-6 lg:px-8"
    >
        <div class="w-full max-w-md space-y-8">
            <div>
                <div
                    class="flex items-center justify-center w-12 h-12 mx-auto rounded-full bg-primary-600"
                >
                    <span class="text-xl font-bold text-white">H</span>
                </div>
                <h2 class="mt-6 text-3xl font-bold tracking-tight text-center text-gray-900">
                    Create your account
                </h2>
                <p class="mt-2 text-sm text-center text-gray-600">
                    Or
                    <router-link
                        to="/login"
                        class="font-medium text-primary-600 hover:text-primary-500"
                    >
                        sign in to your existing account
                    </router-link>
                </p>
            </div>

            <form class="mt-8 space-y-6" @submit.prevent="handleSubmit">
                <div class="space-y-4">
                    <div class="grid grid-cols-2 gap-4">
                        <div>
                            <label for="first_name" class="block text-sm font-medium text-gray-700">
                                First Name *
                            </label>
                            <div class="mt-1">
                                <input
                                    id="first_name"
                                    v-model="form.first_name"
                                    name="first_name"
                                    type="text"
                                    autocomplete="given-name"
                                    required
                                    class="relative block w-full px-3 py-2 text-gray-900 placeholder-gray-500 border border-gray-300 rounded-md appearance-none focus:outline-none focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
                                    :class="{
                                        'border-red-300 focus:ring-red-500 focus:border-red-500':
                                            errors.first_name,
                                    }"
                                    placeholder="First name"
                                />
                                <p v-if="errors.first_name" class="mt-1 text-xs text-red-600">
                                    {{ errors.first_name }}
                                </p>
                            </div>
                        </div>

                        <div>
                            <label for="last_name" class="block text-sm font-medium text-gray-700">
                                Last Name *
                            </label>
                            <div class="mt-1">
                                <input
                                    id="last_name"
                                    v-model="form.last_name"
                                    name="last_name"
                                    type="text"
                                    autocomplete="family-name"
                                    required
                                    class="relative block w-full px-3 py-2 text-gray-900 placeholder-gray-500 border border-gray-300 rounded-md appearance-none focus:outline-none focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
                                    :class="{
                                        'border-red-300 focus:ring-red-500 focus:border-red-500':
                                            errors.last_name,
                                    }"
                                    placeholder="Last name"
                                />
                                <p v-if="errors.last_name" class="mt-1 text-xs text-red-600">
                                    {{ errors.last_name }}
                                </p>
                            </div>
                        </div>
                    </div>

                    <div>
                        <label for="email" class="block text-sm font-medium text-gray-700">
                            Email Address *
                        </label>
                        <div class="mt-1">
                            <input
                                id="email"
                                v-model="form.email"
                                name="email"
                                type="email"
                                autocomplete="email"
                                required
                                class="relative block w-full px-3 py-2 text-gray-900 placeholder-gray-500 border border-gray-300 rounded-md appearance-none focus:outline-none focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
                                :class="{
                                    'border-red-300 focus:ring-red-500 focus:border-red-500':
                                        errors.email,
                                }"
                                placeholder="Enter your email"
                            />
                            <p v-if="errors.email" class="mt-2 text-sm text-red-600">
                                {{ errors.email }}
                            </p>
                        </div>
                    </div>

                    <div>
                        <label for="university" class="block text-sm font-medium text-gray-700">
                            University
                        </label>
                        <div class="mt-1">
                            <input
                                id="university"
                                v-model="form.university"
                                name="university"
                                type="text"
                                autocomplete="organization"
                                class="relative block w-full px-3 py-2 text-gray-900 placeholder-gray-500 border border-gray-300 rounded-md appearance-none focus:outline-none focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
                                placeholder="Your university (optional)"
                            />
                        </div>
                    </div>

                    <div>
                        <label for="major" class="block text-sm font-medium text-gray-700">
                            Major/Field of Study
                        </label>
                        <div class="mt-1">
                            <input
                                id="major"
                                v-model="form.major"
                                name="major"
                                type="text"
                                class="relative block w-full px-3 py-2 text-gray-900 placeholder-gray-500 border border-gray-300 rounded-md appearance-none focus:outline-none focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
                                placeholder="Your major (optional)"
                            />
                        </div>
                    </div>

                    <div>
                        <label for="password" class="block text-sm font-medium text-gray-700">
                            Password *
                        </label>
                        <div class="relative mt-1">
                            <input
                                id="password"
                                v-model="form.password"
                                name="password"
                                :type="showPassword ? 'text' : 'password'"
                                autocomplete="new-password"
                                required
                                class="relative block w-full px-3 py-2 pr-10 text-gray-900 placeholder-gray-500 border border-gray-300 rounded-md appearance-none focus:outline-none focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
                                :class="{
                                    'border-red-300 focus:ring-red-500 focus:border-red-500':
                                        errors.password,
                                }"
                                placeholder="Create a password"
                            />
                            <button
                                type="button"
                                class="absolute inset-y-0 right-0 flex items-center pr-3"
                                @click="togglePasswordVisibility"
                            >
                                <EyeIcon
                                    v-if="!showPassword"
                                    class="w-5 h-5 text-gray-400 hover:text-gray-500"
                                />
                                <EyeSlashIcon
                                    v-else
                                    class="w-5 h-5 text-gray-400 hover:text-gray-500"
                                />
                            </button>
                            <p v-if="errors.password" class="mt-2 text-sm text-red-600">
                                {{ errors.password }}
                            </p>
                        </div>
                    </div>

                    <div>
                        <label
                            for="confirmPassword"
                            class="block text-sm font-medium text-gray-700"
                        >
                            Confirm Password *
                        </label>
                        <div class="relative mt-1">
                            <input
                                id="confirmPassword"
                                v-model="form.confirmPassword"
                                name="confirmPassword"
                                :type="showConfirmPassword ? 'text' : 'password'"
                                autocomplete="new-password"
                                required
                                class="relative block w-full px-3 py-2 pr-10 text-gray-900 placeholder-gray-500 border border-gray-300 rounded-md appearance-none focus:outline-none focus:ring-primary-500 focus:border-primary-500 sm:text-sm"
                                :class="{
                                    'border-red-300 focus:ring-red-500 focus:border-red-500':
                                        errors.confirmPassword,
                                }"
                                placeholder="Confirm your password"
                            />
                            <button
                                type="button"
                                class="absolute inset-y-0 right-0 flex items-center pr-3"
                                @click="toggleConfirmPasswordVisibility"
                            >
                                <EyeIcon
                                    v-if="!showConfirmPassword"
                                    class="w-5 h-5 text-gray-400 hover:text-gray-500"
                                />
                                <EyeSlashIcon
                                    v-else
                                    class="w-5 h-5 text-gray-400 hover:text-gray-500"
                                />
                            </button>
                            <p v-if="errors.confirmPassword" class="mt-2 text-sm text-red-600">
                                {{ errors.confirmPassword }}
                            </p>
                        </div>
                    </div>
                </div>

                <!-- Display auth error -->
                <div v-if="authStore.error" class="p-4 rounded-md bg-red-50">
                    <div class="text-sm text-red-700">
                        {{ authStore.error }}
                    </div>
                </div>

                <div>
                    <button
                        type="submit"
                        :disabled="isLoading || authStore.isLoading"
                        class="relative flex justify-center w-full px-4 py-2 text-sm font-medium text-white border border-transparent rounded-md group bg-primary-600 hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary-500 disabled:opacity-50 disabled:cursor-not-allowed"
                    >
                        <span
                            v-if="isLoading || authStore.isLoading"
                            class="absolute inset-y-0 left-0 flex items-center pl-3"
                        >
                            <svg
                                class="w-5 h-5 mr-3 -ml-1 text-white animate-spin"
                                xmlns="http://www.w3.org/2000/svg"
                                fill="none"
                                viewBox="0 0 24 24"
                            >
                                <circle
                                    class="opacity-25"
                                    cx="12"
                                    cy="12"
                                    r="10"
                                    stroke="currentColor"
                                    stroke-width="4"
                                ></circle>
                                <path
                                    class="opacity-75"
                                    fill="currentColor"
                                    d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
                                ></path>
                            </svg>
                        </span>
                        {{
                            isLoading || authStore.isLoading
                                ? 'Creating account...'
                                : 'Create account'
                        }}
                    </button>
                </div>
            </form>
        </div>
    </div>
</template>
