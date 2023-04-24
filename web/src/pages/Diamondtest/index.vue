<template>
    <dialog-container label="Giỏ hàng" @:value="show" :width="1000"><span class="title">Giỏ Hàng</span>
        <v-data-table class="elevation-1" >
          <template><span></span></template>
          <template >
            <v-img  max-width="80"></v-img>
          </template>
          <template ><span></span></template>
          <template >
            <v-chip class="pointer" color="green" dark="dark"><span>Đăt hàng</span></v-chip>
            <v-chip class="pointer" color="red" dark="dark" ><span>Xóa</span></v-chip>
          </template>
        </v-data-table><span class="title">Đơn Mua</span>
        <v-data-table class="elevation-1" >
          <template ><span></span></template>
          <template>
            <v-img  max-width="80"></v-img>
          </template>
          <template><span></span></template>
          <template >
            <v-chip class="pointer" color="red" dark="dark"><span>Xóa</span></v-chip>
          </template>
        </v-data-table>
        <template >
          <v-card-actions></v-card-actions>
        </template>
      </dialog-container>
</template>

<script>

import {HeaderBar,Categories,Carousel,Subpro,MobileCategories} from '@/components'
import api from '@/plugins/api'

const CartAndOrderDialog = {}

export default CartAndOrderDialog

</script>

<style lang="sass">
.pointer
  cursor: pointer
.title
  font-size: 17px
  color: green
  padding: 2px
</style>