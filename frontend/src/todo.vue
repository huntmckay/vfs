<template>
  <div class="todo">
      <todo_comp/>
  </div>
</template>

<script>
// @ is an alias to /src
import todo_comp from '@/components/todo_comp.vue'
export default {
  name: 'todo',
  components: {
    todo_comp,
  }
}
</script>