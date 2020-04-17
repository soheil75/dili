import Vue from 'vue';
import VueRouter from 'vue-router';
import Welcome from '../views/Welcome.vue';
import Login from '../views/Login.vue';

Vue.use(VueRouter)


const MyAccount = resolve => {
  require.ensure(['../views/MyAccount.vue'], () =>{
    resolve(require('../views/MyAccount.vue'));
  });
};
const NewOrder = resolve => {
  require.ensure(['../views/Client/NewOrder.vue'], () =>{
    resolve(require('../views/Client/NewOrder.vue'));
  });
};
const AllOrder = resolve => {
  require.ensure(['../views/Client/AllOrder.vue'], () =>{
    resolve(require('../views/Client/AllOrder.vue'));
  });
};
const OrderDetails = resolve => {
  require.ensure(['../views/Client/OrderDetails.vue'], () =>{
    resolve(require('../views/Client/OrderDetails.vue'));
  });
};
const MyOrder = resolve => {
  require.ensure(['../views/Client/MyOrder.vue'], () =>{
    resolve(require('../views/Client/MyOrder.vue'));
  });
};
const MyOrderDetails = resolve => {
  require.ensure(['../views/Client/MyOrderDetails.vue'], () =>{
    resolve(require('../views/Client/MyOrderDetails.vue'));
  });
};




const AllOrderPass = resolve => {
  require.ensure(['../views/Passenger/AllOrder.vue'], () =>{
    resolve(require('../views/Passenger/AllOrder.vue'));
  });
};
const OrderDetailsPass = resolve => {
  require.ensure(['../views/Passenger/OrderDetails.vue'], () =>{
    resolve(require('../views/Passenger/OrderDetails.vue'));
  });
};
const AcceptOrderPass = resolve => {
  require.ensure(['../views/Passenger/AcceptOrder.vue'], () =>{
    resolve(require('../views/Passenger/AcceptOrder.vue'));
  });
};
const MySuggestionsPass = resolve => {
  require.ensure(['../views/Passenger/MySuggestions.vue'], () =>{
    resolve(require('../views/Passenger/MySuggestions.vue'));
  });
};
const MySuggestionsDetailsPass = resolve => {
  require.ensure(['../views/Passenger/MySuggestionsDetails.vue'], () =>{
    resolve(require('../views/Passenger/MySuggestionsDetails.vue'));
  });
};

  const routes = [
  {
    path: '/',
    name: 'Welcome',
    component: Welcome
  },
  {
    path: '/Login',
    name: 'Login',
    component: Login
  },
  {
    path: '/MyAccount',
    name: 'MyAccount',
    component: MyAccount,
    //beforeEnter: (to, from, next) => {
    //  if(true & true){
    //    next()
    //  }else{
    //    next('/Login')
    //  }
    //}
  },
  {
    path: '/NewOrder',
    name: 'NewOrder',
    component: NewOrder
  },
  {
    path: '/AllOrder',
    name: 'AllOrder',
    component: AllOrder
  },
  {
    path: '/OrderDetails/:id',
    name: 'OrderDetails',
    component: OrderDetails
  },
  {
    path: '/MyOrder',
    name: 'MyOrder',
    component: MyOrder
  },
  {
    path: '/MyOrderDetails/:id',
    name: 'MyOrderDetails',
    component: MyOrderDetails
  },
  {
    path: '/AllOrderPass',
    name: 'AllOrderPass',
    component: AllOrderPass
  },
  {
    path: '/OrderDetailsPass/:id',
    name: 'OrderDetailsPass',
    component: OrderDetailsPass
  },
  {
    path: '/AcceptOrderPass/:id',
    name: 'AcceptOrderPass',
    component: AcceptOrderPass
  },
  {
    path: '/MySuggestionsPass',
    name: 'MySuggestionsPass',
    component: MySuggestionsPass
  },
  {
    path: '/MySuggestionsDetailsPass/:id',
    name: 'MySuggestionsDetailsPass',
    component: MySuggestionsDetailsPass
  },
  {
    path: '*',redirect:'/MyAccount'
  }
]

const router = new VueRouter({
  routes,
  mode: 'history',
  base: process.env.BASE_URL,
})

export default router
