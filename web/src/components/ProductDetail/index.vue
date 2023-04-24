<template>
    <div>
         <v-row>
            <v-col cols="1"></v-col>
            <v-col cols="5" class="pa-10">
                <v-row>
                    <v-col cols="12">
                        <v-img :src="product.img" ></v-img>
                    </v-col>
                </v-row>
                <v-row>
                </v-row>
            </v-col>
            <v-col cols="5">
                <p class="align-left"> {{product.trademark}}</p>
                <h1 class="align-left"> {{product.name}} 
                </h1>
                <p class="align-left">
                    <v-icon  v-for="i in product.star" color="yellow">
                    mdi-star 
                    </v-icon>
                    <span class="pa-2">
                    Đã bán: 12k
                    </span>
                </p>
                <p class="align-left">
                    <del class="color-price"> {{product.sales}} đ</del>
                    -> 
                    <span class="align-left color-price">  {{product.price}} đ </span>
                </p>
        
                <p class="align-left">
                    <span> Shipping </span>
                        <v-icon class="pl-3" color="green">
                            mdi-baby-carriage 
                        </v-icon> 
                        <span class="pl-3"> Free shipping </span>
                </p>
                <p class="align-left pt-4">
                    <span> Quantity </span>
                </p>
                <InputQuantity class="float-left" :value="product.quantity" @change-value="changequantity"/>

                <div style="clear:both;">
                    <v-list-item class="pa-0">
                        <v-btn color="pink" class="white--text mt-10" :disabled="product.quantity===0" @click="gotocheckout()"> Buy Now </v-btn>
                        <v-btn :loading="loading" color="green" class="white--text mt-10 ml-4" :disabled="product.quantity===0" @click="AddToOrder()"> Add to Cart </v-btn>
                    </v-list-item>
                </div>

            </v-col>
            <v-col cols="1"></v-col>
         </v-row>
         <v-row>
            <v-col cols="1"></v-col>
            <v-col cols="10">
               <div class="linear-color borderlight">
                     <h2 class="float-left white--text pl-4"> Product Description </h2> 
               </div>
            </v-col>
            <v-col cols="1"></v-col>
         </v-row>
         <v-row>
            <v-col cols="1"></v-col>
            <v-col cols="10">
               <div class="pink-color borderlight bigsize">
                     <p class="float-left pl-4"> {{product.description}} </p> 
               </div>
            </v-col>
            <v-col cols="1"></v-col>
         </v-row>
         
    </div>

</template>
<script>

import InputQuantity from '../InputQuantity/index.vue'
import router from '@/router'
import {UrlPath} from '@/utils'
import axios from "axios"

const ProductDetails = {
    data(){
        return{
            product:{ },
            alert: true,
        }
    },
    mounted(){
        console.log(router.currentRoute.query)
        const {product_id} = router.currentRoute.query
        this.getproduct(product_id)
    },
    components:{
        InputQuantity
    },
    methods:{
        changequantity(action){
            if (action==='+') this.product.quantity +=1
            if (this.product.quantity===0) return{}
            if (action==='-') this.product.quantity -=1
        },
        gotocheckout(){ 
            localStorage.setItem('total',this.product.quantity * this.product.price)
            router.push({path: UrlPath.Checkout.path })},

        async getproduct(product_id) {
            try {
               // console.log(product_id)
                const {data} = await axios.get(`http://127.0.0.1:2100/product/get_one/${product_id}`)
                //console.log(data)
               this.product = { ...data, quantity: 1}
                } 
            catch (e) {
                console.log(e)
            }
        },
        async AddToOrder() {
        const body = {
            user_id: localStorage.getItem('userid'),
            product_id: this.product.id,
            total_qty: this.product.quantity,
            price: this.product.quantity * this.product.price,
            img: this.product.img,
            gun_name: this.product.name,
            gun_star: this.product.star
      }
      try {  axios.post('http://127.0.0.1:2100/cart/', body),console.log('Done')}
      catch (e) {
                console.log(e)
            }
    }
    }
   
}

export default ProductDetails

</script>
<style scoped lang="sass">
.align-left
    text-align: left
.color-price
    color: red
.float-left
    float: left
.white--text
    color: white
.pink-color
    display:block 
    overflow: auto
    background-image: linear-gradient(pink, white)
    width: 100%
    height: auto
.white--text
    color: white
.borderlight
    border: 2px solid #ff4ca2
.linear-color
  display:block 
  overflow: auto
  background-image: linear-gradient(#ff4ca2, white)
  width: 100%
  height: 60px
.bigsize
 font-size: 20px
.alert 
 position: fixed
 top: 10px
 right: 10px
 padding: 10px
 background-color: red
 color: white
 display: none

</style>