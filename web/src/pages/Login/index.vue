<template>
    <div>
    <div lass="video-layer">
        <video autoplay loop muted>
            <source src="@/assets/sung-131127.mp4" type="video/mp4">
          </video>
    </div>
    <div class="login-layer">
    <v-container class="fill-height" fluid>
      <v-row align="center" justify="center" dense>
        <v-col cols="12" sm="8" md="4" lg="4">         
          <v-card elevation="0">
            <div class="text-center">
              <h1 class="mb-2">Login</h1>
            </div>
            <a  target="_blank">
              <v-img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWOZ2AXr2myEZrpjROk5_53razqAouOwHaxQ&usqp=CAU" contain height="200"></v-img>
            </a>
            <v-card-text>
              <v-form>
                <v-text-field label="Enter your Username" prepend-inner-icon="mdi-account-arrow-left" class="rounded-0" outlined v-model="inputname"></v-text-field>
                <v-text-field label="Enter your password" name="password" prepend-inner-icon="mdi-lock" type="password" suffix="| Forgot?" class="rounded-0" outlined v-model="inputpass"></v-text-field>
                <v-btn class="rounded-0" color="#000000" x-large block dark @click="loginclick">Login</v-btn>
                <v-alert :value="alert" color="pink" dark border="top" icon="mdi-home" transition="scale-transition">
                        Nhập Sai Rồi ?? 
                </v-alert>

                <v-card-actions class="text--secondary">
                  <v-checkbox color="#000000" label="Remember me"></v-checkbox>
                  <v-spacer></v-spacer>
                  No account? <a href="#" class="pl-2" style="color: #000000">Sign Up</a>
                </v-card-actions>
              </v-form>
            </v-card-text>
            <v-card-actions class="ml-6 mr-6 text-center">
              <p>By continuing, you agree to Diamond Rule <a href="#" class="pl-2" style="color: #000000">Policy</a> and <a href="#" class="pl-2" style="color: #000000">Terms of Use</a></p>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
    </div>
</div>

</template>

<script>

import router from '@/router'
import {createData} from "@/utils";
import {defineComponent, getCurrentInstance, ref, watch} from "vue";
import axios from "axios"
import {UrlPath} from '@/utils'

const apiUrl = 'http://127.0.0.1:2100/user/login';

const Login = defineComponent({

  data(){
    return {
      alert: false ,
      overlay: false,
      zIndex: 0,
      inputname: '',
      inputpass: '',
    }
  },
  methods: {
    async loginclick() {
          axios.post(apiUrl, { user_name: this.inputname, user_password: this.inputpass })
          .then(response => {
            console.log(response)
          if (response.data.status =='200') 
            {
             router.push({path: UrlPath.Home.path }),
             localStorage.setItem('userid',response.data.data.id),
             localStorage.setItem('username',response.data.data.user_name),
             localStorage.setItem('type',response.data.data.user_type)
            }
          else 
            {
              this.alert = !this.alert 
            }
          }) 
    }
}
}
)





export default Login
</script>

<style lang="sass" scoped>
.video-layer 
    position: fixed
    top: 0
    left: 0
    width: 100%
    height: 100%
    
.login-layer 
    position: absolute
    top: 50%
    left: 50%
    transform: translate(-50%, -50%)
    z-index: 1
    width: 1500px
  
</style>