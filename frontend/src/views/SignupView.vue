
import SignupComp from '@/components/SignupComp.vue';

<template>
    <div class="signup" align = center>
        <SignupComp id = "comp-signup"/>
    </div>
</template>

<script>
    import SignupComp from '@/components/SignupComp.vue'
    export default {
        name: 'SignupView',
        components: {
            SignupComp
        }
    }
</script>

<style scoped>

</style>

