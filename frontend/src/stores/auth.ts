import { defineStore } from 'pinia';
import { ref, computed } from 'vue';
import { apiClient } from '@/services/api';

export interface User {
    id: string;
    email: string;
    role: 'student' | 'admin';
    is_active: boolean;
    is_verified: boolean;
    profile: {
        first_name: string;
        last_name: string;
        phone?: string;
        bio?: string;
        location?: string;
        university?: string;
        major?: string;
        graduation_year?: number;
        linkedin_url?: string;
        github_url?: string;
        portfolio_url?: string;
    };
    skills: {
        technical_skills: string[];
        soft_skills: string[];
        languages: string[];
        certifications: string[];
    };
    goals: {
        target_roles: string[];
        target_companies: string[];
        career_level?: string;
        preferred_locations: string[];
        salary_expectation?: string;
    };
    progress: {
        total_quizzes_taken: number;
        total_challenges_completed: number;
        total_interviews_completed: number;
        badges_earned: string[];
        total_points: number;
        level: number;
    };
    created_at: string;
    updated_at: string;
    last_login?: string;
}

export const useAuthStore = defineStore('auth', () => {
    const user = ref<User | null>(null);
    const token = ref<string | null>(localStorage.getItem('access_token'));
    const isLoading = ref(false);
    const error = ref<string | null>(null);

    const isAuthenticated = computed(() => !!token.value && !!user.value);
    const fullName = computed(() =>
        user.value ? `${user.value.profile.first_name} ${user.value.profile.last_name}` : '',
    );

    // Set auth header when token changes
    const setAuthHeader = (authToken: string | null) => {
        if (authToken) {
            apiClient.defaults.headers.common['Authorization'] = `Bearer ${authToken}`;
            localStorage.setItem('access_token', authToken);
        } else {
            delete apiClient.defaults.headers.common['Authorization'];
            localStorage.removeItem('access_token');
        }
    };

    const login = async (email: string, password: string) => {
        try {
            isLoading.value = true;
            error.value = null;

            const response = await apiClient.post('/auth/login', {
                email,
                password,
            });

            token.value = response.data.access_token;
            setAuthHeader(token.value);

            // Fetch user profile
            await fetchUserProfile();

            return true;
        } catch (err: any) {
            error.value = err.response?.data?.detail || 'Login failed';
            return false;
        } finally {
            isLoading.value = false;
        }
    };

    const register = async (userData: {
        email: string;
        password: string;
        first_name: string;
        last_name: string;
        university?: string;
        major?: string;
    }) => {
        try {
            isLoading.value = true;
            error.value = null;

            const response = await apiClient.post('/auth/register', userData);

            // Auto login after registration
            return await login(userData.email, userData.password);
        } catch (err: any) {
            error.value = err.response?.data?.detail || 'Registration failed';
            return false;
        } finally {
            isLoading.value = false;
        }
    };

    const fetchUserProfile = async () => {
        try {
            const response = await apiClient.get('/users/me');
            user.value = response.data;
        } catch (err: any) {
            error.value = 'Failed to fetch user profile';
            logout();
        }
    };

    const updateProfile = async (profileData: Partial<User>) => {
        try {
            isLoading.value = true;
            error.value = null;

            const response = await apiClient.put('/users/me', profileData);
            user.value = response.data;

            return true;
        } catch (err: any) {
            error.value = err.response?.data?.detail || 'Profile update failed';
            return false;
        } finally {
            isLoading.value = false;
        }
    };

    const logout = () => {
        user.value = null;
        token.value = null;
        setAuthHeader(null);
        error.value = null;
    };

    // Initialize auth state on store creation
    if (token.value) {
        setAuthHeader(token.value);
        fetchUserProfile();
    }

    return {
        user,
        token,
        isLoading,
        error,
        isAuthenticated,
        fullName,
        login,
        register,
        fetchUserProfile,
        updateProfile,
        logout,
    };
});
