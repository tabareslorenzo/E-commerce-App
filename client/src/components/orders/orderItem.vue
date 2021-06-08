<template>
  <div class="hello">
    Order Item Page {{id = $route.params.id}}
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data()
  {
      return {
          id: null
      }
  },
    mounted(){
        this.fetchOrder();
    },
    methods: {
      fetchOrder(){
          console.log(this.id);
          console.log("this.id");
      }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>