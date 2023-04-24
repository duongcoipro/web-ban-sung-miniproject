<template>
<div>
     <div>
          <header-bar/>
          <ProductDetails class="max-width center pt-10"/>
     </div>
</div>

</template>
<script>
import {HeaderBar,Categories,Carousel,Subpro,MobileCategories} from '@/components'
import ProductDetails from '@/components/ProductDetail/index.vue'
import Description from '@/components/ProductDescription/index.vue'

const Details={
     components:{
          HeaderBar,
          Categories,
          ProductDetails,
          Description
     }
}

    
export default Details
</script>
<style scoped lang="sass">
.max-width
    max-width: 1600px
    margin: 0 auto
.center
    margin: 0 auto
    text-align: center
</style>