<template >
<div>
<dialog-container label="Tài Khoản" @on-close="$emit('on-close')" :value="show" :width="400">
    <v-text-field label="Code (Tên đăng nhập)" v-model="masterData.code"></v-text-field>
    <v-text-field label="Mật Khẩu" type="password" v-model="masterData.password"></v-text-field>
    <div v-if="!isLogin">
      <v-text-field label="Tên" v-model="masterData.name"></v-text-field>
      <v-text-field label="Điện Thoại" v-model="masterData.tel"></v-text-field>
      <v-text-field label="Email" v-model="masterData.email"></v-text-field>
      <v-text-field label="Địa chỉ" v-model="masterData.address"></v-text-field>
    </div>
    <template v-slot:actions="v-slot:actions">
      <v-card-actions>
        <v-col :cols="isLogin ? 6 : 12">
          <v-btn class="relative-btn white--text" :large="!$vuetify.breakpoint.xsOnly" block="block" color="#f57e2e" @click="onRegister">Đăng kí</v-btn>
        </v-col>
        <v-col cols="6" v-if="isLogin">
          <v-btn class="relative-btn white--text" :large="!$vuetify.breakpoint.xsOnly" block="block" color="#f57e2e" @click="onLogin">Đăng Nhập</v-btn>
        </v-col>
      </v-card-actions>
    </template>
  </dialog-container>
</div>
</template>
  
<script>

import {defineComponent, getCurrentInstance, ref, watch} from "vue";
import {createData} from "@/utils";
  
  const AccountDialog = defineComponent({
      components: {DialogContainer},
      props: {
          show: {default: false}
      },
      setup(props, {emit}) {
          const instance = getCurrentInstance().proxy
          const {$toast} = instance
          const masterData = ref({})
          const isLogin = ref(true)
  
          const onRegister = async () => {
              if (isLogin.value) {
                  isLogin.value = false
                  return
              }
  
              await createData('/user/', masterData.value)
              emit('on-close')
          }
  
          const onLogin = async () => {
              const data = await createData(
                  '/user/login',
                  {code: masterData.value.code, password: masterData.value.password},
                  false
              )
              if (data.status === 400) $toast.error('Login failed')
              else if (data.status === 200) {
                  $toast.success('Login successful')
                  localStorage.setItem('user', JSON.stringify(data.data))
                  emit('on-close')
                  emit('update-user')
                  emit('update-cart-order')
              }
          }
  
          watch(
              () => props.show,
              () => {
                  if (props.show) {
                      isLogin.value = true
                      masterData.value = {
                          code: null,
                          password: null,
                          name: null,
                          tel: null,
                          email: null,
                          address: null
                      }
                  }
              }
          )
  
          return {
              masterData,
              isLogin,
              onRegister,
              onLogin
          }
      }
  })
  
  export default AccountDialog
  </script>