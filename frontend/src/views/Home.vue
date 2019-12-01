<template>
    <section class="animated fadeIn">
        <NavBar/>
        <div class="container">
            <div class="columns is-mobile">
                <div class="column is-4 is-offset-4">
                    <figure class="">
                        <img src="../assets/logo_transparent.png">
                    </figure>
                </div>
            </div>
            <PetsResume/>
        </div>
        <Footer/>
    </section>
</template>

<script>
// @ is an alias to /src
import NavBar from '@/components/NavBar.vue';
import PetsResume from '@/components/PetsResume.vue';
import Footer from '@/components/Footer.vue';

export default {
  components: {
    NavBar,
    PetsResume,
    Footer,
  },
};
</script>
