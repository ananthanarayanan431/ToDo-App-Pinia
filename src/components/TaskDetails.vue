
<template>
    <div class="task">
      <h3>{{ props.task.title }}</h3>
      <div class="icons">
        <i class="material-icons" @click="TaskStore.deleteTask(task.id)">delete</i>
        <i class="material-icons" :class="{active: task.isFav}" @click="TaskStore.togglefav(task.id)">favorite</i>
      </div>
    </div>
  </template>

<script setup>
import { useTaskStore } from '@/stores/TaskStore';

const TaskStore = useTaskStore();
const props = defineProps({
    task: {
        type:Object,
        required:true,
    },
})
</script>
<style scoped>
</style>