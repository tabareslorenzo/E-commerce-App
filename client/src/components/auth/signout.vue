<template>
  <div class="hello">
    <button @click="handleSubmit">Sign Out</button>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  methods: {
        handleSubmit(){
            localStorage.removeItem('token');
            console.log(localStorage.getItem('token'));
        }
    },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>