<template>
  <div class="hello">
    Landing Page
    <ul v-if="data !== null">
        <li v-for="d in data" :key="d.id">
            <div>
                <p>
                    {{d.title}}
                </p>
                <p>
                    <router-link 
                        :to="d.path">
                        
                        <NavLink :class="nav">
                            {{d.id}}
                        </NavLink>
                    
                        </router-link>
                </p>
                <p>
                    {{d.price}}
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
          data: null
      }
  },
  created() {
      this.getTickets()
  },
  methods:{
    reformat(d){
        // d = JSON.parse(d)
        console.log(d);
        d['id'] = String(d['_id']['$oid'])
        d["path"] = `/tickets/${d['id']}`
        delete d['_id']; 
        

        return d
    },
      async getTickets(){
          const url = "http://localhost:6001/api/tickets"
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
            this.data = data['tickets'];
            this.data = this.data.map(d => this.reformat(d))
            console.log(this.data);

      }
  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>