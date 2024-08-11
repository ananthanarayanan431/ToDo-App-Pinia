
<template>
    <form @submit.prevent="handlesubmit">
        <input type="text" placeholder="I need to..." v-model="newTask">
        <button type="submit">Add</button>
    </form>
</template>

<script setup>

import { ref } from 'vue';
import { useTaskStore } from '@/stores/TaskStore';

const TaskStore = useTaskStore();
const newTask = ref("");

const handlesubmit = ()=> {
    if (newTask.value.trim().length>0) {
        TaskStore.addTask({
            title: newTask.value,
            isFav:false,
            id: Math.floor(Math.round()*1000),
        });
        newTask.value="";
    }

}

</script>

<style scoped>
</style>