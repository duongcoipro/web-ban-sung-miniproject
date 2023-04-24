<template>
  <div>
    <header-bar/>
    <div class="max-width center">
      <v-row class="pt-10 hidden-sm-and-down">
        <v-col cols="2">
          <categories class="hidden-md-an-up" title="Outstanding" :items="outstanditems"/>
        </v-col>
        <v-col cols="8">
          <carousel/>
        </v-col>
        <v-col cols="2">
          <v-img class="hidden-md-an-up" width="370px" src="https://scontent.fhan4-3.fna.fbcdn.net/v/t1.6435-9/83318769_101900661364517_1492352804369465344_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=174925&_nc_ohc=AthnaPrcW_8AX_i4nmF&_nc_ht=scontent.fhan4-3.fna&oh=00_AfChxHxbYzox-jxQ4Mn0MEhPdPmjdC1sK_YKqDnE2MN5DQ&oe=646086EC"></v-img>
        </v-col>
    </v-row>
    <carousel class="mt-3 hidden-md-and-up"/>

    <v-row class="pt-2 hidden-sm-and-down">
      <v-col cols="2">
        <categories title="Category" :items="Categoryitems"/>
      </v-col> 
      <v-col cols="10"> 
        <div  class="trademark linear-color">
          <v-img v-for="img in tradeimgs"  class="float-left ma-3" :src="img" width="180">
          </v-img>
        </div>
      </v-col>
    </v-row>
    <div class="trademark hidden-md-and-up linear-color">
      <v-img v-for="img in tradeimgs"  class="float-left ma-3" :src="img" width="110">
      </v-img>
    </div> 

<!--PC-->
    <v-row class="hidden-sm-and-down">
      <v-col cols="2"></v-col>
      <v-col cols="10">
        <h2 class="color-main"> Want revenge? Buy one </h2>
        <div class="list-product">
          <subpro v-for="prd in product" :product="prd"  class="pa-6" @on-click="onClickSubproduct()"/>
        </div>
      </v-col>
  </v-row>
<!--mobile-->
  <v-row class="hidden-md-and-up">
    <h2 class="color-main center" > Product of the month </h2>
      <div class="list-product" width="90px">
        <subpro v-for="prd in product" :product="prd" class="float-left" />
      </div>
</v-row>
</div>
  </div>
</template>

<script>

import {HeaderBar,Categories,Carousel,Subpro,MobileCategories} from '@/components'
import api from '@/plugins/api'
import axios from "axios"



const Home ={
  components: {
     HeaderBar ,
     Categories,
     Carousel,
     Subpro
  },
  data(){
    return{
      product:[],
      tradeimgs: [
        'https://down-vn.img.susercontent.com/file/c274ea15c00c00ea95ea594fbae8c216',
        'https://bachhoadochoi.vn/wp-content/uploads/2021/01/4-2.jpg',
        'https://linatoysdochoitreem.com/wp-content/uploads/2021/07/do-choi-sung-nhua-tre-tho.jpg',
        'https://cf.shopee.vn/file/e6272a3a393027ae4f9a369a75819ba6&zimken.jpg',
        'https://hazomi.com/wp-content/uploads/2020/04/d5ba89b5e46631a27f832a3ebf1e9a73.jpg',
        'https://bizweb.dktcdn.net/thumb/grande/100/337/913/products/1-5524fb6b-006c-44e1-bb1e-58a7b7b44dc1.jpg?v=1543368362173'

      ],
      outstanditems: [
                {text: 'Good price', icon: 'https://banner2.cleanpng.com/20201026/ta/transparent-summer-sales-icon-coupon-icon-5f966e3fd8e8f8.4735208016036941438885.jpg'},
                {text:'Super bargain', icon: 'https://cdn-icons-png.flaticon.com/512/3588/3588395.png'},
                {text:'Fast delivery', icon: 'https://thumbs.dreamstime.com/b/fast-delivery-truck-icon-shipping-design-website-mobile-apps-vector-illustration-212178641.jpg'},
                {text:'1 shot 1 kill', icon: 'https://cdn-icons-png.flaticon.com/512/6010/6010029.png'},
                {text:'10 shot 1 kill', icon: 'https://cdn-icons-png.flaticon.com/512/5906/5906175.png'},
            ],
      Categoryitems:[
      ]
    }
  },
  methods:{
    onClickSubproduct(){
      console.log('Home')
    },
   async getcategory(){
      try{
        const {data}= await axios.get('http://127.0.0.1:2100/category')
        this.Categoryitems= data.filter(cate=> cate.logo !==null).map(cate=>{ 
          return{...cate,icon: cate.logo, text: cate.name }
        })
      }
      catch (e)
      {  
        console.log(e)  
      }
    },
    async getproduct(){
      try{
        const {data}= await axios.get('http://127.0.0.1:2100/product')
        this.product= data.filter(cate=> cate.img !==null).map(cate=>{ 
          return{...cate,img: cate.img, name: cate.name, details: cate.description, star: cate.star,price: cate.price, }
        })
      }
      catch (e)
      {  
        console.log(e)  
      }
    }
  },
  mounted(){
    this.getcategory(),
    this.getproduct()
  }
  
}

  
  export default Home
</script>

<style  lang="sass">
.max-width
    max-width: 1500px
    margin : 0 auto
.center
    margin: 0 auto
    text-align: center
.trademark
.color-main
  color: red 
.linear-color
  display:block 
  overflow: auto
  background-image: linear-gradient(pink, white)
  width: 100%
  height: 250px
.mobile
.float-left
  float: left

</style>