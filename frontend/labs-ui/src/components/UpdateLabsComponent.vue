<template>
  <form
    @submit.prevent="submitForm"
    class="bg-white p-6 rounded-lg shadow-md space-y-4 max-w-md mx-auto"
  >
    <h2 class="text-2xl font-semibold text-gray-800">Update Lab</h2>

    <div>
      <label class="block text-sm font-medium text-gray-700 mb-1">Lab ID</label>
      <input
        v-model="form.labID"
        type="number"
        @wheel.prevent
        class="w-full border border-gray-300 rounded-md p-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
        required
      />
    </div>

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
      Update Lab
    </button>

    <p v-if="submitted && labResult" class="text-green-600 mt-2">
      Lab has been successfully updated!
    </p>
    <p v-if="submitted && labResult === false" class="text-yellow-600 mt-2">
      No lab found with that ID.
    </p>
    <p v-if="error" class="text-red-600 mt-2">
      Something went wrong. Please check console logs.
    </p>
  </form>
</template>

<script setup>
import { reactive, ref } from 'vue'
import api from '@/services/api'

// Form data
const form = reactive({
  labID: '',
  labName: '',
  labInstructor: '',
  labDescriptions: '',
})


const submitted = ref(false)
const error = ref(false)
const labResult = ref(null)

const submitForm = async () => {
  submitted.value = false
  error.value = false
  labResult.value = null

  try {
    const response = await api.updateLab(form.labID, {
      lab_name: form.labName,
      instructor: form.labInstructor,
      description: form.labDescriptions,
    })

    console.log('Successfully updated:', response.data)
    labResult.value = true 
    submitted.value = true

    form.labID = ''
    form.labName = ''
    form.labInstructor = ''
    form.labDescriptions = ''

    setTimeout(() => (submitted.value = false), 3000)
  } catch (err) {
    if (err.response && err.response.status === 404) {
      labResult.value = false
      submitted.value = true
    } else {
      error.value = true
    }
    console.error('Failed to update lab:', err)
    setTimeout(() => (error.value = false), 3000)
  }
}
</script>
