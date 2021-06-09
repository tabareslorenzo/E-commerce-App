<template>
  <div class="hello">
      Orders
      <ul>
          <li v-for="d in data" :key="d.id">
              <div>
                  <p>
                      <router-link 
                        :to="d.path">
                        
                        <NavLink :class="nav">
                            {{d.id}}
                        </NavLink>
                    
                        </router-link>
                      
                  </p>
                  <p>
                      {{d.status}}
                  </p>
                  <p>
                      {{d.ticket}}
                  </p>
                  <p>
                      {{d.userId}}
                  </p>
              </div>
          </li>
      </ul>
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
          data: []
      }
  },
  created() {
      this.getOrders()
  },
  methods:{
    path(id){
        return `/orders/${id}`
    },
    reformat(d){
        // d = JSON.parse(d)
        
        d['id'] = String(d['_id']['$oid'])
        d['ticket'] = d['ticket']['$oid']
        d['expiresAt'] = new Date(d['expiresAt']["$date"] * 1000);
        d["path"] = `/orders/${d['id']}`
        delete d['_id']; 
        console.log(d);

        return d
    },
      async getOrders(){
          const url = "http://localhost:6002/api/orders"
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
            this.data = data['orders'];
            // console.log(this.data);
            this.data = this.data.map(d => this.reformat(d))
            console.log(this.data);

      }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>