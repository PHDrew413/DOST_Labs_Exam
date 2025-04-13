<template>
  <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6 p-6">
    <div
      v-for="(card, index) in cards"
      :key="index"
      class="bg-white shadow-md rounded-2xl overflow-hidden hover:shadow-xl transition-shadow"
    >
      <div class="p-4">
        <h3 class="text-xl font-semibold mb-2">{{ card.lab_name }}</h3>
        <p class="text-gray-600 mb-4">{{ card.instructor }}</p>
        <DescriptionComponent :message="card"/>
      </div>
    </div>
  </div>
  <div v-if="cards == 0" class="bg-blue-100 border border-blue-400 text-blue-700 px-4 py-3 rounded relative" role="alert">
    <strong class="font-bold">Information: </strong>
    <span class="block sm:inline">No Labs Recorded</span>
  </div>
  <div v-if="error == true" class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
    <strong class="font-bold">Error: </strong>
    <span class="block sm:inline">Something went wrong. Please check console logs</span>
  </div>
</template>

<script setup>
  import { ref, onMounted } from 'vue'
  import DescriptionComponent from './DesciptionComponent.vue' 
  import api from '@/services/api'

  const cards = ref([])
  const error = ref(false)

  onMounted(async () => {
    try {
      const response = await api.getLabs()
      console.log(response.data)
      error.value = false
      cards.value = response.data 
    } catch (err) {
      console.error('Error fetching labs:', err)
      error.value = true
    }
  })
</script>
