<template>
    <div>
    <HeaderBar/>
    <v-container>
      <v-row align="center" justify="center" dense>
        <v-col cols="12" sm="8" md="4" lg="4">
          <v-card elevation="0">
            <div class="text-center">
              <h1 class="mb-2">Delivery Information</h1>
              <p>We will use your information if you are a terrorist </p>
            </div>
            <v-form>
              <v-text-field
                v-model="inputname"
                label="Enter your name"
                name="name"
                prepend-inner-icon="mdi-shield-account"
                class="rounded-0"
                outlined
                ></v-text-field>
                <v-text-field
                v-model="inputmail"
                label="Enter your email address"
                name="email"
                prepend-inner-icon="mdi-email"
                type="email"
                class="rounded-0"
                outlined
                ></v-text-field>
                <v-text-field
                v-model="inputadd"
                label="Enter your address"
                prepend-inner-icon="mdi-location-enter"
                class="rounded-0"
                outlined
                ></v-text-field>
                <v-text-field
                v-model="inputphone"
                label="Enter your Phone-number"
                prepend-inner-icon="mdi-card-account-phone"
                type="phone"
                class="rounded-0"
                outlined
                ></v-text-field>
                <h2 class="mb-2"> Total bill cost: ${{money}}</h2>
                <v-btn class="rounded-0" color="pink" x-large block dark @click="gettemp()">Accept</v-btn>
                <v-btn class="mt-5" color="pink" x-large block dark @click="cancel()">Cancel</v-btn>
            </v-form>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
</div>
</template>

<script>
import {HeaderBar,Categories,Carousel,Subpro,MobileCategories} from '@/components'
import router from '@/router'
import {UrlPath} from '@/utils'
import axios from "axios"

const Checkout={
  data(){
    return{
      temp: {},
      inputname: '',
      inputadd: '',
      inputmail: '',
      inputphone: '',
      money: 0
    }
  },
    components:{
        HeaderBar
    },
    methods:{
      cancel(){router.push({path: UrlPath.Cart.path})},
      getdata(){this.money = localStorage.getItem('total')},
      async gettemp() {
            try {
                const now = new Date();
                const {data} = await axios.get(`http://localhost:2100/cart/forcheckout?user_id=${localStorage.getItem('userid')}`)
                this.temp = { ...data, }
                for (const item of data) {
                const body = {
                user_id: item.user_id,
                product_id: item.product_id,
                gun_id: item.product_id,
                total_qty: item.total_qty,
                gun_qty: item.total_qty,
                img: item.img,
                total_price: item.price,
                gun_name: item.gun_name,
                gun_star: item.star,
                user_name: this.inputname,
                address: this.inputadd,
                status: this.inputmail,
                active: true,
                phone: this.inputphone,
                created_at: now.toLocaleTimeString()
                }
                axios.post('http://localhost:2100/order/', body),console.log('Done')

                console.log(item.user_id, item.product_id, item.gun_name, item.price, item.total_qty)
                router.push({path: UrlPath.Cart.path})
                }
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
            price: this.money,
            gun_name: this.product.name,
        }
        try {  axios.post('http://localhost:2100/order/', body),console.log('Done')}
        catch (e) {
                console.log(e)
            }
          }
    },
    mounted()
    {
      this.getdata()
      //this.gettemp()
    }
}
export default Checkout

</script>

<style lang="sass" scoped>
</style>