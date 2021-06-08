<template>
  <div class="header">
    <ul>
        <li v-for="link in links" :key="link.label">
                <router-link 
                v-if="(link.signedIn && currentUser !== undefined) || (!link.signedIn && currentUser === undefined)" 
                :to="link.href">

                    <NavLink :class="nav">
                        {{ link.label }}
                    </NavLink>
        
                </router-link>
        </li>
         <li>
                <router-link 
                to="/">

                    <NavLink :class="nav">
                        LandingPage
                    </NavLink>
        
                </router-link>
        </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    currentUser: String
  },
  data(){
      return {
          links : [
        { signedIn: false, label: 'Sign Up', href: '/auth/signup' },
        { signedIn: false, label: 'Sign In', href: '/auth/signin' },
        { signedIn: true,label: 'Sell Tickets', href: '/tickets/new' },
        { signedIn: true, label: 'My Orders', href: '/orders' },
        { signedIn: true, label: 'Sign Out', href: '/auth/signout' },
        { signedIn: true, label: 'Sign Out', href: '/auth/signout' }
        ]
      }
    
  } 
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>