<template>
    <div class="width-card border">
    <v-card class="mx-auto" max-width="300" >
    <v-list dense="" > 
        <v-subheader > {{title}} </v-subheader>
        <v-list-item-group v-model="selectedItems" color="#FFC0CB">
        <v-list-item v-for="(item,i) in items" :key="i">
            <v-list-item-icon >
                <v-img :src="item.icon" width="35px">
                </v-img>
            </v-list-item-icon>
            <v-list-item-content>
                    <v-list-item-title v-text="item.text">
                    </v-list-item-title>
            </v-list-item-content>
        </v-list-item>

        </v-list-item-group>
    </v-list>
    </v-card>
</div>
</template>
<script>

const Categories= {
    props: ['title','items'],
    data(){
        return{
            selectedItems: 1,
            }
        },
        
    }
export default Categories

</script>
<style scoped lang="sass">
.border
    border: 2px solid #FFC0CB
    max-width: 300px
.width-card
    max-width: 200px
</style>