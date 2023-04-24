<template>
    <div>
        <span class="btn pa-2" @click="$emit('change-value','-' )">
            -
        </span>
        <span class="input pa-5">
            {{value}}
        </span>
        <span class="btn pa-2" @click="$emit('change-value','+' )">
            +
        </span>
    </div>

</template>
<script>


const InputQuantity= {
    props:['value'],
    methods: {
        onClick(action) {
            this.$emit('change-value',action )
        }

    }

}

export default InputQuantity

</script>
<style scoped lang="sass">
.max-width
   max-width: 1500px
   margin : 0 auto
.center
   margin: 0 auto
   text-align: center
.btn
    width: 10px
    height: 10px
    border: 2px solid pink
    cursor: pointer 
.btn:active
    background-color: pink
.input
    width: 80px
    border: 2px
.float-left
    float: left
</style>