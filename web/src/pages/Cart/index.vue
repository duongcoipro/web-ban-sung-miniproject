<template>
    <div>
        <HeaderBar/>
        <Items v-for="item in product" :product="item" @data-sent="updateTotal"/>
            <v-footer app class="max-width">
                  <v-row justify="center">
                    <v-expansion-panels inset>
                      <v-expansion-panel >
                        <v-expansion-panel-header class="colorfull">
                            <v-col cols="2">
                            </v-col>
                            <v-col cols="4">
                                    <v-icon color="pink">  mdi-firebase </v-icon> 
                                    <span  class="tien"> Total (item): {{count}} </span>
                            </v-col>
                            <v-col cols="4">
                                <v-icon color="pink"> mdi-cart-outline</v-icon>
                                <span class="tien"> $: {{total}} </span>
                        </v-col>
                            <v-col cols="2">
                                <v-btn color="#ff4ca2" class="white--text" width="160px" height="60px" @click="gotocheckout()">     
                                Checkout
                                </v-btn>
                            </v-col>
                            <v-img src="@/assets/package.webp" max-width="50px"/>
                            Your Order
                        </v-expansion-panel-header>
                        <v-expansion-panel-content>
                            <span class="ort"> Information about your orders: </span>
                            <Orderitem v-for="order in orders" :order="order"/>
                        </v-expansion-panel-content>
                      </v-expansion-panel>
                    </v-expansion-panels>
                  </v-row>
              </v-footer>
        </div>
 </template>
 <script>
import {HeaderBar,Categories,Carousel,Subpro,MobileCategories} from '@/components'
import InputQuantity from '@/components/InputQuantity/index.vue'
import router from '@/router'
import {UrlPath} from '@/utils'
import Items from '../Items/index.vue'
import axios from "axios"
import Orderitem from '..//Orderitem/index.vue'

 const Cart={
    data(){   return{
            product:[],
            count: 0,
            countpri: 0,
            total: 0,
            visible: false,
            orders: [],
            countpriceorder: 0,
            countorder: 0
        }
    },
    components: {
     InputQuantity,
     HeaderBar ,
     Categories,
     Carousel,
     Subpro,
     Items,
     Orderitem
 },
 mounted(){
    this.getproduct(),
    this.getorder()
 },
    methods:{
        show: function() {
        this.visible = true;
        setTimeout(() => {
        this.visible = false;
        }, 2000);
        },
        updateTotal: function(data) {
            this.total += data
        },
        gotocheckout(){
            router.push({path: UrlPath.Checkout.path}),
            localStorage.setItem('total',this.total)
        },
        async getproduct(){
            //if {}
           const urltemp= `http://127.0.0.1:2100/cart/one?user_id=${localStorage.getItem('userid')}`
        try {
            const {data}= await axios.get(`http://127.0.0.1:2100/cart/one?user_id=${localStorage.getItem('userid')}`)
            this.product= data.filter(cate=> cate.img !==null).map(
                cate=>{ 
                return{...cate, count: data.length, totalpri: data.reduce((total, current) => total + current.price, 0) }
                },
            this.countpri= data.reduce((total, current) => total + current.price, 0),
            this.count= data.length,
        )
        }
        catch (e)
        {
            console.log(e)  
        }
    },
        async getorder(){
        try{
            const {data}= await axios.get(`http://localhost:2100/order/one/${localStorage.getItem('userid')}`)
            this.orders= data.filter(cate=> cate.img !==null).map(
                cate=>{ 
                return{...cate, count: data.length, totalpri: data.reduce((total, current) => total + current.price, 0) }
                },
            this.countpriceorder= data.reduce((total, current) => total + current.price, 0),
            this.countorder= data.length,
        )
        }
        catch (e)
        {
            console.log(e)  
        }
    }
    }
 }
 
    
 export default Cart
 </script>
 <style scoped lang="sass">
 
 .tien
    font-size: 20px
.ort
    font-size: 25px
.colorfull
    border: 2px solid #FFC0CB
.pink--color
 color: red
 </style>