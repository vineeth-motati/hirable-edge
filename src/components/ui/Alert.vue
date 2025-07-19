<script setup lang="ts">
    import { computed } from 'vue';
    import {
        XMarkIcon,
        CheckCircleIcon,
        XCircleIcon,
        ExclamationTriangleIcon,
        InformationCircleIcon,
    } from '@heroicons/vue/24/outline';

    interface Props {
        type?: 'success' | 'error' | 'warning' | 'info';
        title?: string;
        message: string;
        dismissible?: boolean;
        show: boolean;
    }

    const props = withDefaults(defineProps<Props>(), {
        type: 'info',
        dismissible: true,
    });

    const emit = defineEmits<{
        dismiss: [];
    }>();

    const typeConfig = computed(() => {
        const configs = {
            success: {
                bgClass: 'bg-green-50',
                borderClass: 'border-green-200',
                textClass: 'text-green-800',
                titleClass: 'text-green-900',
                icon: CheckCircleIcon,
                iconClass: 'text-green-400',
            },
            error: {
                bgClass: 'bg-red-50',
                borderClass: 'border-red-200',
                textClass: 'text-red-800',
                titleClass: 'text-red-900',
                icon: XCircleIcon,
                iconClass: 'text-red-400',
            },
            warning: {
                bgClass: 'bg-yellow-50',
                borderClass: 'border-yellow-200',
                textClass: 'text-yellow-800',
                titleClass: 'text-yellow-900',
                icon: ExclamationTriangleIcon,
                iconClass: 'text-yellow-400',
            },
            info: {
                bgClass: 'bg-blue-50',
                borderClass: 'border-blue-200',
                textClass: 'text-blue-800',
                titleClass: 'text-blue-900',
                icon: InformationCircleIcon,
                iconClass: 'text-blue-400',
            },
        };
        return configs[props.type];
    });

    const handleDismiss = () => {
        emit('dismiss');
    };
</script>

<template>
    <Transition
        enter-active-class="transition duration-150 ease-out"
        enter-from-class="transform scale-95 opacity-0"
        enter-to-class="transform scale-100 opacity-100"
        leave-active-class="transition duration-100 ease-in"
        leave-from-class="transform scale-100 opacity-100"
        leave-to-class="transform scale-95 opacity-0"
    >
        <div
            v-if="show"
            class="p-4 border rounded-md"
            :class="[typeConfig.bgClass, typeConfig.borderClass]"
        >
            <div class="flex">
                <div class="flex-shrink-0">
                    <component
                        :is="typeConfig.icon"
                        class="w-5 h-5"
                        :class="typeConfig.iconClass"
                    />
                </div>
                <div class="flex-1 ml-3">
                    <h3 v-if="title" class="text-sm font-medium" :class="typeConfig.titleClass">
                        {{ title }}
                    </h3>
                    <div class="text-sm" :class="[typeConfig.textClass, title ? 'mt-1' : '']">
                        {{ message }}
                    </div>
                </div>
                <div v-if="dismissible" class="pl-3 ml-auto">
                    <div class="-mx-1.5 -my-1.5">
                        <button
                            type="button"
                            @click="handleDismiss"
                            class="inline-flex rounded-md p-1.5 focus:outline-none focus:ring-2 focus:ring-offset-2 hover:opacity-75"
                            :class="[typeConfig.textClass, 'focus:ring-' + type + '-500']"
                        >
                            <span class="sr-only">Dismiss</span>
                            <XMarkIcon class="w-5 h-5" />
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </Transition>
</template>
