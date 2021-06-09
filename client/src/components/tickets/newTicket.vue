<template>
  <div class="hello">
    New Ticket Page
    <form @submit.prevent="handleSubmitTicket">
        <div>
             <label for="title">title:</label>
            <input
                v-model="title" 
                type="text" 
                id="title"
                placeholder="enter title of ticket"
                >
        </div>
        <div>
            <label for="price">price:</label>
            <input 
                 v-model="price" 
                type="text" 
                id="price"
                placeholder="enter price"
                >
        </div>
        <button type="submit">Submit</button>

    </form>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data() {
      return{
          title: "",
          price: "",
      }
  },
  methods: {
      async handleSubmitTicket()
      {
        const url = "http://localhost:6001/api/tickets"
        const token = String(localStorage.getItem('token'))
        const data = {
            "title": this.title,
            "price": this.price,
        }
        const response = await fetch(url, {
        method: 'POST', 
        crossDomain:true,
        mode: 'cors', 
        // cache: 'no-cache', 
        credentials: 'same-origin', 
        headers: {
            'Authorization': token,
            'Content-Type': 'application/json'
        },
        // redirect: 'follow', 
        // referrerPolicy: 'no-referrer', 
        body: JSON.stringify(data) 
        }).catch(
            err => {
                console.log(err);
                console.log(err);
            }
        )
        if (response !== undefined)
        {
            const data = await response.json();
            console.log(data);
            // this.$router.push({ path: `/orders/${data['id']['$oid']}` })
        
        }
            this.title= ""
            this.price= ""
      }

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>