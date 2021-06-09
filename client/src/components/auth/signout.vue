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
            localStorage.setItem('token', undefined)
            console.log(localStorage.getItem('token'));
            this.$emit('updateLocalStorage', localStorage.getItem('token'))
            this.$router.push({ path: '/' })
        }
    },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>