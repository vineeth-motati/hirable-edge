import { ref, reactive } from 'vue';

export interface Notification {
    id: string;
    type: 'success' | 'error' | 'warning' | 'info';
    title?: string;
    message: string;
    duration?: number;
    dismissible?: boolean;
}

const notifications = ref<Notification[]>([]);

export const useNotifications = () => {
    const addNotification = (notification: Omit<Notification, 'id'>) => {
        const id = Date.now().toString();
        const newNotification: Notification = {
            id,
            duration: 5000,
            dismissible: true,
            ...notification,
        };

        notifications.value.push(newNotification);

        // Auto dismiss if duration is set
        if (newNotification.duration && newNotification.duration > 0) {
            setTimeout(() => {
                removeNotification(id);
            }, newNotification.duration);
        }

        return id;
    };

    const removeNotification = (id: string) => {
        const index = notifications.value.findIndex((n) => n.id === id);
        if (index > -1) {
            notifications.value.splice(index, 1);
        }
    };

    const clearAll = () => {
        notifications.value = [];
    };

    // Convenience methods
    const success = (message: string, title?: string, options?: Partial<Notification>) =>
        addNotification({ type: 'success', message, title, ...options });

    const error = (message: string, title?: string, options?: Partial<Notification>) =>
        addNotification({ type: 'error', message, title, ...options });

    const warning = (message: string, title?: string, options?: Partial<Notification>) =>
        addNotification({ type: 'warning', message, title, ...options });

    const info = (message: string, title?: string, options?: Partial<Notification>) =>
        addNotification({ type: 'info', message, title, ...options });

    return {
        notifications: notifications,
        addNotification,
        removeNotification,
        clearAll,
        success,
        error,
        warning,
        info,
    };
};
