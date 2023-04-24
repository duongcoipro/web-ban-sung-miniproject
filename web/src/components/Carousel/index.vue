<template>
    <v-carousel :height="ismobile ? 150:250">
        <v-carousel-item v-for="(image,i) in images" :key="i" :src="image" reverse-transition="fade-transition" transition="fade-transition"
        ></v-carousel-item>
      </v-carousel>
</template>
<script>

const Carousel={
    props: ['ismobile'],
    data(){
        return{
            images: [ 'https://e2.yotools.net/images/user_image/2023/04/644240c67c872.jpg',
                'https://lambaokimairsoft.com/wp-content/uploads/2022/10/S__8781880.jpg',
            'https://www.vuasung.com/assets/upload/gallery/banner3-jpg.jpg'
            
        ]
        }
    },
    mounted(){
        const width=  screen.width
        if (width<=600) this.height= 1500
        else if (width<=900 && width>600 ) this.height=200
        else this.height= 250
    }
}
export default Carousel
</script
<style lang="sass">
</style>