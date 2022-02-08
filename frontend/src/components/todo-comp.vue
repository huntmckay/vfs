<template>
  <div id="todo-vue">
    <div>
      <label>New Task:</label>
      <input id="new-todo" v-model="new_todo" placeholder="edit me" @keyup.enter="add_todo()">
      <button @click="add_todo()">Add</button>
    </div>
    <div>
      <div v-for="(todo, index) in todos" :key="todo.id">
        <label>{{index}}.</label>
        <input v-model="todo.content" :disabled="todo.done" @keyup.enter="update_todo(todo)">
        <input type="checkbox" v-model="todo.done">
        <button @click.="remove_todo(index)">Delete</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "todo_comp",
  data: function() {
    return {
      new_todo: "",
      todos: [
        { id: 1, content: "write paper", done: false },
        { id: 2, content: "read paper", done: false },
        { id: 3, content: "review paper", done: false }
      ]
    };
  },
  computed: {
    // the id of the new todos is the last id + 1
    new_todo_id: function() {
      return this.todos[this.todos.length - 1].id + 1;
    }
  },
  methods: {
    // all the methods will be replaced with REST API call later
    remove_todo: function(index) {
      this.todos.splice(index, 1);
    },
    add_todo: function() {
      this.todos.push({
        id: this.new_todo_id,
        content: this.new_todo,
        done: false
      });
    },
    // this is to update data to backend
    update_todo: function(todo) {
      console.log("new value:");
      console.log(todo.id);
      console.log(todo.content);
    }
  }
};
</script>