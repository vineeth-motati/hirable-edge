<script setup lang="ts">
import { useNotifications } from '@/composables/useNotifications'
import Alert from '@/components/ui/Alert.vue'

const { notifications, removeNotification } = useNotifications()
</script>

<template>
  <div class="fixed top-0 right-0 z-50 p-4 space-y-4">
    <Alert
      v-for="notification in notifications"
      :key="notification.id"
      :type="notification.type"
      :title="notification.title"
      :message="notification.message"
      :dismissible="notification.dismissible"
      :show="true"
      @dismiss="removeNotification(notification.id)"
    />
  </div>
</template>
