
<template>
    <main>
        <header>
            <img src="./assets/todo.png" alt="To-do list logo">
            <h1>Todo List items!</h1>
        </header>
        
        <div class="new-task-form">
            <TaskForm />
        </div>

        <nav class="filter">
            <button @click="filter='all'">All List</button>
            <button @click="filter='favs'">Favs List</button>
        </nav>

        <div class="loading" v-if="TaskStore.loading">
            Loading...
        </div>

        <div class="task-list" v-if="filter==='all'">
            <p>{{ TaskStore.totalCount }} Task left to</p>
            <div v-for="task in TaskStore.tasks" :key="task.id">
                <TaskDetails :task="task"></TaskDetails>
            </div>
        </div>

        <div class="task-list" v-if="filter==='favs'">
            <p>{{ TaskStore.favCount }} Tasks left to</p>
            <div v-for="task in TaskStore.favs" :key="task.id">
                <TaskDetails :task="task"></TaskDetails>
            </div>
        </div>
    </main>

</template>

<script setup>

import TaskDetails from './components/TaskDetails.vue';
import TaskForm from './components/TaskForm.vue';
import { useTaskStore } from './stores/TaskStore';
import { ref } from 'vue';

const TaskStore = ref(useTaskStore());
const filter = ref('all');

TaskStore.getTasks()

</script>

<style scoped>
</style>