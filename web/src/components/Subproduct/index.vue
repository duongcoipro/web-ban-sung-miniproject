<template>
<div class="max-width-product-component float-left" @click="onClick()">
<div class="hidden-sm-and-down max-width">
    <v-img :src="product.img"/>
    <div class="prodname align-left pink--text">
       <span> {{product.name}} </span>
    </div>
    <div class="rv align-left">
        <span> {{product.details.length > 20 ? product.details.slice(0,10) + '...' : product.details }} </span>
        <div>
        <span>{{ product.star }}</span>
        <v-icon color="yellow">   mdi-star </v-icon>
        </div>
    </div>
    <div class="rate align-left">S
        <span> Sold: 10k </span>
    </div>
    <div class="Price">
        <span> ${{ product.price }}</span>
    </div>  
</div>

<div class="hidden-md-and-up max-mobile pa-4">
    <v-row>
        <v-col cols="2">
        </v-col>
    <v-col cols="4">
        <v-img width="300px" :src="product.img"/>
    </v-col>
    <v-col cols="4">
        <span> {{ product.details.slice(0,8) }} </span>
        <div>
            <span> {{product.star}}</span>
        <v-icon color="yellow"> mdi-star </v-icon>
        <div class="rate align-left">
            <span> Sold: 10k </span>
        </div>
        <div class="Price">
            <span>${{product.price}}</span>
        </div>  
        </div>
    </v-col>
    <v-col cols="2">
            
    </v-col>
</v-row>
</div>

</div>

</template>
<script>
import router from '@/router'
import {UrlPath} from '@/utils'

 const Subpro={
    props:['product'],
    methods: {
        onClick() {
      router.push({name: UrlPath.Details.name, query: { product_id: this.product.id } }),
      console.log(this.product),
      localStorage.setItem('gun_id',this.product.id)
    }
}
}

 export default Subpro
</script>
<style scoped lang="sass">
.max-width
    max-width: 200px
.max-mobile
    max-width: 400px
.pink--text
    color: #e500ff
.Price
    font-size: 20px
    font-weight: 800
</style>