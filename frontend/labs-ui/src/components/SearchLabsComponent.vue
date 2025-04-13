<template>
  <form @submit.prevent="submitForm" class="bg-white p-6 rounded-lg shadow-md space-y-4 max-w-md mx-auto">
    <h2 class="text-2xl font-semibold text-gray-800">Search Lab</h2>

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
      class="w-full bg-blue-600 text-white py-2 rounded-md hover:bg-blue-700 transition"
    >
      Search
    </button>

    <div v-if="labResult" class="mt-4 p-4 border rounded-md bg-gray-100">
      <h3 class="text-lg font-semibold mb-2 text-gray-800">Lab Details:</h3>
      <p><strong>ID:</strong> {{ labResult.id }}</p>
      <p><strong>Name:</strong> {{ labResult.lab_name }}</p>
      <p><strong>Instructor:</strong> {{ labResult.instructor }}</p>
      <p><strong>Description:</strong> {{ labResult.description }}</p>
    </div>

    <p v-if="submitted && !labResult" class="text-yellow-600 mt-2">No lab found with that ID.</p>
    <p v-if="error" class="text-red-600 mt-2">Something went wrong. Please check console logs</p>
  </form>
</template>

<script setup>
  import { reactive, ref } from 'vue'
  import api from '@/services/api'

  const form = reactive({
    labID: ''
  })

  const labResult = ref(null)
  const submitted = ref(false)
  const error = ref(false)

  const submitForm = async () => {
    submitted.value = false
    error.value = false
    labResult.value = null

    try {
      const response = await api.getLab(form.labID)
      labResult.value = response.data
      console.log(labResult.value)
      submitted.value = true
    } catch (err) {
      if (err.response && err.response.status === 404) {
        labResult.value = null
        submitted.value = true
      } else {
        console.error('Error searching for lab:', err)
        error.value = true
      }

      setTimeout(() => {
        error.value = false
      }, 3000)
    }
  }
</script>
