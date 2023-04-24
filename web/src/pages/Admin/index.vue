<template>
<div class="pa-15">
  <form>
    <v-text-field v-model="conhang.name" label="Name"></v-text-field>
    <v-text-field v-model="conhang.img"  label="Image" ></v-text-field>
    <v-text-field v-model="conhang.star" label="Star"  ></v-text-field>
    <v-text-field v-model="conhang.description"  label="Details" ></v-text-field>
    <v-text-field v-model="conhang.price" label="Price"></v-text-field>
    <v-text-field v-model="conhang.sales" label="Sales"></v-text-field>
    <v-text-field v-model="conhang.qty" label="Quantity"></v-text-field>
    <v-text-field v-model="conhang.category" label="Category"></v-text-field>
    

    <v-btn class="mr-4" @click="submit()"> Submit </v-btn>
    <v-btn @click="clear"> Clear </v-btn>
  </form>
  </div>

</template>
<script>

import axios from "axios"

 const Admin ={
  data(){
    return {
      conhang:
        { 
                cost: 1
     }
    }
  },
  methods: {
    submit(){
      axios.post('http://127.0.0.1:2100/product/', this.conhang)
    },
    clear(
      conhang=[]
    ){}

  }
 }

export default Admin

</script>
  
  <style scoped lang="sass">
 
  
  </style>