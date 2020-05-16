<template>
    <div>
       <Information v-bind:id="id" v-bind:type="currentView"/> 
       <Comments />
    </div>
</template>

<script>
import Information from '@/components/InfoMovieSerie.vue';
import Comments from '@/components/Comment.vue';

export default {
    props:['currentView'],
    components: {
        Information,
        Comments
    },
    data() {
        return{
            id: this.$route.params.id
        }
    },
    created() {
        window.scrollTo(0, 0);
        this.$store.commit('updateNavbarIndex', 0);
    }

}
</script>

<style>

</style>