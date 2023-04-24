<template>
    <div>
        <v-row class="pt-10">
            <v-col cols="2"></v-col>
            <v-col cols="2" class="">
                <v-row>
                    <v-col cols="12">
                        <v-img :src="product.img" max-width="200px"></v-img>
                    </v-col>
                </v-row>
            </v-col>
            <v-col cols="5">
                <p class="align-left"> Diamond Flashy </p>
                <h1 class="align-left"> {{product.gun_name}} 
                </h1>
                <p class="align-left">
                    <v-icon  v-for="i in product.gun_star" color="yellow">
                    mdi-star 
                    </v-icon>
                </p>
                <p class="align-left">
                    <del class="color-price"> Very expensive</del>
                    -> 
                    <span class="align-left color-price">  {{product.price}} đ </span>
                    <v-icon class="pl-3" color="green">
                        mdi-baby-carriage 
                    </v-icon>
                    <span> Free shipping </span>
                </p>

            </v-col>
            <v-col cols="1">
                <span> Quantity</span>
                <InputQuantity :value="product.total_qty" @change-value="changequantity" class="pt-15"/>
                <p class="pt-5 colorred"> Price: $ {{price}}</p>
                <v-btn icon @click="deleteitem()" class="">
                    <v-icon  color="pink">  mdi-trash-can-outline </v-icon>
                    </v-btn>
            </v-col>
                
         </v-row>
        <div>
        </div>
    </div>
 </template>
 <script>
import {HeaderBar,Categories,Carousel,Subpro,MobileCategories} from '@/components'
import InputQuantity from '@/components/InputQuantity/index.vue'
import router from '@/router'
import {UrlPath} from '@/utils'
import axios from "axios"

 const Items={
    props:['product'],
    data(){   return{
        price:1
        }
    },
    components: {
     InputQuantity,
     HeaderBar ,
     Categories,
     Carousel,
     Subpro
 },
    methods:{
        changequantity(action){
            if (action==='+') this.product.total_qty +=1
            if (this.product.total_qty===0) return{}
            if (action==='-') {this.product.total_qty -=1}
            this.price= this.product.total_qty * this.product.price
            this.$emit('data-sent',this.price )
        },
        async deleteitem(){
               // axios.delete(`http://localhost:2100/cart/${this.product.id}?user_id=${}`)
                axios.delete(`http://localhost:2100/cart/${this.product.product_id}`, {
                params: {
                    user_id: localStorage.getItem('userid'),
                        },
                }).then((response) => {
                console.log(response.data);
                }).catch((error) => {
                console.error(error);
                });
            window.location.reload()
        }
    },
    mounted(){
        this.price= this.product.total_qty * this.product.price
        this.$emit('data-sent',this.price )
    }
 }
 
    
 export default Items
 </script>
 <style scoped lang="sass">
 .colorred
    color: red 
    font-size: 20px
 </style>