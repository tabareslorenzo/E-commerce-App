<template>
  <div class="hello">
    Order Item Page 
    <div>
        {{id = $route.params.id}}
    </div>
    
    <div :v-if="data!==null">
        <p>
            {{data.status}}
        </p>
        <p>
            {{String(data.expiresAt)}}
        </p>
        <p>
            Buyer: {{data.userId}}
        </p>
        <div>
                <p>
                    {{data.ticket.title}}
                </p>
                <p>
                    {{data.ticket.id}}
                </p>
                <p>
                    {{data.ticket.price}}
                </p>
                
                <p>
                    Seller: {{data.ticket.userId}}
                </p>
        </div>
        
        
    </div>
    <!-- <div v-else>
            {{id = $route.params.id}}
        </div> -->
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
        reformat(d){
        // d = JSON.parse(d)
        
        d['id'] = String(d['id']['$oid'])
        d['ticket']['id'] = d['ticket']['id']['$oid']
        d['expiresAt'] = new Date(d['expiresAt']["$date"] * 1000).toString()
        console.log(d);

        return d
        },
      fetchOrder(){
          console.log(this.id);
          console.log("this.id");
          this.getOrder()
      },
      async getOrder(){
          const url = `http://localhost:6002/api/orders/${this.id}`
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
            this.data = this.reformat(data);


      }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>