<template>
   <div>
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
            <div class="pink-color borderlight">
                  <h3 class="float-left pl-4"> {{description}} </h3> 
            </div>
         </v-col>
         <v-col cols="1"></v-col>
      </v-row>
   </div>
</template>
<script>


const Description={

}

   
export default Description
</script>
<style scoped lang="sass">
.trademark
.color-main
  color: #ff4ca2
.linear-color
  display:block 
  overflow: auto
  background-image: linear-gradient(#ff4ca2, white)
  width: 100%
  height: 60px
.pink-color
  display:block 
  overflow: auto
  background-image: linear-gradient(pink, white)
  width: 100%
  height: auto
.max-width
   max-width: 1500px
   margin : 0 auto
.center
   margin: 0 auto
   text-align: center
.float-left
   float: left
.white--text
   color: white
.borderlight
   border: 2px solid #ff4ca2
</style>