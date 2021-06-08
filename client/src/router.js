import Vue from 'vue';
import Router from 'vue-router';
import landingPage from './components/landingPage'

import signin from './components/auth/signin.vue'
import signout from './components/auth/signout.vue'
import signup from './components/auth/signup.vue'

import orders from './components/orders/orders.vue'
import orderItem from './components/orders/orderItem.vue'

import tickets from './components/tickets/tickets.vue'
import ticketItem from './components/tickets/ticketItem.vue'
import newTicket from './components/tickets/newTicket.vue'


Vue.use(Router);

export default new Router({
  base:'',
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'landingPage',
      component: landingPage,
    },
    {
      path: '/auth/signin',
      name: 'signin',
      component: signin,
    },
    {
      path: '/auth/signup',
      name: 'signup',
      component: signup,
    },
    {
      path: '/auth/signout',
      name: 'signout',
      component: signout,
    },
    {
      path: '/orders',
      name: 'orders',
      component: orders,
    },
    {
      path: '/orders/:id',
      name: 'orderItem',
      component: orderItem,
    },
    {
      path: '/tickets/:id',
      name: 'ticketItem',
      component: ticketItem,
    },
    {
      path: '/tickets',
      name: 'tickets',
      component: tickets,
    },
    {
      path: '/tickets/new',
      name: 'newTicket',
      component: newTicket,
    },
  ],
});