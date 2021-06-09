<template>
  <div class="hello">
    Ticket Item Page  
    <p>
        {{id = $route.params.id}}
    </p>
   <div :v-if="data!==null">
        <p>
            {{data.title}}
        </p>
        <p>
            {{data.price}}
        </p>
        <p>
            {{data.userId}}
        </p>
        <button @click="handleOrder">Order</button>
   </div>
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
          id: null,
          data: null
      }
  },
    mounted(){
        this.fetchOrder();
    },
    methods: {
      fetchOrder(){
          console.log(this.id);
          console.log("this.id");
          this.getTickets()
      },
      async handleOrder()
      {
        const url = "http://localhost:6002/api/orders"
        const token = String(localStorage.getItem('token'))
        const data = {
            "ticketId": this.id
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
            this.$router.push({ path: `/orders/${data['id']['$oid']}` })
        
        }
      },
      async getTickets(){
          const url = `http://localhost:6001/api/tickets/${this.id}`
          const token = String(localStorage.getItem('token'))
          const res = await fetch(url, {
                                crossDomain:true,
                                mode: 'cors', 
                                credentials: 'same-origin', 
                                headers: {
                                    'Authorization': token,
                                    'Content-Type': 'application/json'
                                }
                            })
                            .catch(err => {
                                console.log(err);
                            });
            const data = await res.json();
            // console.log(this.data);
            // console.log(this.reformat(data));
            this.data = data;
            console.log(this.data);

      }

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>