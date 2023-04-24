<template>
    <div class="header-color">
    <v-list-item >
        <v-list-item class="max-width">
        <v-img 
        src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWOZ2AXr2myEZrpjROk5_53razqAouOwHaxQ&usqp=CAU"
        max-width="100"
        @click="gotoHome()"
        >
        </v-img>
        <v-spacer/> 
           
            <v-text-field
            background-color="white"
            color="red"
            label="Search"
            solo
            placeholder="Product"
            hide-details
            height="30"
            prepend-inner-icon="mdi-find-replace"
            >
            </v-text-field>
            <v-spacer/>

            <div class="pa-2">
                <v-icon  color="white" @click="gotoHome()">  mdi-home
                </v-icon>
                <span class="hidden-sm-and-down">
                <span class="white--text" > HOME </span>
                </span>
            </div>
            <div class="pa-2">
                <v-icon  color="white" @click="gotoprofile()">  mdi-account
                </v-icon>
                <span class="hidden-sm-and-down">
                <span class="white--text"> {{user_name}} </span></span>
            </div>
            <div >
                <v-btn icon @click="gotocart()">
                <v-icon  color="white">  mdi-cart
                </v-icon>
                </v-btn>
            </div>
            <div  >
                <v-btn icon @click="addpro()" v-if="isShown">
                <v-icon  color="white">  mdi-plus-box-multiple
                </v-icon>
                </v-btn>
            </div>
            <div >
                <v-btn icon @click="logout()">
                <v-icon  color="white">  mdi-logout-variant
                </v-icon>
                </v-btn>
            </div>
           
            <div class="hidden-md-and-up">
                <v-btn icon
                @click="isShowcateinmobile= !isShowcateinmobile" 
                >
                  <v-icon color="white"
                  > 
                    mdi-menu
                  </v-icon>  
                </v-btn>
            </div>
         
        
        </v-list-item>
    </v-list-item>
    <v-divider color="white"/>
    <div class="white--text">
    <div class="center">
        <ul class="pc">
        <ul class="pl-2">
            <li v-for="categoryTop in categoriesTop" @click="gotoProductsPage(categoryTop)">
                <span class="hidden-md-and-down" > {{categoryTop}} </span>
            </li>
        </ul>
        </ul>
    <v-expand-transition>
    <v-card
        v-show="isShowcateinmobile"
        class="mx-auto"
        color="#ff4ca2"
        >
         <ul class="pl-2">
            <li v-for="categoryTop in categoriesTop" @click="gotoProductsPage(categoryTop)">
                <span class="white--text">
                    <span class="hidden-md-and-up" v-if="isShowcateinmobile"> {{categoryTop}} </span>
                </span>
            </li>
        </ul>
    </v-card>
    </v-expand-transition>
    </div>
</div>
</div>
</template> 
    
<script>

import router from '@/router'
import {UrlPath} from '@/utils'

const HeaderBar={
        data() {
        return { 
            user_name:'',
            isShown: false,
            isShowcateinmobile: false,
            categoriesTop:[' Outstanding ',' New Product ', ' Limited ', ' The most powerful ',' Cheap ' ]}
        },
        methods: {
            getdata(){
                this.user_name=  localStorage.getItem('username')
                
            },
            gotoProductsPage(name){
                console.log(name)
                router.push({path: UrlPath.Products.path })
            },
            gotoHome(){
                router.push({path: UrlPath.Home.path })
            },
            gotocart(){ router.push({path: UrlPath.Cart.path })},
            gotoprofile(){router.push({path: UrlPath.Profile.path })},
            logout(){
                localStorage.clear(),
                router.push({path: UrlPath.Login.path })
            },
            addpro(){router.push({path: UrlPath.Admin.path })},
            checkadmin(){if (localStorage.getItem('type')==='1') this.isShown = true  }
        },
        mounted(){
                this.getdata(),
                this.checkadmin()
        }
    }
    
export default HeaderBar
    
</script>
    
<style scoped lang="sass">
.header-color
    background-color: #ff4ca2
.white--text
    color: while
.max-width
    max-width: 1500px
    margin : 0 auto
.center
    margin: 0 auto
    text-align: center
.pc ul li 
    display: inline
ul
    justify-content: center
ul li
    text-align: center
    list-style: none
    
    margin: 0 3px
ul li:hover
    color: red
    cursor: pointer
.category
    height: 40px
</style>