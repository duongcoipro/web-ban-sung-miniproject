import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Home from '@/pages/Home/index.vue'
// @ts-ignore 
import {UrlPath} from '@/utils'


Vue.use(VueRouter)

const routes: Array<RouteConfig> = [
 
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/',
    name: UrlPath.Home.path,
    component: Home
  },
  {
    path: UrlPath.Products.path,
    name: UrlPath.Products.name,
    component: () => import('../pages/Products/index.vue')
  },
  {
    path: UrlPath.Details.path,
    name: UrlPath.Details.name,
    component: () => import('../pages/Products/details.vue')
  },
  {
    path: UrlPath.Login.path,
    name: UrlPath.Login.name,
    component: () => import('../pages/Login/index.vue')
  }
  ,
  {
    path: UrlPath.Cart.path,
    name: UrlPath.Cart.name,
    component: () => import('../pages/Cart/index.vue')
  },
  {
    path: UrlPath.Profile.path,
    name: UrlPath.Profile.name,
    component: () => import('../pages/Profile/index.vue')
  },
  {
    path: UrlPath.Checkout.path,
    name: UrlPath.Checkout.name,
    component: () => import('../pages/Checkout/index.vue')
  },
  {
    path: UrlPath.Admin.path,
    name: UrlPath.Admin.name,
    component: () => import('../pages/Admin/index.vue')
  },
  {
    path: UrlPath.Test.path,
    name: UrlPath.Test.name,
    component: () => import('../pages/Diamondtest/index.vue')
  }
  //{
   // path: UrlPath.AdminFull.path,
    //name: UrlPath.AdminFull.name,
    //component: () => import('../pages/Admin/admin.vue')
  //}
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
