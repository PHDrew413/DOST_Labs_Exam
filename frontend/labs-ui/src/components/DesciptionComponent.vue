<template>
  <div>
    <button @click="openDialog = true" class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-400">
      More Details
    </button>

    <!-- Dialog Overlay -->
    <div
      v-if="openDialog"
      class="fixed inset-0 backdrop-blur-sm bg-opacity-50 flex items-center justify-center z-50"
    >
      <!-- Dialog Box -->
      <div class="bg-white p-6 rounded-lg shadow-lg max-w-md w-full">
        <h2 class="text-xl font-bold mb-4">Lab Name: {{ message.lab_name }}</h2>
        <p class="mb-4">ID: {{ message.id }}</p>
        <p class="mb-4">Instructor: {{ message.instructor }}</p>
        <p class="mb-4">Description: {{ message.description }}</p>
        <div class="flex justify-end space-x-2">
          <button @click="openDialog = false" class="px-4 py-2 bg-blue-500 hover:bg-blue-300 text-white rounded">
            Exit
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

  const props = defineProps({
    message: {
      type: Object,
      required: true
    }
  })
  const openDialog = ref(false)

</script>
