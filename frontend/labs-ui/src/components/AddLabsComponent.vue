<template>
  <form @submit.prevent="submitForm" class="bg-white p-6 space-x-6 rounded-lg shadow-md space-y-4 max-w-md mx-auto">
    <h2 class="text-2xl font-semibold text-gray-800">Add New Lab</h2>
    <div>
      <label class="block text-sm font-medium text-gray-700 mb-1">Lab Name</label>
      <input
        v-model="form.labName"
        type="text"
        class="w-full border border-gray-300 rounded-md p-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
        required
      />
    </div>
    <div>
      <label class="block text-sm font-medium text-gray-700 mb-1">Instructor</label>
      <input
        v-model="form.labInstructor"
        type="text"
        class="w-full border border-gray-300 rounded-md p-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
        required
      />
    </div>
    <div>
      <label class="block text-sm font-medium text-gray-700 mb-1">Descriptions</label>
      <textarea
        v-model="form.labDescriptions"
        rows="4"
        class="w-full border border-gray-300 rounded-md p-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
        required
      ></textarea>
    </div>
    <button
      type="submit"
      class="w-full bg-blue-600 text-white py-2 rounded-md hover:bg-blue-700 transition"
    >
      Submit
    </button>

    <p v-if="submitted" class="text-green-600 mt-2">Your Lab is Created!</p>
    <p v-if="conflicError" class="text-red-600 mt-2">Lab Name is already existing!</p>
    <p v-if="unknownError" class="text-red-600 mt-2">Something went wrong. Please check console logs</p>
  </form>
</template>

<script setup>
  import { reactive, ref } from 'vue'
  import api from '@/services/api' // Make sure your API service path is correct

  const form = reactive({
    labName: '',
    labInstructor: '',
    labDescriptions: '',
  })

  const submitted = ref(false)
  const unknownError = ref(false)
  const conflicError = ref(false)

  const submitForm = async () => {
    submitted.value = false
    unknownError.value = false
    conflicError.value = false

    try {
      const response = await api.createLab({
        lab_name: form.labName,
        instructor: form.labInstructor,
        description: form.labDescriptions,
      })

      console.log('Successfully created:', response.data)
      submitted.value = true

      // Reset form
      form.labName = ''
      form.labInstructor = ''
      form.labDescriptions = ''

      setTimeout(() => (submitted.value = false), 3000)

    } catch (err) {
      console.error('Failed to submit form:', err)
      if(err.code =="ERR_NETWORK") {unknownError.value = true};
      if (err.response.status === 400) {
        conflicError.value = true;
      }
      else{
        unknownError.value = true;
      }

      setTimeout(() => (conflicError.value = false, unknownError.value = false), 3000)
    }
  }
</script>
