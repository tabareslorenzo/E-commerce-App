<template>
  <div class="hello">
    Sign In
    <form @submit.prevent="handleSubmit($event)">
        <div>
             <label for="email">email:</label>
            <input
                v-model="email" 
                type="text" 
                id="email"
                placeholder="enter your email"
                >
        </div>
        <div>
            <label for="password">password:</label>
            <input 
                 v-model="password" 
                type="password" 
                id="password"
                placeholder="enter your password"
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
    methods: {
        handleSubmit(event){
            if (event) {
            event.preventDefault()
            }
            this.postData(
               "http://localhost:6000/api/users/signin",
               {
                   email: this.email,
                   password: this.password
               }
            )
            .then(data => {
                console.log(data);
                localStorage.setItem('token', data['token'])
                console.log(localStorage.getItem('token'));
            })
            .catch(err => {
                console.log(err);
            })

        },
        async postData(url = '', data = {})
        {
            console.log(url, data);
            const response = await fetch(url, {
            method: 'POST', 
            crossDomain:true,
            mode: 'cors', 
            // cache: 'no-cache', 
            credentials: 'same-origin', 
            headers: {
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
            return response.json();
        
        }
    },
    data()
    {
        return {
            email: "",
            password: ""
        }
    },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>