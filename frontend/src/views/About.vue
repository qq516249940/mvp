<template>
    <section class="animated fadeIn" id="about">
        <NavBar/>
        <div class="columns is-mobile">
            <div class="column is-three-fifths is-offset-one-fifth">
                <div class="tile is-parent">
                    <article class="tile is-child notification is-primary">
                        <p class="title has-text-centered">Rescaty MVP</p>
                        <p class="subtitle has-text-centered">
                            Rescaty is a web & mobile app where people can...
                        </p>
                        <ul class="subtitle">
                            <li>Report a missing pet.</li>
                            <li>Report a pet that needs rescue.</li>
                            <li>Adopt a pet.</li>
                            <li>Run a background check for adoption.</li>
                            <li>Report bad actors or pet abuse.</li>
                            <li>Get updates about pet stories.</li>
                        </ul>
                        <br>
                        <p class="title has-text-centered">Benefits for the community</p>
                        <p class="subtitle has-text-centered">
                            We care a lot for our pets, we're looking for...
                        </p>
                        <ul class="subtitle">
                            <li>Improve chances to find missing pets.</li>
                            <li>Centralize bad actors.</li>
                            <li>Improve pet adoption by automate and centralize tasks e.g. Fill
                                forms, take id pictures, etc.</li>
                            <li>Improve pet adoption and follow-up.</li>
                            <li>Avoid fraud on raising money for pet rescue and support.</li>
                        </ul>
                    </article>
                </div>
            </div>
        </div>
        <Footer/>
    </section>
</template>

<script>
import NavBar from '@/components/NavBar.vue';
import Footer from '@/components/Footer.vue';

export default {
  name: 'About',
  components: {
    NavBar,
    Footer,
  },
};
</script>

<style>
#about {
    margin-top: 40px;
    margin-bottom: 40px;
}

</style>
