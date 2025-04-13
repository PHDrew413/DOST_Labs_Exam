<template>
  <form @submit.prevent="submitForm" class="bg-white p-6 rounded-lg shadow-md space-y-4 max-w-md mx-auto">
    <h2 class="text-2xl font-semibold text-gray-800">Delete Lab</h2>
    <div>
      <label class="block text-sm font-medium text-gray-700 mb-1">Lab ID</label>
      <input
        v-model="form.labID"
        type="number"
        class="w-full border border-gray-300 rounded-md p-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
        required
      />
    </div>
    <button
      type="submit"
      class="w-full bg-red-600 text-white py-2 rounded-md hover:bg-red-700 transition"
    >
      Delete Lab
    </button>
    <p v-if="submitted" class="text-green-600 mt-2">Lab has been successfully deleted!</p>
    <p v-if="notFoundError" class="text-red-600 mt-2">Lab is not existing!</p>
    <p v-if="error" class="text-red-600 mt-2">Something went wrong. Please check console logs</p>
  </form>
</template>

<script setup>
  import { reactive, ref } from 'vue'
  import api from '@/services/api'

  const form = reactive({
    labID: ''
  })

  const submitted = ref(false)
  const notFoundError = ref(false)
  const error = ref(false)

  const submitForm = async () => {
    submitted.value = false
    error.value = false

    try {
      const response = await api.deleteLab(form.labID)
      console.log('Deleted lab:', response.data)

      submitted.value = true
      form.labID = ''

      setTimeout(() => (submitted.value = false), 3000)

    } catch (err) {
      console.error('Error deleting lab:', err)
      if (err.response.status === 404) {
        notFoundError.value = true;
      }
      else{
        error.value = true;
      }
      setTimeout(() => (error.value = false, notFoundError.value = false), 3000)
    }
  }
</script>
