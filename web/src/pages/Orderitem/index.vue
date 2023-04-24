<template>
    <div>
        <div class="tien">
          <v-row>
          <v-col cols="2">
          <span class="pink--color"> Receiver:  </span>
          <span class="redtext">{{ order.user_name }}</span>
          </v-col>
          <v-col cols="2">
          <span class="pink--color tien "> Gun:  </span>
          <span class="redtext">{{ order.gun_name}} ({{ order.gun_qty}}) </span>
        </v-col>
        <v-col cols="2">
          <span class="pink--color tien "> Price: $  </span>
          <span class="redtext">{{ order.total_qty }}</span>
        </v-col>
          <v-col cols="2">
          <span class="pink--color tien "> Address:  </span>
          <span class="redtext">{{ order.address }}</span>
        </v-col>
        <v-col cols="2">
          <span class="pink--color tien "> Phone:  </span>
          <span class="redtext">{{ order.phone }}</span>
        </v-col>
          <v-col cols="2">
          <span class="pink--color tien"> Time:  </span>
          <span class="redtext">{{ order.created_at.slice(0,8) }}</span>
        </v-col>
        </v-row>
        </div>
</div>

</template>

<script>

import router from '@/router'
import {createData} from "@/utils";
import {defineComponent, getCurrentInstance, ref, watch} from "vue";
import axios from "axios"
import {UrlPath} from '@/utils'

const Orderitem = {
  props:['order'],
  }
export default Orderitem
</script>

<style lang="sass" scoped>
.redtext
  color: red
.tien
  font-size: 20px
</style>