<template>
  <div id="app" class="min-h-screen bg-gray-100">
    <nav class="bg-gray-800 p-4">
      <div class="flex flex-col space-y-6 sm:flex-row sm:space-y-0 sm:space-x-4 justify-center items-center">
        <button
          v-for="item in navItems"
          :key="item.name"
          @click="activeComponent = item.component"
          class="text-white bg-gray-700 hover:bg-gray-600 px-4 py-2 rounded-md transition-colors w-full sm:w-auto"
        >
          {{ item.label }}
        </button>
      </div>
    </nav>

    <!-- Main Content -->
    <main class=" place-items-center min-h-screen bg-white">
      <component :is="activeComponent" />
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue'

import AddLabsComponent from './components/AddLabsComponent.vue'
import ListLabsComponent from './components/ListLabsComponent.vue'
import DeleteLabsComponent from './components/DeleteLabsComponent.vue'
import SearchLabsComponent from './components/SearchLabsComponent.vue'
import UpdateLabsComponent from './components/UpdateLabsComponent.vue'
import WelcomeComponent from './components/WelcomeComponent.vue' 

const activeComponent = ref(WelcomeComponent)

const navItems = [
  { name: 'All List', label: 'Lab List', component: ListLabsComponent },
  { name: 'Add Lab', label: 'Add Lab', component: AddLabsComponent },
  { name: 'Search Labs', label: 'Search Labs', component: SearchLabsComponent },
  { name: 'Update Labs', label: 'Update Labs', component: UpdateLabsComponent },
  { name: 'Delete Lab', label: 'Delete Lab', component: DeleteLabsComponent },
]

</script>

